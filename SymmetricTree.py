class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymetric(self, root):
        def isMirror(l1, l2):
            if not l1 and not l2:
                return True

            if not l1 or not l2:
                return False

            if l1.val == l2.val:
                return isMirror(l1.right, l2.left) and isMirror(l1.left, l2.right)
            return False

        return isMirror(root.left, root.right)


def createTree(list):
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
    root = [1, 2, 2, 3, 4, 4, 3]
    tree = createTree(root)
    print(sol.isSymetric(tree))  

    root = [1, 2, 2, None, 3, None, 3]
    tree = createTree(root)
    print(sol.isSymetric(tree)) 

    root = [1,2,3]
    tree = createTree(root)
    print(sol.isSymetric(tree)) 

if __name__ == "__main__":
    main()
