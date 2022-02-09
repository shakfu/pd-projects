"""basic python3 script to test midi control of user interface elements.

Uses midipipe (http://www.subtlesoft.square7.net/MidiPipe.html) to create
virtual midi end points.


"""

import sys
import os
import time



CC = 109
N_TRACKS = 11


def forward():
    print('forward')
    for i in range(CC):
        print(i)
        os.system(f'sendmidi dev "MidiPipe Input 1" ch 10 cc {i} 127')
        time.sleep(1)


def back():
    print('back (reset)')
    for i in range(CC):
        print(i)
        os.system(f'sendmidi dev "MidiPipe Input 1" ch 10 cc {i} 0')

if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd in ['r', 'b']:
        back()
    elif cmd in 'f':
        forward()

