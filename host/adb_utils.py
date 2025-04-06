import subprocess


def adb_push(local, remote):
    print(f"[+] Pushing {local} → {remote}")
    subprocess.run(["adb", "push", local, remote], check=True)


def adb_pull(remote, local):
    print(f"[+] Pulling {remote} → {local}")
    subprocess.run(["adb", "pull", remote, local], check=True)


def adb_shell_async(command):
    print(f"[~] Running on device: {command}")
    return subprocess.Popen(["adb", "shell", command])


def kill_sniffer():
    """Kills sniffer by name (requires pkill or hardcoded pid logic)."""
    print("[!] Attempting to kill sniffer (by name)...")
    subprocess.run(["adb", "shell", "pkill", "-f", "sniffer"], check=False)
