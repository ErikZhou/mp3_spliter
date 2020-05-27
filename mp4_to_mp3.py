import os
import sys
from moviepy.editor import *


def to_mp3(filename):
    mp3file = filename[:-3] + 'mp3'
    print(mp3file)
    video = VideoFileClip(os.path.join("./","",filename))
    video.audio.write_audiofile(os.path.join("./","",mp3file))


def usage():
    print('python mp4-to-mp3.py filename')


def main():
    filename = sys.argv[1]
    print(filename)
    to_mp3(filename)

if __name__ == "__main__":
    usage()
    main()

