[![Build Status](https://api.travis-ci.org/fabientownsend/tictactoe.svg?branch=master)](https://travis-ci.org/fabientownsend/tictactoe) 
[![codecov.io](https://codecov.io/github/fabientownsend/tictactoe/coverage.svg?branch=master)](https://codecov.io/github/fabientownsend/tictactoe?branch=master)

#Unbeatable Tic-Tac-Toe
![tictactoe](https://lh3.googleusercontent.com/-a9v5dd-AVfc/VqzalVGTb6I/AAAAAAAAF5A/rIYiW0SVVfU/w1406-h794-no/tictactoe.png)

Here you can find [documentation](https://github.com/fabientownsend/tictactoe/wiki) that I wrote about the project, I tried to cover subject like architecture and algorithm.

## Firstly you need to have `python 2.7` to be installed
[python 2.7.11](https://www.python.org/downloads/release/python-2711/)

If you don't use Vagrant you will also need to install `pip` the Python's package manager and the package enum34.

### On Mac
```bash
$ sudo easy_install pip
$ pip install enum34
```

### On Debian and Ubuntu
```bash
$ sudo apt-get install python-pip
$ pip install enum34
```

### On Windows
You have to add the pip.exe which is install into you python/scripts folder to your environment variable
```bash
$ pip install enum34
```

## Installation
```bash
$ git clone https://github.com/fabientownsend/tictactoe
```

## Run  with Vagrant
```bash
$ cd /tictactoe
$ vagrant up
$ vagrant ssh
```

## Test the application
**Running all tests:**
```bash
$ python -m unittest discover
```

**Running a single test class:**
```bash
$ python -m unittest tests.test_computer
```

**Running a single test method:**
```bash
$ python -m unittest tests.test_comuter.test_computer.test_set_mark_with_cross
```

## Usage
Runn the game
```bash
$ cd /src
$ python python main.py
```

1. First menu you can choose the game mode between 1, 2 and 3
2. You have to pick up which player start between 1 and 2
3. You can put a mark on the board between 0 and 8

## Example 1
```bash
$ python main.py # launch the game
$ 1 # Human v. Human game
$ 1 # Player1 will start
$ 4 # You will put your mark at the position 4
```

## Example 2
```bash
$ python main.py
$ 2 # Human v. Computer game
$ 2 # Player2 (the computer) will start, you can't beat him
```

## Example 3
```bash
$ python main.py
$ 2 # Computer v. Computer game
$ 2 # Player2 will start
```
### TODO
- [x] add French language
- [x] implement language selction
- [ ] implement factory method for players creation [branch](https://github.com/fabientownsend/tictactoe/tree/factory_method)
- [ ] improve performance with [alpha-beta algorithm](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- [ ] record performence about minimax vs alpha-beta
- [ ] Choose the library for the GUI interface https://pythonspot.com/gui/
- [ ] implement GUI
