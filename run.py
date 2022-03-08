import os
import sys
import glob
import os.path
from os import path

import mp4_to_mp3


def to_sh(filename):
    mp3file = filename[:-3] + 'mp3'
    if path.exists(mp3file):
        print('exists:'+mp3file)
        return mp3file

    mp4_to_mp3.to_mp3(filename)
    return mp3file


mylist = [f for f in glob.glob("*.mp4")]
if len(mylist) < 1:
    mylist = [f for f in glob.glob("*.mkv")]
#print(mylist)

for c in mylist:
    print(c)
    mp3file = to_sh(c)
   
    cmd = 'python asplit.py ' + mp3file +' 3 0.1'
    os.system(cmd)

    shfile = mp3file + '-out.sh'

    cmd = 'chmod +x ' + shfile
    os.system(cmd)

    cmd = './' + shfile
    os.system(cmd)



