class Solution:
    def candy(self, ratings):
        n = len(ratings)
    
        # Step 1: Initialize the candies array with 1 candy for each child
        candies = [1] * n

        # Step 2: Left-to-right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right-to-left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Sum up all the candies
        return sum(candies)
