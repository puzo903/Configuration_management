# Цель: создать минимальный прототип. Большинство функций в нем пока
# представляют собой заглушки, но диалог с пользователем уже поддерживается.
# Требования:
# 1. Приложение должно быть реализовано в форме консольного интерфейса
# (CLI).
# 2. Приглашение к вводу должно формироваться на основе реальных данных
# ОС, в которой исполняется эмулятор. Пример: username@hostname:~$.
# 3. Реализовать парсер, который корректно обрабатывает аргументы в
# кавычках.
# 4. Реализовать команды-заглушки, которые выводят свое имя и аргументы: ls,
# cd.
# 5. Реализовать команду exit.
# 6. Продемонстрировать работу прототипа в интерактивном режиме.
# Необходимо показать примеры работы всей реализованной
# функциональности, включая обработку ошибок.
# 7. Результат выполнения этапа сохранить в репозиторий стандартно
# оформленным коммитом.


import os
import socket
import getpass

def pars(x):
    return x.split()

username = os.getenv('LOGNAME') or os.getenv('USER') or getpass.getuser() or 'unknown.user'
hostname = socket.gethostname()

current_dir = os.getcwd()
home_dir = os.path.expanduser('~')

if current_dir.startswith(home_dir):
    display_dir = current_dir.replace(home_dir, '~', 1)
else:
    display_dir = current_dir


while True:
    print(f"{username}@{hostname}:~{display_dir}>")
    a=input()
    if a == "exit":
        exit()
    if a[:2] == "ls" or a[:3] == "ls ":
        print(pars(a))
        continue
    if a[:2] == "cd" or a[:3] == "cd ":
        print(pars(a))
        continue
    else:
        print(f"{a}: unknown command")
