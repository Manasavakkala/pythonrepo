'''import sys
print("version:",sys.version)


import socket
hostname=(socket.gethostname())
print(hostname)

ipadd=socket.gethostbyname(hostname)
print(ipadd)'''

'''
import os

with open("ip_list.txt") as file:
    park=file.read()
    park=park.splitlines()
    print(" {park}  \n")
    #ping for each ip in the file
for ip in park:
    response=os.popen(f"ping {ip} ").read()

    #saving some ping output details to output file

    if("Request timed out." or "unreachable") in response:
        print(response)
        f=open("info_output.txt","a")
        f.write(str(ip)+'link is down'+'\n')
        f.close()
    else:
        print(response)
        f=open("info_output.txt","a")
        f.write(str(ip)+' is up '+'\n')
        f.close()
        #print output file to screen
with open("ip_output.txt") as file:
    output=file.read()
    print(output)
with open("info_output.txt","w") as file:
    pass
#17,22,26'''

'''
import os,ipaddress

#os.system('cls')#os.system will clear the console at the start of the execution

while True:
    ip=input('Enter IP Address:')
    try:
        print(ipaddress.ip_address(ip))
        print('IP Valid')
    except:
        print('-' *50)
        print('IP is not valid')
    finally:
        if ip =='mango':
            print('Script Finished')
            break'''

'''
import os
print(os.system("ipconfig"))
'''
#first of all import the socket
import socket

#next create a socket object
s=socket.socket()
print("socket successfully created")

#reserve a port on yiur computer
port=40674

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)
print("socket is listining")

while True:
    #
    c,addr=s.accept()
    print('Got connection from',addr)
   # print(c)

    c.send(b'Thank you for connecting')
    #print(c)
    #bytes.decode()

    #close the connection with the client
    c.close()


#Import socket module
import socket

#create a socket object
s=socket.socket()

#Define the port on which you want to connect
port=40674

#connect to the server on local computer
s.connect(('127.0.0.1',port))

#receive data from the server
print(s.recv(1024))

#close the connection
s.close()