import os
import sys
import shutil

def directory_list(*file, directory):
    print(os.listdir(directory))

def add_file(file, directory):
    shutil.copy(file, directory)
    print(f'"{file}" added')

def remove_file(file, directory):
    if file in os.listdir(directory):
        os.remove(os.path.join(directory, file))
        print(f'"{file}" removed')
    else:
        print(f'Error: "{file}" is not in your file system.')

commands = {
    'list': directory_list,
    'add': add_file,
    'remove': remove_file
}

def main():
    dir_path = r'C:\Users\Kalyibek\PycharmProjects\pythonTasks\my_file_system'
    operation = sys.argv[1]
    file_name = ''

    if 'list' not in sys.argv:
        if len(sys.argv) < 3:
            exit('Enter file name')
        else:
            file_name = sys.argv[2]

    if operation in commands:
        commands[operation](file_name, directory=dir_path)
    else:
        print(f'Unknown command "{operation}"')


if __name__ == '__main__':
    main()
