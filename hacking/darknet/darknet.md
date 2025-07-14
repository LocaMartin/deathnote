<div align="center">
   <img src="https://i.ibb.co/DDCsmg6t/pngegg.png" width="150px" height="200px">
</div>

<p align="center"><strong>DarkNet Vulnerability Assessment</strong></p>
<p align="center">Everything I Know</p>

>[!WARNING]
></strong> This content is provided <strong>strictly for educational and research purposes only</strong>. <br>
  Unauthorized testing or access of systems without permission is illegal. Use responsibly and ethically.

### Tool table with environment setup is available [here]()
```yaml
# Start tor in terminal 1
tor
```
```yaml
# Keyword search example
onionsearch "songs" --output results.txt
```
```yaml
# Dork-based search
onionsearch "intitle:'index of' /backup site:*.onion" --output results.txt
```
```yaml
# Extract URLs
grep -o 'http[^"]*' results.txt > tor_urls.txt
```
```yaml
# Scan with httpx
cat tor_urls.txt | httpx -sc -proxy socks5://127.0.0.1:9050 -td --title -ct -cl -method -server -ip
```
```yaml
# san with nmap
cat tor_urls.txt | nuclei -as -rl 1500 -bs 50 -nh -proxy socks5://127.0.0.1:9050 
```
```yaml
# port scan
proxychains nmap -sT -Pn -n 2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion
```
```yaml
# crawl with torbot
python TorBot.py -q "filetype:env .onion" --deep 3
```
```yaml
# crawl with katana
katana -proxy socks5://127.0.0.1:9050 -u http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
```
```yaml
# OnionScan (specialized for Tor services)
onionscan 2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion
```
```yaml
# directory enumeration
python3 darkdump.py -d 2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion
```
```yaml
torsocks http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
```
```yaml
proxychains curl http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
```
```yaml
# access with curl
curl -s --socks5-hostname 127.0.0.1:9050 http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
```
### access with cli browser (w3m/lynx)
```yaml
nano ~/.w3m/config 
```
with these settings:
```yaml
# ~/.w3m/config
use_proxy 1
http_proxy http://127.0.0.1:8118/  # Privoxy port
https_proxy http://127.0.0.1:8118/
```
```yaml
echo "forward-socks5t / 127.0.0.1:9050 ." >> $PREFIX/etc/privoxy/config
```
```yaml
# Tab 1: Start Tor
tor
```
```yaml
# Tab 2: Start Privoxy
privoxy --no-daemon $PREFIX/etc/privoxy/config
```
```yaml
# Tab 3: Launch w3m
w3m http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
```
```yaml
proxychains lynx http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion
```
### List of tools used with environment setup (every tool that supports onion proxy you can use it)

>large setup or graphical setups are mentioned below [here]() because they cant fit in the table

