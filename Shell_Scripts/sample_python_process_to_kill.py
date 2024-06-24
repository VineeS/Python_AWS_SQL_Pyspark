# sample_process.py

import time

def main():
    print("Starting sample process...")
    while True:
        print("Running...")
        time.sleep(1)

if __name__ == "__main__":
    main()


# To create a sample process and kill it in the terminal, you can follow these steps. Let's create a simple Python script that runs indefinitely, and then kill it using terminal commands:

# 1. **Create a Python script** (`sample_process.py`):

# Create a Python script that runs an infinite loop to simulate a long-running process.

# ```python
# # sample_process.py

# import time

# def main():
#     print("Starting sample process...")
#     while True:
#         print("Running...")
#         time.sleep(1)

# if __name__ == "__main__":
#     main()
# ```

# 2. **Run the script**:

# Open a terminal, navigate to the directory where `sample_process.py` is saved, and run the script using Python.

# ```bash
# python sample_process.py
# ```

# 3. **Find the process ID (PID)**:

# While the script is running, open another terminal window/tab and find its process ID (PID) using `ps` command. Look for the process by its name or inspect all Python processes.

# ```bash
# ps aux | grep python
# ```

# This command will show you a list of running processes. Locate the PID associated with `sample_process.py`.

# 4. **Kill the process**:

# Once you have identified the PID of `sample_process.py`, use the `kill` command to terminate it.

# ```bash
# kill PID
# ```

# Replace `PID` with the actual process ID you found in the previous step.

# For example:

# ```bash
# kill 12345
# ```

# This command sends a termination signal (SIGTERM) to the process with the specified PID, causing it to stop execution.

# **Note:** Ensure that the process you are terminating is safe to stop.
#  Terminating processes abruptly can lead to data loss or corruption in certain cases, especially for processes handling critical tasks or data operations. Use caution when terminating processes, especially in production environments.