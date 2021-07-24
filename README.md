# AMAG Technical Question

## Setup

Using pipenv, install packages by running `pipenv install` (if you don't have pipenv, you can install it using `pip install pipenv`)

set `PYTHONPATH` to root folder of project
example: run `export PYTHONPATH="path_to/AMAG-Python-exercise/amag_op:path_to/AMAG-Python-exercise/tests"`

## Run Script

The script takes 2 options:

- operate
- process

you can access the options using --help

run `python -m amag_op --help`

```
usage: amag_op [-h] {process,operate} ...

Process some floats.

positional arguments:
{process,operate}
process process an excel or csv file with x, y and operation columns
operate perform an operation on x and y

optional arguments:
-h, --help show this help message and exit
```

process help

```
$ python -m amag_op process --help
usage: amag_op process [-h] [-s S] file

positional arguments:
  file

optional arguments:
  -h, --help      show this help message and exit
  -s S, -sheet S  Excel sheetname
```

operate help

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

## Tests

run `pytest --cov=tests/` to run tests and check coverage
example:

```
$ pytest --cov=tests/
================================================================================================================================= test session starts ==================================================================================================================================
platform win32 -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Yahya Fidouh\OneDrive\Documents\AMAG-Python-exercise
plugins: cov-2.12.1
collected 36 items

tests\test_ops.py ........x...............                                                                                                                                                                                                                                        [ 66%]
tests\test_ops_raises.py ............                                                                                                                                                                                                                                             [100%]

----------- coverage: platform win32, python 3.9.6-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
tests\test_cli.py              0      0   100%
tests\test_ops.py             23      0   100%
tests\test_ops_raises.py      32      0   100%
----------------------------------------------
TOTAL                         55      0   100%


============================================================================================================================ 35 passed, 1 xfailed in 0.17s =============================================================================================================================
```

## Structure

```
.
├───── amag_op
│    ├───── cli
│    │    └───── cli.py
│    │────── exceptions
│    │    ├───── file_type_errors.py
│    │    ├───── op_type_errors.py
│    │    ├───── type_errors.py
│    │    └───── __init__.py
│    ├───── helpers
│    │    ├───── amag_op.py
│    │    ├───── helpers.py
│    │    └───── ops.py
│    ├───── __init__.py
│    └───── __main__.py
├───── tests
│    ├───── test_cli.py
│    ├───── test_ops.py
│    └───── test_ops_raises.py
└────── README.md
```

# TODO

- Add logging
- Add CI/CD
