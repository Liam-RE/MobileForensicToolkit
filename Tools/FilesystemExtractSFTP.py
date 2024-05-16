import subprocess 


def FilesystemExtractSFTP(hostname, username, Devicedir, Localdir):
    try:
        # command to connect to the SFTP server
        command = f'sftp {username}@{hostname}'
        # Open a subprocess to execute the SFTP command
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # Define a list of commands to be executed after connecting
        commands =  f'cd {Devicedir}', f'get -r . {Localdir}', 'exit'
        # Iterate over the commands and send them to the SFTP process
        for cmd in commands:
            process.stdin.write((cmd + '\n').encode())  # Encode and write the command to the subprocess's standard input
            process.stdin.flush()  # Flush the input buffer
        # Communicate with the subprocess and wait for it to finish
        stdout, stderr = process.communicate()
        process.wait()
        print("Transfer Complete")
        
    # Error handling
    except Exception as e:
        print("Error:", str(e))


