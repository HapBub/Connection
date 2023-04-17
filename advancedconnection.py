import socket
from datetime import datetime
import random
import string

# FILE NAME
# getting 4 random characters

random = ''.join(random.choices(string.ascii_lowercase, k=4))

# getting the current time

now = datetime.now()
date = now.strftime("%d_%m_%Y")

# defining the file names

filename = date + "_" + random + ".log"

# CONNECTION

target_host = "127.0.0.1" # ip address or URL (localhost in this case, can differ)
target_port = 7777 # port (can differ)

# create a socket object and handler

with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as client: 
    
    # connect the client

    client.connect((target_host,target_port))
 
    # send some data

    data = bytes (f"GET /connect.html HTTP/1.1\r\nHost: {target_host}\r\n\r\n",'UTF=8')
    client.sendall (data)

    # recieve some data

    response = client.recv (4096)

    # create a file handler for the output

    with open(filename, mode = 'w', encoding = "UTF-8") as output:
        print(response.decode(), file=output)

print ("Connection succeed!") 



