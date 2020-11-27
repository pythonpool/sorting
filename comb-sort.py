def comb_sort(l):
    shrink = 1.3
    gaps = len(l)
    swapped = True
    i = 0

    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink)

        swapped = False
        i = 0

        while gaps + i < len(l):
            if l[i] > l[i+gaps]:
                l[i], l[i+gaps] = l[i+gaps], l[i]
                swapped = True
            i += 1
        
    return l

l1 = [5,15,37,29,25,79]
res = comb_sort(l1)
print(res)