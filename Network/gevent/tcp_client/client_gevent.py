# -*- coding:utf-8 -*-

__author__ = 'chzfmx'
import gevent
from gevent import monkey
monkey.patch_all()
import socket

def do_connect(addr,index):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(addr)
    gevent.sleep(0.5)
    sock.send(b'hello world')
addr = ('localhost',5000)
greenlets = []
num = 1
for i in range(num):
    g = gevent.spawn(do_connect,addr,i)
    greenlets.append(g)
gevent.joinall(greenlets)
