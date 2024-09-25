class Solution:
    def lengthOfLastWord(self, s):
        # Remove trailing spaces
        s = s.rstrip()

        # Find the index of the last space
        last_space_index = s.rfind(' ')

        # If no space is found, the entire string is a word
        if last_space_index == -1:
            return len(s)
        else:
            # Return the length of the last word
            return len(s) - last_space_index - 1
