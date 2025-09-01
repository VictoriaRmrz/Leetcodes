from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result

def createTree(list):
    nodes = [TreeNode(val) if val is not None else None for val in list]
    for i in range(len(list)):
        node = nodes[i]
        left_index = 2 * i + 1
        right_index = left_index + 1
        if left_index < len(list):
            node.left = nodes[left_index]
        if right_index < len(list):
            node.right = nodes[right_index]
    
    return nodes[0]

def main():
    sol = Solution()
    root = [3,9,20,None,None,15,7]
    tree = createTree(root)
    print(sol.levelOrder(tree))

if __name__ == "__main__":
    main()
