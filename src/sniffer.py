# src/sniffer.py
from scapy.all import sniff, IP, TCP
from config import SNIFF_INTERFACE

def packet_callback(packet):
	"""
	This function is called for every packet captured. 
	It's our processing plant.
	"""

	# Check if the packet has an IP layer (layer 3)
	if packet.haslayer(IP):
		src_ip = packet[IP].src
		dst_ip = packet[IP].dst
		proto = packet[IP].proto
		ttl = packet[IP].ttl

		# Check if it also has a TCP Layer (Layer 4)
		if packet.haslayer(TCP):
			payload_size = len(packet[TCP].payload)
			flags = packet[TCP].flags
			dport = packet[TCP].dport

			print(f"[TCP] {src_ip} --> {dst_ip}:{dport} | TTL: {ttl} | Flags: {flags} | Size: {payload_size} bytes")

		else:
			print(f"[IP] {src_ip} --> {dst_ip} | Protocol: {proto}")

def start_sniffer():
	print(f"[*] Starting Sentinel-Flow sniffer on {SNIFF_INTERFACE}")
	print(f"[*] Press Ctrl+C to stop.")

	# sniff() is the core scapy function
	# iface is the ear we choose 
	# prn is the callback function to run on each packet
	# store=0 means don't keep packets in RAM to prevent memory leaks
	sniff(iface=SNIFF_INTERFACE, prn=packet_callback, store=0)

if __name__ == "__main__":
	start_sniffer()
