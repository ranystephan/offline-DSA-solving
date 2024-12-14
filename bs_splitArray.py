
from typing import List

class Solution:
    """
    Given an array nums and an integer k, split nums into k non-empty subarrays such that
    the largest sum of any subarray is minimized. Return the minimized largest sum.

    Example 1:
        Input: nums = [7,2,5,10,8], k = 2
        Output: 18

    Example 2:
        Input: nums = [1,2,3,4,5], k = 2
        Output: 9

    Constraints:
        - 1 <= nums.length <= 1000
        - 0 <= nums[i] <= 10^6
        - 1 <= k <= min(50, nums.length)
    """
    
    def splitArray(self, nums: List[int], k: int) -> int:
        # Function to check if we can split nums into k or fewer subarrays
        # such that no subarray has a sum greater than mid
        def canSplit(mid: int) -> bool:
            current_sum = 0
            splits = 1  # Start with one subarray
            for num in nums:
                if current_sum + num > mid:
                    # Create a new subarray
                    splits += 1
                    current_sum = num
                    if splits > k:
                        return False
                else:
                    current_sum += num
            return True
        
        # Binary search bounds
        left, right = max(nums), sum(nums)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if canSplit(mid):
                result = mid
                right = mid - 1  # Try for a smaller largest sum
            else:
                left = mid + 1  # Increase the largest sum
        
        return result


# Pytest test cases
def test_example1():
    solution = Solution()
    nums = [7, 2, 5, 10, 8]
    k = 2
    assert solution.splitArray(nums, k) == 18

def test_example2():
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 2
    assert solution.splitArray(nums, k) == 9

def test_single_element():
    solution = Solution()
    nums = [10]
    k = 1
    assert solution.splitArray(nums, k) == 10

def test_all_elements_equal():
    solution = Solution()
    nums = [5, 5, 5, 5]
    k = 2
    assert solution.splitArray(nums, k) == 10

def test_large_k():
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 5
    assert solution.splitArray(nums, k) == 5

def test_large_sum():
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3
    assert solution.splitArray(nums, k) == 17

def test_large_input():
    solution = Solution()
    nums = [1] * 1000
    k = 10
    assert solution.splitArray(nums, k) == 100
