# Server-Side Request Forgery (SSRF) Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Endpoint Affected
- URL: [URL where vulnerability was found]
- Method: [HTTP method used]
- Parameter(s): [affected parameter(s)]

### Proof of Concept
```http
[Request showing SSRF exploitation]
```

### Impact
- Internal service enumeration
- Cloud metadata access
- Network reconnaissance
- Potential lateral movement

### Steps to Reproduce
1. Send request to trigger SSRF:
   ```bash
   curl -X [METHOD] "[URL]" \
     -H "Content-Type: application/json" \
     -d "[PAYLOAD]"
   ```

### Expected Behavior
- Only authorized services should be accessible
- Input validation should restrict requests

### Actual Behavior
- Requests to unauthorized services succeed
- Internal resources are accessible

### Recommendation
Implement proper request validation and network restrictions.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[High/Critical]

## References
[Link to relevant documentation]