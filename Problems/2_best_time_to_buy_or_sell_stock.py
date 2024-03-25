"""You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

from tests_utils import evaluate_tests


def max_profit(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            curr_profit = prices[j] - prices[i]
            if prices[j] - prices[i] > profit:
                profit = curr_profit
        i = i + 1
    return profit


tests = [
    {
        'input': {
            'prices': [7, 1, 5, 3, 6, 4],
        },
        'output': 5
    },
    {
        'input': {
            'prices': [7, 6, 4, 3, 1],
        },
        'output': 0
    },
]

evaluate_tests(tests, max_profit)
