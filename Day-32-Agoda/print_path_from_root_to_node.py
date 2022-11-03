def helper_solve(A, B, path):
    if A:
        helper_solve(A.left, B, path)
        if not path:
            helper_solve(A.right, B, path)
        if path != [] or A.val == B:
            path.append(A.val)

    return path[::-1]


if __name__ == '__main__':
    """
    https://www.interviewbit.com/problems/path-to-given-node/
    
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    """
    helper_solve(A, B, [])