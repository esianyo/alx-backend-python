## Python Async Comprehension Exercises

This project explores asynchronous generators and async comprehensions in Python. It implements functions to generate random numbers asynchronously and utilize async comprehensions for collecting and manipulating the results.

**Requirements:**

* Python 3.7
* `asyncio` library

**Directory Structure:**

```
0-async_generator.py  # Defines the async_generator coroutine
1-async_comprehension.py  # Implements the async_comprehension coroutine
2-measure_runtime.py  # Measures execution time using async_comprehension
main_*.py (optional)  # Example usage scripts (e.g., 0-main.py, 1-main.py, etc.)
README.md  # This file (you are editing)
```

**Code Structure:**

* `0-async_generator.py`: Defines the `async_generator` coroutine that iterates 10 times, asynchronously waits 1 second for each iteration, and yields a random number between 0 and 10.
* `1-async_comprehension.py`: Implements the `async_comprehension` coroutine that uses an async comprehension to collect 10 random numbers from the `async_generator` and returns them as a list.
* `2-measure_runtime.py`: Defines the `measure_runtime` coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather`. It measures the total execution time and returns it.

**Explanation of 10-Second Runtime:**

While each iteration of `async_generator` waits for 1 second, running four parallel comprehensions in `measure_runtime` doesn't necessarily guarantee a total runtime of 4 seconds. This is because asynchronous tasks can run concurrently, potentially overlapping wait times. The actual runtime might be slightly higher than 4 seconds due to scheduling overhead and potential context switching between tasks.

**Running the Code:**

1. Ensure you have Python 3.7 installed.
2. Navigate to the project directory in your terminal.
3. Execute the main scripts with `python3 <filename>.py`. For example, to run the test script for `async_comprehension`: `python3 1-main.py`

**Further Exploration:**

* Experiment with different numbers of parallel comprehensions in `measure_runtime` and observe the impact on execution time.
* Explore more advanced asynchronous operations and patterns in Python.
