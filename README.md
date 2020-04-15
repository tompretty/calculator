# calculator

A simple python app for evaluating mathematical strings.

Strings are parsed into an expression tree using a [recursive descent parser](https://en.wikipedia.org/wiki/Recursive_descent_parser).
The expression tree is then evaluated recursively to produce the result.

## Usage

Evaluating a string is simple, just use the `evaluate` function

```python
from calculator import evaluate

evaluate("(3 + 4 - 5 * 6) ^ 7")
```

Variables can be used too, provided you give them a value through the `context`
argument

```python
from calculator import evaluate

evaluate("x + y", context={"x": 3, "y": 4})
```

The supported operators are

| symbol        | operator       |
| ------------- | -------------- |
| `4` e.g.      | constant       |
| `my_var` e.g. | variable       |
| `+`           | addition       |
| `-`           | subtraction    |
| `*`           | multiplication |
| `^`           | exponentiation |
| `()`          | parenthesis    |
