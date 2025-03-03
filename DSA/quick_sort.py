def quick_sort(arr:list):
    if len(arr)<=1:
        return arr
    elif len(arr)==2:
        if arr[0]>arr[1]:
            return [arr[1],arr[0]]
        else:
            return arr
    else:
        temp=arr[0]
        low=[i for i in arr[1:] if i<temp]
        high=[j for j in arr[1:] if j>=temp]
        return quick_sort(low)+[temp]+quick_sort(high)

print(quick_sort([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))
