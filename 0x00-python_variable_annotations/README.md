# Python - Variable Annotations

## Overview

This project focuses on using type annotations in Python to specify function signatures and variable types. Type annotations enhance code readability and help with static type checking, making it easier to catch errors before runtime. The project includes tasks to practice type annotations, duck typing, and validating code with `mypy`.

## Resources

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Project Structure

```
0x00-python_variable_annotations/
├── 0-add.py
├── 1-concat.py
├── 2-floor.py
├── 3-to_str.py
├── 4-define_variables.py
├── 5-sum_list.py
├── 6-sum_mixed_list.py
├── 7-to_kv.py
├── 8-make_multiplier.py
├── 9-element_length.py
├── 100-safe_first_element.py
├── 101-safely_get_value.py
└── 102-type_checking.py
├── README.md
```

## Tasks

### Task 0: Basic Annotations - Add

Write a type-annotated function `add` that takes two floats and returns their sum.

### Task 1: Basic Annotations - Concat

Write a type-annotated function `concat` that takes two strings and returns their concatenation.

### Task 2: Basic Annotations - Floor

Write a type-annotated function `floor` that takes a float and returns its floor as an integer.

### Task 3: Basic Annotations - To String

Write a type-annotated function `to_str` that takes a float and returns its string representation.

### Task 4: Define Variables

Define and annotate the following variables with the specified values:

- `a`: an integer with a value of 1
- `pi`: a float with a value of 3.14
- `i_understand_annotations`: a boolean with a value of True
- `school`: a string with a value of "Holberton"

### Task 5: Complex Types - List of Floats

Write a type-annotated function `sum_list` which takes a list of floats and returns their sum.

### Task 6: Complex Types - Mixed List

Write a type-annotated function `sum_mixed_list` which takes a list of integers and floats and returns their sum.

### Task 7: Complex Types - String and Int/Float to Tuple

Write a type-annotated function `to_kv` that takes a string and an int/float and returns a tuple. The first element of the tuple is the string. The second element is the square of the int/float and should be annotated as a float.

### Task 8: Complex Types - Functions

Write a type-annotated function `make_multiplier` that takes a float and returns a function that multiplies a float by the multiplier.

### Task 9: Let's Duck Type an Iterable Object

Annotate the function parameters and return values with appropriate types.

### Task 10: Duck Typing - First Element of a Sequence

Augment the code with the correct duck-typed annotations.

### Task 11: More Involved Type Annotations

Add type annotations to the function.

### Task 12: Type Checking

Use `mypy` to validate and apply necessary changes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/esianyo/alx-backend-python.git
    cd alx-backend-python/0x00-python_variable_annotations
    ```

2. Install dependencies (if any).

## Usage

Run the example scripts to test the functions. For example:

```bash
./0-main.py
```

Ensure all Python files are executable:
```bash
chmod +x *.py
```

## Contributors

- **Esianyo Dzisenu** - [LinkedIn](https://linkedin.com/in/esianyo)
