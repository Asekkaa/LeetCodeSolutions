class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1 or greater than the length of s
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0  # Start from the first row
        going_down = False  # Initially we are going down the zigzag
        
        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char  # Add character to the current row
            
            # Change direction if we are at the top or bottom row
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            
            # Move up or down
            current_row += 1 if going_down else -1
        
        # Join all rows to get the final string
        return ''.join(rows)

# Example usage:
sol = Solution()

