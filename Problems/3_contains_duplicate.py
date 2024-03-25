"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if
every element is distinct."""
from tests_utils import evaluate_tests


# sort the array
# if any value repeated, return false
# Time complexity = O(n log n)
def contains_duplicate(nums):
    prev = -1
    for num in sorted(nums):
        if prev == num:
            return True
        prev = num
    return False


tests = [
    {
        'input': {
            'nums': [1, 2, 3, 1],
        },
        'output': True
    },
    {
        'input': {
            'nums': [1, 2, 3, 4],
        },
        'output': False
    },
    {
        'input': {
            'nums': [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        },
        'output': True
    }
]

evaluate_tests(tests, contains_duplicate)
