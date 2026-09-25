import zipfile, os
def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        backupZip.write(foldername)
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue  # از پشتیبان‌گیری از خود فایل‌های ZIP جلوگیری کن
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
backupToZip(r'D:\Desktop\پوشه ها\کار\python\automation\ch10_Organizing Files\p2_zip')