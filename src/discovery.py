# src/discovery.py
from scapy.all import conf

def list_interfaces():
    print("--- Sentinel-Flow: Interface Discovery ---")
    
    # conf.ifaces is a dictionary-like object containing all detected interfaces
    interfaces = conf.ifaces
    
    print(f"{'Name':<15} {'MAC Address':<20} {'IP Address':<15}")
    print("-" * 50)
    
    for iface_name in interfaces:
        details = interfaces[iface_name]
        
        # We extract the human-readable name, the hardware MAC, and the logical IP
        name = details.name
        mac = details.mac if details.mac else "NO MAC"

        ip = details.ip if details.ip != None else "NO IP"
        
        print(f"{name:<15} {mac:<20} {ip:<15}")

if __name__ == "__main__":
    list_interfaces()
