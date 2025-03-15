import timeit

code_to_test = """
result = [x**2 for x in range(1000)]
"""

execution_time = timeit.timeit(code_to_test, number=1000)
print(f"Execution Time: {execution_time:.5f} seconds")
