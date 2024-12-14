
from collections import Counter

class Solution:
    """
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using 
    the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    Example 1:
        Input: ransomNote = "a", magazine = "b"
        Output: false

    Example 2:
        Input: ransomNote = "aa", magazine = "ab"
        Output: false

    Example 3:
        Input: ransomNote = "aa", magazine = "aab"
        Output: true

    Constraints:
        - 1 <= ransomNote.length, magazine.length <= 10^5
        - ransomNote and magazine consist of lowercase English letters.
    """
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        
        return True


# Pytest test cases
def test_example1():
    solution = Solution()
    ransomNote = "a"
    magazine = "b"
    assert solution.canConstruct(ransomNote, magazine) == False

def test_example2():
    solution = Solution()
    ransomNote = "aa"
    magazine = "ab"
    assert solution.canConstruct(ransomNote, magazine) == False

def test_example3():
    solution = Solution()
    ransomNote = "aa"
    magazine = "aab"
    assert solution.canConstruct(ransomNote, magazine) == True

def test_exact_match():
    solution = Solution()
    ransomNote = "abc"
    magazine = "abc"
    assert solution.canConstruct(ransomNote, magazine) == True

def test_empty_ransom_note():
    solution = Solution()
    ransomNote = ""
    magazine = "abc"
    assert solution.canConstruct(ransomNote, magazine) == True

def test_empty_magazine():
    solution = Solution()
    ransomNote = "a"
    magazine = ""
    assert solution.canConstruct(ransomNote, magazine) == False

def test_large_input():
    solution = Solution()
    ransomNote = "a" * 50000 + "b"
    magazine = "a" * 50000 + "c"
    assert solution.canConstruct(ransomNote, magazine) == False

def test_repeated_characters():
    solution = Solution()
    ransomNote = "aaaa"
    magazine = "aaa"
    assert solution.canConstruct(ransomNote, magazine) == False

def test_extra_characters_in_magazine():
    solution = Solution()
    ransomNote = "abc"
    magazine = "abcdabcdabcd"
    assert solution.canConstruct(ransomNote, magazine) == True
