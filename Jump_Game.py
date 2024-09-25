class Solution:
    def canJump(self, nums):
        max_reach = 0
        n = len(nums)

        for i in range(n):
            # Check if the current index is unreachable
            if i > max_reach:
                return False

            # Update the maximum reachable index
            max_reach = max(max_reach, i + nums[i])

            # If the last index is reachable, return True
            if max_reach >= n - 1:
                return True

        return False
