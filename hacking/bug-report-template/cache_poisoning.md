# Web Cache Poisoning Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Endpoint Affected
- URL: [URL where vulnerability was found]
- Method: [HTTP method used]

### Proof of Concept
```http
[Request showing cache poisoning]
```

### Impact
- Malicious content caching
- User exploitation
- Denial of Service
- Security bypass

### Steps to Reproduce
1. Send malicious request:
   ```bash
   curl -X [METHOD] "[URL]" \
     -H "[MALICIOUS_HEADER]"
   ```

2. Verify cache behavior:
   ```bash
   curl -X GET "[URL]" \
     -H "Cache-Control: max-age=3600"
   ```

### Expected Behavior
- Cache keys should be properly validated
- Request headers should be sanitized

### Actual Behavior
- Cache stores malicious responses
- Cached content affects other users

### Recommendation
Implement proper cache key validation and header restrictions.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[Medium/Low]

## References
[Link to relevant documentation]