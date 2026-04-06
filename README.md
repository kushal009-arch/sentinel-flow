# Sentinel-Flow: Network Detection & Response (NDR) Engine

Sentinel-Flow is a behavioral "Digital Immune System" for Ubuntu environments. Unlike signature-based firewalls, it utilizes an **Isolation Forest** (Unsupervised ML) to identify network anomalies such as SYN Floods, Port Scans, and OS Fingerprinting attempts.

## Project Architecture (C4 Level 2)
The system follows a modular pipeline:
1. **Traffic Ingestion:** Raw packet capture via Scapy on a silent interface.
2. **Feature Extraction:** Dissecting the TCP/IP stack for behavioral markers (TTL, Flags, Window Size).
3. **Processor:** Transforming live streams into structured datasets using Pandas.
4. **Brain:** Anomaly detection via Scikit-Learn.

## Current Progress: Phase 2 (The Senses)
We have successfully implemented the **Dissector** module. The engine can now programmatically discover network interfaces and extract "DNA markers" from live traffic.

### Key Capabilities:
- **Interface Discovery:** Automated identification of the "Stealth" internal adapter.
- **Protocol Dissection:** Real-time extraction of Layer 3 (IP) and Layer 4 (TCP) headers.
- **Behavioral Markers:** Tracking of **TTL** (for OS detection) and **TCP Flags** (for handshake analysis).
- **Synthetic Testing:** Custom Layer 2 packet generator for testing silent/isolated networks.

## Getting Started
### Prerequisites
- Ubuntu 24.04 VM
- Python 3.12+
- Scapy

### Running the Dissector
1. Ensure your internal interface is configured in `src/config.py`.
2. Run the sniffer with root privileges:
	```bash
   sudo python3 src/sniffer.py
	```
3. To test the engine on an isolated network, use the internal noise generator:
	```bash
	sudo python3 src/noise.py
	```
### Security & Privacy
- Environment Isolation: All local VM specifics (IPs, Interface names) are stored in src/config.py and are excluded from version control via .gitignore.

- Passive Monitoring: The engine is designed to run on interfaces with No IP address, making the sensor invisible to standard network scans.
