
from typing import List
from collections import deque

class Solution:
    """
    Given two gene strings startGene and endGene, and a gene bank, return the minimum number of mutations
    needed to mutate from startGene to endGene. Return -1 if it's not possible.

    Example 1:
        Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
        Output: 1

    Example 2:
        Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        Output: 2

    Constraints:
        - 0 <= bank.length <= 10
        - startGene.length == endGene.length == bank[i].length == 8
        - startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
    """

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        # Create a set for quick lookup
        bank_set = set(bank)
        
        # BFS initialization
        queue = deque([(startGene, 0)])  # (current_gene, steps)
        visited = set()  # To avoid revisiting genes
        visited.add(startGene)
        
        # Character set for possible mutations
        gene_chars = ['A', 'C', 'G', 'T']
        
        while queue:
            current_gene, steps = queue.popleft()
            
            # If we reach the end gene, return the number of steps
            if current_gene == endGene:
                return steps
            
            # Generate all possible one-mutation genes
            for i in range(len(current_gene)):
                for char in gene_chars:
                    if char != current_gene[i]:
                        mutated_gene = current_gene[:i] + char + current_gene[i+1:]
                        if mutated_gene in bank_set and mutated_gene not in visited:
                            visited.add(mutated_gene)
                            queue.append((mutated_gene, steps + 1))
        
        return -1  # If no mutation path exists


# Pytest test cases
def test_example1():
    solution = Solution()
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    assert solution.minMutation(startGene, endGene, bank) == 1

def test_example2():
    solution = Solution()
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    assert solution.minMutation(startGene, endGene, bank) == 2

def test_no_mutation_possible():
    solution = Solution()
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGCTA", "AACCGGTA"]
    assert solution.minMutation(startGene, endGene, bank) == -1

def test_start_equals_end():
    solution = Solution()
    startGene = "AACCGGTT"
    endGene = "AACCGGTT"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    assert solution.minMutation(startGene, endGene, bank) == 0

def test_empty_bank():
    solution = Solution()
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = []
    assert solution.minMutation(startGene, endGene, bank) == -1

def test_multiple_paths():
    solution = Solution()
    startGene = "AAAAACCC"
    endGene = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    assert solution.minMutation(startGene, endGene, bank) == 3
