import os
import shutil

ROOT_DIR = r'C:\Users\Kalyibek\PycharmProjects\pythonTasks\my_file_system'

def directory_list(*args: str) -> None:
    _ = args
    for file_name in os.listdir(ROOT_DIR):
        file_path = os.path.join(ROOT_DIR, file_name)
        file_size = os.stat(file_path).st_size

        print(f'{file_name}: {file_size}')

def add_file(*args: str) -> None:
    if len(args) < 1:
        print("Enter file name")
        exit()

    file_name = args[0]
    shutil.copy(file_name, ROOT_DIR)

    print(f'"{file_name}" added')


def remove_file(*args: str) -> None:
    if len(args) < 1:
        print("Enter file name")
        exit()

    file_name = args[0]

    if file_name not in os.listdir(ROOT_DIR):
        print(f'Error: "{file_name}" is not in your file system.')
        exit()

    os.remove(os.path.join(ROOT_DIR, file_name))

    print(f'"{file_name}" removed')
