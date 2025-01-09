import os
import subprocess as sp
import signal

def os_module():
    while True:
        # Display current working directory in the prompt
        cmd = input(f"{os.getcwd()}$ ")
        if cmd == "exit":
            os.kill(os.getpid(), signal.SIGTERM)
            break
        if cmd.startswith("cd"): 
            relative_path = cmd[3:].strip()
            try:
                os.chdir(os.path.abspath(relative_path))
            except FileNotFoundError:
                print(f"No such directory: {relative_path}")
        else:
            os.system(cmd)

def subprocess_module():
    while True:
        cmd = input(f"{os.getcwd()}$ ")
        if cmd == "exit":
            break  # Exit the shell loop
        elif cmd.startswith("cd"):
            relative_path = cmd[3:].strip()
            try:
                os.chdir(os.path.abspath(relative_path))
            except FileNotFoundError:
                print(f"No such directory: {relative_path}")
        else:
            # Handle I/O redirection
            if ">" in cmd:  # Output redirection
                command, file = cmd.split(">")
                command = command.strip()
                file = file.strip()
                try:
                    with open(file, "w") as f:
                        sp.run(command.split(), stdout=f, text=True)
                except Exception as e:
                    print(f"Error: {e}")
            elif "<" in cmd:  # Input redirection
                command, file = cmd.split("<")
                command = command.strip()
                file = file.strip()
                try:
                    with open(file, "r") as f:
                        sp.run(command.split(), stdin=f, text=True)
                except FileNotFoundError:
                    print(f"No such file: {file}")
            else:
                # Execute regular commands
                try:
                    sp.run(cmd.split(), text=True)
                except Exception as e:
                    print(f"Error: {e}")

def main():
    while True:
        choice = input("Choose a module (os or subprocess): ").strip().lower()
        if choice == "os":
            os_module()
        elif choice == "subprocess":
            subprocess_module()
        elif choice == "exit":
            print("Exiting shell program.")
            break
        else:
            print("Invalid choice. Please type 'os', 'subprocess', or 'exit'.")

if __name__ == "__main__":
    main()
