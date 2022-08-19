import os
import shutil

ROOT_DIR = r'C:\Users\Kalyibek\PycharmProjects\pythonTasks\my_file_system'

def directory_list(*args):
    print(os.listdir(ROOT_DIR))

def add_file(*args):
    if len(args) < 1:
        print("Enter file name")
        exit()
    shutil.copy(args[0], ROOT_DIR)
    print(f'"{args[0]}" added')

def remove_file(*args):
    if len(args) < 1:
        print("Enter file name")
        exit()
    if args[0] not in os.listdir(ROOT_DIR):
        print(f'Error: "{args[0]}" is not in your file system.')
        exit()
    os.remove(os.path.join(ROOT_DIR, args[0]))
    print(f'"{args[0]}" removed')
