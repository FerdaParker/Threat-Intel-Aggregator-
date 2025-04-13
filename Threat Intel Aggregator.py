import requests
import csv

# Output file
output_file = "public_threat_feeds.csv"
iocs = []

# Source 1: URLhaus (malicious URLs)import requests
import csv

output_file = "Public_threat_feeds.csv"
iocs = []

def fetch_urlhaus():
    print("[*] Fetching from URLhaus...")
    url = "https://urlhaus.abuse.ch/downloads/text/"
    try:
        response = response.get(url)
        if response.status_code == 200:
            for line in response.text.splitlines():
                iocs.append({
                    "type": "URL"
                    "indicator": line.script(),
                    "source": "URLhaus"
                })
    except Exception as e:
        print(f"[!] Error fetching URLhaus: {e}")

def fetch_blocklistde():
    print("[*] Fetching from Blocklist.de...")
    url = "https://lists.blocklist.de/lists/all.txt"
    try:
        response = requests.get(url)
        if response.status_code == 200
            for line in response.text.splitlines():
                if line.strip():
                    iocs.append({
                        "type": "IP"
                        "indicator": line.strip(),
                        "source": "Blocklist.de"
                    })
    except Exception as e:
        print(f"[!] Error fetching Blocklist.de: {e}")

print(f"[*] Writing {len(iocs)} IOCs to {output_file}")
with open (output_file, mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["type", "indicator", "source"])
    writer.writeheader()
    writer.writerows(iocs)

print ("Threat Intel Aggregation Complete")
def fetch_urlhaus():
    print("[*] Fetching from URLhaus...")
    url = "https://urlhaus.abuse.ch/downloads/text/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            for line in response.text.splitlines():
                if not line.startswith("#") and line.strip():
                    iocs.append({
                        "type": "URL",
                        "indicator": line.strip(),
                        "source": "URLhaus"
                    })
    except Exception as e:
        print(f"[!] Error fetching URLhaus: {e}")

# Source 2: Blocklist.de (bad IPs)
def fetch_blocklistde():
    print("[*] Fetching from Blocklist.de...")
    url = "https://lists.blocklist.de/lists/all.txt"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            for line in response.text.splitlines():
                if line.strip():
                    iocs.append({
                        "type": "IP",
                        "indicator": line.strip(),
                        "source": "Blocklist.de"
                    })
    except Exception as e:
        print(f"[!] Error fetching Blocklist.de: {e}")

# Fetch from sources
fetch_urlhaus()
fetch_blocklistde()

# Save to CSV
print(f"[*] Writing {len(iocs)} IOCs to {output_file}")
with open(output_file, mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["type", "indicator", "source"])
    writer.writeheader()
    writer.writerows(iocs)

print("Threat intel aggregation complete.")