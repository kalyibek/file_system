import sys
from operations import *

commands = {
    'list': directory_list,
    'add': add_file,
    'remove': remove_file,
}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: no arguments')
        exit()

    _, command, *args = sys.argv

    if command not in commands:
        print(f'Unknown command "{command}"')
        exit()

    commands[command](*args)
