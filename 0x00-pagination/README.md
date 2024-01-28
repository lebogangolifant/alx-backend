# 0x00. Pagination

This directory contains Python projects focused on implementing pagination in a backend context. Each task explores different aspects of pagination, including simple page and page_size parameters, hypermedia metadata, and deletion-resilient pagination.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-simple_helper_function.py](0x00-pagination/0-simple_helper_function.py)** - Implementation of a simple pagination helper function.
- **Task 1: [1-simple_pagination.py](0x00-pagination/1-simple_pagination.py)** - Implementation of a class for simple pagination using the helper function.
- **Task 2: [2-hypermedia_pagination.py](0x00-pagination/2-hypermedia_pagination.py)** - Implementation of hypermedia pagination with additional metadata.
- **Task 3: [3-hypermedia_del_pagination.py](0x00-pagination/3-hypermedia_del_pagination.py)** - Implementation of deletion-resilient hypermedia pagination.

## Overview Concepts

The tasks in this directory cover the following Pagination concepts:

- Simple pagination techniques with page and page_size parameters.
- Hypermedia pagination with additional metadata.
- Deletion-resilient hypermedia pagination for handling removed rows between queries.

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

To run each task, execute the Python script using Python 3.7* or corresponding test file.


- Example for Task 0:

```bash
python3 0-simple_helper_function.py
```
or

```bash
./0-main.py
```
