def cocktail_sort(l):

    for i in range(len(l)-1, 0, -1):
        swapped = False

        for j in range(i,0,-1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
                swapped = True

        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True

        if not swapped:
            return l

l1 = [9,7,2,5,4,1,12,3]
res = cocktail_sort(l1)
print(res)