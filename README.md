# AMAG Technical Question

## Setup

using pipenv, install packages

set PYTHONPATH to root folder of project

example: run `export PYTHONPATH="path_to/AMAG-Python-exercise/amag_op:path_to/AMAG-Python-exercise/tests"`

## Run Script

The script takes 2 options:

- operate
- process

you can access the options using --help

run `python -m amag_op --help`

`usage: amag_op [-h] {process,operate} ...

Process some floats.

positional arguments:
{process,operate}
process process an excel or csv file with x, y and operation columns
operate perform an operation on x and y

optional arguments:
-h, --help show this help message and exit`

## Tests

run `pytest --cov=tests/ -v` to run tests and check coverage

# TODO

- Add logging
- Add CI/CD
