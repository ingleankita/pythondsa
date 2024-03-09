"""Question: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given
number by turning over as few cards as possible. Write a function to help Bob locate the card."""

import time

# Problem: Find the card with query with the least possible turning over of cards.

# Define test cases.
tests = []

# Normal test
tests.append({
    'input': {
        'cards': [14, 11, 10, 7, 4, 2],
        'query': 7
    },
    'output': 3
})

# With negatives
tests.append({
    'input': {
        'cards': [22, 14, 11, 9, -7, -10, -22],
        'query': -7
    },
    'output': 4
})

# Cards contains just 1 element
tests.append({
    'input': {
        'cards': [14],
        'query': 14
    },
    'output': 0
})

# Query not in cards
tests.append({
    'input': {
        'cards': [14, 11, 9, -7, -10, -22],
        'query': 5
    },
    'output': -1
})

# Empty cards
tests.append({
    'input': {
        'cards': [],
        'query': 5
    },
    'output': -1
})


# Brute force implementation: Linear search (iterate over all cards to find the card with the query)
# Time complexity: O(n); n = number of cards
# Space complexity: O(1); index and card are re-used every iteration of the loop
def find_card_linear_search(cards, query):
    for index, card in enumerate(cards):  # enumerate returns an iterable object that yields index, value pairs
        if card == query:
            return index
    return -1


def find_card_binary_search(cards, query):
    return binary_search(cards, query, 0, len(cards) - 1)


# Binary search
def binary_search(cards, query, start, end):
    mid = (end + start) // 2  # Get mid (average) value between start and end

    if start > end:  # If query does not exist in cards
        return -1

    if cards[mid] == query:  # If query found
        return mid
    elif cards[mid] < query:  # If mid value is smaller than query, check left of mid value
        return binary_search(cards, query, start, mid - 1)
    elif cards[mid] > query:  # If mid value is greater than query, check right of mid value
        return binary_search(cards, query, mid + 1, end)


# Run tests.

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


evaluate_tests(tests, find_card_linear_search)
evaluate_tests(tests, find_card_binary_search)
