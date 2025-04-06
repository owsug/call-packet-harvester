from dotenv import load_dotenv
import os

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER", "01000000000")
CALL_DURATION = int(os.getenv("CALL_DURATION", "15"))
CAPTURE_TIMEOUT = int(os.getenv("CAPTURE_TIMEOUT", "20"))

SNIFFER_DEVICE_PATH = os.getenv("SNIFFER_DEVICE_PATH", "/data/local/tmp/sniffer")
OUTPUT_DEVICE_PATH = os.getenv("OUTPUT_DEVICE_PATH", "/sdcard/capture.pcap")

LOCAL_OUTPUT_DIR = "output"
LOCAL_OUTPUT_FILE = os.path.join(LOCAL_OUTPUT_DIR, "capture.pcap")
