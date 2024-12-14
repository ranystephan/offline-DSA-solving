
from typing import List

class Solution:
    """
    You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge 
    between ai and bi in the graph.

    Return the number of connected components in the graph.

    Example 1:
        Input: n = 5, edges = [[0,1],[1,2],[3,4]]
        Output: 2

    Example 2:
        Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
        Output: 1

    Constraints:
        - 1 <= n <= 2000
        - 1 <= edges.length <= 5000
        - edges[i].length == 2
        - 0 <= ai <= bi < n
        - ai != bi
        - There are no repeated edges.
    """
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union-Find implementation
        parent = list(range(n))  # Initially, every node is its own parent
        rank = [0] * n           # Rank for union by rank

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Union function
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                # Union by rank
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        # Apply union for all edges
        for u, v in edges:
            union(u, v)

        # Count unique roots
        return len(set(find(x) for x in range(n)))


# Pytest test cases
def test_example1():
    solution = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    assert solution.countComponents(n, edges) == 2

def test_example2():
    solution = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert solution.countComponents(n, edges) == 1

def test_no_edges():
    solution = Solution()
    n = 5
    edges = []
    assert solution.countComponents(n, edges) == 5

def test_disjoint_edges():
    solution = Solution()
    n = 6
    edges = [[0, 1], [2, 3], [4, 5]]
    assert solution.countComponents(n, edges) == 3

def test_large_graph():
    solution = Solution()
    n = 10
    edges = [[i, i + 1] for i in range(9)]  # Single chain
    assert solution.countComponents(n, edges) == 1

def test_single_node():
    solution = Solution()
    n = 1
    edges = []
    assert solution.countComponents(n, edges) == 1

def test_two_disconnected_chains():
    solution = Solution()
    n = 10
    edges = [[0, 1], [1, 2], [2, 3], [5, 6], [6, 7], [7, 8]]
    assert solution.countComponents(n, edges) == 3
