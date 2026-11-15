
import os
import shutil

# Set the folder to organize
folder = 'test folder'

# Get all files in the folder
for fileName in os.listdir(folder):
    filePath = os.path.join(folder, fileName)

    # Skip folders
    if os.path.isfile(filePath):
        fileName, fileExtension = os.path.splitext(fileName)
        fileExtension = fileExtension.lower()

        # Determine destination folder
        if fileExtension in ['.jpg', '.png', '.jpeg', '.gif']:
            folderName = 'Images'
        elif fileExtension == '.pdf':
            folderName = 'PDFs'
        elif fileExtension in ['.xlsx', '.xls', '.csv']:
            folderName = 'Excel'
        elif fileExtension in ['.mp3', '.wav']:
            folderName = 'Audio'
        elif fileExtension in ['.mp4', '.mkv']:
            folderName = 'Videos'
        elif fileExtension == '.txt':
            folderName = 'Text'
        else:
            folderName = 'Others'

        # Create destination folder
        destinationFolder = os.path.join(folder, folderName)
        os.makedirs(destinationFolder, exist_ok=True)

        # Move file
        sourcePath = os.path.join(folder, fileName + fileExtension)
        destinationPath = os.path.join(
            destinationFolder, fileName + fileExtension
        )

        if not os.path.exists(destinationPath):
            shutil.move(sourcePath, destinationPath)

print('Files organized successfully!')
