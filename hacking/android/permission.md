>This table lists common and security-relevant Android permissions, not the complete Android permission set.

| Permission                             | One-line description                                                       |
| -------------------------------------- | -------------------------------------------------------------------------- |
| `INTERNET`                             | Allows the app to make network connections (API calls, data exfiltration). |
| `ACCESS_NETWORK_STATE`                 | Checks whether network connectivity exists.                                |
| `ACCESS_WIFI_STATE`                    | Reads Wi-Fi connection info (SSID, state).                                 |
| `CHANGE_WIFI_STATE`                    | Enables/disables or modifies Wi-Fi settings.                               |
| `ACCESS_FINE_LOCATION`                 | Accesses precise GPS location.                                             |
| `ACCESS_COARSE_LOCATION`               | Accesses approximate location via network.                                 |
| `READ_CONTACTS`                        | Reads user’s contact list.                                                 |
| `WRITE_CONTACTS`                       | Modifies or adds contacts.                                                 |
| `READ_SMS`                             | Reads SMS messages (OTP leakage risk).                                     |
| `SEND_SMS`                             | Sends SMS without user interaction.                                        |
| `RECEIVE_SMS`                          | Listens for incoming SMS messages.                                         |
| `READ_CALL_LOG`                        | Reads call history (privacy sensitive).                                    |
| `WRITE_CALL_LOG`                       | Modifies call logs.                                                        |
| `CALL_PHONE`                           | Makes phone calls without dialer UI.                                       |
| `RECORD_AUDIO`                         | Records audio using microphone.                                            |
| `CAMERA`                               | Takes photos or videos silently.                                           |
| `READ_EXTERNAL_STORAGE`                | Reads files from shared storage.                                           |
| `WRITE_EXTERNAL_STORAGE`               | Writes files to shared storage.                                            |
| `MANAGE_EXTERNAL_STORAGE`              | Full access to all files (Android 11+).                                    |
| `SYSTEM_ALERT_WINDOW`                  | Draws overlays (tapjacking risk).                                          |
| `REQUEST_INSTALL_PACKAGES`             | Allows installing APKs from unknown sources.                               |
| `PACKAGE_USAGE_STATS`                  | Tracks which apps user is using.                                           |
| `GET_TASKS`                            | Retrieves running apps (deprecated but risky).                             |
| `FOREGROUND_SERVICE`                   | Runs persistent background tasks.                                          |
| `RECEIVE_BOOT_COMPLETED`               | Starts app automatically after reboot.                                     |
| `BIND_ACCESSIBILITY_SERVICE`           | Full UI access (high-risk, automation abuse).                              |
| `BIND_NOTIFICATION_LISTENER_SERVICE`   | Reads all notifications (OTP/token leaks).                                 |
| `WRITE_SETTINGS`                       | Modifies system settings (brightness, rotation).                           |
| `WRITE_SECURE_SETTINGS`                | Modifies protected system settings (ADB/system only).                      |
| `INSTALL_PACKAGES`                     | Installs apps silently (system-level).                                     |
| `DELETE_PACKAGES`                      | Uninstalls apps without user confirmation.                                 |
| `READ_LOGS`                            | Reads system logs (sensitive info leakage).                                |
| `BLUETOOTH`                            | Basic Bluetooth communication.                                             |
| `BLUETOOTH_ADMIN`                      | Discovers and pairs Bluetooth devices.                                     |
| `NFC`                                  | Uses Near-Field Communication.                                             |
| `USE_BIOMETRIC`                        | Uses fingerprint/face authentication.                                      |
| `MANAGE_ACCOUNTS`                      | Adds/removes system accounts.                                              |
| `AUTHENTICATE_ACCOUNTS`                | Uses account credentials for login.                                        |
| `BIND_VPN_SERVICE`                     | Creates a VPN connection (traffic interception).                           |
| `CONTROL_VPN`                          | Manages VPN state (system apps).                                           |
| `MODIFY_AUDIO_SETTINGS`                | Changes volume and audio routing.                                          |
| `ACCESS_NOTIFICATION_POLICY`           | Controls Do Not Disturb settings.                                          |
| `EXPAND_STATUS_BAR`                    | Opens/closes status bar programmatically.                                  |
| `KILL_BACKGROUND_PROCESSES`            | Stops other apps’ background processes.                                    |
| `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` | Bypasses Doze / battery limits.                                            |
| `START_ACTIVITIES_FROM_BACKGROUND`     | Launches UI without user action.                                           |
| `QUERY_ALL_PACKAGES`                   | Enumerates all installed apps (privacy risk).                              |
