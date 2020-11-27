def selection_sort(l):
    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                min_index = j

        l[i], l[min_index] = l[min_index], l[i]
    return l

l1 = [7,5,4,2]
res = selection_sort(l1)
print(res)