# 0x01-caching

This directory contains Python projects focused on implementing various caching systems. Each task explores different cache replacement policies and their implementation.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-basic_cache.py](0x01-caching/0-basic_cache.py)** - Implementation of a basic caching system.
- **Task 1: [1-fifo_cache.py](0x01-caching/1-fifo_cache.py)** - Implementation of a caching system using the First-In-First-Out (FIFO) replacement policy.
- **Task 2: [2-lifo_cache.py](0x01-caching/2-lifo_cache.py)** - Implementation of a caching system using the Last-In-First-Out (LIFO) replacement policy.
- **Task 3: [3-lru_cache.py](0x01-caching/3-lru_cache.py)** - Implementation of a caching system using the Least Recently Used (LRU) replacement policy.
- **Task 4: [4-mru_cache.py](0x01-caching/4-mru_cache.py)** - Implementation of a caching system using the Most Recently Used (MRU) replacement policy.
- **Task 5: [100-lfu_cache.py](0x01-caching/100-lfu_cache.py)** - Implementation of a caching system using the Least Frequently Used (LFU) replacement policy.

## Overview Concepts

- Understand various cache replacement policies such as FIFO, LIFO, LRU, MRU, and LFU.
- Implement caching systems based on different replacement policies.
- Learn about the limitations and use cases of caching systems.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- Pycodestyle (version 2.5.*)

## Setup

1. Install Python 3.7:

```bash
sudo apt update
sudo apt install python3.7
```

2. Install Pycodestyle:

```bash
pip3 install pycodestyle==2.5.0
```

## Usage

To run each caching system, execute the Python script using Python 3.7* or corresponding test file.

- Example for Task 0:

```bash
python3 0-basic_cache.py
```

or

```bash
./0-main.py
```
