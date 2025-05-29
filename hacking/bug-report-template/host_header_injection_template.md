# Host Header Injection Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Endpoint Affected
- URL: [URL where vulnerability was found]
- Method: [HTTP method used]

### Proof of Concept
```http
GET / HTTP/1.1
Host: attacker.com
```

### Impact
- Potential SSRF attacks
- Cache poisoning
- DNS rebinding attacks
- Authentication bypass

### Steps to Reproduce
1. Send request with modified Host header:
   ```bash
   curl -X GET "[URL]" \
     -H "Host: attacker.com"
   ```

### Expected Behavior
- Server should validate Host headers
- Only authorized hostnames should be accepted

### Actual Behavior
- Arbitrary Host headers are processed
- Request is handled differently based on injected header

### Recommendation
Implement proper Host header validation and normalization.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[High/Medium/Low]

## References
[Link to relevant documentation]