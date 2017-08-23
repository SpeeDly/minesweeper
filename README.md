# Minesweeper

Minimalistic python game intended to Python course

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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

## Authors

Georgi Zhuhov

## License

No License
