# Operating Systems Lab Assignment 1: Process Creation and Management Using Python OS Module

**Author:** Adarsh Kumar Sharma  
**Roll Number:** 2301420058  
**Course:** B.Tech CSE (Data Science)

---

## Experiment Title  
Process Creation and Management Using Python OS Module

---

## Overview
This repository contains Python scripts demonstrating core concepts of process management in Unix-like operating systems using the Python `os` module. Concepts covered include process creation and termination, command execution, zombie and orphan processes, inspection of process details from the `/proc` filesystem, and process prioritization using nice values.

---

## Tasks Implemented

### Task 1: Process Creation Utility
- Creates multiple child processes using `os.fork()`.  
- Each child prints its PID, parent PID, and a greeting message.  
- Parent process waits for all children to complete.

### Task 2: Command Execution Using `exec()`
- Spawns child processes to execute Linux commands using `os.execvp()`.  
- Parent monitors and prints child termination statuses.

### Task 3: Zombie and Orphan Processes Demonstration
- Shows creation of a zombie process by not waiting for child termination.  
- Shows orphan process when parent exits before the child.

### Task 4: Process Information Inspection from `/proc`
- Reads and outputs process attributes such as name, state, memory usage, executable path, and open file descriptors from the `/proc` filesystem.

### Task 5: Process Prioritization with `nice`
- Creates worker processes with different priorities (nice values).  
- Demonstrates effect of prioritization on CPU time allocation.

---

## Usage

- Run the Python scripts on a Linux or Unix-based system with Python 3.  
- Each task can be executed independently.  
- Ensure necessary permissions to create processes and access `/proc`.


