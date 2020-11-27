def insertion_sort(l):
    for i in range(1, len(l)):
        item = l[i]
        j=i-1
        while j>=0 and l[j] > item:
            l[j+1] = l[j]
            j -= 1

        l[j+1] = item
    return l

l1 = [8,2,6,4,5]
res = insertion_sort(l1)
print(res)