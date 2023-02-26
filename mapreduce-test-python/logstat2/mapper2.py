#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import os
import sys

I_hour, F_hour = 12,12 #os.environ['RANGE'].strip().split("-") #the user inputs the hour range
I_hour, F_hour = int(I_hour), int(F_hour)

if I_hour > 23 or F_hour >23 or I_hour<0 or F_hour<0:
    #errors in the hours
    #print('Invalid input')
    raise Exception('Invalid Input')

pat = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match:

        hour = int(match.group('hour'))

        if hour >= I_hour and hour <= F_hour:
            #only consider the visits inside this hour range
            print('{}\t{}'.format('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1))
