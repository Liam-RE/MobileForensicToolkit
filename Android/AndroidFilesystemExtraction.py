import subprocess


def AndroidFilesystemExtract(OutputDir):
    try:
        
        # adb shell command to perform filesystem extarction of the root directory
        adbShell = ["sudo", "adb", "pull", "/", OutputDir]
        subprocess.run(adbShell, capture_output=True, text=True, check=True)
        # Error Handling 
    except subprocess.CalledProcessError as e:
        print("Error: ", e)