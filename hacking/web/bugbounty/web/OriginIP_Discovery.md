**What is Origin IP ?**

 Origin IP refers to the source IP address from which a request or interaction with a target system originates.

1. Check Historical DNS Records

    Why: Websites often switch to Cloudflare after initial deployment, leaving historical DNS records pointing to the origin IP.

    Tools:

        SecurityTrails (securitytrails.com): Search historical DNS data.

        ViewDNS.info (viewdns.info): Check historical IPs.

        DNSdumpster (dnsdumpster.com): Map historical infrastructure.

2. Analyze SSL/TLS Certificates

    Why: Misconfigured servers may expose origin IPs in SSL certificates.

    Steps:

        Use Censys (censys.io) or Crt.sh (crt.sh) to search SSL certificates for the domain.

        Look for IP addresses in the certificate's Subject Alternative Names (SANs).

3. Subdomain Enumeration

    Why: Subdomains (e.g., staging.example.com, direct.example.com) might bypass Cloudflare.

    Tools:

        Sublist3r or Amass: Enumerate subdomains.

        Shodan (shodan.io): Search for subdomains with direct IP exposure.

    Example:
    Copy

    dig staging.example.com

4. Check Misconfigured Services

    Email Servers (MX Records):

        Check MX records: dig MX example.com.

        Email servers sometimes share infrastructure with the origin server.

    Old Ports:

        Scan non-standard ports (e.g., 8080, 8443) with Nmap or Masscan.

5. Cloudflare Bypass via Vulnerabilities

    SSRF (Server-Side Request Forgery):

        If you find an SSRF vulnerability, use it to fetch internal metadata (e.g., AWS IMDS) or internal IPs.

    DNS Rebinding:

        Exploit DNS misconfigurations to bypass Cloudflare.

6. Check Cloudflare-specific Headers

    Headers like CF-Connecting-IP:

        If the origin server leaks headers, it might expose internal IPs (rare in modern setups).

7. Search Public Databases

    Shodan/Censys:

        Search for the domain name in Shodan/Censys. The origin server might have hosted other services with the same IP.

    Wayback Machine (archive.org):

        Check historical snapshots for exposed IPs.

8. WHOIS and ASN Lookups

    ASN Search:

        Use BGPView (bgpview.io) to find the organization's Autonomous System Number (ASN) and associated IP ranges.

    WHOIS:

        Use whois example.com to identify IP ranges owned by the organization.