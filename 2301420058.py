# process_management.py
# Author: Adarsh
# Assignment: OS Lab - Process Creation and Management

import os
import time
import subprocess

# ---------- Task 1: Process Creation ----------
def task1_process_creation(n=3):
    print("\n--- Task 1: Process Creation (by Adarsh) ---")
    children = []
    for i in range(n):
        pid = os.fork()
        if pid == 0:  # Child
            print(f"[Child] PID={os.getpid()}, PPID={os.getppid()}, Message=Hello from Adarsh’s child {i}")
            os._exit(0)
        else:
            children.append(pid)
    for cpid in children:
        os.waitpid(cpid, 0)


# ---------- Task 2: Command Execution ----------
def task2_exec_commands(commands=["date", "ls", "ps"]):
    print("\n--- Task 2: Command Execution using execvp/subprocess (by Adarsh) ---")
    for cmd in commands:
        pid = os.fork()
        if pid == 0:  # Child
            print(f"[Child] Executing command: {cmd} (by Adarsh)")
            os.execvp(cmd, [cmd])
        else:
            os.waitpid(pid, 0)


# ---------- Task 3: Zombie & Orphan ----------
def task3_zombie_orphan():
    print("\n--- Task 3: Zombie & Orphan Processes (by Adarsh) ---")

    # Zombie: Child exits, parent doesn't wait
    pid = os.fork()
    if pid == 0:  # Child
        print(f"[Zombie Child] PID={os.getpid()}, PPID={os.getppid()} - exiting immediately (Adarsh)")
        os._exit(0)
    else:
        print(f"[Parent] Created zombie process with PID={pid}, not waiting (Adarsh)")
        time.sleep(5)  # Observe zombie with: ps -el | grep defunct

    # Orphan: Parent exits before child finishes
    pid = os.fork()
    if pid == 0:  # Child
        time.sleep(5)
        print(f"[Orphan Child] PID={os.getpid()}, PPID={os.getppid()} (Adarsh)")
        os._exit(0)
    else:
        print(f"[Parent] Exiting before child finishes, making orphan (Adarsh)")
        os._exit(0)


# ---------- Task 4: Inspect /proc ----------
def task4_proc_inspection(pid):
    print(f"\n--- Task 4: Inspecting /proc/{pid} (by Adarsh) ---")
    try:
        with open(f"/proc/{pid}/status") as f:
            status = f.read()
        exe_path = os.readlink(f"/proc/{pid}/exe")
        fds = os.listdir(f"/proc/{pid}/fd")

        print(f"Process {pid} Info:")
        print("---- STATUS (first 10 lines) ----")
        print("\n".join(status.splitlines()[:10]))
        print(f"---- Executable Path: {exe_path}")
        print(f"---- Open FDs: {fds}")

    except Exception as e:
        print(f"Error reading /proc/{pid}: {e}")


# ---------- Task 5: Process Prioritization ----------
def cpu_task():
    total = 0
    for i in range(10**7):
        total += i
    print(f"[Child {os.getpid()} by Adarsh] Finished CPU task")


def task5_prioritization():
    print("\n--- Task 5: Process Prioritization with nice() (by Adarsh) ---")
    priorities = [0, 5, 10]
    children = []
    for priority in priorities:
        pid = os.fork()
        if pid == 0:  # Child
            os.nice(priority)
            print(f"[Child] PID={os.getpid()}, Priority={priority} (Adarsh)")
            cpu_task()
            os._exit(0)
        else:
            children.append(pid)
    for cpid in children:
        os.waitpid(cpid, 0)


# ---------- Main ----------
if __name__ == "__main__":
    print("========= OS Lab Assignment by Adarsh =========")

    # Run tasks one by one (comment/uncomment as needed)
    task1_process_creation(3)
    task2_exec_commands()

    # Task 3 creates zombies/orphans and may exit parent early,
    # so run separately if needed
    # task3_zombie_orphan()

    # Inspect current process (self)
    task4_proc_inspection(os.getpid())

    task5_prioritization()

    print("========= End of Assignment (Adarsh) =========")
