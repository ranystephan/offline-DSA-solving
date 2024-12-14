
class Solution:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

    Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

    Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Constraints:
        - 0 <= s.length <= 5 * 10^4
        - s consists of English letters, digits, symbols, and spaces.
    """
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3

def test_example2():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("bbbbb") == 1

def test_example3():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("pwwkew") == 3

def test_empty_string():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("") == 0

def test_single_character():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("a") == 1

def test_all_unique_characters():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcdef") == 6

def test_repeated_pattern():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abababab") == 2

def test_large_input():
    solution = Solution()
    s = "a" * 50000
    assert solution.lengthOfLongestSubstring(s) == 1

def test_mixed_characters():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("dvdf") == 3
