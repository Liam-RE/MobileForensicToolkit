import subprocess
import os

def RuniLEAPP(Path, output, BackupType):
    # Check if the backup folder exists
    if not os.path.exists(Path):
        print("Backup folder does not exist.")
        return
    # Run iLEAPP 
    try:
        iLEAPPCommand = ["python3", "./Tools/iLEAPP/ileapp.py", "-i", Path, "-o", output, "-t", BackupType] 
        subprocess.run(iLEAPPCommand, check=True)
        print("Completed.")
   # Error handling 
    except subprocess.CalledProcessError as e:
        print("Error: ", e)