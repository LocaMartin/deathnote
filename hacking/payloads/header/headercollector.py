#!/usr/bin/env python3
import sys
import requests
from urllib.parse import urlparse
from typing import Set

def get_headers(url: str) -> requests.Response | None:
    """Get the HTTP response from a URL using HEAD request."""
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response
    except requests.RequestException:
        print(f"Error fetching {url}", file=sys.stderr)
        return None

def main():
    """Main function to process domains from stdin."""
    seen_headers: Set[str] = set()
    
    for line in sys.stdin:
        domain = line.strip()
        if not domain:
            continue
            
        # Ensure protocol is specified
        if not domain.startswith(('http://', 'https://')):
            domain = f"https://{domain}"
            
        # Get response
        response = get_headers(domain)
        if not response:
            continue  # Skip if request failed
        
        # Collect header names only
        headers = response.headers.keys()
        seen_headers.update(headers)
    
    # Print results
    print("Unique Headers Found:")
    print("-" * 50)
    for header in sorted(seen_headers):
        print(f"  - {header}")

if __name__ == "__main__":
    main()
