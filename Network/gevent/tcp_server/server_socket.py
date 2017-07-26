# -*- coding: utf-8 -*-

__author__ = 'chzfmx'
import sys
import socket

host = 'localhost'
port = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(100)
while True:
    conn,addr = s.accept()
    print('connected with %s:%s' %(addr[0],addr[1]))
    data = conn.recv(1024)
    print(data)
    conn.close()
s.close()

