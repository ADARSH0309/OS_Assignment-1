
#!/usr/bin/env python3
import os
import sys
import time
import platform

def show_priority(pid):
    try:
        if hasattr(os, "getpriority"):
            return os.getpriority(os.PRIO_PROCESS, pid)
        with open(f"/proc/{pid}/status", "r") as f:
            for line in f:
                if line.startswith("Nice:"):
                    return int(line.split()[1])
    except Exception:
        return None

def increase_nice_by(delta=5):
    pid = os.getpid()
    print(f"Current nice for PID {pid}: {show_priority(pid)}")
    try:
        new_nice = os.nice(delta)
        print(f"os.nice({delta}) called. New niceness: {new_nice}")
    except Exception as e:
        print("Unable to change niceness:", e)
    print("Updated nice:", show_priority(pid))

def try_setpriority(pid, value):
    if hasattr(os, "setpriority"):
        try:
            os.setpriority(os.PRIO_PROCESS, pid, value)
            print(f"Priority set to {value} for PID {pid}")
        except Exception as e:
            print("setpriority failed:", e)

def cpu_workload(seconds=3):
    print(f"Doing CPU work for {seconds}s...")
    t_end = time.time() + seconds
    cnt = 0
    while time.time() < t_end:
        cnt += 1
    print("Iterations:", cnt)

def main():
    if platform.system() == "Windows":
        sys.exit("This script uses niceness APIs and /proc; intended for Unix-like systems.")

    pid = os.getpid()
    print(f"PID: {pid}, Original nice: {show_priority(pid)}")
    increase_nice_by(10)
    try_setpriority(pid, 15)
    cpu_workload()

if __name__ == "__main__":
    main()
