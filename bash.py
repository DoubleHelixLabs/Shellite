import subprocess
import shlex

while True:
    try:
        shcmd = input("shellite@bash-$ ").strip()
        
        if shcmd.lower() in ['exit', 'quit']:
            break
            
        if not shcmd:
            continue
        cmd_parts = shlex.split(shcmd)
        
        cmd_parts[0] = f"/usr/bin/{cmd_parts[0]}"

        subprocess.run(cmd_parts, cwd="/usr/bin")

    except FileNotFoundError:
        print(f"Error: The command '{shcmd.split()[0]}' was not found in /usr/bin.")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting Shellite.")
        break
