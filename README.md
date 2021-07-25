# AMAG Technical Question

A simple project to showcase a potential solution to setting up a production ready project.

The project aims to create a command line interface that allows the user to perform an operation on two numbers.

The input can be either a csv or excel file, or the numbers that the user wishes to perform an operation on.

## Setup

Using pipenv, install packages by running `pipenv install` (if you don't have pipenv, you can install it by running `pip install pipenv`)

set `PYTHONPATH` to root folder of project
example: run `export PYTHONPATH="path_to/AMAG-Python-exercise/amag_op:path_to/AMAG-Python-exercise/tests"`

## Run Script

### --help

The script can be used to perform an operation on 2 numbers, or take in an excel file that has a standard column structure (columns must include x, y and operation).

The script takes 2 options:

- operate
- process

you can access some documentation using the `--help` optional argument.

```
$ python -m amag_op --help
usage: amag_op [-h] {process,operate} ...

Process some floats.

positional arguments:
{process,operate}
process process an excel or csv file with x, y and operation columns
operate perform an operation on x and y

optional arguments:
-h, --help show this help message and exit
```

Furthermore, you can access the `process` command documentation using the optional `--help` argument:

```
$ python -m amag_op process --help
usage: amag_op process [-h] [-s S] [-o O] file

positional arguments:
  file

optional arguments:
  -h, --help       show this help message and exit
  -s S, -sheet S   Excel sheetname
  -o O, -output O  output file name, defaults to filename with _out suffix
```

In addition to the `process` command documentation using the optional `--help` argument:

```
$ python -m amag_op operate --help
usage: amag_op operate [-h] x y op

positional arguments:
  x           the first float argument
  y           the second float argument
  op          the operation name

optional arguments:
  -h, --help  show this help message and exit
```

### Running the script

To read in an excel file with the standard x, y and operation columns, and produce a results output excel file, run the following command `python -m amag_op process "Sample Input.xlsx"`.

```
$ python -m amag_op process "Sample Input.xlsx"
Saved results to 'Sample Input_out.xlsx'
```

You can also specify the sheet name, and the output file name as follows:

```
$ python -m amag_op process "Sample Input.xlsx" -s "Sheet1" -o "test_output.csv"
Saved results to 'test_output.csv'
```

If you want to run the script on a single row, you can use the operate command as follows:

```
$ python -m amag_op operate 100 5 division
division(100.0, 5.0) = 20.0
```

## Frameworks and Libraries used

- pytest (for writing unit tests)
- argparse (for writing the command line interface)
- pandas (for dealing with data frames), this library relies on openpyxl.

## Tests

### Running tests

run `pytest --cov=tests/` to run tests and check coverage
example:

```
$ pytest --cov=tests/
======================================================================================================= test session starts ========================================================================================================
platform win32 -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Yahya Fidouh\OneDrive\Documents\AMAG-Python-exercise
plugins: cov-2.12.1
collected 45 items

tests\test_amag_op.py xxxx                                                                                                                                                                                                    [  8%]
tests\test_cli.py xxxxx                                                                                                                                                                                                       [ 20%] ===================================================
tests\test_ops.py ........x...............                                                                                                                                                                                    [ 73%]
tests\test_ops_raises.py ............                                                                                                                                                                                         [100%]

----------- coverage: platform win32, python 3.9.6-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
tests\test_amag_op.py         14      0   100%
tests\test_cli.py             17      0   100%
tests\test_ops.py             23      0   100%
tests\test_ops_raises.py      32      0   100%
----------------------------------------------
TOTAL                         86      0   100%


================================================================================================== 35 passed, 10 xfailed in 0.67s ==================================================================================================
```

## Folder Structure

The project is set up as a python module to facilitate installation (once the setup script is added) and organising the files.

```
.
├───── amag_op
│    ├───── cli
│    │    ├───── __init__.py
│    │    └───── cli.py
│    │────── exceptions
│    │    ├───── file_type_errors.py
│    │    ├───── op_type_errors.py
│    │    ├───── type_errors.py
│    │    └───── __init__.py
│    │────── ops
│    │    ├───── amag_op.py
│    │    ├───── ops.py
│    ├───── helpers
│    │    ├───── io_helpers.py
│    ├───── __init__.py
│    └───── __main__.py
├───── tests
│    ├───── test_amag_op.py
│    ├───── test_cli.py
│    ├───── test_ops.py
│    └───── test_ops_raises.py
└───── README.md
```

### Reasoning behind architecture design:

When a project grows, referencing the different files/folders becomes a nightmare.

Setting the `PYTHONPATH` to include all relevant folders helps reference each function by the absolute file path. This removes any ambiguity to which file is being referenced/imported and saves time trying to figure out relative paths between files.

#### CLI

The command line interface module handles the arguments passed in when running the script. I decoupled it from the script for the following reasons:

- Ease of testing:
  - I can test this module independently of running the script, as it only handles parsing arguments.
  - More work can be done to completely decouple the cli from the business logic.
- Ease of replacement/substitution:
  - At the moment, the main function just calls the cli function. However, it can be set up in the future to call a different cli function, or a gui function for example.
- The main function is the glue that connects the user interface to the business logic.

Since the cli is a module, it can be reused in a different project that accepts the same arguments.

#### Helpers

The helpers folder holds some io helper functions that are general enough to be called a helper function but still specific to this project.

I believe these functions can be generalised even further/expanded into their own modules.

#### ops

This is where the business logic lives. The name of the folder is loosely related to the nature of the functions defined within this folder.

Since the main purpose of this project is to process an excel file, I named the file containing the logic of dealing with the excel file `amag_op.py`.

The business logic is completely decoupled from the interface, although some assumptions are made based on the shape of the arguments. The call_func function acts as the glue between the cli and the business logic.

#### Exceptions

Here the custom exceptions are defined. It is useful to write custom exceptions for testing purposes and for ease of logging. If the nature of a custom exception changes over time, but the name of the exception stays the same, the rest of the project won't need to be updated to handle these custom exceptions.

#### Tests

All of the tests live here. I used the `Pytest` Framework as it simplifies writing tests.
The main benefits are the following:

- Only needing to use assert in a test.
- The framework finds all tests based on the test\_ prefix.
- Tests can be parameterised.
- A coverage report can be created using the --cov argument.

# TODO

- Add setup installer
- Cover all functions with tests
- Add logging
- Add special log messages in the custom exceptions
- Add CI/CD
