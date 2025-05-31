# SQL Injection Vulnerability Report

## Summary
[ Brief description of the vulnerability ]

## Details
### Type
- Error-based SQL Injection

### Endpoint Affected
- URL: [URL where vulnerability was found]
- Method: [HTTP method used]
- Parameter(s): [affected parameter(s)]

### Proof of Concept
```http
[Request showing SQL injection payload]
```

### Database Information
- DBMS: [Identified database management system]
- Version: [Version if identified]
- Tables/Columns: [List discovered schema elements]

### Impact
- Unauthorized data access
- Data tampering
- System compromise
- Business logic manipulation

### Steps to Reproduce
1. Send malicious request:
   ```bash
   curl -X [METHOD] "[URL]" \
     -d "[PAYLOAD]"
   ```

### Expected Behavior
- Input validation should prevent SQL syntax
- Error messages should be generic

### Actual Behavior
- SQL errors reveal database information
- Query structure can be determined

### Recommendation
Implement prepared statements and proper input sanitization.

## Additional Notes
[Add any relevant screenshots or additional context]

## Severity
[High/Critical]

## References
[Link to relevant documentation]