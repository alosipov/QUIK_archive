#!/usr/bin/python
 
import os
import zipfile
from datetime import date, timedelta
 
os.system("taskkill /f /im  info.exe") #убиваем запущенные процессы квика

 
def main():

    archive_dir = "C:/ARCHIVE/" # место куда кладем архивы
    source_dir = "C:/QUIK/TEST/Quik_DM"  # место откуда берем данные для архива
 
    yesterday = date.today() - timedelta(days=1)    # вчерашняя дата
 
    archive_name = str(yesterday) + '_' + os.getlogin() + '.zip'        # получаем имя архива 'вчерашняя дата' + 'имя пользователя'
 
    zf = zipfile.ZipFile(archive_dir+archive_name, "w", zipfile.ZIP_DEFLATED)
    for dirname, subdirs, files in os.walk(source_dir):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
    
print('Archive has been created successfully')
    
if __name__ == '__main__':
    main()
