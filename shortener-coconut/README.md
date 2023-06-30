# Url shortener API

This is a simple project to use [Coconut](https://coconut.readthedocs.io/).

## Requirements

- [Poetry](https://github.com/python-poetry/poetry)

## Set up

Install dependencies:

```
poetry install
```


## Compile

```
poetry shell
coconut run.coco --verbose --mypy
```

Watch it if you want:

```
coconut -w shortener
```

## Run

Once the code is compiled, you can:

```
python run.py
```

Or, you can run the code directly:


```
coconut run.coco -r
```

## Test

You need to compile the tests first:

```
coconut tests
```

Then, use `pytest`:

```
pytest tests
```
