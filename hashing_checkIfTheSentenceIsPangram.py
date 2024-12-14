# Hashing 

class Solution:
    """
    A pangram is a sentence where every letter of the English alphabet appears at least once.

    Given a string sentence containing only lowercase English letters, return true if 
    sentence is a pangram, or false otherwise.

    Example 1:
        Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
        Output: true
        Explanation: sentence contains at least one of every letter of the English alphabet.

    Example 2:
        Input: sentence = "leetcode"
        Output: false

    Constraints:
        1 <= sentence.length <= 1000
        sentence consists of lowercase English letters only.
    """
    
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True

def test_example2():
    solution = Solution()
    assert solution.checkIfPangram("leetcode") == False

def test_empty_string():
    solution = Solution()
    assert solution.checkIfPangram("") == False

def test_partial_alphabet():
    solution = Solution()
    assert solution.checkIfPangram("abcdefghijklm") == False

def test_full_alphabet_mixed_order():
    solution = Solution()
    assert solution.checkIfPangram("abcdefghijklmnopqrstuvwxyz") == True

def test_repeated_letters():
    solution = Solution()
    assert solution.checkIfPangram("abcabcabcabcabcabcabcabcxyz") == False

def test_large_input():
    solution = Solution()
    long_sentence = "thequickbrownfoxjumpsoverthelazydog" * 10
    assert solution.checkIfPangram(long_sentence) == True
