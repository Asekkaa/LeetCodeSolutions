class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1  # Initialize the unique element count
        i = 1  # Start from the second element

        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
            i += 1

        return k
        
