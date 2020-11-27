def shell_sort(l):
    gap = len(l) // 2
    while gap > 0:
        for i in range(gap, len(l)):
            temp = l[i]
            j = i
            while j>=gap and l[j-gap] > temp:
                l[j] = l[j-gap]
                j = j-gap
            l[j] = temp
        gap = gap//2
    return l

l1 = [17,3,9,1,8]
res = shell_sort(l1)
print(res)