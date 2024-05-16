import os
import shutil

def keywordFileSearch(SourceDir, OutputDir, keyword):
    # Check if source directory exists
    if not os.path.exists(SourceDir):
        print(f"Source directory '{SourceDir}' does not exist.")
        return
    
    # Check if destination directory exists
    if not os.path.exists(OutputDir):
        os.makedirs(OutputDir)
    
    # Check files and directories in source directory
    for item in os.listdir(SourceDir):
        filePath = os.path.join(SourceDir, item)
        
        # Check if the item name contains the keyword
        if keyword.lower() in item.lower():
            # Check if the item is a file
            if os.path.isfile(filePath):
                OutputPath = os.path.join(OutputDir, item)
                shutil.copy2(filePath, OutputPath)
                print(f"Copied '{item}' to '{OutputDir}'")
            # Check if the item is a directory
            elif os.path.isdir(filePath):
                OutputPath = os.path.join(OutputDir, item)
                shutil.copytree(filePath, OutputPath)
                print(f"Copied directory '{item}' to '{OutputDir}'")
        # Find _elements
        elif os.path.isdir(filePath) and item.lower() == "_elements":
            destination_elements_path = os.path.join(OutputDir, "_elements")
            shutil.copytree(filePath, destination_elements_path)
            print(f"Copied '_elements' folder to '{OutputDir}'")


