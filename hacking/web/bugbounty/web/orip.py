import argparse
import requests
from bs4 import BeautifulSoup
import dns.resolver
import re
import json
from concurrent.futures import ThreadPoolExecutor

# ---- ANSI Color Codes ----
class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# ---- Configuration ----
DNSDUMPSTER_URL = "https://dnsdumpster.com"
CRTSH_URL = "https://crt.sh/?q=%25.{}&output=json"
THREADS = 5

# ---- Helper Functions ----
def print_status(message, color=Color.YELLOW):
    print(f"{color}[*]{Color.RESET} {message}")

def print_success(message):
    print(f"{Color.GREEN}[+]{Color.RESET} {message}")

def print_error(message):
    print(f"{Color.RED}[!]{Color.RESET} {message}")

def get_historical_dns(domain):
    """Check DNSDumpster for historical DNS records"""
    try:
        session = requests.Session()
        resp = session.get(DNSDUMPSTER_URL)
        soup = BeautifulSoup(resp.content, "html.parser")
        csrf = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]
        headers = {"Referer": DNSDUMPSTER_URL}
        data = {"csrfmiddlewaretoken": csrf, "targetip": domain}
        resp = session.post(DNSDUMPSTER_URL, data=data, headers=headers)
        return set(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", resp.text))
    except Exception as e:
        print_error(f"DNSDumpster error for {domain}: {e}")
        return set()

def get_certificate_ips(domain):
    """Check crt.sh for SSL certificate IPs in SANs"""
    try:
        resp = requests.get(CRTSH_URL.format(domain), timeout=10)
        certs = resp.json()
        ips = set()
        for cert in certs:
            ips.update(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", cert.get("name_value", "")))
        return ips
    except Exception as e:
        print_error(f"crt.sh error for {domain}: {e}")
        return set()

def get_subdomain_ips(domain):
    """Resolve common subdomains to find IPs"""
    subdomains = ["direct", "origin", "staging", "api", "backend", "mail", "mx", "ftp", "old", "test"]
    resolver = dns.resolver.Resolver()
    ips = set()
    for sub in subdomains:
        try:
            answers = resolver.resolve(f"{sub}.{domain}", "A")
            ips.update(str(answer) for answer in answers)
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            continue
    return ips

def process_domain(domain):
    """Process a single domain and return results"""
    results = {
        "domain": domain,
        "historical_ips": list(get_historical_dns(domain)),
        "certificate_ips": list(get_certificate_ips(domain)),
        "subdomain_ips": list(get_subdomain_ips(domain))
    }
    results["all_ips"] = list(set(results["historical_ips"] + results["certificate_ips"] + results["subdomain_ips"]))
    return results

def main():
    parser = argparse.ArgumentParser(description=f"{Color.BOLD}Cloudflare Origin IP Finder{Color.RESET}")
    parser.add_argument("-d", "--domain", help="Single domain to scan")
    parser.add_argument("--file", help="File containing list of domains")
    parser.add_argument("-o", "--output", help="Save results to JSON file")
    parser.add_argument("-t", "--threads", type=int, default=THREADS, 
                       help=f"Number of threads (default: {THREADS})")
    args = parser.parse_args()

    domains = []
    if args.domain:
        domains.append(args.domain)
    if args.file:
        try:
            with open(args.file, "r") as f:
                domains.extend([line.strip() for line in f if line.strip()])
        except FileNotFoundError:
            print_error(f"File {args.file} not found")
            return

    if not domains:
        print_error("Please provide a domain (-d) or file (--file)")
        return

    print_status(f"Scanning {Color.CYAN}{len(domains)}{Color.RESET} domain(s)...", Color.CYAN)
    
    all_results = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = executor.map(process_domain, domains)
        all_results = list(results)

    # Print results with colors
    for result in all_results:
        domain_header = f"\n{Color.BOLD}{Color.UNDERLINE}Results for {result['domain']}{Color.RESET}"
        print(domain_header)
        
        print(f"{Color.CYAN}Historical IPs:{Color.RESET} {', '.join(result['historical_ips']) or 'None found'}")
        print(f"{Color.CYAN}Certificate IPs:{Color.RESET} {', '.join(result['certificate_ips']) or 'None found'}")
        print(f"{Color.CYAN}Subdomain IPs:{Color.RESET} {', '.join(result['subdomain_ips']) or 'None found'}")
        print(f"{Color.GREEN}Unique IPs:{Color.RESET} {', '.join(result['all_ips']) or 'No IPs found'}")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(all_results, f, indent=2)
        print_success(f"Results saved to {Color.CYAN}{args.output}{Color.RESET}")

if __name__ == "__main__":
    main()
