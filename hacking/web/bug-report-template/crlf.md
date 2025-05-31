# 1. CRLF Injection

## **Title**: CRLF Injection in [Component/Endpoint]

### **Description**  
CRLF (Carriage Return Line Feed) injection allows attackers to inject arbitrary HTTP headers or split responses. This occurs due to improper sanitization of user input in headers or redirects.

### **Steps to Reproduce**  
1. Navigate to [Vulnerable Endpoint]
2. Inject CRLF characters (`%0D%0A`) in a parameter (e.g., `?param=test%0D%0AInjected-Header:%20value`)
3. Observe injected headers or response splitting.

### **Proof of Concept**  