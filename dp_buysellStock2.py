
from typing import List

class Solution:
    """
    Given an array prices where prices[i] is the price of a stock on the i-th day, return the maximum profit
    you can achieve. You may complete as many transactions as you like, but you must cooldown for one day after
    each sell.

    Example 1:
        Input: prices = [1, 2, 3, 0, 2]
        Output: 3
        Explanation: transactions = [buy, sell, cooldown, buy, sell]

    Example 2:
        Input: prices = [1]
        Output: 0

    Constraints:
        - 1 <= prices.length <= 5000
        - 0 <= prices[i] <= 1000
    """

    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        n = len(prices)
        # Initialize dp arrays
        hold = [-float('inf')] * n  # Max profit if holding a stock on day i
        cash = [0] * n              # Max profit if not holding a stock on day i (cooldown or rest)

        # Base cases
        hold[0] = -prices[0]  # Buy on the first day
        
        for i in range(1, n):
            hold[i] = max(hold[i - 1], cash[i - 2] - prices[i] if i > 1 else -prices[i])
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i])
        
        return cash[-1]  # Max profit when not holding a stock on the last day


# Pytest test cases
def test_example1():
    solution = Solution()
    prices = [1, 2, 3, 0, 2]
    assert solution.maxProfit(prices) == 3

def test_example2():
    solution = Solution()
    prices = [1]
    assert solution.maxProfit(prices) == 0

def test_no_profit():
    solution = Solution()
    prices = [5, 4, 3, 2, 1]
    assert solution.maxProfit(prices) == 0

def test_single_buy_sell():
    solution = Solution()
    prices = [1, 2]
    assert solution.maxProfit(prices) == 1

def test_alternating_prices():
    solution = Solution()
    prices = [1, 2, 3, 0, 2, 1]
    assert solution.maxProfit(prices) == 3

def test_large_prices():
    solution = Solution()
    prices = [1] * 5000
    assert solution.maxProfit(prices) == 0

def test_peak_and_valley():
    solution = Solution()
    prices = [1, 2, 3, 0, 2, 4, 1, 5]
    assert solution.maxProfit(prices) == 8
