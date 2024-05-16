import subprocess


def AndroidBackup():
    try:
        # Initiate logical backup 
        backupCMD = ["sudo", "adb", "backup", "-all", "-f", "backup.ab"]
        subprocess.run(backupCMD, capture_output=True, text=True, check=True)
    
    except subprocess.CalledProcessError as e:
        print("Error: ", e)

def ConvertabFile(OutputFileName):
    try:
        # Run backup extractor 
        convertCMD = ["sudo", "java", "-jar", "abe.jar", "unpack", "backup.ab", OutputFileName]
        subprocess.run(convertCMD, capture_output=True, text=True, check=True)
        print("Complete")
    
    except subprocess.CalledProcessError as e:
        print("Error: ", e)