import subprocess
import os

def RunALEAPP(Path, output, BackupType):
    # Check if the backup folder exists
    if not os.path.exists(Path):
        print("Backup folder does not exist.")
        return
   
    try:
        # Run Command
        command = ["python3", "./Tools/ALEAPP/aleapp.py", "-i", Path, "-o", output, "-t", BackupType] 
        subprocess.run(command, check=True)
        print("ALEAPP processing completed successfully.")
    # Error handling
    except subprocess.CalledProcessError as e:
        print("Error: ", e)