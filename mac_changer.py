#!/usr/bin/env  pyhton

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify the new mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface])  # TODO: Handle it if interface not exist
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("[-] Could not read MAC address")
    except:
        print("[-] Could not read MAC address")


result = get_arguments()
current_mac = get_current_mac(result.interface)
print("Current MAC = " + str(current_mac))
change_mac(result.interface, result.new_mac)
current_mac = get_current_mac(result.interface)

if current_mac == result.new_mac:
    print("[+] Mac address was successfully changed to " + current_mac)
else:
    print("[-] Mac address did not get changed.")
