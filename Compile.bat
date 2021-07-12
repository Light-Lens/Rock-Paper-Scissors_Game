@ECHO OFF

title Compile Game
echo Compiling Game.

pyinstaller.exe --icon=Logo.ico --noconsole --onefile main.py

mkdir Rock-Paper-Scissors\res
copy res\* Rock-Paper-Scissors\res\*
move dist\main.exe Rock-Paper-Scissors\Rock-Paper-Scissors.exe

rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__

del main.spec

cls
if EXIST Rock-Paper-Scissors\Rock-Paper-Scissors.exe goto Compiled
if NOT EXIST Rock-Paper-Scissors\Rock-Paper-Scissors.exe goto NotCompiled

:Compiled
echo Rock-Paper-Scissors Compiled Successfully!
echo Get ready to PLAY it!
echo|set /p="Continue."
pause >nul
exit

:NotCompiled
echo Can't Compile Rock-Paper-Scissors!
echo|set /p="Continue."
pause >nul
exit
