## Python Async Function Exercises

This project explores concepts related to asynchronous programming in Python. It implements various functions and coroutines for interacting with asynchronous tasks and measuring their execution time.

**Requirements:**

* Python 3.7
* `pylint` (optional, for static code analysis)

**Directory Structure:**

```
0-basic_async_syntax.py  # Defines the wait_random coroutine
1-concurrent_coroutines.py  # Implements wait_n coroutine for spawning multiple wait_random tasks
2-measure_runtime.py  # Measures execution time of wait_n
3-tasks.py  # Creates tasks using task_wait_random
4-tasks.py  # Implements task_wait_n using task_wait_random calls
main_*.py (optional)  # Example usage scripts (e.g., 0-main.py, 1-main.py, etc.)
```

**Code Structure:**

Each Python file focuses on specific functionalities:

* `0-basic_async_syntax.py`: Defines the `wait_random` coroutine, which waits for a random delay between 0 and a specified `max_delay` and returns the delay value.
* `1-concurrent_coroutines.py`: Implements the `wait_n` coroutine, which spawns multiple `wait_random` tasks with a given `max_delay` and returns a list of delays in ascending order (achieved without using `sort`).
* `2-measure_runtime.py`: Defines the `measure_time` coroutine, which measures the execution time of `wait_n` and returns the average time per task.
* `3-tasks.py`: Creates tasks using the `task_wait_random` function, which takes a `max_delay` and returns an `asyncio.Task` object.
* `4-tasks.py`: Implements the `task_wait_n` function using `task_wait_random` calls. This function spawns multiple tasks with a given `max_delay` and returns a list of delays in ascending order.
* `main_*.py` (optional): These files can be used as examples to demonstrate how to run the coroutines and functions.

**Running the Code:**

1. Ensure you have Python 3.7 installed.
2. Navigate to the project directory in your terminal.
3. Execute the main files with `python3 <filename>.py`. For example, to run the test script for `wait_n`: `python3 1-main.py`

**Using `pylint` (Optional):**

* Install `pylint` using `pip install pylint`.
* From the project directory, run `pylint *.py` to perform static code analysis and identify potential errors or stylistic issues.

**Further Exploration:**

* Experiment with different `max_delay` values in the main scripts to observe the behavior of asynchronous tasks.
* Consider testing the code with a more comprehensive unit testing framework.
* Explore more advanced asynchronous patterns and libraries in Python.
