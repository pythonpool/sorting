def comp_and_swap(a, i, j, dire):
    if (dire==1 and a[i]>a[j]) or (dire==0 and a[i]<a[j]):
        a[i], a[j] = a[j], a[i]

def bitonic_merge(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt/2)
        for i in range(low, low+k):
            comp_and_swap(a, i, i+k, dire)
        bitonic_merge(a, low, k, dire)
        bitonic_merge(a, low+k, k, dire)

def bitonic_sort(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt/2)
        bitonic_sort(a, low, k, 1)
        bitonic_sort(a, low+k, k, 0)
        bitonic_merge(a, low, cnt, dire)

l1 = [3,7,4,8,6,2,1,5]
n = len(l1)
up = 1
low = 0

bitonic_sort(l1, low, n, up)
print(l1)