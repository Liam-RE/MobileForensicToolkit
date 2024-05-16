import subprocess


def ScreenCopy():
    try:
        # Run scrcpy when deivce is connected 
        command = ["scrcpy"] 
        subprocess.run(command, check=True)
   # Error handling
    except Exception as e:
        print(f"Error: {e}")


