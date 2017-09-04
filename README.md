# Minesweeper

Minimalistic python game for the Python course in FMI, Sofia University.
The game is written in python3, using the PyQt5 library.
There are 2 modules:
* Server - Observing current games and providing functionality to watch it online
* Client - PyQt5 base user interface for playing minesweeper

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

To install the game, you should go through a few simple steps:
Clone the repo
```
git clone https://github.com/SpeeDly/minesweeper.git
```

Once it is done, you need to install the dependencies:
```
pip install -r requirements.txt
```

## Running the tests

Before we start the game, we need to verify that the tests are working
To run the test, you just need execute the following command:
```
python -m pytest minesweeper/tests/ --cov=minesweeper --cov-branch --cov-report=term-missing
```

## Starting the process

There are 2 parts of the project. The instruction for each of it are different.
To start the client, you need to execute. After the successful running of the command, you will be able to play the game locally.
```
python main.py
```
To start the server, use the following command.
```
FLASK_APP=server/server.py flask run
```

NB!: You can play the game, without starting the server!

To start the serve

## TODO

* Move the calls for the server in a separate thread.
* Add fabric like library for abstracting of start commands.

## Authors

Georgi Zhuhov

## License

No License
