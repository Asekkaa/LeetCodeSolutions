class Solution:
    def trap(self, height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            # Process the side with the smaller max height
            if left_max <= right_max:
                # Water trapped at the current left position
                water_trapped += left_max - height[left]
                # Update left max
                left += 1
                left_max = max(left_max, height[left])
            else:
                # Water trapped at the current right position
                water_trapped += right_max - height[right]
                # Update right max
                right -= 1
                right_max = max(right_max, height[right])

        return water_trapped
