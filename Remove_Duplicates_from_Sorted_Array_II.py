class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        count = 1  # Initialize the count for the first element
        i = 1  # Start from the second element

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                else:
                    i += 1
            else:
                count = 1
                i += 1

        return len(nums)
