# -*- coding : utf-8 -*-

__author__ = 'chzfmx'

'''''
# getservbyport()函数
如果知道网络服务使用的端口，可以调用socket库中的getservbyport()函数来获取服务的名字。
调用这个函数时可以根据情况决定是否提供协议名。
'''''
import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80,25]:
        print('Port: %s ==> servicename: %s' %(port,socket.getservbyport(port,protocolname)))
    print('Port: %s ==> servicename: %s' %(53,'udp'))

if __name__ == '__main__':
    find_service_name()
