
from typing import List

class Solution:
    """
    Given an array cost where cost[i] is the cost of the i-th step, return the minimum cost to
    reach the top of the staircase.

    Example 1:
        Input: cost = [10, 15, 20]
        Output: 15

    Example 2:
        Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        Output: 6

    Constraints:
        - 2 <= cost.length <= 1000
        - 0 <= cost[i] <= 999
    """
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Edge case: Only two steps
        if n == 2:
            return min(cost[0], cost[1])
        
        # Initialize dp array
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Fill the dp array
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        # The minimum cost to reach the top can be from the last step or the second last step
        return min(dp[n - 1], dp[n - 2])


# Pytest test cases
def test_example1():
    solution = Solution()
    cost = [10, 15, 20]
    assert solution.minCostClimbingStairs(cost) == 15

def test_example2():
    solution = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert solution.minCostClimbingStairs(cost) == 6

def test_small_stairs():
    solution = Solution()
    cost = [10, 15]
    assert solution.minCostClimbingStairs(cost) == 10

def test_all_equal_cost():
    solution = Solution()
    cost = [5, 5, 5, 5]
    assert solution.minCostClimbingStairs(cost) == 10

def test_large_stairs():
    solution = Solution()
    cost = [i for i in range(1000)]
    assert solution.minCostClimbingStairs(cost) == sum(range(999, 0, -2))  # Expected result
