class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # Count of words passing through this node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1  # Increment the count for this prefix

    def calculate_score(self, word):
        node = self.root
        score = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                score += node.count  # Add the count at this prefix node
            else:
                break  # No further prefixes in Trie
        return score

class Solution:
    def sumPrefixScores(self, words):
        # Create a Trie and insert all words
        trie = Trie()
        for word in words:
            trie.insert(word)

        # Calculate scores for each word
        answer = []
        for word in words:
            score = trie.calculate_score(word)
            answer.append(score)

        return answer

# Example usage:
sol = Solution()

