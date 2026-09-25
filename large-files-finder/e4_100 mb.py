import os
folder = r'D:\Desktop'
limit = 100 * 1024 * 1024
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        filepath = os.path.join(foldername, filename)
        size = os.path.getsize(filepath)
        if size > limit:
            sizeMB = size / (1024 * 1024)
            print(filename)
            print(filepath)
            print(f'Size: {sizeMB:.2f} MB')
            print('-' * 40)