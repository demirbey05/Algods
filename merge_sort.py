def merge(A,L,R,i,j,p,q):
    # Merge L[:i] and R[:j] to A[p:q]
    if p < q :
        if (j <= 0) or (i > 0 and L[i-1] > R[j-1]):
            A[q-1] = L[i-1]
            i = i-1
        else:
            A[q-1] = R[j-1]
            j = j-1

        merge(A,L,R,i,j,p,q-1)



def merge_sort(A,a= 0, b= None):
    if b == None : b = len(A)
    if b - a > 1:
        mid = (a + b + 1) // 2 #Divide
        merge_sort(A,a,mid)  #Conquer
        merge_sort(A,mid,b)
        merge(A,A[a:mid],A[mid:b],mid-a,b-mid,a,b) # Combine
A = [1,2,3,4,5,6,7,8]
B = [12, 15, 23, 4 , 6, 10, 35]
C = []

merge_sort(A)
merge_sort(B)
merge_sort(C)

print(A)
print(B)
print(C)

