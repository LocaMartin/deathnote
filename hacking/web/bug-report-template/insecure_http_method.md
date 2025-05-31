# Insecure HTTP Methods Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Endpoint Affected
- URL: [URL where vulnerability was found]
- Method: [HTTP method used]

### Allowed Methods
List of enabled methods:
- [Method 1]
- [Method 2]
- ...

### Proof of Concept
```http
[Request showing unauthorized method usage]
```

### Impact
- API abuse
- Security bypass
- Unintended functionality
- Privilege escalation

### Steps to Reproduce
1. Test method support:
   ```bash
   curl -X OPTIONS "[URL]" -i
   ```

2. Verify insecure method:
   ```bash
   curl -X [METHOD] "[URL]"
   ```

### Expected Behavior
- Only necessary methods should be supported
- Dangerous methods should be restricted

### Actual Behavior
- Insecure methods are enabled
- No method restriction enforcement

### Recommendation
Disable unnecessary HTTP methods and restrict dangerous ones.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[Medium/Low]

## References
[Link to relevant documentation]