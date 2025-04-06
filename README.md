# call-packet-harvester
Automated packet collection tool for VoLTE and VoIP calls using CMC/COD triggers on Android devices.

---

## Development Environment

- **Host OS**: Windows 11  
- **WSL Version**: WSL2  
- **WSL Distro**: Ubuntu 24.04 LTS  
- **Python**: 3.10+  
- **Android NDK**: r27c or later 
- **Required Tools**:
  - `adb` (Android Debug Bridge)
  - `iproute2`
  - `python3-venv`

Install them on Ubuntu with:

```bash
sudo apt update
sudo apt install -y adb iproute2 python3-venv unzip
```

> Make sure your Android device has **root access** and USB debugging enabled.

---

## Project Structure

```
call-packet-harvester/
├── android/               # Raw socket sniffer written in C
│   ├── sniffer.c
│   └── Android.mk
│
├── host/                  # Python automation scripts (adb, call, pull)
│   ├── main.py
│   ├── adb_utils.py
│   ├── call_controller.py
│   └── config.py
│
├── output/                # Collected .pcap or .log files
│
├── .env                   # Runtime settings (call number, time, etc.)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Quick Start

### 1. Build sniffer binary (NDK)

```bash
cd android
ndk-build NDK_PROJECT_PATH=. APP_BUILD_SCRIPT=Android.mk APP_ABI=arm64-v8a
```

### 2. Create virtualenv & install Python deps

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure `.env`

```env
PHONE_NUMBER=01012345678
CALL_DURATION=15
CAPTURE_TIMEOUT=20
SNIFFER_DEVICE_PATH=/data/local/tmp/sniffer
OUTPUT_DEVICE_PATH=/sdcard/capture.pcap
```

### 4. Run full collection flow

```bash
python3 host/main.py
```

---

## Notes

- The sniffer uses `AF_PACKET` to capture raw Ethernet frames. Root permission is required on Android.
- You can optionally implement `.pcap` saving or protocol-specific filtering later.
- Make sure the device remains awake and has mobile signal during test.

---

## 🛠️ TODO (coming soon)

- [ ] Save packets in `.pcap` format
- [ ] SIP/RTP protocol detection
- [ ] Auto-start sniffer on CMC/COD trigger
- [ ] Wireshark-compatible parsing tools
```
