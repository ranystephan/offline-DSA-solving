
from typing import List

class Solution:
    """
    Given an array prices where prices[i] is the price of a stock on the i-th day, and a transaction fee fee,
    return the maximum profit you can achieve.

    Example 1:
        Input: prices = [1,3,2,8,4,9], fee = 2
        Output: 8

    Example 2:
        Input: prices = [1,3,7,5,10,3], fee = 3
        Output: 6

    Constraints:
        - 1 <= prices.length <= 5 * 10^4
        - 1 <= prices[i] < 5 * 10^4
        - 0 <= fee < 5 * 10^4
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Initialize variables to track the states
        cash = 0  # Maximum profit when not holding a stock
        hold = -prices[0]  # Maximum profit when holding a stock
        
        for price in prices[1:]:
            # Update cash and hold states
            cash = max(cash, hold + price - fee)  # Sell the stock
            hold = max(hold, cash - price)  # Buy the stock
        
        return cash  # Return the maximum profit when not holding a stock


# Pytest test cases
def test_example1():
    solution = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    assert solution.maxProfit(prices, fee) == 8

def test_example2():
    solution = Solution()
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    assert solution.maxProfit(prices, fee) == 6

def test_no_fee():
    solution = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 0
    assert solution.maxProfit(prices, fee) == 10

def test_high_fee():
    solution = Solution()
    prices = [1, 3, 7, 5, 10, 3]
    fee = 10
    assert solution.maxProfit(prices, fee) == 0

def test_one_day():
    solution = Solution()
    prices = [5]
    fee = 2
    assert solution.maxProfit(prices, fee) == 0

def test_all_same_prices():
    solution = Solution()
    prices = [5, 5, 5, 5]
    fee = 1
    assert solution.maxProfit(prices, fee) == 0

def test_large_prices_and_fee():
    solution = Solution()
    prices = [1, 5, 3, 8, 4, 12]
    fee = 3
    assert solution.maxProfit(prices, fee) == 11
