# -*- coding : utf-8 -*-

__author__ = 'chzfmx'

import socket
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.0.1','192.168.0.1']:
        packet_ip_addr = socket.inet_aton(ip_addr)
        unpacket_ip_addr = socket.inet_ntoa(packet_ip_addr)
        print("IP Address: %s ==> Packet: %s Upacket: %s" % (ip_addr,hexlify(packet_ip_addr),unpacket_ip_addr))

if __name__ == '__main__':
    convert_ip4_address()
