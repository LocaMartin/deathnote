- Radio Frequency (RF) Hacking
  - RF Signal Sniffing & Interception
  - Software-Defined Radio (SDR) Exploitation
  - RF Jamming & Signal Blocking
  - Modulation & Demodulation Manipulation
- Satellite Signal Hacking
  - GPS & GNSS Spoofing
  - Satellite Communication Interception
  - Uplink & Downlink Signal Manipulation
  - Weather & Surveillance Satellite Exploits 
- Cellular Network Hacking
  - IMSI Catcher & Stingray Device Exploitation
  - Baseband & SIM Card Attacks
  - 2G/3G/4G/5G Protocol Manipulation
  - SMS & Call Interception
- Radar & Sonar Signal Manipulation
  - Military & Civilian Radar Jamming
  - Echo & Reflection Manipulation
  - Underwater Sonar Exploits
  - Doppler Signal Interference
- Bluetooth & NFC Exploitation
  - Bluetooth Sniffing & Injection
  - NFC Relay & Replay Attacks
  - Unauthorized Pairing & Device Hijacking
  - Wearable & Smart Gadget Signal Manipulation
- WiFi Signal Interference & Manipulation
  - WiFi Jamming & Deauthentication Attacks
  - Signal Amplification & Redirection
  - Hidden SSID & MAC Address Spoofing
  - Frequency Manipulation Techniques
- RFID Signal Hijacking
  - RFID Cloning & Duplication
  - Wireless Access Card Exploits
  - NFC & RFID-Based Payment System Attacks
  - Contactless Authentication Bypass
- GPS Spoofing & Jamming
  - Location Manipulation Attacks
  - GPS-Based Navigation System Exploits
  - High-Precision Timing Signal Interference
  - Military & Aviation GPS Disruptions
- Broadcast Signal Interception
  - AM/FM Radio Signal Hijacking
  - Emergency Broadcast Manipulation
  - Digital TV & DVB Signal Exploitation
  - Pirate Radio & Unauthorized Transmission
- Remote Control Signal Exploitation
  - Drone & UAV Signal Hijacking
  - Smart Home Device Signal Manipulation
  - Garage Door & Key Fob Signal Replay Attacks
  - Industrial Remote Control Takeover
- Infrared & Laser Signal Manipulation
  - Infrared Camera & Sensor Spoofing
  - Laser Communication Interference
  - Military & Tactical Optical Signal Disruption
  - LIDAR Signal Manipulation
- Electromagnetic Signal Interference
  - EMP (Electromagnetic Pulse) Attacks
  - TEMPEST & Side-Channel Exploits
  - Magnetic Stripe Manipulation
  - Electrical Grid Signal Disruption
- Smart Antenna & Beamforming Attacks
  - Directional Signal Hijacking
  - Multi-User MIMO (MU-MIMO) Exploitation
  - Adaptive Beamforming Manipulation
  - Wireless Network Beam Steering Attacks

1. Scan for nearby WiFi networks and signal strengths:
```bash 
iwlist wlan0 scan | grep -E 'ESSID|Signal'
```
2. Scan and list nearby Bluetooth devices:
```bash
hcitool scan
```
3. Spoof GPS coordinates for testing navigation apps:
```python
import gpsd

gpsd.connect()
packet = gpsd.get_current()
print("Current Location:", packet.position())

# Spoof GPS
fake_lat, fake_lon = 37.7749, -122.4194
print("Spoofed Location:", fake_lat, fake_lon)  
```
4. Radio Frequency Sniffing (SDR) Capture and analyze RF signals using rtl-sdr:
```bash
rtl_sdr -f 433920000 -s 2000000 -g 40 output.bin
```
5. Dump RFID tag data using MFOC  (Linux - NFC Card):
```bash
mfoc -O dump.mfd
```
6. IMSI Catcher Detection (Android/Linux) Detect rogue cellular towers using SnoopSnitch or manually:
```bash
sudo gsmdecode -c
```