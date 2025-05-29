# Cross-Site Scripting (XSS) Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Type
- [Stored/Persistent | Reflected | DOM-based]

### Endpoint Affected
- URL: [URL where vulnerability was found]
- Method: [HTTP method used]
- Parameter(s): [affected parameter(s)]

### Proof of Concept
```http
[Request showing XSS payload]
```

### Payload Used
```javascript
// Example payload:
<script>alert('XSS')</script>
```

### Impact
- Potential theft of user sessions
- Malicious actions on behalf of users
- Data exfiltration
- Phishing attacks

### Steps to Reproduce
1. Send malicious request:
   ```bash
   curl -X [METHOD] "[URL]" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "[PAYLOAD]"
   ```

### Expected Behavior
- Input validation should prevent XSS payloads
- Output encoding should prevent script execution

### Actual Behavior
- Payload executes successfully
- Malicious JavaScript runs in context

### Recommendation
Implement proper input validation and output encoding.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[High/Medium/Low]

## References
[Link to relevant documentation]