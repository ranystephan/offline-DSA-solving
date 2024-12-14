
from typing import List

class Solution:
    """
    The next greater element of some element x in an array is the first greater element that 
    is to the right of x in the same array.

    You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

    For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the 
    next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for 
    this query is -1.

    Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

    Example 1:
        Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        Output: [-1,3,-1]

    Example 2:
        Input: nums1 = [2,4], nums2 = [1,2,3,4]
        Output: [3,-1]

    Constraints:
        - 1 <= nums1.length <= nums2.length <= 1000
        - 0 <= nums1[i], nums2[i] <= 10^4
        - All integers in nums1 and nums2 are unique.
        - All the integers of nums1 also appear in nums2.

    Follow-up:
        - Could you find an O(nums1.length + nums2.length) solution?
    """
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # Traverse nums2 from right to left
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater[num] = stack[-1] if stack else -1
            stack.append(num)

        # Map results for nums1 from next_greater
        return [next_greater[num] for num in nums1]


# Pytest test cases
def test_example1():
    solution = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert solution.nextGreaterElement(nums1, nums2) == [-1, 3, -1]

def test_example2():
    solution = Solution()
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    assert solution.nextGreaterElement(nums1, nums2) == [3, -1]

def test_no_greater_elements():
    solution = Solution()
    nums1 = [5, 6]
    nums2 = [6, 5]
    assert solution.nextGreaterElement(nums1, nums2) == [-1, -1]

def test_all_greater_elements():
    solution = Solution()
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3, 4]
    assert solution.nextGreaterElement(nums1, nums2) == [2, 3, 4]

def test_large_input():
    solution = Solution()
    nums1 = list(range(500, 1000))
    nums2 = list(range(1000))
    expected = [i + 1 for i in nums1]
    assert solution.nextGreaterElement(nums1, nums2) == expected

def test_single_element():
    solution = Solution()
    nums1 = [1]
    nums2 = [1]
    assert solution.nextGreaterElement(nums1, nums2) == [-1]

def test_mixed_order():
    solution = Solution()
    nums1 = [4, 5]
    nums2 = [5, 3, 4, 2, 6]
    assert solution.nextGreaterElement(nums1, nums2) == [6, 6]
