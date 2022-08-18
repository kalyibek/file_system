import os
import sys
import shutil

dir_path = r'C:\Users\Kalyibek\PycharmProjects\pythonTasks\my_file_system'
operation = sys.argv[1]

if operation == 'list':
    print(os.listdir(dir_path))
else:
    file_name = sys.argv[2]
    match operation:
        case 'add':
            shutil.copy(file_name, os.path.join(dir_path))
            print(f'{os.path.join(dir_path, file_name)} added')
        case 'delete':
            if file_name in os.listdir(dir_path):
                os.remove(os.path.join(dir_path, file_name))
                print(f'{os.path.join(dir_path, file_name)} deleted')
            else:
                print('ERROR')
