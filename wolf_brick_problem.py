

def solve_wolf_brick(A):
    D = [1 for i in A]
    H = [[i,idx] for idx,i in enumerate (A)]
    brick_wolf(H,D,0)
    return D


def brick_wolf(A,D,i=0,j=None):
    if j == None: j = len(A)
    if(j - i > 1):
        c = (i+j+1) //2
        brick_wolf(A,D,i,c)
        brick_wolf(A,D,c,j)
        L,R = A[i:c],A[c:j]
        merge(L,R,len(L),len(R),i,j,D,A)


def merge(L,R,i,j,a,b,D,A):
    if a < b:
        if(L[i-1] >= R[j-1] and i > 0) or (j<=0):
            A[b-1] = L[i-1]
            D[L[i-1][1]] += j
            i = i -1
        else:
            A[b-1] = R[j-1]
            j = j-1
        merge(L,R,i,j,a,b-1,D,A)
    

def main():
    X = [34,57,70,19,48,2,94,7,63,75]
    A = solve_wolf_brick(X)
    assert(A == [4,5,6,3,3,1,4,1,1,1])


main()