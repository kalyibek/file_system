import os
import sys
import shutil

dir_path = r'C:\Users\Kalyibek\PycharmProjects\pythonTasks\my_file_system'
operation = sys.argv[1]

if operation == 'list':
    print(os.listdir(dir_path))
else:
    file_name = sys.argv[2]
    file_path = os.path.join(dir_path, file_name)
    if operation == 'add':
        shutil.copy(file_name, dir_path)
        print(f'{file_path} added')
    elif operation == 'remove' and file_name in os.listdir(dir_path):
        os.remove(file_path)
        print(f'{file_path} deleted')
    else:
        print('ERROR')
