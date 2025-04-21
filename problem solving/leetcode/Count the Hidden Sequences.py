class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_sum = 0
        max_sum = 0
        current_sum = 0

        for diff in differences:
            current_sum += diff
            min_sum = min(min_sum, current_sum)
            max_sum = max(max_sum, current_sum)

        min_start = lower - min_sum
        max_start = upper - max_sum

        return max(0, max_start - min_start + 1)
