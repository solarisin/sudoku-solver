# Sudoku Solver

This is a Sudoku solver implemented in Python. It provides a graphical user interface (GUI) to solve Sudoku puzzles.

## Installation

To install the project dependencies, you can use [Poetry](https://python-poetry.org/). First, ensure you have Poetry installed, then run the following command in the project directory:

```sh
poetry install
```

To install `pytest` and `pytest-pygame`, run the following commands:

```sh
poetry add pytest
poetry add pytest-pygame
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
poetry run python src/main.py --board "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
```

This command will solve the provided Sudoku puzzle and display the solution in the terminal.

## Running UI Tests

To run the UI tests using `pytest` and `pytest-pygame`, use the following command:

```sh
poetry run pytest tests/test_ui.py
```

To run all tests, including the new tests for the "Solve" and "Undo" buttons, use the following command:

```sh
poetry run pytest
```

## Running Tests

To run the tests, use the following command:

```sh
poetry run pytest
```

We use `pytest` for testing.
