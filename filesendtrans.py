import sys

from socket import *

s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = 9999
buf =1024
addr = (host,port)

file_name="/Users/sanjaygupta/Documents/Blender/Assets"

s.sendto(file_name,addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print("Sendingg ...... ")
        data = f.read(buf)
s.close()
f.close()

