def bubble_sort(l):
    n = len(l)

    for i in range(n):
        sorted = True
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                sorted = False

        if sorted:
            break
    return l

li = [8,2,6,4,5]
res = bubble_sort(li)
print(res)
