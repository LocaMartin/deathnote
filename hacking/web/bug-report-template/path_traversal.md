# Path Traversal Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Endpoint Affected
- URL: [URL where vulnerability was found]
- Method: [HTTP method used]
- Parameter(s): [affected parameter(s)]

### Proof of Concept
```http
GET /[endpoint]?file=../../../../etc/passwd
```

### Impact
- Access to sensitive files
- System configuration exposure
- Potential credential disclosure
- Lateral movement

### Steps to Reproduce
1. Send request with traversal sequence:
   ```bash
   curl -X GET "[URL]" \
     -H "Accept: */*"
   ```

### Expected Behavior
- Input validation should prevent path traversal
- Canonical paths should be enforced

### Actual Behavior
- Directory traversal is successful
- Files outside intended directory are accessible

### Recommendation
Implement proper path normalization and canonicalization.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[High/Critical]

## References
[Link to relevant documentation]