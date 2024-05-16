import subprocess
import os

def CheckPartitions():
    partitions = []
    try:
        # Command to retrieve partition information
        command = ["adb", "shell", "su", "-c", "cat /proc/partitions"]
        output = subprocess.check_output(command).decode("utf-8")
        # Split output by newline characters and extract partition names
        lines = output.strip().split('\n')[2:]  
        for line in lines:
            partition = line.split()[-1]
            partitions.append(partition)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    return partitions

def CopyPartitions(OutputDir):
    try:
        # Get the list of partitions using CheckPartitions function
        partitions = CheckPartitions()
        if not partitions:
            print("No partitions found.")
            return

        for partition in partitions:
            OutputFile = os.path.join(OutputDir, f"{partition}.dd")
            # Execute adb command to copy partition
            command = f'adb shell su -c "dd if=/dev/block/{partition}"'
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            # Loops until there's no more data to copy
            with open(OutputFile, "wb") as f:
                while True:
                    data = process.stdout.read(4096)
                    if not data:
                        break
                    f.write(data)
            print(f"Partition '{partition}' copied")
    # Error handling 
    except Exception as e:
        print("Error:", e)


