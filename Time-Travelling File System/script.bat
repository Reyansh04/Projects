@echo off
g++ -std=c++20 assignment1.cpp -o assignment1.exe
if %errorlevel% neq 0 (
    echo Compilation failed.
    pause
    exit /b %errorlevel%
)
echo Compilation successful. Running program...
assignment1.exe
pause
