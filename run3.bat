@echo off
chcp 65001 > nul
call D:\UniStuff\Змэюка\Configuration_management\.venv\Scripts\activate
cd "D:\UniStuff\Змэюка\Configuration_management"
python main.py "D:\UniStuff\Змэюка\vfs_vault" vfs_test3.sh
pause