import os
import socket
import getpass
import sys

vfs_path = sys.argv[1] if len(sys.argv) > 1 else r"C:\default\vfs\path"
startup_script = sys.argv[2] if len(sys.argv) > 2 else None

class VFSNode:
    def __init__(self, name, is_dir):
        self.name = name
        self.is_dir = is_dir
        self.children = {}
        self.content = None

def load_vfs(root_path):
    def load(path):
        if os.path.isdir(path):
            node = VFSNode(os.path.basename(path), True)
            for entry in os.listdir(path):
                child_path = os.path.join(path, entry)
                node.children[entry] = load(child_path)
            return node
        else:
            node = VFSNode(os.path.basename(path), False)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    node.content = f.read()
            except:
                node.content = ""
            return node

    if os.path.isdir(root_path):
        root = load(root_path)
        root.name = ""
        return root
    else:
        # если передан файл вместо папки, создаём виртуальную папку-обёртку
        wrapper = VFSNode("", True)
        wrapper.children[os.path.basename(root_path)] = load(root_path)
        return wrapper

vfs_root = load_vfs(vfs_path)
vfs_cwd = vfs_root
cwd_path = "\\"

def resolve_path(path):
    global vfs_cwd
    if path.startswith("\\"):
        node = vfs_root
        parts = path.strip("\\").split("\\")
    else:
        node = vfs_cwd
        parts = path.split("\\")
    for p in parts:
        if p == "" or p == ".":
            continue
        if p == "..":
            def find_parent(root, target):
                if root is target:
                    return None
                for ch in root.children.values():
                    if ch is target:
                        return root
                    f = find_parent(ch, target)
                    if f:
                        return f
                return None
            parent = find_parent(vfs_root, node)
            if parent:
                node = parent
            continue
        if node.is_dir and p in node.children:
            node = node.children[p]
        else:
            return None
    return node

def ls_command():
    if not vfs_cwd.is_dir:
        print("ls: not a directory")
        return
    for name in sorted(vfs_cwd.children.keys()):
        print(name)

def cd_command(path):
    global vfs_cwd, cwd_path
    target = resolve_path(path)
    if target is None or not target.is_dir:
        print("cd: no such directory:", path)
        return
    if path.startswith("\\"):
        cwd_path = "\\" + path.strip("\\")
    else:
        if cwd_path.endswith("\\"):
            cwd_path = cwd_path + path
        else:
            cwd_path = cwd_path + "\\" + path
    cwd_path = "\\" + "\\".join([p for p in cwd_path.split("\\") if p])
    if cwd_path == "":
        cwd_path = "\\"
    vfs_cwd = target

def pars(x):
    return x.split()

def conf_dump():
    print("conf-dump initiating...")
    print("vfs-path=" + vfs_path)
    print("startup-script=" + str(startup_script))
    print("version=1.0")
    print("author=" + username)
    print("hostname=" + hostname)
    print("current-directory=" + cwd_path)

username = os.getenv('LOGNAME') or os.getenv('USER') or getpass.getuser() or 'unknown.user'
hostname = socket.gethostname()

if "motd.txt" in vfs_root.children and not vfs_root.children["motd.txt"].is_dir:
    print(vfs_root.children["motd.txt"].content)

def run_script(path):
    if path is None:
        return
    if not os.path.exists(path):
        print("Startup script not found:", path)
        return
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            cmd = line.strip()
            if not cmd:
                continue
            process_command(cmd)

def process_command(a):
    if a == "exit":
        exit()
    tokens = pars(a)
    if not tokens:
        return
    if tokens[0] == "ls":
        ls_command()
        return
    if tokens[0] == "cd":
        if len(tokens) < 2:
            print("cd: missing operand")
            return
        cd_command(tokens[1])
        return
    if tokens[0] == "echo":
        print(a[5:])
        return
    if tokens[0] == "conf-dump":
        conf_dump()
        return
    print(f"{tokens[0]}: command not found")

run_script(startup_script)

while True:
    print(f"{username}@{hostname}:{cwd_path}$", end=" ")
    try:
        a = input().strip()
    except EOFError:
        print("\nExiting...")
        break
    process_command(a)
