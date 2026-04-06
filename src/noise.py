# src/noise.py
from scapy.all import sendp, IP, TCP, Ether
from config import SNIFF_INTERFACE

# We spoof a fake source IP since enp0s3 doesn't have one
packet = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src="192.168.56.10", dst="192.168.56.100") / TCP(dport=80, flags="S")

print(f"[*] Sending 1 SYN packet out of {SNIFF_INTERFACE}...")

#send() works at layer 3 {Network Layer}
sendp(packet, iface=SNIFF_INTERFACE)
