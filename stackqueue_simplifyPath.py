
class Solution:
    """
    You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
    Your task is to transform this absolute path into its simplified canonical path.

    The rules of a Unix-style file system are as follows:
        - A single period '.' represents the current directory.
        - A double period '..' represents the previous/parent directory.
        - Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
        - Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.

    The simplified canonical path should follow these rules:
        - The path must start with a single slash '/'.
        - Directories within the path must be separated by exactly one slash '/'.
        - The path must not end with a slash '/', unless it is the root directory.
        - The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.

    Example 1:
        Input: path = "/home/"
        Output: "/home"

    Example 2:
        Input: path = "/home//foo/"
        Output: "/home/foo"

    Example 3:
        Input: path = "/home/user/Documents/../Pictures"
        Output: "/home/user/Pictures"

    Example 4:
        Input: path = "/../"
        Output: "/"

    Example 5:
        Input: path = "/.../a/../b/c/../d/./"
        Output: "/.../b/d"

    Constraints:
        - 1 <= path.length <= 3000
        - path consists of English letters, digits, period '.', slash '/' or '_'.
        - path is a valid absolute Unix path.
    """
    
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')
        
        for component in components:
            if component == "..":
                if stack:  # Go up one level if possible
                    stack.pop()
            elif component and component != ".":  # Ignore empty components and "."
                stack.append(component)
        
        return "/" + "/".join(stack)


# Pytest test cases
def test_example1():
    solution = Solution()
    assert solution.simplifyPath("/home/") == "/home"

def test_example2():
    solution = Solution()
    assert solution.simplifyPath("/home//foo/") == "/home/foo"

def test_example3():
    solution = Solution()
    assert solution.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"

def test_example4():
    solution = Solution()
    assert solution.simplifyPath("/../") == "/"

def test_example5():
    solution = Solution()
    assert solution.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"

def test_empty_path():
    solution = Solution()
    assert solution.simplifyPath("/") == "/"

def test_only_slashes():
    solution = Solution()
    assert solution.simplifyPath("////") == "/"

def test_complex_path():
    solution = Solution()
    assert solution.simplifyPath("/a/./b/../../c/") == "/c"

def test_multiple_parent_directories():
    solution = Solution()
    assert solution.simplifyPath("/a/../../b/../c//.//") == "/c"

def test_trailing_slash():
    solution = Solution()
    assert solution.simplifyPath("/a/b/c/") == "/a/b/c"
