class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count_map = defaultdict(int)
        pairs = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # Normalize the domino
            pairs += count_map[key]  # Add all previous dominoes of same type
            count_map[key] += 1

        return pairs
            
