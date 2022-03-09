import subprocess as sp
import sys
import os
import numpy

FFMPEG_BIN = "ffmpeg"

print ('ASplit.py <src.mp3> <silence duration in seconds> <threshold amplitude 0.0 .. 1.0>')
print('eg. python asplit.py 1_1.mp3 3 0.1')

src = sys.argv[1]
dur = float(sys.argv[2])
thr = int(float(sys.argv[3]) * 65535)

if os.name == 'nt':
    # Windows
    f = open('%s-out.bat' % src, 'w+')
else:
    # other (unix)
    f = open('%s-out.sh' % src, 'w+')

tmprate = 22050
len2 = dur * tmprate
buflen = int(len2     * 2)
#            t * rate * 16 bits

oarr = numpy.arange(1, dtype='int16')
# just a dummy array for the first chunk

command = [ FFMPEG_BIN,
        '-i', src,
        '-f', 's16le',
        '-acodec', 'pcm_s16le',
        '-ar', str(tmprate), # ouput sampling rate
        '-ac', '1', # '1' for mono
        '-']        # - output to stdout

pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10**8)

tf = True
pos = 0
opos = 0
part = 0

while tf :

    raw = pipe.stdout.read(buflen)
    if raw == '' :
        tf = False
        break

    try:
        arr = numpy.fromstring(raw, dtype = "int16")
        rng = numpy.concatenate([oarr, arr])
        mx = numpy.amax(rng)
    except ValueError:  #raised if `y` is empty.
        print('ValueError')
        break
        #pass
    if mx <= thr :
        # the peak in this range is less than the threshold value
        trng = (rng <= thr) * 1
        # effectively a pass filter with all samples <= thr set to 0 and > thr set to 1
        sm = numpy.sum(trng)
        # i.e. simply (naively) check how many 1's there were
        print('sm={}, len2={}'.format(sm, len2))
        apos1 = pos + dur * 0.5
        
        if sm >= len2 and (apos1 - opos) > 20:
            part += 1
            apos = pos + dur * 0.5
            print (mx, sm, len2, apos)
            #f.write('ffmpeg -i "%s" -ss %f -to %f -c copy -y "%s-p%04d.mp3"\r\n' % (src, opos, apos, src, part))
            f.write('ffmpeg -i {} -ss {} -to {} -c copy -y {}p{:02n}.mp3 &\r\n'.format(src, opos, apos, src[:3], part))
            opos = apos

    pos += dur

    oarr = arr

part += 1    
#f.write('ffmpeg -i "%s" -ss %f -to %f -c copy -y "%s-p%04d.mp3"\r\n' % (src, opos, pos, src, part))
#f.write('ffmpeg -i {} -ss {} -to {} -c copy -y {}p{:04n}.mp3 \r\n'.format(src, opos, apos, '', part))
f.close()
