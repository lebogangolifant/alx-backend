# 0x02. i18n

This directory contains Python projects focused on implementing internationalization (i18n) in a Flask application. Each task explores different aspects of i18n, including language localization, timezone support, and user login emulation.

## Table of Contents

- [Task Descriptions](#task-descriptions)
- [Overview Concepts](#overview-concepts)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Task Descriptions

- **Task 0: [0-app.py](0x02-i18n/0-app.py)** - Basic Flask app with a single route and template.
- **Task 1: [1-app.py](0x02-i18n/1-app.py)** - Setting up Flask-Babel extension and configuring available languages.
- **Task 2: [2-app.py](0x02-i18n/2-app.py)** - Implementing language selection based on URL parameters.
- **Task 3: [3-app.py](0x02-i18n/3-app.py)** - Parametrizing Flask templates for localization and creating translation files.
- **Task 4: [4-app.py](0x02-i18n/4-app.py)** - Implementing forced locale through URL parameters.
- **Task 5: [5-app.py](0x02-i18n/5-app.py)** - Emulating user login system and displaying user-specific messages.
- **Task 6: [6-app.py](0x02-i18n/6-app.py)** - Using user's preferred locale for language selection.
- **Task 7: [7-app.py](0x02-i18n/7-app.py)** - Setting up timezone selection for users.
- **Task 8: [app.py](0x02-i18n/app.py)** - Displaying the current time in the user's timezone and language.

## Overview Concepts

The tasks in this directory cover the following i18n concepts:

- Setting up Flask-Babel extension and configuring available languages.
- Language selection based on URL parameters and user settings.
- Localization of Flask templates and creation of translation files.
- Implementation of forced locale through URL parameters.
- Emulating user login system and displaying user-specific messages.
- Using user's preferred locale for language selection.
- Setting up timezone selection for users.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- Flask-Babel (version 2.0.0)
- Pycodestyle (version 2.5.*)

## Setup

1. Install Python 3.7:

```bash
sudo apt update
sudo apt install python3.7
```

2. Install Flask-Babel:

```bash
pip3 install flask_babel==2.0.0
```

3. Install Pycodestyle:

```bash
pip3 install pycodestyle==2.5.0
```

## Usage

To test different translations visit:

- Example for Task 4:

```bash
http://127.0.0.1:5000?locale=[fr|en]
```
