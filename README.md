[![Build Status](https://api.travis-ci.org/fabientownsend/tictactoe.svg?branch=master)](https://travis-ci.org/fabientownsend/tictactoe) 
[![codecov.io](https://codecov.io/github/fabientownsend/tictactoe/coverage.svg?branch=master)](https://codecov.io/github/fabientownsend/tictactoe?branch=master)
#Unbeatable Tic-Tac-Toe

## First in first you need to have python 2.7 to be installed
[python 2.7.11](https://www.python.org/downloads/release/python-2711/)

You also need pip:

### On Mac
```bash
$ sudo easy_install pip
```

### On Debian and Ubuntu
```bash
$ sudo apt-get install python-pip
```

### On Windows
You have to add the pip.exe which is install into you python/scripts folder to your environment variable

## Installation & Launch

```bash
$ git clone https://github.com/fabientownsend/tictactoe
$ pip install enum34
$ cd tictactoe
$ python main.py
```

## Usage

```bash
$ python main.py # launch the game
$ 1 # Human v. Human game
$ 1 # Player1 will start
$ 4 # you will put your mark at the position 4
```

```bash
$ python main.py
$ 2 # Human v. Computer game
$ 2 # Player2 (the computer) will start, you can't beat him
```

```bash
$ python main.py
$ 2 # Computer v. Computer game
$ 2 # player2 will start
```

Todo:
- [x] initialise the markdown
- [x] initialise travis ci
- [x] player v. player
- [x] chose who start possibility
- [x] Minimax algorithm
- [x] player v. computer
- [x] computer v. computer
- [ ] refactoring
- [ ] improve the status game
- [x] improve readme for users
- [ ] complete the wiki
- [ ] add logs
