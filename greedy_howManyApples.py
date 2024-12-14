
from typing import List

class Solution:
    """
    Given an integer array weight where weight[i] is the weight of the i-th apple,
    return the maximum number of apples you can put in the basket with a weight limit of 5000.

    Example 1:
        Input: weight = [100, 200, 150, 1000]
        Output: 4

    Example 2:
        Input: weight = [900, 950, 800, 1000, 700, 800]
        Output: 5

    Constraints:
        - 1 <= weight.length <= 10^3
        - 1 <= weight[i] <= 10^3
    """

    def maxNumberOfApples(self, weight: List[int]) -> int:
        # Sort the weights in ascending order
        weight.sort()
        total_weight = 0
        count = 0
        
        # Add apples to the basket until the weight exceeds 5000
        for w in weight:
            if total_weight + w <= 5000:
                total_weight += w
                count += 1
            else:
                break
        
        return count


# Pytest test cases
def test_example1():
    solution = Solution()
    weight = [100, 200, 150, 1000]
    assert solution.maxNumberOfApples(weight) == 4

def test_example2():
    solution = Solution()
    weight = [900, 950, 800, 1000, 700, 800]
    assert solution.maxNumberOfApples(weight) == 5

def test_all_small_apples():
    solution = Solution()
    weight = [1, 1, 1, 1, 1]
    assert solution.maxNumberOfApples(weight) == 5

def test_single_apple_too_large():
    solution = Solution()
    weight = [6000]
    assert solution.maxNumberOfApples(weight) == 0

def test_large_weights():
    solution = Solution()
    weight = [4000, 400, 400, 300, 200]
    assert solution.maxNumberOfApples(weight) == 3

def test_edge_case_one_apple():
    solution = Solution()
    weight = [3000]
    assert solution.maxNumberOfApples(weight) == 1
