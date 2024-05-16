import subprocess


def FilesystemExtractiOSUSB(Path, pasteDir):
    # Runs ifuse for filesystem Extraction
    try:
        subprocess.run(['ifuse', '--root', Path], check=True)
        print("Device Mounted")
        # Copies / Directory
        subprocess.run(['cp', '-r', Path, pasteDir], check=True)
        print("Complete")
    # Error handling   
    except subprocess.CalledProcessError as e:
        print("Error:", e)
