# -*- coding: utf-8 -*-

import datetime
from time import sleep

def p(obj):
    print obj

def pp(obj):
    print obj,

def nowdt():
    return datetime.datetime.now()

def msec_diff(left, right):
    delta = left-right
    msec = delta.seconds*1000 + delta.microseconds/1000
    return msec

def pause():
    """ Must press Enter to break. """
    raw_input()

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description='body clock.')
    parser.add_argument('-s', '--span', default=1, type=int)
    parser.add_argument('-r', '--repeat', default=10, type=int)

    args = parser.parse_args()
    return args

args = parse_arguments()
span = args.span
repeatcount = args.repeat

c = 0
total_diff_msec = 0

pp('Are you ready? Press enter to start...')
pause()

while True:
    if c>=repeatcount:
        break

    pp('Try[{0}/{1}] Press enter after {2}-secs passed.'.format(
        c+1, repeatcount, span))
    startdt = nowdt()
    pause()
    enddt = nowdt()

    your_diff_msec = msec_diff(enddt, startdt)
    diff_diff_msec = your_diff_msec - args.span*1000
    total_diff_msec += your_diff_msec
    your_diff_sec = float(your_diff_msec)/1000
    diff_diff_sec = float(diff_diff_msec)/1000
    total_diff_sec =float(total_diff_msec)/1000
    sign = ''
    if diff_diff_sec>0:
        sign = '+'

    p('{0:0.3f}({1}{2:0.3f}) {3:0.3f}'.format(
        your_diff_sec,
        sign,
        diff_diff_sec,
        total_diff_sec)
    )
    c += 1

total_diff_sec = float(total_diff_msec)/1000
total_diff_diff_msec = total_diff_msec- args.span*1000*repeatcount
total_diff_diff_sec = float(total_diff_diff_msec)/1000
sign = ''
if total_diff_diff_sec>0:
    sign = '+'
p('Total: {0:0.3f}({1}{2:0.3f})'.format(total_diff_sec, sign, total_diff_diff_sec))