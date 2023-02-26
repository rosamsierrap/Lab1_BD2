#!/usr/bin/python
# --*-- coding:utf-8 --*-
from operator import itemgetter
import sys

dictionary_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split()
    #here ip is ip + hour, now we extract only the ip address:
    ip_address = ip[7:]

    try:
        num = int(num)
        dictionary_ip_count[ip_address] = dictionary_ip_count.get(ip_address, 0) + num
        # adding the values of each ip search in the hour range

    except ValueError:
        pass

sorted_dictionary_ip_count = sorted(dictionary_ip_count.items(), key=itemgetter(1), reverse=True)
#sort reserved = the max to minimun count
for ip_address, count in sorted_dictionary_ip_count:
    print ('{}\t{}'.format(ip_address, count)) #print the top 3 addresses in the range
               