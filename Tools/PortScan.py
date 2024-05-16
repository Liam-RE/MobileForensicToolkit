import subprocess


def PortScan(DeviceIP): 
    # Run nmap command - Searches for Operating System on Port 22 and the user selected IP Range 
    try:
        command = ["sudo", "nmap", "-O", "-p", "22", DeviceIP]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    # Error handling
    except subprocess.CalledProcessError as e:
        print("Error: ", e)
