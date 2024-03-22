import time


def evaluate_tests(testcases, function):
    for test_case_number, test in enumerate(testcases):  # Print information
        start_time = time.time()  # Get start time
        print(f"\033[1mTest case {test_case_number + 1}\033[0m")
        print(f"Input:\n{test['input']}")
        print(f"Expected output:\n{test['output']}")
        print(f"Actual output:\n{function(**test['input'])}")
        if function(**test['input']) == test['output']:
            print("\033[92m" + "Test passed :)" + "\033[0m")
        else:
            print("\033[91m" + "Test failed :(" + "\033[0m")
        end_time = time.time()  # Get end time
        elapsed_time_seconds = end_time - start_time  # Get elapsed time in seconds
        elapsed_time_ms = elapsed_time_seconds * 1000  # Convert elapsed time to ms
        print(f"Execution time: {elapsed_time_ms:.2f} milliseconds\n")
