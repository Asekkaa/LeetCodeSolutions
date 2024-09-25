class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
    
        needle_len = len(needle)
        haystack_len = len(haystack)
        
        if needle_len > haystack_len:
            return -1

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i

        return -1
