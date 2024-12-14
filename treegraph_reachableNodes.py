
from typing import List
from collections import defaultdict

class Solution:
    """
    Given an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges, determine the maximum
    number of nodes reachable from node 0 without visiting restricted nodes.

    Example 1:
        Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
        Output: 4

    Example 2:
        Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
        Output: 3

    Constraints:
        - 2 <= n <= 10^5
        - edges.length == n - 1
        - edges[i].length == 2
        - 0 <= ai, bi < n
        - ai != bi
        - edges represent a valid tree.
        - 1 <= restricted.length < n
        - 1 <= restricted[i] < n
        - All values of restricted are unique.
    """

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # Build adjacency list for the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Convert restricted nodes to a set for O(1) lookup
        restricted_set = set(restricted)

        # Perform DFS from node 0
        def dfs(node, parent):
            count = 1  # Count this node
            for neighbor in graph[node]:
                if neighbor != parent and neighbor not in restricted_set:
                    count += dfs(neighbor, node)
            return count

        return dfs(0, -1)


# Pytest test cases
def test_example1():
    solution = Solution()
    n = 7
    edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
    restricted = [4, 5]
    assert solution.reachableNodes(n, edges, restricted) == 4

def test_example2():
    solution = Solution()
    n = 7
    edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
    restricted = [4, 2, 1]
    assert solution.reachableNodes(n, edges, restricted) == 3

def test_single_node():
    solution = Solution()
    n = 2
    edges = [[0, 1]]
    restricted = [1]
    assert solution.reachableNodes(n, edges, restricted) == 1

def test_no_restriction():
    solution = Solution()
    n = 5
    edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
    restricted = []
    assert solution.reachableNodes(n, edges, restricted) == 5

def test_all_nodes_restricted_except_root():
    solution = Solution()
    n = 4
    edges = [[0, 1], [1, 2], [2, 3]]
    restricted = [1, 2, 3]
    assert solution.reachableNodes(n, edges, restricted) == 1

def test_large_tree():
    solution = Solution()
    n = 100000
    edges = [[i, i + 1] for i in range(99999)]  # Linear tree
    restricted = [99999]
    assert solution.reachableNodes(n, edges, restricted) == 99999
