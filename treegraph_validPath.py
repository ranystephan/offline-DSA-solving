
from typing import List

class Solution:
    """
    Given edges of a bi-directional graph and integers n, source, and destination, 
    determine if there is a valid path that exists from vertex source to vertex destination.

    Example 1:
        Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
        Output: true

    Example 2:
        Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
        Output: false

    Constraints:
        - 1 <= n <= 2 * 10^5
        - 0 <= edges.length <= 2 * 10^5
        - edges[i].length == 2
        - 0 <= ui, vi <= n - 1
        - ui != vi
        - 0 <= source, destination <= n - 1
        - There are no duplicate edges.
        - There are no self edges.
    """

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
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

        # Union all edges
        for u, v in edges:
            union(u, v)

        # Check if source and destination are in the same connected component
        return find(source) == find(destination)


# Pytest test cases
def test_example1():
    solution = Solution()
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    assert solution.validPath(n, edges, source, destination) is True

def test_example2():
    solution = Solution()
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5
    assert solution.validPath(n, edges, source, destination) is False

def test_single_node():
    solution = Solution()
    n = 1
    edges = []
    source = 0
    destination = 0
    assert solution.validPath(n, edges, source, destination) is True

def test_disconnected_graph():
    solution = Solution()
    n = 4
    edges = [[0, 1], [2, 3]]
    source = 0
    destination = 3
    assert solution.validPath(n, edges, source, destination) is False

def test_large_graph():
    solution = Solution()
    n = 100000
    edges = [[i, i + 1] for i in range(99999)]
    source = 0
    destination = 99999
    assert solution.validPath(n, edges, source, destination) is True
