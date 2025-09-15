# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object): #DFS
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1
        return max(left_depth, right_depth)



def makeTree(list):
    nodes = [TreeNode(val) if val is not None else None for val in list]
    for i in range(len(list)):
        node = nodes[i]
        if node is not None:
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
    tree = makeTree(root)
    print(sol.maxDepth(tree))

if __name__ == "__main__":
    main()