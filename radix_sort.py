from counting_sort import counting_sort
from element import Element

def radix_sort(A):
    n = len(A)
    u = 1 + max([a.key for a in A])
    c = 1 + (u.bit_count() // n.bit_count())

    ## Create digits
    class Obj:pass
    D = [Obj() for a in range(n)]
    for i in range(n):
        D[i].item = A[i]
        D[i].digits = []
        high = A[i].key
        for j in range(c):
            high,low = divmod(high,n)
            D[i].digits.append(low)
    for k in range(c):
        for j in range(n):
            D[j].key = D[j].digits[k]
        counting_sort(D)
    
    for i in range(n):
        A[i] = D[i].item



if __name__ == "__main__":
    arr = [Element(1,3),Element(1,2),Element(15,2),Element(3,4),Element(42,1),Element(2,4)]
    radix_sort(arr)
    print(arr)


    