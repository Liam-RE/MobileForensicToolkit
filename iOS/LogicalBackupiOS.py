import subprocess

def BackupDeviceiOS(BackupDir):
    # Check if the device is connected
    CheckIDCommand = ["idevice_id", "-l"]
    CheckDevice = subprocess.run(CheckIDCommand, capture_output=True, text=True)
    # If a device is not detected
    if not CheckDevice.stdout:
        print("No iOS device is connected.")
        return
    udid = CheckDevice.stdout.strip()  
    print(f"Backing up: {udid}")
    # Run backup with device detected. 
    try:
        subprocess.run(["idevicebackup2", "-u", udid, "backup", BackupDir], check=True)
        print(f"Backup successful: {BackupDir}")
    # Error handling 
    except subprocess.CalledProcessError:
        print("Backup Failed.")


