#!/usr/bin/env  pyhton

import subprocess
import optparse

# Give arguments like --interface --mac  in the terminal  final
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac


# interface = input("interface > ")
# new_mac = input("new MAC > ")

print("[+] Changing the MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig " + interface + "down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + "up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
