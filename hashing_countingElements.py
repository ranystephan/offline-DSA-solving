# Hashing


from typing import List

class Solution:
    """
    Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
    If there are duplicates in arr, count them separately.

    Example 1:
        Input: arr = [1, 2, 3]
        Output: 2
        Explanation: 1 and 2 are counted because 2 and 3 are in arr.

    Example 2:
        Input: arr = [1, 1, 3, 3, 5, 5, 7, 7]
        Output: 0
        Explanation: No numbers are counted because there is no 2, 4, 6, or 8 in arr.

    Constraints:
        1 <= arr.length <= 1000
        0 <= arr[i] <= 1000
    """
    
    def countElements(self, arr: List[int]) -> int:
        element_set = set(arr)
        count = 0
        
        for x in arr:
            if x + 1 in element_set:
                count += 1
                
        return count


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.countElements([1, 2, 3]) == 2

def test_example2():
    solution = Solution()
    assert solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0

def test_single_element():
    solution = Solution()
    assert solution.countElements([1]) == 0

def test_all_elements_form_pairs():
    solution = Solution()
    assert solution.countElements([0, 1, 2, 3, 4]) == 4

def test_duplicates():
    solution = Solution()
    assert solution.countElements([1, 2, 2, 3, 3, 4]) == 4

def test_large_numbers():
    solution = Solution()
    assert solution.countElements([999, 1000, 1000]) == 2

def test_no_valid_elements():
    solution = Solution()
    assert solution.countElements([10, 20, 30]) == 0

def test_all_identical_numbers():
    solution = Solution()
    assert solution.countElements([5, 5, 5, 5]) == 0

def test_large_input():
    solution = Solution()
    arr = list(range(1000))  # Array with all numbers from 0 to 999
    assert solution.countElements(arr) == 999

def test_reverse_order():
    solution = Solution()
    assert solution.countElements([3, 2, 1]) == 2
