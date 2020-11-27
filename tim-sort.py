def insertion_sort(l, left=0, right=None):
    if right is None:
        right = len(l) - 1

    for i in range(left+1, right+1):
        key = l[i]
        j = i-1
        while j>= left and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

def tim_sort(l):
    min_run = 32
    n = len(l)

    for i in range(0,n,min_run):
        insertion_sort(l,i,min((i+min_run-1), (n-1)))

        size = min_run
        while size < n:
            for s in range(0,n, size*2):
                mid = s+ size-1
                end = min((s+sie*2-1), (n-1))

                merged = merge(left=l[s:mid+1], right=l[mid+1:end+1])

                l[s:s+len(merged)] = merged
            
        size *= 2
    return l

l1 = [34,10,64,51,32,21]
res = tim_sort(l1)
print(res)
