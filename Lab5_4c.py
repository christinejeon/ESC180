def mult_M_v(M, v):
    new_v = [0]*len(M)
    for i in range(len(M)): # i is row num of M
        for k in range(len(M[i])): # k is col num of M
            new_v[i] += M[i][k] * v[k]
    return new_v

def mult_M_W(M, W):
    new_M = []
    k = 0
    for i in range(len(M)):
        new_M.append([0]*len(W[0]))
    for i in range(len(M)): # i is row num of M
        k = 0
        for j in range(len(W[i])): # j is col num of W
            for k in range(len(M[0])): # k is k
                new_M[i][j] += (M[i][k] * W[k][j])
    return new_M

if __name__ == '__main__':

    M = [[1, 2, 3], [4, 5, 6]] # 2 x 3
    W = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] # 3 x 3
    Z = [[1, 0, 0, 2], [0, 1, 0, 2], [0, 0, 1, 2]] # 3 x 4
    v = [0, 1, 2] # 3 x 1
    print(mult_M_v(M, v))
    print(mult_M_W(M, W))
    print(mult_M_W(M, Z))