#!/bin/bash
# Compile main.cpp with C++20 and run the resulting binary
g++ -std=c++20 main.cpp -o main.out
if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit 1
fi

echo "Compilation successful. Running program..."
./main.out
