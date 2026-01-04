### Test file URI injection (deep link)
```bash
am start -a android.intent.action.VIEW \
  -d "file:///sdcard/test.txt"
```
### Test a deep link manually
```bash
am start -a android.intent.action.VIEW -d "scheme://path?param=test"
```
### Test deep link without user interaction
```bash
am start -W -a android.intent.action.VIEW -d "https://evil.com"
```
### Launch exported activity directly
```bash
am start -n com.target.app/.ExportedActivity
```
### Send intent with extras (input injection)
```bash
am start -n com.target.app/.ExportedActivity \
  --es url "https://evil.com"
```
### Send broadcast to exported receiver
```bash
am broadcast -n com.target.app/.ExportedReceiver \
  --es cmd "test"
```
#### Replay API calls (example)
```bash
curl -i https://api.target.com/v1/user
```
### Test auth bypass
```bash
curl -i https://api.target.com/v1/user -H "Authorization:"
```

---
### List VIEW intent handlers (system-wide)

```bash
cmd package query-intent-activities \
  -a android.intent.action.VIEW
```