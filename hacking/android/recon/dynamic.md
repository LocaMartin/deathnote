<div align="center"><p><b>Dynamic App Analysis</b></p>
</div>

### 1. App & Component Discovery (Attack Surface)

#### List all third-party apps

```bash
pm list packages -3
```
#### Dump full app manifest info

```bash
pm dump com.target.app
```
#### Find exported components (remote entry points)

```bash
pm dump com.target.app | grep -n "exported=true"
```
### List activities, services, receivers

```bash
pm dump com.target.app | grep -E "Activity|Service|Receiver"
```
---
### 2. Intent / Deep Link Recon (VERY IMPORTANT)

#### Find all deep links (URI schemes)
```bash
pm dump com.target.app | grep -oE '[a-zA-Z][a-zA-Z0-9+.-]*://[^" ]+' | sort -u
```
#### Filter browsable deep links only
```bash
pm dump com.target.app | grep -n "BROWSABLE"
```
---
### 3. Exported Component Abuse Checks

#### List exported activities

```bash
pm dump com.target.app | grep -n "exported=true" | grep Activity
```
---
### 4. Permission & Auth Boundary Recon

#### List requested permissions

```bash
pm dump com.target.app | grep -n "requested permissions" -A50
```

#### Find custom permissions

```bash
pm dump com.target.app | grep -n "permission:"
```

#### Check if exported component lacks permission

```bash
pm dump com.target.app | grep -n "exported=true" -A5 | grep -i permission
```
---
# 5. WebView & Remote Content Recon

### Find WebView usage

```bash
pm dump com.target.app | grep -i "WebView"
```

### Find JavaScript interfaces

```bash
pm dump com.target.app | | grep -i "addJavascriptInterface" -n
```

### Look for HTTP URLs (cleartext risk)

```bash
pm dump com.target.app | grep -oE 'http://[^" ]+'
```

### Check Network Security Config

```bash
pm dump com.target.app | grep -i "networkSecurityConfig"
```
---
### 6. API / Backend Recon (Remote Bugs)

#### Extract API endpoints

```bash
pm dump com.target.app | grep -oE 'https?://[^" ]+' | sort -u
```

#### Identify GraphQL

```bash
pm dump com.target.app | grep -i "graphql"
```
### 7. File Handling / Download Recon

#### Find file paths

```bash
pm dump com.target.app | grep -i "/sdcard\|/data/data"
```

#### Look for file:// usage

```bash
pm dump com.target.app | grep -i "file://"
```
---
### 8. Push Notification / FCM Recon

### Find FCM services

```bash
pm dump com.target.app | grep -i "FirebaseMessagingService"
```

### Check exported messaging receivers

```bash
pm dump com.target.app | grep -n "messaging"
```
---
### 9. Logging & Sensitive Data Recon

#### Monitor runtime logs

```bash
logcat | grep -i "com.target.app"
```
#### Look for tokens / secrets
```
logcat | grep -Ei "token|auth|bearer|cookie|session|jwt"
```
```bash
logcat | grep -Ei "token|auth|jwt|session"
```
---
### 10. Installed App-wide Recon (Automation)

#### Dump all apps & extract deep links

```bash
pm list packages -3 | cut -d: -f2 | while read p; do
  pm dump "$p" 2>/dev/null
done | grep -oE '[a-zA-Z][a-zA-Z0-9+.-]*://[^" ]+' | sort -u
```
