# Hashing 


from typing import List

class Solution:
    """
    Given an array nums containing n distinct numbers in the range [0, n], return the only number 
    in the range that is missing from the array.

    Example 1:
        Input: nums = [3, 0, 1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number.

    Example 2:
        Input: nums = [0, 1]
        Output: 2
        Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number.

    Example 3:
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number.

    Constraints:
        n == nums.length
        1 <= n <= 10^4
        0 <= nums[i] <= n
        All the numbers of nums are unique.

    Follow up:
        Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
    """
    
    def missingNumber(self, nums: List[int]) -> int:
        # Using the mathematical formula for the sum of the first n natural numbers
        n = len(nums)
        total_sum = n * (n + 1) // 2
        return total_sum - sum(nums)


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.missingNumber([3, 0, 1]) == 2

def test_example2():
    solution = Solution()
    assert solution.missingNumber([0, 1]) == 2

def test_example3():
    solution = Solution()
    assert solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

def test_no_missing_number():
    solution = Solution()
    assert solution.missingNumber([0, 1, 2, 3]) == 4

def test_large_input():
    solution = Solution()
    nums = list(range(10000))  # Create a list from 0 to 9999
    nums.remove(4567)  # Remove a random number
    assert solution.missingNumber(nums) == 4567
