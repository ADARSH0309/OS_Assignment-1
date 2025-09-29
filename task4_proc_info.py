
#!/usr/bin/env python3
import os
import sys
import platform

def read_proc_status(pid):
    try:
        with open(f"/proc/{pid}/status", "r") as f:
            return f.read()
    except Exception:
        return None

def read_proc_cmdline(pid):
    try:
        with open(f"/proc/{pid}/cmdline", "rb") as f:
            raw = f.read()
            return raw.replace(b'\x00', b' ').decode().strip()
    except Exception:
        return None

def list_some_pids(limit=10):
    return sorted([int(e) for e in os.listdir("/proc") if e.isdigit()])[:limit]

def main():
    if platform.system() == "Windows":
        sys.exit("This script inspects /proc and is intended for Linux.")

    print("Task 4: Inspecting /proc for process info")
    for pid in list_some_pids(8):
        print("\n" + "="*40)
        print(f"PID: {pid}")
        cmdline = read_proc_cmdline(pid) or "<no access>"
        print("Cmdline:", cmdline)
        status = read_proc_status(pid)
        if status:
            for line in status.splitlines()[:10]:
                print(line)

if __name__ == "__main__":
    main()
