#!/usr/bin/env python3
import os
import sys
import time
import platform

def main():
    if platform.system() == "Windows":
        sys.exit("This script uses fork() and is intended for Unix-like systems.")

    print("Starting Task 1: Process Creation Utility")
    parent_pid = os.getpid()
    print(f"Parent PID: {parent_pid}")

    try:
        pid = os.fork()
    except OSError as e:
        sys.exit(f"Fork failed: {e}")

    if pid == 0:
        child_pid = os.getpid()
        parent_of_child = os.getppid()
        print(f"[Child] PID: {child_pid}, Parent PID: {parent_of_child}")
        for i in range(3):
            print(f"[Child] working... ({i+1}/3)")
            time.sleep(1)
        print("[Child] Exiting.")
        os._exit(0)
    else:
        print(f"[Parent] fork() returned child PID: {pid}")
        print("[Parent] Waiting for child to finish...")
        finished_pid, status = os.wait()
        print(f"[Parent] Child {finished_pid} finished with status {status}")
        print("[Parent] Done.")

if __name__ == "__main__":
    main()
