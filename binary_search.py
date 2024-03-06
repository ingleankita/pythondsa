"""Question: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given
number by turning over as few cards as possible. Write a function to help Bob locate the card."""

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


# Brute force implementation: iterate over all cards to find the card with the query
def find_card(cards, query):
    for index, card in enumerate(cards):  # enumerate returns an iterable object that yields index, value pairs
        if card == query:
            return index
    return -1


# Run tests.

def evaluate_tests(testcases, function):
    for test in testcases:
        print(f"Input:\n{test['input']}")
        print(f"Expected output:\n{test['output']}")
        print(f"Actual output:\n{function(**test['input'])}")
        if function(**test['input']) == test['output']:
            print("\033[92m" + "Test passed :)" + "\033[0m")
        else:
            print("\033[91m" + "Test failed :(" + "\033[0m")
        print()



evaluate_tests(tests, find_card)
