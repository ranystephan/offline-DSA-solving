
class Solution:
    """
    You're given strings jewels representing the types of stones that are jewels, 
    and stones representing the stones you have. Each character in stones is a type 
    of stone you have. You want to know how many of the stones you have are also jewels.

    Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Example 1:
        Input: jewels = "aA", stones = "aAAbbbb"
        Output: 3

    Example 2:
        Input: jewels = "z", stones = "ZZ"
        Output: 0

    Constraints:
        - 1 <= jewels.length, stones.length <= 50
        - jewels and stones consist of only English letters.
        - All the characters of jewels are unique.
    """
    
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)  # Create a set for fast lookup
        return sum(stone in jewel_set for stone in stones)


# Pytest test cases
def test_example1():
    solution = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    assert solution.numJewelsInStones(jewels, stones) == 3

def test_example2():
    solution = Solution()
    jewels = "z"
    stones = "ZZ"
    assert solution.numJewelsInStones(jewels, stones) == 0

def test_all_jewels():
    solution = Solution()
    jewels = "abc"
    stones = "aabbcc"
    assert solution.numJewelsInStones(jewels, stones) == 6

def test_no_jewels():
    solution = Solution()
    jewels = ""
    stones = "aabbcc"
    assert solution.numJewelsInStones(jewels, stones) == 0

def test_no_stones():
    solution = Solution()
    jewels = "abc"
    stones = ""
    assert solution.numJewelsInStones(jewels, stones) == 0

def test_case_sensitivity():
    solution = Solution()
    jewels = "aA"
    stones = "aaaAAA"
    assert solution.numJewelsInStones(jewels, stones) == 3

def test_large_input():
    solution = Solution()
    jewels = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stones = "aA" * 25 + "zZ" * 25
    assert solution.numJewelsInStones(jewels, stones) == 100

def test_repeated_jewels():
    solution = Solution()
    jewels = "aA"
    stones = "aAaAaA"
    assert solution.numJewelsInStones(jewels, stones) == 6
