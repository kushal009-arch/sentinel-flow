# Sentinel-Flow: Autonomous NDR Engine

## Project Overview
Sentinel-Flow is a Network Detection and Response (NDR) tool built to detect anomalies in live VM traffic using Machine Learning. Unlike rule-based firewalls, it learns a "Pattern of Life" to identify unknown threats.

## Architecture (C4 Model)
- **Level 1 (Context):** Monitors traffic between an Attacker (Kali) and the Network.
- **Level 2 (Containers):** 
    1. **Sniffer:** Python/Scapy (Raw Capture)
    2. **Processor:** Pandas (Feature Extraction)
    3. **Storage:** CSV (Data Cache)/ DataFrames
    4. **Brain:** Scikit-Learn (Isolation Forest)

## Tech Stack
- **OS:** Ubuntu (Sentinel-Flow), Kali Linux (Attacker)
- **Languages:** Python
- **Libraries:** Scapy, Pandas, Scikit-Learn
- **Methodology:** Agile, MoSCoW Scoping

## How to Run (Phase 1: Discovery)
Currently in Day 1: Environment setup and C4 Level 01 and Level 02 Diagram.
