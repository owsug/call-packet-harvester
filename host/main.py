import subprocess
import time
import os
from adb_utils import adb_push, adb_pull, adb_shell_async, kill_sniffer
from call_controller import call_with_timeout
from config import PHONE_NUMBER, CALL_DURATION, CAPTURE_TIMEOUT, SNIFFER_DEVICE_PATH, OUTPUT_DEVICE_PATH, LOCAL_OUTPUT_DIR, LOCAL_OUTPUT_FILE, 


def ensure_output_dir():
    if not os.path.exists(LOCAL_OUTPUT_DIR):
        os.makedirs(LOCAL_OUTPUT_DIR)


def start_sniffer():
    """Starts sniffer in background (non-blocking)."""
    print("[*] Starting sniffer on device...")
    return adb_shell_async(f"su -c '{SNIFFER_DEVICE_PATH} > /sdcard/sniffer.log'")


def main():
    print("[+] Starting call-packet-harvester automation")

    ensure_output_dir()

    # 1. Push sniffer binary
    adb_push("android/sniffer", SNIFFER_DEVICE_PATH)

    # 2. Start sniffer
    sniffer_proc = start_sniffer()

    # 3. Wait a bit before call
    time.sleep(2)

    # 4. Dial + hangup
    call_with_timeout(PHONE_NUMBER, duration=CALL_DURATION)

    # 5. Wait a bit before stopping sniffer
    print("[*] Waiting a bit before pulling file...")
    time.sleep(3)

    # 6. Kill sniffer process (optional: you can also let it auto-exit)
    kill_sniffer()  # if your sniffer supports signal-based exit

    # 7. Pull result
    print(f"[+] Pulling captured file to {LOCAL_OUTPUT_FILE}")
    adb_pull(OUTPUT_DEVICE_PATH, LOCAL_OUTPUT_FILE)

    print("[✅] Done.")


if __name__ == "__main__":
    main()
