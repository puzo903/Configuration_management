import os
import socket
import getpass
import sys

# Параметры эмулятора (должны быть установлены при запуске)
vfs_path = sys.argv[1] if len(sys.argv) > 1 else "/default/vfs/path"
startup_script = sys.argv[2] if len(sys.argv) > 2 else "/default/startup/script"


def pars(x):
    return x.split()


def conf_dump():
    """Команда conf-dump - вывод параметров эмулятора в формате ключ-значение"""
    print("conf-dump initiating...")
    print("vfs-path=" + vfs_path)
    print("startup-script=" + startup_script)
    print("version=1.0")
    print("author=" + username)
    print("hostname=" + hostname)
    print("current-directory=" + current_dir)


username = os.getenv('LOGNAME') or os.getenv('USER') or getpass.getuser() or 'unknown.user'
hostname = socket.gethostname()

current_dir = os.getcwd()
home_dir = os.path.expanduser('~')

if current_dir.startswith(home_dir):
    display_dir = current_dir.replace(home_dir, '~', 1)
else:
    display_dir = current_dir

while True:
    print(f"{username}@{hostname}:{display_dir}$", end=" ")
    a = input().strip()

    if a == "exit":
        exit()

    if pars(a)[0] == "ls":
        print(pars(a))
        continue

    if pars(a)[0] == "cd":
        print(pars(a))
        continue

    if pars(a)[0] == "echo":
        print(a[5:])
        continue
    if pars(a)[0] == "conf-dump":
        conf_dump()
        continue

    else:
        print(f"{pars(a)[0]}: command not found")