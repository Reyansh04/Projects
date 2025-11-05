@echo off
rem Compile main.cpp with C++20 and run the executable
g++ -std=c++20 main.cpp -o main.exe
if %errorlevel% neq 0 (
    echo Compilation failed.
    pause
    exit /b %errorlevel%
)
echo Compilation successful. Running program...
main.exe
pause
