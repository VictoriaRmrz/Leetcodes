class Solution(object):
    def isSameTreeEasy(self, p, q):
        if p == q:
            return True
        
        if p != q:
            return False
        
    # in theory this could work but given that we are working with tree structures
    # we need to check the null values of the tree  and their structure
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# [head, left, right]

def main():
    sol = Solution()
    p = [1,2,3]
    q = [1,2,3]
    print(sol.isSameTree(p, q))  # Output: True

    p = [1, 2]
    q = [1, None, 2]
    print(sol.isSameTree(p, q))  # Output: False

    p = [1,2,1]
    q = [1,1,2]
    print(sol.isSameTree(p, q))

if __name__ == "__main__":
    main()