# RCE

To identify a remotely exploitable bug in an Android app, certain technical conditions must align.

1. There must be a remote attack surface
>A bug cannot be remotely exploitable unless external input reaches the app.
Common remote entry points:

- Network APIs (REST, GraphQL, WebSockets)
- Deep links / App Links (intent-filter with BROWSABLE)
- Push notifications (FCM payloads)
- Downloaded files (PDF, JSON, images, configs)
- WebView content (remote URLs, JS bridges)

> No external input = no remote exploit

2. Input reaches security-sensitive code
> User-controlled or server-controlled data must reach logic that matters.

Examples:

- Authentication / session handling
- File handling or parsing
- Command execution or dynamic loading
- Database queries
- WebView JavaScript interfaces
- Crypto / token validation logic

3. Insufficient validation, sanitization, or trust boundaries

> Remote exploits usually exist when trust is misplaced.

Red flags:

- Blindly trusting server responses
- No schema validation (JSON/XML)
- Weak MIME / file type checks
- Unsafe deserialization
- No URL allowlist in WebView
- Missing signature / integrity checks

4. No strong platform mitigations blocking it

Android has many protections. A remote exploit survives only if it bypasses or avoids them.

Mitigations that often stop exploits:

App sandboxing

SELinux

Scoped storage

Network Security Config

TLS certificate validation

Exported component restrictions

A real remote bug:

Works within Android’s security model

Doesn’t rely on deprecated or debug-only behavior