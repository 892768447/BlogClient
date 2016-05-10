@echo off

cd

:inname
set /p name=请输入ui文件名字:

if not defined name goto inname

pyuic5 "%name%".ui -o "%name%".py -x

pause