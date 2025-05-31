# Clickjacking Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Endpoint Affected
- URL: [URL where vulnerability was found]
- Method: [HTTP method used]

### Proof of Concept
```html
<iframe src="[URL]" width="500" height="500"></iframe>
```

### Impact
- UI redressing attacks
- User action manipulation
- Data theft
- Unauthorized actions

### Steps to Reproduce
1. Create malicious page:
   ```bash
   curl -X GET "[URL]" \
     -H "Accept: text/html"
   ```

2. Test frame busting protection:
   ```bash
   curl -X GET "[URL]" \
     -H "X-Frame-Options: DENY"
   ```

### Expected Behavior
- Frame restrictions should prevent embedding
- Clickjacking defense headers present

### Actual Behavior
- Page can be framed
- No clickjacking protections

### Recommendation
Implement proper frame restrictions and security headers.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[Medium/Low]

## References
[Link to relevant documentation]