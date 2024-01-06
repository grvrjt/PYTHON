#!/usr/bin/env python
import scapy.layers.l2
from scapy.all import *


def scan(ip):
    scapy.layers.l2.arping(ip)


scan("192.168.159.1/24")
