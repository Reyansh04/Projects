Overview

This project implements a simplified in-memory version control system inspired by Git.
It allows users to create, update, and manage versioned files, including branching, snapshots, rollbacks, and analytics.

The project demonstrates the use of fundamental data structures:

Trees – To manage the version history of each file.

HashMaps – To enable O(1) average-time lookups of versions by ID.

Heaps – To track system-wide metrics like most recently modified files and files with the largest version history.

Note: All data structures (Tree, HashMap, and Heap) are implemented from scratch without using prebuilt C++ libraries like std::map or std::unordered_map.
