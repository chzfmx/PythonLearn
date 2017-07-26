# -*- coding : utf-8 -*-

__author__ = 'chzfmx'

'''''
socket库中的类函数ntohl()把网络字节序转换成了长整形主机字节序。
函数名中的n表示网络； h表示主机； l表示长整形； s表示短整形，即16位
'''''
import socket

def convert_integer():
    data = 1234
    # 32bit
    print('Original: %s ==> long host byte order: %s,Network byte order: %s' % (data,socket.ntohl(data),socket.htonl(data)))
    # 16bit
    print('Original: %s ==> long host byte order: %s,Network byte order: %s' % (data, socket.ntohs(data), socket.htons(data)))

if __name__ == '__main__':
    convert_integer()
