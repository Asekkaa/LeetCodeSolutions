class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        content_children = 0
        i = 0

        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                content_children += 1
                i += 1

        return content_children
