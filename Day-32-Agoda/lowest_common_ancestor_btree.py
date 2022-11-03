from functools import cache

@cache
def search(_root, k):
    if _root == None:
        return False

    if _root == k:
        return True
    if search(_root.left, k):
        return True
    return search(_root.right, k)


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in (p, q):
            return root

        p_left = search(root.left, p)
        p_right = search(root.right, p)
        q_left = search(root.left, q)
        q_right = search(root.right, q)

        if p_left and q_right or p_right and q_left:
            return root
        elif p_left and not q_right or q_left and not p_right:
            return self.lowestCommonAncestor(root.left, p, q)
        elif not p_left and q_right or not q_left and p_right:
            return self.lowestCommonAncestor(root.right, p, q)