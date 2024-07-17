import shutil
import os

source = 'file.txt'
destination = 'file_backup.txt'

if os.path.exists(source):
    shutil.copy(source, destination)
    print(f'{source} backed up as {destination}')
else:
    print(f'{source} does not exist')
