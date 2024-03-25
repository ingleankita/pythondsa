"""Given a string s, find the length of the longest substring without repeating characters."""
from tests_utils import evaluate_tests


def len_longest_substring(s):
    current_longest = ""
    substring = ""
    for i in range(len(s)):
        if s[i] not in substring:
            substring += s[i]
        elif len(current_longest) < len(substring):
            current_longest = substring
            substring = s[i]  # start new substring where last substring broke
    return len(current_longest)


tests = [
    {
        'input': {
            's': "abcabcbb",
        },
        'output': 3
    },
    {
        'input': {
            's': "bbbbb",
        },
        'output': 1
    },
    {
        'input': {
            's': "pwwkew",
        },
        'output': 3
    }
]

evaluate_tests(tests, len_longest_substring)
