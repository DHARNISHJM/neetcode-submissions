"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_maps = {}

        def dfs(node):
            if not node:
                return None

            if node in node_maps:
                return node_maps[node]
            
            node_maps[node] = Node(node.val)
            for i in node.neighbors:
                node_maps[node].neighbors.append(dfs(i))
            return node_maps[node]
        return dfs(node)