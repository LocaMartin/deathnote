<div align="center">
<h1>Network Misconfiguration</h1>
</div>

<div align="center">
<details>
<summary><strong>Table of Content</strong></summary>

|Section|Description|
|---|---|
|**[DNS](#dns)**|DNS-related misconfigurations (e.g., Rebinding, Tunneling)|
|**[TCP](#tcp)**|Common TCP misconfigurations like open services, weak auth|
|**[UDP](#udp)**|UDP protocol issues including open resolvers, TFTP leaks|
|**[SMTP / Email](#smtp--email)**|Email-related issues (SPF, DKIM, relays)|
|**[FTP / SFTP](#ftp--sftp)**|Insecure file transfer configurations|
|**[SMB](#smb)**|Windows file sharing (SMBv1, guest access, NTLM)|
|**[NTP](#ntp)**|Time protocol misconfigs like amplification attacks|
|**[ICMP](#icmp)**|Ping/tunnel-based issues, DoS vectors|
|**[SNMP](#snmp)**|Network management issues (default communities, exposure)|
|**[LDAP](#ldap)**|Directory service vulnerabilities|
|**[RDP](#rdp)**|Remote Desktop Protocol issues (exposed ports, clipboard)|
|**[VPN / Tunneling](#vpn--tunneling)**|VPN-specific weaknesses (no MFA, split tunneling)|
|**[MQTT / AMQP / Broker](#mqttamqpbroker)**|IoT messaging protocol issues (no auth, wildcard topics)|
|**[SSH](#ssh)**|SSH-related threats like open ports, weak keys|
|**[WinRM](#winrm)**|Remote PowerShell execution (auth, access controls)|
|**[MSSQL](#mssql)**|SQL Server misconfigs (xp_cmdshell, internet exposure)|
|**[HTTP / HTTPS](#http--https)**|Web layer issues (SSRF, CORS, proxy bypass)|

</details>


### DNS

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**DNS Rebinding**|DNS + HTTP|DNS TTL misuse or wildcard DNS, browser trust of repeated lookups|Bypass browser same-origin policy|Host a domain that resolves to attacker IP, then rebinding to 127.0.0.1 or internal IP|Access internal apps (Elasticsearch, Redis, dashboards) via browser|
|**Subdomain Takeover**|DNS + HTTP|CNAME points to unclaimed 3rd-party resource (S3, GitHub, Heroku, etc.)|Gain control of abandoned subdomain|Claim resource, serve payload/XSS/phishing page|Full control over subdomain, phishing, XSS, CSRF|
|**CNAME Chain Rebinding**|DNS|Multiple CNAME levels mask ultimate resolution to internal IP|Evade SSRF filters or local IP detection|CNAME → CNAME → 127.0.0.1 → `localhost`|SSRF targeting internal services, metadata endpoints|
|**Internal DNS Zone Leak**|DNS|Recursion and/or zone transfer enabled for unauthorized clients|Enumerate internal records|Attempt zone transfers (AXFR) or brute subdomain queries|Discovery of sensitive hosts (e.g. dev-db, vault, staging-api)|
|**DNS Cache Poisoning**|DNS (UDP/TCP)|Insufficient validation, no DNSSEC, predictable TXIDs|Insert malicious DNS entries into resolver|Spoofed response sent faster than legitimate DNS server|Redirect to phishing sites, MITM, domain hijack|
|**DNS Tunneling**|DNS (UDP/TCP)|Lack of DNS egress control, firewall allows all outbound DNS|Establish covert channel (C2, data exfiltration)|Encode data in subdomain of DNS queries to controlled domain|Bypass firewalls, maintain C2, exfil sensitive data|
|**Open DNS Resolver**|DNS (UDP)|Resolver accessible to all IPs (not IP-restricted)|Reflection/amplification DDoS or DNS recon|Spoofed DNS queries with victim IP|Amplification DDoS, leak internal name resolution|
|**Wildcard DNS**|DNS|Wildcard `*.` DNS records misused or misconfigured|Unexpected routing, phishing, abuse of dynamic subdomains|Any non-existent subdomain resolves to attacker domain|Cookie scope abuse, phishing on unexpected subdomains|
|**Dynamic DNS Abuse**|DNS|Misconfigured dynamic DNS (DDNS) or lack of validation|Persist C2 / phishing under trusted domain|Register attacker-controlled dynamic subdomains|Evade blocklists, maintain stealthy presence|
|**TTL Manipulation**|DNS|Extremely low TTL (or 0) set intentionally or misconfigured|Force frequent re-resolution of attacker domains|Rebind IP rapidly or poison caches|Help DNS rebinding, stealthy phishing infrastructure|
|**Leaky Reverse DNS**|DNS|PTR records exposed or misconfigured|Map internal systems via reverse lookups|Perform `dig -x` or automated PTR scans|Leak naming conventions, user IDs, environment layout|
|**Split-horizon DNS exposed**|DNS|Split-view DNS zones accidentally exposed externally|Leak internal-only DNS records|DNS responses differ for internal vs external clients|Bypass perimeter, enumerate infrastructure|
|**Misconfigured DNSSec**|DNS|Missing, expired, or broken DNSSEC records|Disable integrity validation|Tamper or downgrade DNS validation|Makes spoofing easier, enables cache poisoning|
|**NXDOMAIN Hijacking**|DNS + CDN|Non-existent domains caught by wildcard catch-all/CDN provider|Abuse for content injection or phishing|Register `.cdnprovider.net` CNAME catchalls|Host malicious content under unused subdomains|
|**Recursive DNS on Auth Servers**|DNS|Authoritative DNS servers also act as resolvers|Allow attackers to abuse recursion on sensitive infra|Use auth server for external DNS queries|Cache pollution, zone enumeration, performance DoS|
|**Response Policy Zone (RPZ) Misconfig**|DNS|RPZ rules allow or block wrong domains|Enable/disable access to malicious domains|RPZ list misapplied or misaligned|Block legitimate services or allow malicious domains|
|**Lame Delegation**|DNS|NS records configured for zones that don’t respond|Resolution fails or leaks to wrong nameserver|Delegation to unreachable/broken NS|Failed DNS queries, timeout issues, data leaks|
|**CDN Domain Fronting (via DNS)**|DNS + CDN + HTTPS|Misuse of SNI vs Host header routing mismatch|Hide true destination of traffic|Use CDN’s shared IP for disguised TLS tunnels|Censorship evasion, phishing, stealth C2|
|**DNS Zone Transfer Leak**|DNS (TCP)|AXFR allowed without IP ACLs|Download full zone contents|Use `dig AXFR @ns1.example.com example.com`|Leak of all internal/external records|

### TCP

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Publicly Exposed Services**|TCP (various)|Services bound to `0.0.0.0`, no firewall/ACL|Remote access to internal services|Scan with Shodan, Nmap, masscan|Unauthorized access to DBs (Redis, Mongo, etc.), RCE|
|**Lack of Rate Limiting**|TCP (any login service)|No per-IP rate limit on TCP endpoints|Brute-force password guessing|Repeated login attempts|Account compromise, credential stuffing|
|**No SYN Cookie Protection**|TCP|No defense against SYN floods|Denial of Service|Flood with SYN packets without completing handshake|Exhaust server resources, DoS|
|**XSPA (Cross-Site Port Attack)**|TCP + HTTP|Browser allows internal resource loading|Port scan from victim’s browser|Load `<img src="http://localhost:PORT">` or via JS|Identify internal services, SSRF vector discovery|
|**Service on Non-Standard Port**|TCP|Obscure services running on uncommon ports|Avoid detection, bypass firewalls|Port scans reveal hidden services|Unexpected exposure of admin/dev interfaces|
|**Misconfigured Access Control**|TCP|No IP filtering on exposed ports|Allow unauthorized connections|Direct TCP connections to internal service|Control panels, APIs, message brokers exposed|
|**Weak Auth or No Auth**|TCP (custom or legacy services)|Service has no authentication layer|Full access to backend without creds|Connect via telnet/nc/custom client|Admin/root-level access|
|**Unencrypted TCP Protocols**|TCP|No TLS on sensitive services|Eavesdrop or MITM plaintext sessions|Sniff packets on same network|Leak passwords, sessions, queries|
|**Port Knocking Misconfigured**|TCP|Knocking mechanism exposed or bypassed|Unauthorized access to protected ports|Scan for open ports or guess knock sequence|Bypass perimeter firewall, gain shell|
|**TCP Reset Injection**|TCP|Middleboxes misconfigured or vulnerable|Terminate legitimate connections|Inject spoofed TCP RSTs|Interrupt sessions, DoS|
|**Improper Service Banner**|TCP (SMTP/FTP/SSH/etc.)|Verbose banner leaks version info|Gather recon/fingerprint services|Connect and read banner or error messages|Target version-specific exploits|
|**TCP Fast Open Misuse**|TCP|TFO used without proper validation|Replay or spoof connection attempts|Send data in initial SYN|Bypass firewall rules, injection|
|**Default Creds on TCP Services**|TCP (Telnet, FTP, DB)|Default credentials not changed|Unauthorized access|Login via default username/password|Root/admin control, lateral movement|

### UDP

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Open DNS Resolver**|UDP (DNS)|Resolver accessible from internet|DDoS via reflection, info leakage|Spoofed DNS queries with victim IP|Reflection/amplification DDoS, internal hostname leak|
|**DNS Tunneling**|UDP (DNS)|No outbound DNS control, no DPI|Covert data exfiltration or C2|Encode payload in DNS queries to attacker domain|Bypass firewalls, leak credentials/files|
|**DNS Cache Poisoning**|UDP (DNS)|Predictable TXID, no DNSSEC|Insert malicious DNS entries|Spoof DNS reply before legitimate one arrives|Redirect victims to malicious sites|
|**Open NTP Server**|UDP (NTP)|No IP restriction on `monlist` or responses|Amplify DDoS attacks|Use spoofed requests to elicit large NTP replies|Amplification DDoS, up to 550x|
|**SNMPv1/2c Enabled with Default Strings**|UDP (SNMP)|"public"/"private" left unchanged|Device reconnaissance|Use `snmpwalk` with default creds|Network topology disclosure, device config leak|
|**SSDP/UPnP Exposed**|UDP (1900)|UPnP/SSDP services exposed to WAN|Internal network discovery, pivoting|SSDP request from LAN or internet|Device info leakage, NAT table manipulation|
|**TFTP Exposed**|UDP (TFTP)|TFTP open to all IPs, no auth|Download/upload configuration files|Send `GET` or `PUT` to known paths|Leak of config files, credential theft|
|**mDNS (Multicast DNS) Leak**|UDP (5353)|mDNS service running on public interface|Service enumeration|Query via multicast or replay sniffed mDNS packets|Service name, hostname, OS, printer info disclosure|
|**No Source Port Randomization**|UDP (DNS/NTP/etc.)|Static or predictable source ports|Easier spoofing attacks|Predict port + TXID → forge responses|Cache poisoning, DoS, hijack attacks|
|**UDP Port Multiplexing Misuse**|UDP (custom)|Services sharing a port without auth checks|Gain unintended access|Send crafted datagrams to multiplexed service|Message leakage or unauthorized response|

### SMTP / Email

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Open Mail Relay**|SMTP|Relay allowed for unauthenticated or external IPs|Send spam or spoofed emails|Connect to SMTP server and spoof sender/recipient|Spam, phishing, IP/domain blacklisting|
|**Missing SPF Record**|SMTP + DNS|No `SPF` TXT record in DNS|Allow attacker to spoof sending domain|Forge emails from trusted-looking domains|Email spoofing, BEC (Business Email Compromise)|
|**Missing DKIM Signature**|SMTP + DNS|No DKIM key or signing misconfigured|Skip email integrity verification|Strip/mangle headers, modify email content|Message tampering, impersonation|
|**Missing or Weak DMARC Policy**|SMTP + DNS|No DMARC policy, or `p=none`|Lack of spoofing enforcement|Abuse SPF/DKIM absence or bypass|Undetected email spoofing campaigns|
|**SMTP STARTTLS Downgrade**|SMTP|STARTTLS not enforced or fallback allowed|Force plaintext email delivery|Strip STARTTLS support via MITM|Credential sniffing, message interception|
|**Self-Signed or Expired TLS Certs**|SMTP|Poor TLS config for mail delivery|MITM email transmission|TLS cert not validated or expired|Message interception, downgrade attacks|
|**Exposed Webmail Interface**|HTTP + SMTP|Webmail login page open on internet|Credential theft or brute force|Find `/webmail`, `/roundcube`, `/mail` etc.|Account takeover, full mailbox access|
|**Credential Stuffing via SMTP Auth**|SMTP (AUTH LOGIN)|Weak or reused credentials|Gain authenticated access|Brute-force or reuse leaked email/password combos|Spam, phishing from legit mailboxes|
|**SMTP VRFY/EXPN Commands Enabled**|SMTP|Legacy commands not disabled|Enumerate valid email addresses|Use `VRFY user@domain.com` or `EXPN` lists|User discovery, social engineering, recon|
|**Misconfigured Submission Port (587)**|SMTP|Allows relay without proper authentication|Abuse relay channel|Send unauthenticated mail via submission port|Relay spam from legitimate infra|
|**SMTP Header Injection**|SMTP|Lack of input sanitization|Spoof sender, BCC exfil|Inject CRLF into mail headers|Phishing, internal BCC exfiltration|
|**Lack of Rate Limiting on Auth/RCPT**|SMTP|No throttling on login or RCPT TO|Brute force or DoS|Rapid credential guess or RCPT flooding|Account takeover or mail queue DoS|
|**Verbose SMTP Banners**|SMTP|Banner shows software and version info|Aid attacker recon|Grab banner using telnet/Netcat|Target version-specific vulnerabilities|

### FTP / SFTP

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Anonymous FTP Access**|FTP|`anonymous` login enabled by default|Unauthorized access to files|Login with username `anonymous` and any email|Data leakage, malware distribution, abuse of storage|
|**Unencrypted FTP Sessions**|FTP|No TLS/SSL (FTPS) or insecure config|Intercept credentials and files|MITM on control or data channels|Plaintext credential theft, file leakage|
|**Weak SFTP Authentication**|SFTP (over SSH)|Password-based auth with weak creds|Brute-force login to shell/file system|Password guessing via SSH clients or bots|Remote shell, data theft, lateral movement|
|**Default Credentials**|FTP/SFTP|Default usernames/passwords not changed|Gain unauthorized access|Use vendor-default login combos|Remote file access, privilege escalation|
|**Writable FTP Directories**|FTP|Permissions allow upload or overwrite|Upload malicious scripts or files|FTP `STOR` command to webroot or exec dir|Webshell upload, malware injection|
|**FTP Bounce Attack**|FTP|Passive FTP mode misconfigured (PORT reuse)|Port scan internal network via FTP|Use `PORT` command to target 3rd-party IPs|Internal port scanning, service discovery|
|**Directory Traversal Allowed**|FTP|Improper path sanitization|Access unauthorized directories|Use `..` or absolute paths in FTP commands|View system files (e.g., `/etc/passwd`)|
|**Exposed Config/Backup Files**|FTP/SFTP|Sensitive files stored in public directories|Access internal configs/secrets|Download `.bak`, `.conf`, `.sql` files|Leak credentials, DB dumps, API keys|
|**Banner Disclosure**|FTP/SFTP|Banner leaks version/platform info|Fingerprint for exploits|Use `ftp` client or `telnet` to read welcome banner|Exploit known CVEs tied to that version|
|**FTP over Tor / Hidden Services**|FTP|Service available over anonymized networks|Stealthy data transfer or C2|FTP over `.onion` service|Undetected data exfiltration, cybercrime hosting|
|**Weak SSH Ciphers in SFTP**|SFTP|Deprecated ciphers (e.g., `CBC`, `MD5`) enabled|Cryptographic downgrade or MITM|Force weak cipher use via client config|Traffic decryption, session hijack|
|**Excessive File Permissions**|FTP/SFTP|Files uploaded with `777` or similar|Allow code execution by attackers|Upload PHP/CGI and access via browser|Remote code execution via file server|
|**Logging Disabled or Misconfigured**|FTP/SFTP|No audit trail of user activity|Hide attacker footprints|Disable or rotate logs aggressively|Incident response blind spots|

### SMB

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**SMBv1 Enabled**|SMB (NetBIOS, CIFS)|Legacy protocol still allowed|Exploit known vulnerabilities|Use EternalBlue, SMBGhost, etc.|Remote code execution, ransomware (e.g., WannaCry)|
|**Guest Access Enabled**|SMB|Misconfigured share permissions (`Everyone`, `Guest`)|Access shared files without auth|Connect as Guest to `\\target\share`|Unauthorized data access, malware drop|
|**Null Sessions Allowed**|SMB|No restrictions on anonymous enumeration|Enumerate users, groups, shares|Tools like `enum4linux`, `rpcclient` without creds|Recon, user list harvesting, pivot planning|
|**SMB Signing Not Required**|SMB|Signing optional or disabled|MITM / relay attack|Intercept or tamper SMB messages|Credential relay, SMB spoofing, NTLM hash capture|
|**Sensitive Shares Exposed**|SMB|Share config includes backups, credentials, config dirs|Extract secrets from shared files|Browse/download files via SMB|Credential theft, config leaks (e.g., `config.php`)|
|**Writable Shares for Untrusted Users**|SMB|Misconfigured `write` permissions|Upload webshells or backdoors|Write to webroot or startup folders|Remote code execution, persistence|
|**Unpatched SMB Services**|SMB|Legacy Windows/Linux systems with known CVEs|RCE or privilege escalation|Use Metasploit, EternalSynergy, etc.|Full system compromise|
|**NTLM Authentication Only**|SMB|No Kerberos, only weak NTLM auth|Capture and relay NTLM hashes|Use Responder or relay tools|Credential reuse, domain compromise|
|**SMB Over Internet**|SMB|Port 445 exposed to the public|External attack surface|Shodan/Nmap, brute force, RCE|External compromise, ransomware entry point|
|**Named Pipe Exposure**|SMB + RPC|Insecure RPC pipes (`svcctl`, `samr`) accessible|Enumerate or control services remotely|Abuse over SMB with admin token or escalation|Remote service control, SAM dump, lateral movement|
|**Lack of Access Auditing**|SMB|No logging of access/share usage|Prevent incident detection|Exfiltrate quietly or map shares|Silent data theft, persistence setup|
|**IPC\$ Share Misuse**|SMB|IPC\$ (inter-process comms) share accessible to low-priv users|Abuse for recon or lateral moves|Connect to `\\host\IPC$` for remote commands|RPC-based recon, domain enumeration|

### NTP

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Open NTP Server**|NTP (UDP/123)|Server responds to unauthenticated requests from any IP|Amplify DDoS attacks|Send spoofed requests using victim’s IP|Reflection/amplification DDoS (up to 550x amplification)|
|**`monlist` / `ntpdc` Enabled**|NTP|Monitoring features not disabled|Abuse diagnostics for info or amplification|Send `ntpdc -c monlist` to target|Leak client IPs, amplify attacks, enable tracking|
|**No Source IP Filtering**|NTP|Accepts requests from untrusted IPs|Allow attacker interaction|Send crafted packets from anywhere|Information leak, potential spoofing|
|**Weak or Missing Authentication**|NTP|No key-based authentication for clients/servers|Spoof server responses|Spoof NTP time with fake updates|Time manipulation, break logs, bypass certs|
|**Time Spoofing / MITM**|NTP|Lack of integrity checks in sync traffic|Shift system time|MITM between client and server|Break scheduled jobs, session timeouts, log integrity|
|**Legacy NTP Versions**|NTP|Unpatched services running on outdated daemons|Exploit known CVEs (e.g., buffer overflows)|Send malformed packets to daemon|Remote DoS or potential RCE|
|**NTP over Public Internet**|NTP|Exposed to WAN without need|External targeting of internal services|Internet-based scans and spoofing|Service disruption or footprint in attacks|
|**Unrestricted Peer/Server Mode**|NTP|Allows bidirectional sync with unknown peers|Join NTP mesh and manipulate others|Send `mode 6` or `mode 7` control packets|Rogue peer can poison network-wide time|
|**No Logging / Monitoring**|NTP|Logs not enabled or retained|Evade detection of abuse|Perform attacks without traceability|Blindspot in SIEM, hard to trace spoof attempts|

### ICMP

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**ICMP Unrestricted (Echo Requests)**|ICMP|Firewall allows all ICMP types from any source|Host/network discovery|Ping sweeps, traceroute, automated scans|Helps attackers map networks for lateral movement|
|**ICMP Tunneling**|ICMP|No egress filtering or DPI on ICMP traffic|Covert data exfiltration / C2 channel|Tools like `icmp-tunnel`, `ptunnel`, `PingTunnel`|Stealthy backdoor, bypass firewalls and proxies|
|**ICMP Timestamp Response Enabled**|ICMP|Devices respond to timestamp requests (`type 13`)|Fingerprint OS/device uptime|Send `ICMP type 13` and read time info|OS fingerprinting, internal recon|
|**ICMP Redirect Enabled**|ICMP|Routers configured to send redirect messages|Hijack traffic to malicious gateway|ICMP Type 5 redirects from compromised routers|MITM, route manipulation, traffic diversion|
|**Fragmented ICMP Allowed**|ICMP|No filtering on fragmented ICMP packets|Evasion of detection systems|Send fragmented ICMP payloads to bypass DPI|IDS/IPS evasion, covert payload delivery|
|**Rate Limiting Disabled**|ICMP|ICMP flood not throttled or limited|Denial of Service|Ping flood (ICMP echo storm), Smurf attacks|Resource exhaustion, system unavailability|
|**No ICMP Logging**|ICMP|ICMP requests/replies not logged|Evade detection during recon|Silent sweeps or tunneling with no alerts|Undetected lateral movement, blindspot for blue team|
|**ICMP Type 3 (Unreachable) Leaks**|ICMP|Devices return detailed unreachable messages|Reveal internal network structure|Send spoofed packets to trigger ICMP errors|Firewall rules, subnet layouts disclosed|
|**Overly Broad ICMP Allow Rules**|ICMP|`ALLOW icmp` without restricting types/codes|Enable excessive access to ICMP functions|Custom-crafted ICMP messages|Exploitation of router/device behavior quirks|

### SNMP

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Default Community Strings**|SNMPv1/v2c (UDP/161)|`public`/`private` strings left unchanged|Enumerate network devices and configs|`snmpwalk -c public target`|Device info leak, config dump, printer/network abuse|
|**SNMPv1/SNMPv2c Enabled**|SNMP|Legacy versions with no encryption or auth|Eavesdrop SNMP traffic, spoof access|Passive sniffing or replaying requests|Device takeover, config reading/changing|
|**Write Community Access**|SNMP|Community string allows `RW` instead of `RO`|Modify device settings remotely|`snmpset -c private` with OIDs|Change router/firewall rules, reroute traffic|
|**SNMP Exposed to Internet**|SNMP|Port 161 open to WAN|Remote reconnaissance|Use `onesixtyone`, `snmpenum`, Shodan|Leak topology, device info, possible entry point|
|**No Access Control (ACLs)**|SNMP|SNMP daemon responds to any IP address|Unauthorized queries from external IPs|Remote SNMP queries without filtering|Leak of credentials, routing tables, SNMP traps|
|**SNMP Trap Listeners Misused**|SNMP (UDP/162)|Trap destinations misconfigured or overly permissive|Spoof SNMP alerts or intercept them|Send fake trap messages to admin listener|Alert suppression, redirection, false positives|
|**Unrestricted OID Access**|SNMP|No restriction on Management Information Base (MIB)|Dump full device state|Enumerate with full SNMP walk|Leak of software versions, interfaces, users|
|**SNMP Version Disclosure**|SNMP|Service leaks SNMP version during negotiation|Choose weakest version for attack|Connect with any SNMP scanner|Attack legacy (v1/v2c), force downgrade|
|**No Rate Limiting**|SNMP|Unrestricted request rate per IP|DoS device or brute force community strings|Flood SNMP requests or try multiple strings|Exhaust resources, leak via brute force|
|**Com**||||||

### LDAP

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential||
|---|---|---|---|---|---|---|
|**Anonymous Bind Enabled**|LDAP (389)|Directory allows unauthenticated queries|Enumerate users, groups, OUs|Connect with no credentials (`ldapsearch -x`)|User listing, brute-force prep, internal recon||
|**LDAPS Not Enforced**|LDAP (389)|No TLS used for directory connections|Intercept LDAP credentials or data|MITM LDAP bind request|Credential theft, session hijack||
|**Weak Bind DN Credentials**|LDAP|Low-complexity passwords for service accounts|Brute-force user binds|Password guessing on known Bind DNs|Auth bypass, lateral movement||
|**LDAP Injection**|LDAP + Web Apps|Unvalidated input passed to LDAP filters|Escalate privileges or bypass auth|Craft filter strings like \`*)(uid=*))(|(uid=\*\`|Privilege escalation, unauthorized access|
|**No Account Lockout Policy**|LDAP/AD|Infinite authentication attempts allowed|Brute-force user logins|Repeated bind requests using password lists|Account takeover, credential stuffing||
|**Excessive Directory Disclosure**|LDAP|Directory returns full user attributes|Leak of PII, emails, roles, etc.|Read `mail`, `telephoneNumber`, `memberOf` attrs|Phishing, spearphishing, insider recon||
|**Unrestricted Access to Sensitive OUs**|LDAP|ACLs not enforced for specific org units|Read/write to critical parts of directory|Modify group memberships or user attributes|Privilege escalation, persistence||
|**No Logging or Auditing**|LDAP|Bind and query operations not monitored|Hide attacker activity|Query and exfil without logs|Undetected recon, no forensics trail||
|**Fallback to Simple Bind Auth**|LDAP|Supports legacy auth without encryption|Transmit credentials in plaintext|Sniff on LAN or via MITM|Password theft, user impersonation||
|**Unfiltered LDAP Referrals**|LDAP|Accepts and follows external referrals|Redirect directory requests|Supply malicious LDAP server in response|Redirect queries for spoofing or DOS||
|**Exposed Global Catalog Port**|LDAP (3268/3269)|Global Catalog reachable from untrusted networks|Query cross-domain info|Connect to GC and extract user data|Cross-domain recon, lateral movement||
|**Stored Passwords in Attributes**|LDAP|Custom or legacy fields store credentials|Steal plaintext or weakly hashed creds|Read `userPassword`, `shadowLastChange`, etc.|Credential leak, full compromise||
|**LDAP Enumeration via Timing**|LDAP|Response time varies based on query correctness|Enumerate valid users|Use response time for valid/invalid usernames|Low-noise recon, bruteforce prep||

### RDP

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Exposed RDP Port (3389)**|RDP (TCP/3389)|RDP open to internet without filtering|Remote access to internal systems|Port scans + brute-force (Hydra, Ncrack, Shodan)|Remote desktop takeover, ransomware delivery|
|**Weak NLA Enforcement**|RDP|Network Level Authentication (NLA) not required|Trigger RDP protocol-level vulnerabilities|Exploit BlueKeep (CVE-2019-0708), etc.|Pre-auth RCE, system compromise|
|**Default or Weak Credentials**|RDP|No enforced password policy|Gain remote access via guessable creds|Brute-force admin/RDP user accounts|Privileged system access|
|**No Account Lockout Policy**|RDP (AD/Windows)|Unlimited login attempts allowed|Credential stuffing / brute force|Repeated RDP login attempts|Account compromise, DoS via password exhaustion|
|**Clipboard / Drive Redirection Enabled**|RDP|Default feature allows bidirectional data sharing|Exfiltrate or implant files silently|Copy sensitive files over clipboard or drive map|Data theft, malware injection|
|**Outdated RDP Client/Server**|RDP|Missing patches for client/server|Exploit known vulnerabilities|CVEs like DejaBlue, RDP clipboard channels|RCE or elevation of privilege|
|**RDP Without Encryption / Using RC4**|RDP|Weak or outdated TLS/cipher usage|Decrypt session traffic|MITM with access to network|Credential or session data leak|
|**No MFA on RDP Logins**|RDP|Sole reliance on password-based auth|Bypass single-factor login|Compromise credentials via phishing or brute-force|Full access without resistance|
|**Verbose Error Messages**|RDP|Error reveals valid usernames or AD structure|User enumeration|Use failed login messages (e.g., “user not found”)|Recon for targeted password attacks|
|**RDP Over VPN Without Restriction**|RDP + VPN|RDP allowed over VPN without segmentation|Pivot post-VPN auth|Use VPN access to target RDP inside|Lateral movement, privilege escalation|
|**RDP Session Hijack (via Token Theft)**|RDP|Insecure handling of session tokens|Steal active RDP session|Use tools like `mimikatz`, `RDPHijack`|Full session takeover without login|
|**No Session Timeout or Idle Lock**|RDP|Session persists indefinitely|Piggyback on stale sessions|Reuse or connect to idle sessions|Silent access, data exfiltration|

### VPN / Tunneling

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Weak VPN Authentication**|OpenVPN, IKEv2, L2TP, PPTP|Use of weak shared secrets, password-only auth|Unauthorized remote access|Brute-force VPN creds or reuse leaked passwords|Bypass perimeter security, internal access|
|**Split Tunneling Enabled**|VPN (all)|Traffic not forced through VPN|Leak internal data over insecure networks|Access corp/internal IPs while user browses internet|Sensitive data exposure, traffic hijacking|
|**No MFA for VPN Logins**|VPN + RADIUS/LDAP|VPN relies solely on passwords|Bypass access control|Use stolen or brute-forced creds|Full remote access with minimal resistance|
|**Reused VPN Credentials**|VPN + LDAP/AD|Passwords reused across services|Lateral movement from other breaches|Credential stuffing from leaks|Rapid compromise across services|
|**VPN Accessible from Any IP**|VPN|No geo-IP or IP whitelisting in place|Allow unrestricted VPN attempts|Botnet-driven brute force|External RDP/SMB/HTTP exposure post-auth|
|**Poor Certificate Handling**|OpenVPN, IPsec|Certificates not validated or rotated|Spoof servers or persist access|MITM, stolen certs reused by attacker|Credential theft, persistent access|
|**Deprecated Protocols Enabled**|PPTP, L2TP, IKEv1|Legacy VPN protocols not disabled|Exploit protocol-level flaws|Use known exploits or weak crypto|RCE, decryption, session hijack|
|**Leaky VPN DNS**|VPN + DNS|DNS requests not tunneled via VPN|Internal hostname leakage|Monitor DNS over local resolver|Reveal accessed hosts, exfil domain names|
|**Credential in Config Files**|VPN (clients)|Hardcoded passwords in `.ovpn` or `.conf`|Credential theft|Access local client files or GitHub leaks|Remote access via recovered config|
|**No Logging or Anomaly Detection**|VPN (server)|Auth logs not monitored|Evade detection|Repeated login attempts go unnoticed|Persistent attacker presence|
|**Open Internal Routes Without Access Control**|VPN + Routing|VPN assigns unrestricted subnet access|Access segmented or sensitive services|Access `10.x.x.x`, `192.168.x.x` freely|Access to database, dev, prod environments|
|**Lack of Session Timeout / Idle Detection**|VPN|VPN sessions remain indefinitely active|Maintain stealth access|Never-expiring sessions|Long-lived, unmonitored backdoor|
|**No Endpoint Validation**|VPN|Any device can connect if creds/certs valid|Bypass corporate controls|Compromised or unpatched personal devices connect|Malware entry, unscanned devices inside LAN|

### MQTT/AMQP/Broker

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Unauthenticated Broker Access**|MQTT, AMQP|Authentication disabled or optional|Read/publish to message topics/queues|Connect directly to broker (e.g., Mosquitto, RabbitMQ)|IoT data theft, command injection, spoofed telemetry|
|**Default Credentials**|MQTT, AMQP|Default `guest:guest`, `admin:admin` unchanged|Gain unauthorized access|Login using factory/default creds|Admin panel access, queue/topic takeover|
|**Anonymous Access Allowed**|MQTT|Broker permits anonymous clients|Bypass identity enforcement|Connect with no username/password|Read/write sensitive data streams|
|**Wildcard Subscriptions**|MQTT|Broker allows `#` or `+` wildcards|Subscribe to all topics|Subscribe to `#`, intercept all messages|Global data leak, passive monitoring|
|**Open Internet Exposure**|MQTT, AMQP|Broker listening on public IP without IP filtering|Remote unauthorized access|Use Shodan to find brokers|Botnet C2 channel, sensitive data leak|
|**No TLS Encryption**|MQTT, AMQP|Plain TCP with no SSL/TLS wrapper|Intercept or tamper data|MITM, sniff credentials and messages|Data integrity loss, stolen auth, device hijack|
|**Lack of ACLs**|MQTT, AMQP|All clients can publish/subscribe freely|Abuse or overwrite important data|Inject to system control or sensor queues|IoT malfunction, denial of control|
|**Management Panel Exposed**|AMQP (RabbitMQ), MQTT|Web UI available without auth/IP restriction|Take over broker configuration|Access admin panel at `/admin` or `:15672`|Queue manipulation, user creation, backdoor|
|**Retained Messages Misuse**|MQTT|Retained flag used without expiration|Persistent injection of malicious data|Send retained payload to important topic|Replay or poison messages for new clients|
|**Unrestricted Topic Naming**|MQTT|No rules on topic structure or limits|Abuse topic namespace|Flood broker with thousands of topics|Broker crash or DoS due to overload|
|**Insecure Bridge Config**|MQTT|Broker bridging without auth or filtering|Cross-broker hijack or sniff|Bridge a malicious broker to trusted one|Inter-broker takeover, cross-domain data leak|
|**Heartbeat/Keepalive Disabled**|MQTT, AMQP|Idle clients stay connected indefinitely|Maintain long-lived C2 or listener|Establish persistent channel via idle client|Covert channel for APTs, exfiltration path|

### SSH

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Password Authentication Enabled**|SSH (TCP/22)|Password-based login allowed|Brute-force or credential reuse|Use tools like Hydra, Ncrack on SSH login|Unauthorized shell access|
|**Weak or Reused Credentials**|SSH|Poor password hygiene or shared accounts|Gain shell access|Reuse leaked creds or brute-force|System compromise, lateral movement|
|**Root Login Enabled**|SSH|`PermitRootLogin yes` in sshd\_config|Direct root access without privilege escalation|Brute-force or login as `root`|Immediate full-system control|
|**No Rate Limiting / Lockout**|SSH|Lack of fail2ban or equivalent|Unlimited login attempts|Dictionary or password spraying attacks|Credential stuffing success, DoS via brute|
|**SSH Keys Without Passphrase**|SSH|Private keys not protected|Use stolen keys without cracking|Dump `.ssh/id_rsa` from compromised device|Silent and persistent access|
|**Authorized Keys Mismanagement**|SSH|Keys added by automation/scripts|Maintain persistent access|Inject into `.ssh/authorized_keys`|Hidden backdoor, hard to detect|
|**Open SSH Port (22) to Internet**|SSH|No IP whitelisting or VPN restriction|Attack surface expansion|Shodan, Censys, or random scans|External entry point for attackers|
|**Weak Host Key Algorithms**|SSH|Use of deprecated ciphers like DSA, MD5|Downgrade or break crypto|Force downgrade, MITM attempts|Session hijack, encrypted traffic weakening|
|**Agent Forwarding Enabled**|SSH|Default SSH config or convenience|Steal forwarding tokens|Attacker pivots from compromised host|Lateral movement using stolen auth|
|**No Idle Timeout**|SSH|Sessions stay open indefinitely|Hijack open sessions|Reuse active shell from exposed terminals|Unattended access, data theft|
|**Verbose SSH Banner**|SSH|System reveals version details or OS info|Aid fingerprinting|Banner shows `OpenSSH 7.2p2 Ubuntu` etc.|Target-specific exploits become easier|
|**SSH Over Weak Transport (No VPN)**|SSH|No tunnel or bastion host used|Intercept metadata or brute from public IPs|Direct SSH from internet|Traffic metadata leaks, easier attack surface|

### WinRM

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**WinRM Enabled on Public Interface**|WinRM (HTTP/5985, HTTPS/5986)|Default config allows external access|Remote command execution|Connect via `evil-winrm`, `PowerShell Remoting`, etc.|Remote code execution from anywhere|
|**Weak Authentication (No Kerberos or Cred Guard)**|WinRM|NTLM allowed, CredSSP not hardened|Credential theft / reuse|NTLM relaying or pass-the-hash attacks|Lateral movement, privilege escalation|
|**HTTP (Port 5985) Without HTTPS**|WinRM|Plain HTTP used without TLS|MITM or sniff credentials|Intercept traffic on network|Credential exposure, command tampering|
|**Local Admins Can Use WinRM**|WinRM|All local admins allowed by default|Lateral access if 1 host is compromised|Use valid creds from compromised host|Easy horizontal movement across systems|
|**No IP Restriction or ACLs**|WinRM|No firewall or group policy limits|Abusable by any authenticated user|Scan + brute or use leaked creds|Remote access from untrusted machines|
|**Stored or Hardcoded Credentials**|WinRM|Scripts or task schedulers with plaintext creds|Reuse credentials across hosts|Dump config files or Task Scheduler|Compromise of multiple systems|
|**Misconfigured PSRemoting Policy**|PowerShell + WinRM|Remoting enabled for all users or groups|Execute PowerShell remotely|Invoke-Command, Enter-PSSession|RCE via PowerShell abuse|
|**TrustedHosts Wildcard (`*`) Set**|WinRM|Client-side config trusts all remote hosts|Accept MITM or fake servers|Redirect session to attacker-controlled host|Credential theft or spoofed sessions|
|**Weak Logging/Auditing**|WinRM|Remote session activity not logged or forwarded|Avoid detection of RCE|Use `Invoke-Command`, `evil-winrm` quietly|Hard to detect remote attacker actions|
|**Lack of JEA (Just Enough Admin)**|WinRM|Full admin rights given to remote users|Avoid privilege segmentation|Execute privileged commands over WinRM|Full system takeover when only partial access needed|

### MSSQL

|Misconfiguration|Protocol(s)|Cause|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|---|
|**Weak / Default Credentials**|MSSQL (TCP/1433)|Default creds (e.g., `sa` with weak password)|Gain DB access or remote shell|Brute-force with `hydra`, `mssqlclient.py`, `sqlcmd`|Full DB compromise, privilege escalation|
|**SQL Server Exposed to Internet**|MSSQL|Listening on 0.0.0.0 without firewall|Remote exploitation or bruteforce|Nmap, Shodan, or direct login attempts|Data theft, remote command execution|
|**xp\_cmdshell Enabled**|MSSQL|Dangerous feature not disabled|Execute OS commands from SQL|Use `EXEC xp_cmdshell 'cmd'`|RCE on DB host, lateral movement|
|**High Privilege SQL User Accounts**|MSSQL|Applications run under `sysadmin` role|Privilege abuse|Exploit app-level SQLi → sysadmin access|Full system access from web layer|
|**No TLS Encryption**|MSSQL|SQL Server accepts unencrypted logins|Credential sniffing|MITM on login or query sessions|Password or query leakage|
|**Excessive Permissions**|MSSQL|All users granted `db_owner` or `sysadmin`|Abuse overly permissive roles|Enumerate and escalate via role abuse|Schema changes, data wipes, RCE|
|**Linked Servers Without Constraints**|MSSQL|Linked servers allowed without auth restriction|Move across DB servers|Query remote MSSQL instances|Lateral movement, data theft from other DBs|
|**SQL Injection in Front-End**|MSSQL + HTTP|Unsanitized input in web apps|Gain control over SQL context|`' OR 1=1 --`, stacked queries, blind SQLi|DB dump, login bypass, OS command injection|
|**No Login Auditing / Logging**|MSSQL|Failed or suspicious logins not monitored|Stay stealthy|Repeated password attempts unnoticed|Undetected brute-force or persistent backdoor|
|**Unused Features Enabled**|MSSQL|Features like CLR, OLE, Automation enabled|RCE via extended functionality|Use assemblies or automation to escape SQL context|Shell access via .NET or COM objects|
|**Hardcoded DB Credentials in Apps**|MSSQL|Apps store creds in plaintext configs|Steal SQL login|Extract from `.env`, `web.config`, etc.|Persistent DB access without user knowledge|
|**Misconfigured Trusts Between Domains**|MSSQL (Kerberos/AD)|Cross-domain trust abused|Lateral movement via token impersonation|Abuse `TrustedForDelegation` + MSSQL SPNs|AD compromise via Kerberoasting|

###  HTTP/HTTPS

|Misconfiguration|Protocol(s)|Goal|Attack Vector|Impact / Exploit Potential|
|---|---|---|---|---|
|**Host Header Injection**|HTTP|Influence routing/caching|Malicious `Host:` header|SSRF, cache poisoning, vhost bypass|
|**SSRF**|HTTP/HTTPS|Access internal or cloud services|Server-side fetch from user-controlled URL|Metadata theft, RCE, internal port scanning|
|**Reverse Proxy Misrouting**|HTTP + Proxy|Bypass routing logic|Crafted paths with `@`, `..`, or path normalization|SSRF, admin panel access|
|**Overly Permissive CORS**|HTTP + Browser|Cross-origin access to internal APIs|Malicious `Origin:` headers|Read internal data from client-accessible API|
|**Insecure Protocol Fallback**|TLS/HTTP|Downgrade secure communication|Downgrade to HTTP or weak TLS versions|Credential theft, MITM|
|**CDN Trust Exploitation**|HTTP/CDN|Bypass access control based on IP headers|Spoofed `X-Forwarded-For`, `X-Real-IP` headers|Auth bypass, zone hopping|