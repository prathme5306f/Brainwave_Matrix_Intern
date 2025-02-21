import requests
import time
import json

# API key for VirusTotal (Ensure you keep it safe)
API_KEY = "(here put you're API key in given inverted commas)"
VT_URL = "https://www.virustotal.com/api/v3/urls"

def submit_url_for_scan(url):
    """Submits a URL to VirusTotal for analysis."""
    headers = {"x-apikey": API_KEY}
    data = {"url": url}
    response = requests.post(VT_URL, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json().get("data", {}).get("id", "")
    else:
        print("[ERROR] Failed to submit URL. Status Code:", response.status_code)
        return None

def fetch_scan_results(url_id):
    """Fetches the analysis results from VirusTotal."""
    time.sleep(10)  # Wait to ensure scan is completed
    headers = {"x-apikey": API_KEY}
    analysis_url = f"https://www.virustotal.com/api/v3/analyses/{url_id}"
    response = requests.get(analysis_url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("data", {}).get("attributes", {}).get("results", {})
    else:
        print("[ERROR] Failed to retrieve analysis results.")
        return {}

def analyze_results(results):
    """Processes the results and provides a summary."""
    malicious, suspicious = 0, 0
    for vendor, details in results.items():
        category = details.get("category", "")
        if category == "malicious":
            malicious += 1
        elif category == "suspicious":
            suspicious += 1
    
    return malicious, suspicious

def scan_url(url):
    """Handles the entire URL scanning process."""
    print("\n[INFO] Scanning:", url)
    url_id = submit_url_for_scan(url)
    if not url_id:
        return
    
    results = fetch_scan_results(url_id)
    malicious, suspicious = analyze_results(results)
    
    print("\n[🔍] VirusTotal Scan Results:")
    print(f"   🛑 Malicious Reports: {malicious}")
    print(f"   ⚠️ Suspicious Reports: {suspicious}")
    print(f"   🔗 Full Report: https://www.virustotal.com/gui/url/{url_id}")
    
    if malicious > 0:
        print("🚨 [ALERT] This URL is flagged as MALICIOUS!")
    elif suspicious > 0:
        print("⚠️ [WARNING] This URL appears SUSPICIOUS. Proceed cautiously!")
    else:
        print("✅ [SAFE] No threats detected.")

def main():
    print("===== Phishing Link Scanner =====")
    url = input("Enter URL to check: ").strip()
    scan_url(url)
    
if __name__ == "__main__":
    main()
