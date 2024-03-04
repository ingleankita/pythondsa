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
    for index, card in enumerate(cards):
        if card == query:
            return index
    return -1


# Run tests.
for test in tests:
    print(find_card(**test['input']) == test['output'])
