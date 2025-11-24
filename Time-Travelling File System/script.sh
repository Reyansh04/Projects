#!/bin/bash

g++ -std=c++20 assignment1.cpp -o assignment1.exe
if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit 1
fi

echo "Compilation successful. Running program..."
./as1.out
