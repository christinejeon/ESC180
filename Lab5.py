def list1_start_with_list2(list1, list2):
    if len(list1) < len(list2):
        return False
    for i in range(len(list2)):
        if list2[i] != list1[i]:
            return False
    return True

def match_pattern(list1, list2):
    if len(list1) < len(list2):
        return False
    num = list1.count(list2[0])
    result = None
    for j in range(num):
        i = list1.index(list2[0])
        for k in range(i, i+len(list2)):
            if list1[k] != list2[k - i]:
                list1[i] = None
                result = False
                break
            result = True
    return result

def repeats(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i + 1]:
            return True
    return False

def print_matrix_dim(M):
    print(len(M), 'x', len(M[0]))

def mult_M_v(M, v):
    new_v = [0]*len(M)
    for i in range(len(M)): # i is row num of M
        for k in range(len(M[i])): # k is col num of M
            new_v[i] += M[i][k] * v[k]
    return new_v

if __name__ == '__main__':
    list1 = [1, 2, 5, 7, 2, 3, 4, 5]
    list2 = [2, 3, 4]
    list3 = [1, 3, 2, 2, 3, 5]
    list4 = [2, 3, 4, 5, 6]
    print(list1_start_with_list2(list4, list2))
    print(list1_start_with_list2(list1, list2))
    print(match_pattern(list1, list2))
    print(match_pattern(list3, list2))
    print(repeats(list3))
    print(repeats(list1))

    print_matrix_dim([[1,2],[3,4],[5,6]])
    M = [[1, 2, 3], [4, 5, 6]] # 2 x 3
    v = [0, 1, 2] # 3 x 1
    print(mult_M_v(M, v))