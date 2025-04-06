# call-packet-harvester
Automated packet collection tool for VoLTE and VoIP calls using CMC/COD triggers on Android devices.

---

## 🧱 Development Environment

- **Host OS**: Windows 11  
- **WSL Version**: WSL2  
- **WSL Distro**: Ubuntu 24.04 LTS  
- **Python**: 3.10+  
- **Required Tools**:
  - `libpcap-dev`
  - `adb` (Android Debug Bridge)
  - `iproute2`

Install them on Ubuntu with:

```bash
sudo apt update
sudo apt install -y tcpdump libpcap-dev adb iproute2 python3-venv
```

> Make sure your Android device has **root access** and USB debugging enabled.
