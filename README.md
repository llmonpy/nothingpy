# nothingpy
Nothing is a replacement for None that eliminates the need for many if statements.  I am tired of writing code like this:

```python
if some_list:
    for item in some_list:
        do_something(item)
```

If you use Nothing instead of None, you can write code like this:

```python
for item in some_list:
    do_something(item)
```

**Nothing** is a global variable of the class NothingClass.  **Nothing** has a len of 0, is False, returns an empty iterable,
converts to an empty string, and responds to values(), keys() and items() like an empty dictionary.  **Nothing** equals
other NothingClass instances, None and False.  

## Installation

```pip install nothingpy```

## Usage

```python
from nothingpy import Nothing

some_variable = Nothing
```