from socket import *

s= socket()

print('socket created')

s.bind(('192.168.56.1',9999))

s.listen(3)
print('waiting for connection')

while True:
    c, addr = s.accept()
    name=c.recv(1024).decode()
    print('connected with', addr,name)
    c.send(bytes('Welcome to Telusko','utf-8'))
    c.close()