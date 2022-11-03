def lca(root, a, b):
    if root is None:
        return None

    if root.data in (a, b):
        return root

    left = lca(root.left, a, b)
    right = lca(root.right, a, b)

    if left is None:
        return right
    if right is None:
        return left

    return root


def height(root, k, h):
    # find height of a node from root
    if root is None:
        return -1
    if root.data == k:
        return h

    res = height(root.left, k, h + 1)
    if res > 0:
        return res
    return height(root.right, k, h + 1)


class Solution:
    def findDist(self, root, a, b):
        lca_node = lca(root, a, b)
        return height(lca_node, a, 0) + height(lca_node, b, 0)