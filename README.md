🛡️ Threat Intelligence Aggregator
A simple Python script that collects Indicators of Compromise (IOCs) from multiple public threat intelligence feeds (no API key required). It parses and aggregates malicious IP addresses and URLs into a single CSV file for use in investigations, monitoring, or threat hunting.

📌 Features
🔍 Pulls malicious URLs from Abuse.ch URLhaus

⚠️ Collects IP addresses from Blocklist.de

🗂️ Aggregates threat intel into a unified .csv file

✅ Requires no API keys or authentication

🧠 Useful for SOC analysts, Blue Teamers, and threat researchers

🚀 Getting Started
🔧 Requirements
Python 3.x

requests module

Install dependencies:

bash
Copy
Edit
pip install requests
▶️ Run the Script
bash
Copy
Edit
python threat_aggregator.py
📂 Output
The script creates a file called:

Copy
Edit
public_threat_feeds.csv
With the structure:

Type	Indicator	Source
IP	185.100.87.50	Blocklist.de
URL	http://malicious-url.com	URLhaus
🧠 Use Cases
Feed data into a SIEM or firewall blocklist

Enrich SOC investigation workflows

Practice threat hunting with real-world IOCs

Learn basic threat intel automation

📌 Future Enhancements (Ideas)
Add more sources (OTX, MalwareBazaar, MISP)

JSON export and timestamp logging

IOC deduplication and reputation scoring

Email or Slack alerts for new threats

📜 License
MIT License


