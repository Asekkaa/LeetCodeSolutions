class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Strip leading and trailing spaces
        s = s.strip()
        
        # Step 2: Split the string into words based on whitespace
        words = s.split()
        
        # Step 3: Reverse the list of words
        reversed_words = words[::-1]
        
        # Step 4: Join the reversed list into a single string with a single space
        return ' '.join(reversed_words)

# Example usage:
sol = Solution()
