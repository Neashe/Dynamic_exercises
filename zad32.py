"""BST cost"""

def BST_cost(T):
    n = len(T)
    F = [[0,0] for i in range(n)]
    for