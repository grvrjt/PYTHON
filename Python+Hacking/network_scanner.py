#!/usr/bin/env python
import scapy.layers.l2
from scapy.all import *


def scan(ip):
    arp_request = scapy.layers.l2.ARP(pdst=ip)
    broadcast = scapy.layers.l2.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered, unasnwered = scapy.layers.l2.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())
    print(unasnwered.summary())


scan("192.168.159.1/24")

# TODO: scapy.ls(scapy.layers.l2.ARP(pdst=ip))
