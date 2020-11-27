def pigeohole_sort(l):
    mini = min(l)
    maxi = max(l)
    size = maxi-mini+1

    holes = [0] * size
    for i in l:
        assert type(i) is int, "Integers are accepted"
        holes[i-mini] +=1

    a = 0
    for c in range(size):
        while holes[c]>0:
            holes[c] -=1
            l[a] = c+mini
            a += 1

    return l

l1 = [9,2,3,8,1,6,9]
res = pigeohole_sort(l1)
print(res)