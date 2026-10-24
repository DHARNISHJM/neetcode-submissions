class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
            
    def dfs(self, curr, word) -> bool:
        node = curr

        index = 0
        for char in word:
            if char == ".":
                flag = False
                for i in node.children.values():
                    flag = flag or self.dfs(i, word[index+1:])
                    if flag:
                        return flag
                return flag
            if char not in node.children:
                return False
            node = node.children[char]
            index += 1
        return node.endOfWord

    def search(self, word: str) -> bool:
        curr = self.root
        return self.dfs(curr, word)