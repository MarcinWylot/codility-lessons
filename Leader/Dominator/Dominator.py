def solution(A):
    idx = -1
    size = 0
    for i in range(len(A)):
        if size == 0: 
            idx = i
            size = 1
        elif A[i] != A[idx]:
            size = size - 1
        elif A[i] == A[idx]:
             size = size +1

    cnt = 0
    for a in A:
        if a == A[idx]: cnt = cnt +1

    if cnt > len(A)/2: 
        return idx
    else:
        return -1