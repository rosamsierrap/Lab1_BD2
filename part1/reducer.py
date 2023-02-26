
from operator import itemgetter
import sys

dictionary_ip_count={}

for line in sys.stdin:
    line=line.strip()
    #print(line)
    ip, num=line.split('\t')
    #print(ip)
    #divide per hour and ip address as key parameters: later on use it as connectors
    hour=ip[1:6]
    ip_address=ip[7:]
    #print(hour)
    #print(ip_address)


    try:
        num=int(num)
        if dictionary_ip_count.get(hour):
            #creating a dictionary with hour and all ip_address within that hour as key in map structure, count will be value
            dictionary_ip_count[hour][ip_address]=dictionary_ip_count[hour].get(ip_address,0)+num
            #print(dictionary_ip_count)
        else:
            dictionary_ip_count[hour]={ip_address:1}
    except ValueError:
        pass
#sorted by hour
sorted_dictionary=sorted(dictionary_ip_count.items(), key=itemgetter(0))
#print(sorted_dictionary)

#Create a sorted way stay with top 3 ip_addres per hour
for hour, count in sorted_dictionary:
    sorted_ip_count = sorted(count.items(), key=itemgetter(1), reverse=True) #sort in descending order
    #print(sorted_ip_count)
    for ip, count in sorted_ip_count[:3]: #stay with top 3 ip_address per hour
        print('[{}]{}\t{}'.format(hour,ip, count))


