
from typing import List
from collections import defaultdict

class Solution:
    """
    You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri
    defeated player loseri in a match.

    Return a list answer of size 2 where:
        - answer[0] is a list of all players that have not lost any matches.
        - answer[1] is a list of all players that have lost exactly one match.
    
    The values in the two lists should be returned in increasing order.

    Note:
    - You should only consider the players that have played at least one match.
    - The testcases will be generated such that no two matches will have the same outcome.

    Example 1:
        Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
        Output: [[1,2,10],[4,5,7,8]]
        Explanation:
        - Players 1, 2, and 10 have not lost any matches.
        - Players 4, 5, 7, and 8 each have lost one match.
        - Players 3, 6, and 9 each have lost two matches.
        - Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

    Example 2:
        Input: matches = [[2,3],[1,3],[5,4],[6,4]]
        Output: [[1,2,5,6],[]]
        Explanation:
        - Players 1, 2, 5, and 6 have not lost any matches.
        - Players 3 and 4 each have lost two matches.
        - Thus, answer[0] = [1,2,5,6] and answer[1] = [].

    Constraints:
        - 1 <= matches.length <= 10^5
        - matches[i].length == 2
        - 1 <= winneri, loseri <= 10^5
        - winneri != loseri
        - All matches[i] are unique.
    """
    
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int)
        players = set()
        
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1
        
        not_lost = [player for player in players if loss_count[player] == 0]
        lost_once = [player for player in players if loss_count[player] == 1]
        
        return [sorted(not_lost), sorted(lost_once)]


# Pytest test cases
def test_example1():
    solution = Solution()
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    assert solution.findWinners(matches) == [[1, 2, 10], [4, 5, 7, 8]]

def test_example2():
    solution = Solution()
    matches = [[2,3],[1,3],[5,4],[6,4]]
    assert solution.findWinners(matches) == [[1, 2, 5, 6], []]

def test_no_losers():
    solution = Solution()
    matches = [[1,2],[2,3],[3,4]]
    assert solution.findWinners(matches) == [[1], [2, 3, 4]]

def test_no_matches():
    solution = Solution()
    matches = []
    assert solution.findWinners(matches) == [[], []]

def test_all_lost():
    solution = Solution()
    matches = [[1,2],[2,1]]
    assert solution.findWinners(matches) == [[], []]

def test_large_input():
    solution = Solution()
    matches = [[i, i + 1] for i in range(1, 100001)]
    assert solution.findWinners(matches) == [[1], [2]]

def test_multiple_losses():
    solution = Solution()
    matches = [[1,2],[2,3],[3,4],[4,5],[5,2]]
    assert solution.findWinners(matches) == [[1], [3, 4, 5]]
