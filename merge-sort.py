def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    l_ind = r_ind = 0

    while len(result) < len(left) + len(right):
        if left[l_ind] <= right[r_ind]:
            result.append(left[l_ind])
            l_ind += 1
        else:
            result.append(right[r_ind])
            r_ind += 1

        if r_ind == len(right):
            result += left[l_ind:]
            break  
        if l_ind == len(left):
            result += right[r_ind:]
            break
    return result

def merge_sort(l):
    if len(l) < 2:
        return l
    mp = len(l) // 2
    return merge(left = merge_sort(l[:mp]), right = merge_sort(l[mp:]))

l1 = [8,2,6,4,5]
res = merge_sort(l1)
print(res)