from random import randint

def quick_sort(l):
    if len(l) < 2:
        return l
    low, same, high = [], [], []
    pivot = l[randint(0, len(l)-1)]
    for i in l:
        if i < pivot:
            low.append(i)
        elif i == pivot:
            same.append(i)
        elif i > pivot:
            high.append(i)

    return quick_sort(low) + same + quick_sort(high)

l1 = [8,2,6,4,5]
res = quick_sort(l1)
print(res)