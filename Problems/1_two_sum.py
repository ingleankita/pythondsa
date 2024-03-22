"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""
from tests_utils import evaluate_tests

tests = [
    {
        'input': {
            'nums': [2, 7, 11, 15],
            'target': 9
        },
        'output': [0, 1]
    },
    {
        'input': {
            'nums': [3, 2, 4],
            'target': 6
        },
        'output': [1, 2]
    },
    {
        'input': {
            'nums': [3, 3],
            'target': 6
        },
        'output': [0, 1]
    }
]


def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1


evaluate_tests(tests, two_sum_brute_force)
