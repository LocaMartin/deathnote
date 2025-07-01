## Windows protocols

| Protocol | Transport | Port | Network Layer | Language (Original/Typical) | Communication Type | Default Credentials | Encryption / Encoding | Raw Request Example | Raw Response Example |
|---|--|---|---|---|---|---|---|---|---|
| **NFS** | TCP/UDP | 2049  | Application | C | Binary (XDR) | None | None (NFSv3), Kerberos (v4) | `CALL 100003 2 READ /path/file` | `REPLY OK <file data>` |
| **VNC** | TCP | 5900 | Application | C | Text + Binary | None / default is blank | Optional (VNC password auth) | `ProtocolVersion 003.008\n` | `ProtocolVersion 003.008\n` |
| **SMB** | TCP | 445 | Application | C/C++ | Binary | Guest/Anonymous (in old) | NTLM / Kerberos | `\xFFSMB\x72` (Negotiate Request) | `\xFFSMB\x73` (Negotiate Response) |
| **WMI** | DCOM/HTTP | Varies / 5985 | Application | C++ / PowerShell | Text (SOAP/XML) | Windows User Account | NTLM / Kerberos / HTTPS | `<w:Command>hostname</w:Command>` | `<rsp:CommandOutput>...</rsp:CommandOutput>` |
| **MSSQL** | TCP          | 1433        | Application     | C/C++                        | Binary (TDS)         | `sa` / blank password     | TLS (optional)                | `TDS: SQLBatch - SELECT @@VERSION`             | `TDS: Response - Microsoft SQL Server...`                   |
| **LDAP**  | TCP          | 389 (636 LDAPS) | Application  | C                            | Binary (ASN.1 BER)   | `cn=admin`, `uid=admin`  | StartTLS or SSL (LDAPS)       | `bindRequest` (BER encoded) | `bindResponse success` (BER encoded) |
| **FTP** | TCP | 21 | Application | C | Text | `anonymous / guest@` | None by default, FTPS optional | `USER anonymous\r\n`<br>`PASS guest@\r\n` | `220 FTP ready\r\n`<br>`230 Login successful\r\n`           |
| **WinRM** | HTTP/S | 5985/5986 | Application | PowerShell / C# | Text (SOAP/XML) | Windows Account | HTTPS or NTLM/Kerberos | `POST /wsman` with SOAP headers | `HTTP/1.1 200 OK` + `<rsp:...>` |
| **SSH** | TCP | 22 | Application | C | Text (Handshake), Binary (Payload) | None / root (deprecated) | Encrypted by default (various ciphers) | `SSH-2.0-OpenSSH_8.2\r\n` | `SSH-2.0-OpenSSH_7.9\r\n` |
| **RDP** | TCP | 3389 | Application     | C/C++                        | Binary (X.224 + RDP) | Windows Account           | TLS + CredSSP | `03 00 00 13 0e d0 ...` (X.224 Connect Request) | `03 00 00 0b 06 d0 ...` (Connect Confirm)                   |

# Local Protocol

# Global/Remote protocol