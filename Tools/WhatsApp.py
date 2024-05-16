import subprocess

def WhatsappChats():
    try:
        # directory to whapa program 
        ScriptPath = 'Tools/whapa/whapa-gui.py'
        # Run whapa 
        subprocess.run(['python3', ScriptPath])
    # Error handling 
    except Exception as e:
        print(f"Error: {e}")


