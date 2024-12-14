# Hashing



from typing import List

class Solution:
    """
    Given a binary array nums, return the maximum length of a contiguous subarray
    with an equal number of 0 and 1.

    Example 1:
        Input: nums = [0, 1]
        Output: 2
        Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

    Example 2:
        Input: nums = [0, 1, 0]
        Output: 2
        Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

    Constraints:
        1 <= nums.length <= 10^5
        nums[i] is either 0 or 1.
    """
    
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        count_index_map = {0: -1}
        
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_index_map:
                max_length = max(max_length, i - count_index_map[count])
            else:
                count_index_map[count] = i
        
        return max_length


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.findMaxLength([0, 1]) == 2

def test_example2():
    solution = Solution()
    assert solution.findMaxLength([0, 1, 0]) == 2

def test_all_zeros():
    solution = Solution()
    assert solution.findMaxLength([0, 0, 0]) == 0

def test_all_ones():
    solution = Solution()
    assert solution.findMaxLength([1, 1, 1]) == 0

def test_mixed():
    solution = Solution()
    assert solution.findMaxLength([0, 1, 0, 1, 1, 0, 0]) == 6

def test_large_input():
    solution = Solution()
    nums = [0, 1] * 50000  # Creates a list with 100,000 elements
    assert solution.findMaxLength(nums) == 100000
