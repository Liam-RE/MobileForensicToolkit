import os
import sys


# Add Android and iOS directories to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Android'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'iOS'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Tools'))

# Import functions from Android directory
from AndroidFilesystemExtraction import AndroidFilesystemExtract
from AndroidLogicalBackup import AndroidBackup, ConvertabFile 
from physicalextractionAndroid import CopyPartitions
from RunALEAPP import RunALEAPP

# Import functions from iOS directory
from imageExtarctioniOS import ImageExtraction
from iOSFilesystemUSB import FilesystemExtractiOSUSB
from LogicalBackupiOS import BackupDeviceiOS
from RuniLEAPP import RuniLEAPP

# Import functions from Tools directory
from e01Conversion import e01Convert
from FilesystemExtractSFTP import FilesystemExtractSFTP
from PortScan import PortScan
from RunAutopsy import RunAtpy
from ScreenMirror import ScreenCopy
from WhatsApp import WhatsappChats
from KeyFileSeach import keywordFileSearch

def Menu():
    while True:

        print("""
  __  __       _     _ _        _____                        _        _____           _ _    _ _   
 |  \/  | ___ | |__ (_) | ___  |  ___|__  _ __ ___ _ __  ___(_) ___  |_   _|__   ___ | | | _(_) |_ 
 | |\/| |/ _ \| '_ \| | |/ _ \ | |_ / _ \| '__/ _ \ '_ \/ __| |/ __|   | |/ _ \ / _ \| | |/ / | __|
 | |  | | (_) | |_) | | |  __/ |  _| (_) | | |  __/ | | \__ \ | (__    | | (_) | (_) | |   <| | |_ 
 |_|  |_|\___/|_.__/|_|_|\___| |_|  \___/|_|  \___|_| |_|___/_|\___|   |_|\___/ \___/|_|_|\_\_|\__|

            ╔════════════════════════════════════════════════════════════════════════════╗   
            ║       Github : https://github.com/Liam-RE/MobileDeviceForensicToolkit      ║   
            ║                         Created by: Liam Reynolds                          ║   
            ╚════════════════════════════════════════════════════════════════════════════╝   

                                 1. Device Backup                                               
                                 2. Forensic Tools
                                 3. Others
                                 
                                 0. Exit
""")

        choice = input("> ")

        if choice == '1':
            while True:
                print("""
                                  ╔════════════════════════════╗
                                  ║         Acquisition        ║   
                                  ╚════════════════════════════╝   

                                  1. iOS Backup                             
                                  2. Android Backup                  
                                  3. Android Root Extraction (USB)       
                                  4. Root/Jailbreak Extraction (SFTP) 
                                  5. Jailbreak Extraction (USB)              
                                  6. Physical Extraction (Android)                             
                                  
                                  0. Main Menu                   
                """)
                choice = input("> ")

                if choice == '1':
                    BackupDir = input("Backup Directory: ")
                    BackupDeviceiOS(BackupDir)
                elif choice == '2':
                    AndroidBackup()
                    OutputFileName = input("Backup File Name (.tar): ") 
                    ConvertabFile(OutputFileName)

                elif choice == '3':
                    OutputDir = input("Output Location: ")
                    AndroidFilesystemExtract(OutputDir)
                elif choice == '4':
                    hostname = input("Enter hostname (IP): ")
                    username = input("Enter username: ")
                    Devicedir = input("Directory to copy from (on remote device): ")
                    Localdir = input("Directory to paste into (on local machine): ")
                    FilesystemExtractSFTP(hostname, username, Devicedir, Localdir)
                elif choice == '5':
                    Path = input("Path to mount filesystem: ")
                    pasteDir = input("Output Directory: ")
                    FilesystemExtractiOSUSB(Path, pasteDir)
                
                elif choice == '6':
                    OutputDir = input("Output directory path: ")
                    CopyPartitions(OutputDir)



                elif choice.lower() == '0':
                    
                    break
                    
                else:
                    print("Invalid choice.")
        elif choice == '2':
            while True:
        
                print("""
                                    ╔═══════════════════════════╗   
                                    ║       Forensic Tools      ║   
                                    ╚═══════════════════════════╝   

                                    1. Convert Logical Folder to .e01      
                                    2. Run iLEAPP                                         
                                    3. Run ALEAPP                           
                                    4. Run Autopsy                       
                                    5. NMAP (Check Device IP)                    
                                                                    
                                    0. Main Menu               
                """)
                choice = input("> ")

                if choice == '1':
                    FilePath = input("File Path: ")
                    outpuFile = input("Output File: ")
                    e01Convert(FilePath, outpuFile)
                elif choice == '2':

                    Path = input("Enter the path to backup folder: ")
                    output = input("Enter the output path: ")
                    BackupType = input("Enter Backup Type (e.g., fs, tar, zip, gz, itunes): ")
                    RuniLEAPP(Path, output, BackupType)
                elif choice == '3':
                    
                    Path = input("Enter the path to backup folder: ")
                    output = input("Enter the output path: ")
                    BackupType = input("Enter Backup Type (e.g., fs, tar, zip, gz): ")
                    RunALEAPP(Path, output, BackupType)
                elif choice == '4':
                    RunAtpy()
                elif choice == '5':
                    DeviceIP = input("IP Range: ")
                    PortScan(DeviceIP)
                elif choice.lower() == '0':
                 
                    break
                else:
                    print("Invalid choice.")

        elif choice == '3':
            while True:

                print("""
                                    ╔═════════════════════════╗   
                                    ║          Others         ║   
                                    ╚═════════════════════════╝   
               
                                    1. Key File Search                               
                                    2. Mirror + Control Device (Android) 
                                    3. Whatsapp Message Viewer
                                    4. Image Gathering                

                                    0. Main Menu                    
                """)
                choice = input("> ")
                if choice == '1':
                    print("This module takes key sections from application reports from A/iLEAPP")
                    SourceDir = input("A/iLEAPP Directory: ")
                    OutputDir = input("Output Folder: ")
                    keyword = input("Enter the keyword to search for: ")
                    keywordFileSearch(SourceDir, OutputDir, keyword)
                elif choice == '2':
                    ScreenCopy()
                elif choice == '3':
                    WhatsappChats()
                elif choice == '4':
                    BackupDir = input("iPhone backup directory: ")
                    ManifestPath = input("Path to the Manifest.db file: ")
                    OutputDir = input("Saved images directory: ")
                    ImageExtraction(ManifestPath, BackupDir, OutputDir)

                elif choice.lower() == '0':
               
                    break
                else:
                  print("Invalid Input.")

        elif choice.lower() == '0':
            print("Exiting....")
            break
        else:
            print("Invalid Input.")

Menu()