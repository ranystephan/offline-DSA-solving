
class Solution:
    """
    Given a string s of lower and upper case English letters.

    A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
        - 0 <= i <= s.length - 2
        - s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

    To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
    You can keep doing this until the string becomes good.

    Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

    Notice that an empty string is also good.

    Example 1:
        Input: s = "leEeetcode"
        Output: "leetcode"

    Example 2:
        Input: s = "abBAcC"
        Output: ""

    Example 3:
        Input: s = "s"
        Output: "s"

    Constraints:
        - 1 <= s.length <= 100
        - s contains only lower and upper case English letters.
    """
    
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            # Check if the current character makes the stack "bad"
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:  # Case difference is 32 in ASCII
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.makeGood("leEeetcode") == "leetcode"

def test_example2():
    solution = Solution()
    assert solution.makeGood("abBAcC") == ""

def test_example3():
    solution = Solution()
    assert solution.makeGood("s") == "s"

def test_empty_string():
    solution = Solution()
    assert solution.makeGood("") == ""

def test_no_reduction_needed():
    solution = Solution()
    assert solution.makeGood("abcABC") == "abcABC"

def test_full_reduction():
    solution = Solution()
    assert solution.makeGood("aAaA") == ""

def test_mixed_cases():
    solution = Solution()
    assert solution.makeGood("aAbBcCdDeE") == ""

def test_partial_reduction():
    solution = Solution()
    assert solution.makeGood("aAbBC") == "C"
