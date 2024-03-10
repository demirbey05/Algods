from element import Element
def counting_sort(A):
    keys = [i.key for i in A]
    u = max(keys) + 1
    ram = [[] for i in range(u)]

    for a in A:
        ram[a.key].append(a)
    j = 0
    for u in ram:
        for i in u:
            A[j] = i
            j += 1
    





if __name__ == "__main__":
    arr = [Element(1,3),Element(1,2),Element(15,2),Element(3,4),Element(42,1),Element(2,4)]
    counting_sort(arr)
    print(arr)


    
