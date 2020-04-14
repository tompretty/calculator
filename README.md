# calculator

A simple python app for evaluating mathematical strings.

Strings are parsed into an expression tree using the [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).
The expression tree is then evaluated recursively to produce the result.

## Usage

Evaluating a string is simple, just use the `evaluate` function

```python
from calculator import evaluate

evaluate("(3 + 4 - 5 * 6) ^ 7")
```

The supported operators are

| symbol   | operator        |
| -------- | --------------- |
| `4` e.g. | number constant |
| `+`      | addition        |
| `-`      | subtraction     |
| `*`      | multiplication  |
| `^`      | exponentiation  |
| `()`     | parenthesis     |
