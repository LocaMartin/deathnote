# Subdomain Takeover Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Domain Affected
- Subdomain: [subdomain.example.com]
- Parent Domain: [example.com]

### Service Provider
- [Cloud provider/platform]

### Proof of Concept
```bash
dig [subdomain.example.com]
```

### Impact
- DNS control compromise
- Traffic hijacking
- Brand reputation damage
- Potential phishing attacks

### Steps to Reproduce
1. Verify domain status:
   ```bash
   host [subdomain.example.com]
   ```
2. Check service configuration:
   ```bash
   curl -I http://[subdomain.example.com]
   ```

### Expected Behavior
- Subdomains should be properly configured
- Deactivated resources should be removed

### Actual Behavior
- Resource is deactivated but still resolvable
- DNS record exists without active service

### Recommendation
Remove unused DNS records and implement proper resource cleanup.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[Medium/High]

## References
[Link to relevant documentation]