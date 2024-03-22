"""Question: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given
number by turning over as few cards as possible. Write a function to help Bob locate the card."""
from tests_utils import evaluate_tests

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
# Time complexity: O(log n) for both recursive and iterative implementation; with each comparison the  search space is halved
# Space complexity: O(log n); with each recursive call size of cards array is halved
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


# TODO Question: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.


# Run tests.


evaluate_tests(tests, find_card_linear_search)
evaluate_tests(tests, find_card_binary_search)
