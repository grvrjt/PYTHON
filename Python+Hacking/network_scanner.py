#!/usr/bin/env python
import scapy.layers.l2
from scapy.all import *
import argparse


def get_client_ip():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip", help="Target IP / IP range ")
    options = parser.parse_args()
    target = options.target_ip
    return target


def scan(ip):
    arp_request = scapy.layers.l2.ARP(pdst=ip)
    broadcast = scapy.layers.l2.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.layers.l2.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_results(results_list):
    print("__________________________________________________________________")
    print("IP\t\t\t At MAC Address")
    print("------------------------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


client_ip = get_client_ip()
scan_results = scan(client_ip)
print_results(scan_results)
# TODO: scapy.ls(scapy.layers.l2.ARP(pdst=ip))
