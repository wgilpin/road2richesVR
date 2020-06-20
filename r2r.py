# Author: Will Gilpin
# Road to riches paste system name for Elite Dangerous

import sys


def text2clip(text):
    import subprocess
    subprocess.run('clip.exe', input=text.strip().encode('utf-16'))


def process_file(file_name):
    systems = []
    next_system = ''
    done_mark = "[x] "
    with open(file_name, mode='r') as f:
        header = f.readline()
        for line in f.readlines():
            toks = line.split(sep=',')
            system_name = toks[0].strip('"')
            if not system_name.startswith(done_mark) and len(next_system) == 0:
                next_system = system_name
                text2clip(system_name)
                system_name = done_mark + system_name
            systems.append(system_name)
    with open(file_name, mode='w') as new_f:
        new_f.write(header)
        new_f.writelines(f"{system.rstrip()}\n" for system in systems)
    print(f"Next System: {next_system}")


if len(sys.argv) != 2:
    print("Usage: r2r <File Name>")
    print("  where <File Name> refers to a CSV file, with header row, where first column is system name")

process_file(sys.argv[1])
