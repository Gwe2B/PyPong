# PyPong

A really simple python arcade game for exploring the library

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![Arcade version](https://img.shields.io/badge/Arcade_V-3.3.2-green)](https://api.arcade.academy/en/3.3.2/)
[![Python version](https://img.shields.io/badge/Python_V-3.11.0-green?logo=python&logoColor=white)](https://www.python.org/)


## Installation

Simply download the executable that match your OS and enjoy.

*Note: If your OS isn't listed, you have the instructions to compile it yourself bellow*

## Install project (for dev)

### Requirements

 - Python version 3.11 or higher
 - PIP package
 - VENV package (`pip install venv`)

### Project set up

```txt
~ $> git clone git@github.com:Gwe2B/PyPong.git
~ $> cd PyPong
~/PyPong $> python -m venv .venv
# On Windows
~/PyPong $> .venv/Scripts/activate
# On Linux
~/PyPong $> source .venv/bin/activate

~/PyPong $> pip install -r requirements.txt

# To launch the project
~/PyPong $> python main.py
```

### Build project (optionnal)

First follow the instructions on how to set up the project then:

```txt
~/PyPong $> pip install pyinstaller
~/PyPong $> pyinstaller -F main.py
```

It will generate a main.exe file in the dist folder. You just have to double click and enjoy.

## Credits

 - Ball bounce sound effect: [https://freesound.org/people/adh.dreaming/sounds/615576/](Bit Bounce by adh.dreaming)
 - Scoring sound effect: [https://freesound.org/people/AceOfSpadesProduc100/sounds/333785/?](8-bit "failure" sound by AceOfSpadesProduc100)
 - Count down: Myself (made with [https://www.audacityteam.org/](Audacity))