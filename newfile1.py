'''import uuid
print("The MAC address in formatted way is:", end="")
print(':'.join(['{:02x}'.format((uuid.getnode()>>ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))'''

'''import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)'''

'''import ifaddr

adapters=ifaddr.get_adapters()
for adapter in adapters:
    print("IPs of network adapter"+adapter.nice_name)
    for ip in adapter.ips:
        print("  %s/%s" %(ip.ip,ip.network_prefix))'''



'''import  ifaddr

adapters=ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IPs of network adapter"+adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
            print("  %s/%s" %(ip.ip,ip.network_prefix))
    else:
        print(" NO IPs configured")'''



'''import psutil

result02=psutil.cpu_stats()
result04=psutil.disk_partitions()
result05=psutil.net_io_counters(pernic=True)

#pernic=true:False::collect the snetio info from all the NICs together and displaylay the overall result

print(result02)
print(result04)
print(result05)'''

'''import psutil

network_stats=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_stats,'bytes_sent')
bytes_recv=getattr(network_stats,'bytes_recv')

print("Bytes sent={0} | Bytes Received={1}".format(bytes_sent,bytes_recv))'''


'''import socket
import subprocess
import sys

from datetime import datetime

subprocess.call('clear',shell=True)

#Blank your screen
#subprocess.call('clear',shell=True)

#Ask for input
remoteServer=input("Enter a remote host to scan:")
remoteServerIp=socket.gethostbyname(remoteServer)

#print a nice banner with info
print("_"*60)
print("please wait,scanning remote host",remoteServerIP)
print("_"*60)






t1=datetime.now()
print(t1)

try:
    for port in range (1,5000):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP,port))
        if result==0:
            print ("port {}:      open".format(port))
            sock.close()

except KeyboardInterrupt:
    print("You pressed ctrl+c")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()'''





import scapy.all as scapy
request=scapy.ARP()
print(request.summary())

import scapy.all as scapy
request=scapy.ARP()
print(request.show())