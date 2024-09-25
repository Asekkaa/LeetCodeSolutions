class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Sort the strings to make it easy to find the common prefix
        strs.sort()

        # Take the first and last string in the sorted array
        first_str = strs[0]
        last_str = strs[-1]

        common_prefix = []

        # Compare characters of the first and last string
        for i in range(len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break

        return ''.join(common_prefix)
