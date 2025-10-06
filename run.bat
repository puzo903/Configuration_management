@echo off
chcp 65001 > nul
call D:\UniStuff\Змэюка\Новая папка\.venv\Scripts\activate
cd "D:\UniStuff\Змэюка\Новая папка"
py main.py < script1.sh
py main.py < script2.sh
pause