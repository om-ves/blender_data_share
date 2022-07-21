import tqdm
import os
import socket

SEPERATOR = "<SEPERATOR>"

bfrsz = 4026 

host = "192.168.0.112"

port = 8000 

file_name = "untitled.blend"

filesize = os.path.getsize(file_name)

s= socket.socket()

s.connect((host , port))

s.send(f"{file_name}{SEPERATOR}{filesize}".encode())


#for the visual representation of the progress of data transfer 

progress = tqdm.tqdm(range(filesize), f"Sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
with open(file_name, "rb") as f:
    while True:
        bytes_read = f.read(bfrsz)
        if not bytes_read:

            break


        s.sendall(bytes_read)
        progress.update(len(bytes_read))
s.close()