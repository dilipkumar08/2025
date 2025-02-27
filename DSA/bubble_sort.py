def bubble_sort(li:list):
    l=len(li)
    if l==1:
        return li
    else:
        for i in range(l-1):
            for j in range(l-1-i):
                if li[j]>li[j+1]:
                    li[j],li[j+1]=li[j+1],li[j]
        
        return li

print(bubble_sort([4,5,2,6,7,1,9,3,8,4]))
