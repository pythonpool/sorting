def cycle_sort(l):
    writes = 0

    for c_start in range(0, len(l)-1):
        item = l[c_start]

        pos = c_start
        for i in range(c_start+1, len(l)):
            if l[i] < item:
                pos += 1

        if pos == c_start:
            continue
    
        while item == l[pos]:
            pos +=1 

        l[pos], item = item, l[pos]
        writes += 1


        while pos != c_start:
            pos = c_start
            for i in range(c_start+1, len(l)):
                if l[i] < item:
                    pos += 1

            while item == l[pos]:
                pos += 1
            l[pos], item = item, l[pos]
            writes += 1

l1 = [3,2,1,4,6,5]
cycle_sort(l1)
print(l1)