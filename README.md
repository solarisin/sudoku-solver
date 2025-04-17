# Sudoku Solver

This is a Sudoku solver implemented in Python. It provides a graphical user interface (GUI) to solve Sudoku puzzles.

## Installation

To install the project dependencies, you can use [Poetry](https://python-poetry.org/). First, ensure you have Poetry installed, then run the following command in the project directory:

```sh
poetry install
```

## Usage

To run the Sudoku solver, use the following command:

```sh
poetry run python src/main.py
```

This will launch the graphical user interface where you can interact with the Sudoku solver.

## Example

Here is an example of how to use the command-line interface to solve a Sudoku puzzle:

```sh
poetry run python src/main.py --board "5,3,0,0,7,0,0,0,0;6,0,0,1,9,5,0,0,0;0,9,8,0,0,0,0,6,0;8,0,0,0,6,0,0,0,3;4,0,0,8,0,3,0,0,1;7,0,0,0,2,0,0,0,6;0,6,0,0,0,0,2,8,0;0,0,0,4,1,9,0,0,5;0,0,0,0,8,0,0,7,9"
```

This command will solve the provided Sudoku puzzle and display the solution in the terminal.