| TOOL | DESCRIPTION | SETUP COMMAND/NOTES |
| --- | --- | --- |
| tor | Anonymizing overlay network | `apt install tor` (Debian), `pkg install tor` (Android) |
| onionsearch | Python-based onion crawler | `pip install onionsearch` |
| TorBot | Dark web OSINT tool | `git clone https://github.com/DedSecInside/TorBot` |
| proxychains | Proxy tunnel tool | `apt install proxychains` |
| BurpSuite | Web security testing | Download from [portswigger.net](https://portswigger.net) |
| darkdump | Directory enumeration | `git clone https://github.com/josh0xA/darkdump` |
| lynx | Text-based web browser | `apt install lynx` |
| w3m | Text-based web browser | `apt install w3m` |
| onionscan | Onion service analyzer | `go install github.com/s-rah/onionscan@latest` |
| privoxy | Non-caching web proxy | `pkg install privoxy` |
| torsocks | SOCKS proxy for Tor | `apt install torsocks` |
| nuclei | Vulnerability scanner | `go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest` |
| httpx | HTTP toolkit | `go install github.com/projectdiscovery/httpx/cmd/httpx@latest` |
| nmap | Network scanner | `apt install nmap` |

### graphical and large environment setup

Burp suite - (pending)

### Vulnerabilities Exclusive to Onion Routing Networks

| Vulnerability | Mechanism | Why It's Unique to Onion Routing | Mitigation Strategies |
| --- | --- | --- | --- |
| Exit Node Eavesdropping | Exit nodes decrypt the final layer of encryption, exposing raw traffic (e.g., HTTP) to the destination server. | Only onion routing requires volunteer-operated exit nodes to handle final decryption, creating a trust dependency not found in end-to-end encrypted systems (e.g., HTTPS). | Use end-to-end encryption (HTTPS/SSL); Zero-Knowledge Proofs (ZKPs) to validate data without decryption. |
| Timing Correlation Attacks | Adversaries monitoring both entry and exit nodes correlate traffic timing/volume to de-anonymize users. | Onion routing’s multi-hop design makes simultaneous observation of entry/exit traffic feasible for adversaries; single-hop networks (e.g., VPNs) lack this vulnerability. | Limit concurrent applications over Tor; use bridges or private relays. |
| Circuit Reuse Exploits | Reusing the same circuit for multiple TCP connections links anonymous and non-anonymous traffic. | Tor’s performance optimization (circuit reuse) creates cross-activity correlation risks absent in systems where sessions are isolated. | Run separate Tor clients for sensitive/non-sensitive tasks; disable circuit reuse. |
| Guard Node Compromise | Guard nodes (first hop) are used long-term; if compromised, they enable persistent de-anonymization. | Tor’s node-selection algorithm prioritizes guard nodes for stability, creating a fixed attack point; decentralized networks without fixed entry points avoid this. | Increase guard node pool size; rotate guard nodes frequently. |
| Onion Service Fingerprinting | Adversaries analyze encrypted traffic patterns to identify specific .onion services (e.g., V3 services are more vulnerable than V2). | Unique to Tor’s hidden services, where traffic patterns to .onion sites are identifiable despite encryption. | Traffic obfuscation (e.g., padding); protocol improvements to standardize packet sizes. |
| Bridge Discovery Attacks | Censors scan public IPs to detect and block private Tor bridges (entry points). | Bridges are unique to Tor’s anti-censorship infrastructure; centralized tools (e.g., VPNs) lack distributed bridge mechanisms. | Use pluggable transports (e.g., obfs4) to disguise bridge traffic. |

# Darknet-Exclusive Protocols & Services



## Protocols

| Protocol/Service | Key Features | Darknet Exclusivity | Primary Use Cases |
| --- | --- | --- | --- |
| Tor (Onion Routing) | Multi-layered encryption with traffic routed through ≥3 volunteer relays; .onion addressing. | .onion services are inaccessible via standard browsers; require Tor Browser. Exit nodes decrypt final traffic layer, exposing risks. | Anonymous browsing, hidden services, censorship circumvention. |
| I2P (Invisible Internet) | "Garlic routing" (multi-layered encryption + bundling); peer-to-peer decentralized network; .i2p eepsites. | Eepsites only resolvable within I2P network; no clearnet gateway. Traffic never exits to public internet. | Secure email, anonymous hosting, P2P file sharing. |
| Freenet | Decentralized data storage; content distributed across nodes; addresses use content-hashing (e.g., CHK@...). | Freesites/data exist only within Freenet; no IP-based addressing. Data persistence relies on node participation. | Censorship-resistant publishing, community forums. |
| Zeronet | Decentralized sites hosted via BitTorrent network; Bitcoin cryptography for ownership; .bit domains. | Sites powered by P2P network; no central servers. Requires Zeronet client for access. | Uncensorable blogs, forums, cryptocurrency projects. |
| Riffle (MIT) | Onion routing + verifiable shuffles + authentication; designed to resist traffic-correlation attacks. | Academic prototype focused on enhancing Tor's anonymity; not publicly deployed but darknet-specific by design. | High-risk communications (e.g., whistleblowing). |
| GNUnet | Mesh routing with delay-tolerant networking (DTN); GNU Name System (GNS) for decentralized DNS. | GNS replaces DNS with blockchain-like resolution; services only accessible via GNUnet peers. | Private messaging, file sharing, decentralized DNS. |
| Tribler | Anonymous BitTorrent via onion routing; no central trackers. | Modifies BitTorrent to embed Tor-like encryption; no clearnet equivalent for anonymity. | P2P file sharing without IP exposure. |

## Darknet-Exclusive Services

| Service Type | Protocol Dependency | Exclusivity Mechanism | Examples |
| --- | --- | --- | --- |
| Onion Services (.onion) | Tor | Only accessible via Tor Browser; no DNS resolution in clearnet. | DuckDuckGo's Tor mirror, CIA SecureDrop. |
| Eepsites (.i2p) | I2P | I2P network required for resolution; traffic remains end-to-end encrypted within I2P. | I2P-based forums, anonymous blogs. |
| Freesites | Freenet | Content stored/distributed within Freenet nodes; inaccessible via HTTP/HTTPS. | Political dissident archives. |
| ZeroSites | Zeronet | Sites hosted on P2P network; require Zeronet client and Bitcoin keys for updates. | Decentralized social media platforms. |
| GNS (GNU Name System) | GNUnet | Replaces DNS with decentralized, censorship-resistant naming; integrates with GNUnet services. | Private intranet resource naming. |
