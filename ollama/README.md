# Ollama

Playing around with Ollama, a tool for running large language models locally.

## Try out the CLI

```
ollama run llama2
```

## Run your own model

```
cd inside_out
ollama create joy -f joy.Modelfile
ollama create saddness -f joy.Modelfile
ollama run joy
ollama run saddness
```

## Test the API

```
sh inside_out/ask.sh
```

## Python

### Example 1

Basic question:

```python
python test1.py
```

### Example 2

More prompting

```python
python test2.py
```

### Example 3

Get `avatar_the_last_air_bender_the_art_of_the_animated_series.txt` from [here](https://archive.org/stream/avatar-the-last-airbender-the-art-of-the-animated-series/Avatar%20-%20The%20Last%20Airbender%20-%20The%20Art%20of%20the%20Animated%20Series_djvu.txt).
