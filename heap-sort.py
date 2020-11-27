from heapq import heappush, heappop

def heap_sort(l):
    heap = []
    for i in l:
        heappush(heap, i)

    ordered = []
    while heap:
        ordered.append(heappop(heap))

    return ordered

l1 = [2,3,7,1,8,5,6]
res = heap_sort(l1)
print(res)