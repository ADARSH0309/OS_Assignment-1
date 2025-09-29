#!/usr/bin/env python3
import os
import sys
import time
import platform

def demonstrate_zombie():
    print("=== Zombie demonstration ===")
    pid = os.fork()
    if pid == 0:
        print(f"[Child: {os.getpid()}] Exiting immediately to become a zombie.")
        os._exit(0)
    else:
        print(f"[Parent: {os.getpid()}] Sleeping 6s without wait so child becomes zombie.")
        time.sleep(6)
        print("[Parent] Now calling wait() to reap child.")
        os.wait()
        print("[Parent] Child reaped.")

def demonstrate_orphan():
    print("\n=== Orphan demonstration ===")
    pid = os.fork()
    if pid == 0:
        child_pid = os.getpid()
        print(f"[Child: {child_pid}] Sleeping 5s so parent can exit and child becomes orphan.")
        time.sleep(5)
        print(f"[Child: {child_pid}] New parent PID: {os.getppid()}")
        os._exit(0)
    else:
        print(f"[Parent: {os.getpid()}] Exiting immediately. Child will be orphaned.")
        os._exit(0)

def main():
    if platform.system() == "Windows":
        sys.exit("This script uses fork() and is intended for Unix-like systems.")

    demonstrate_zombie()
    time.sleep(1)
    demonstrate_orphan()

if __name__ == "__main__":
    main()
