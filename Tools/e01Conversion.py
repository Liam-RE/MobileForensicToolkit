import subprocess

def e01Convert(FilePath, outputFile): 
    try:
        # Runs ewfacquire tool 
        command = ["sudo", "ewfacquire", "-t", outputFile, FilePath] 
        subprocess.run(command, check=True)
    # Error handling 
    except Exception as e:
        print(f"Error: {e}")

