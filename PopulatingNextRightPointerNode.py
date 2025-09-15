from collections import deque
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    # DFS
    def connect(self, root):
        result = []
        def saveList(root):
            if root is None:
                return
            if root.right and root.left:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
            result.append((root.val, root.next.val if root.next else None))
            saveList(root.left)
            saveList(root.right)
        saveList(root)
        return result

    #BFS

    def BFS(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            right = None
            for _ in range(len(queue)):
                node = queue.popleft()
                node.next = right
                right = node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return root
    
    def anotherOption(self, root):
        if not root:
            return None

        leftmost = root
        while leftmost.left: # if there is a left child
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root


def createTree(list):
    nodes = [Node(val) if val is not None else None for val in list]
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
    root = [1,2,3,4,5,6,7]
    tree = createTree(root)
    result = sol.BFS(tree)
    print(result)

if __name__ == "__main__":
    main()