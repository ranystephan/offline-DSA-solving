
from typing import List
from collections import Counter

class Solution:
    """
    Given an integer array nums, return the largest integer that only occurs once. 
    If no integer occurs once, return -1.

    Example 1:
        Input: nums = [5,7,3,9,4,9,8,3,1]
        Output: 8
        Explanation:
            The maximum integer in the array is 9 but it is repeated.
            The number 8 occurs only once, so it is the answer.

    Example 2:
        Input: nums = [9,9,8,8]
        Output: -1
        Explanation:
            There is no number that occurs only once.

    Constraints:
        - 1 <= nums.length <= 2000
        - 0 <= nums[i] <= 1000
    """
    
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique_numbers = [num for num, freq in count.items() if freq == 1]
        return max(unique_numbers) if unique_numbers else -1


# Pytest test cases
def test_example1():
    solution = Solution()
    nums = [5,7,3,9,4,9,8,3,1]
    assert solution.largestUniqueNumber(nums) == 8

def test_example2():
    solution = Solution()
    nums = [9,9,8,8]
    assert solution.largestUniqueNumber(nums) == -1

def test_single_element():
    solution = Solution()
    nums = [42]
    assert solution.largestUniqueNumber(nums) == 42

def test_all_unique():
    solution = Solution()
    nums = [1,2,3,4,5]
    assert solution.largestUniqueNumber(nums) == 5

def test_all_duplicates():
    solution = Solution()
    nums = [2,2,3,3,4,4]
    assert solution.largestUniqueNumber(nums) == -1

def test_large_input():
    solution = Solution()
    nums = [i for i in range(1000)] + [999]  # Duplicates the largest number
    assert solution.largestUniqueNumber(nums) == 998

def test_negative_numbers():
    solution = Solution()
    nums = [-1, -2, -3, -2, -1]
    assert solution.largestUniqueNumber(nums) == -3

def test_mixed_numbers():
    solution = Solution()
    nums = [10, 15, 10, 20, 30, 15]
    assert solution.largestUniqueNumber(nums) == 30
