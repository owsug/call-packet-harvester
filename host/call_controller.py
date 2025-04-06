import subprocess
import time


def dial_number(phone_number: str):
    """Initiates a call to the specified phone number via adb."""
    print(f"[+] Dialing number: {phone_number}")
    subprocess.run([
        "adb", "shell",
        "am", "start",
        "-a", "android.intent.action.CALL",
        "-d", f"tel:{phone_number}"
    ], check=True)


def hangup():
    """Ends an ongoing call via adb."""
    print("[+] Hanging up the call")
    subprocess.run([
        "adb", "shell",
        "input", "keyevent", "KEYCODE_ENDCALL"
    ], check=True)


def call_with_timeout(phone_number: str, duration: int = 10):
    """
    Dials a number, waits for a fixed duration, then ends the call.
    :param phone_number: The phone number to call.
    :param duration: Duration in seconds to wait before hanging up.
    """
    dial_number(phone_number)
    print(f"[+] Waiting {duration} seconds during call...")
    time.sleep(duration)
    hangup()


# Usage Example:
# if __name__ == "__main__":
#     # Example usage
#     phone_number = "1234567890"  # Replace with the actual number
#     call_duration = 10  # Duration in seconds
#     call_with_timeout(phone_number, call_duration)