@echo off

cd

:inname
set /p name=������ui�ļ�����:

if not defined name goto inname

pyuic5 "%name%".ui -o "%name%".py -x

pause