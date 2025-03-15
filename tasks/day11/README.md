# Timeit Performance Testing

## Overview
This script measures the execution time of a Python list comprehension that calculates the squares of numbers from 0 to 999 using the `timeit` module.

## Features
- Uses the `timeit` module to measure execution time.
- Runs the code snippet 1000 times for accurate timing.
- Prints the execution time in seconds.

## Requirements
- Python 3.x

## Installation
No external dependencies are required. The script uses Python's built-in `timeit` module.

## Usage
1. Save the script as `performance_test.py`.
2. Run the script:
   ```sh
   python performance_test.py
   ```
3. The execution time of the test will be printed in seconds.

## Code Explanation
- The `timeit.timeit()` function runs the code snippet multiple times and measures the total execution time.
- `number=1000` ensures the code runs 1000 times for better accuracy.
- The formatted print statement displays the execution time with five decimal places.

## Example Output
```
Execution Time: 0.12345 seconds
```

## Future Enhancements
- Test different list comprehension techniques.
- Compare execution times with alternative approaches (e.g., `map()` function or loops).
- Implement command-line arguments to customize test parameters.

