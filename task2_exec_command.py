#!/usr/bin/env python3
import os
import sys
import platform

def run_exec(command_args):
    try:
        os.execvp(command_args[0], command_args)
    except Exception as e:
        print("exec failed:", e)
        os._exit(1)

def main():
    if platform.system() == "Windows":
        sys.exit("This script uses exec/fork and is intended for Unix-like systems.")

    if len(sys.argv) == 1:
        print("Usage: python3 task2_exec_command.py <command> [args...]")
        sys.exit(0)

    cmd = sys.argv[1:]
    pid = os.fork()
    if pid == 0:
        print(f"[Child] Execing: {' '.join(cmd)}")
        run_exec(cmd)
    else:
        pid_done, status = os.wait()
        print(f"[Parent] Child {pid_done} finished with status {status}")

if __name__ == "__main__":
    main()
