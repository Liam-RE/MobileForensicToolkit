import subprocess


def RunAtpy(): 
    try:
        # Run autopsy 
        command = ["sudo","autopsy"] 
        subprocess.run(command, check=True)
   # Error handling 
    except Exception as e:
        print(f"Error: {e}")