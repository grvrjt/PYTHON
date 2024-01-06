#!/usr/bin/env python
import scapy.layers.l2
from scapy.all import *


def scan(ip):
    arp_request = scapy.layers.l2.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.layers.l2.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()
    # scapy.layers.l2.arping(ip)


scan("192.168.159.1/24")

# TODO: scapy.ls(scapy.layers.l2.ARP(pdst=ip))
