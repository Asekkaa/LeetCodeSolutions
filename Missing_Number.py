class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
        actual_sum = sum(nums)
        return total_sum - actual_sum

