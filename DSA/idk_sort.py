def bubble_sort(li: list):
    l=len(li)
    for i in range(l-1):
        for j in range(i+1,l):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    return li

print(bubble_sort([4,3,5,6,1,7,9,10,2,3]))
