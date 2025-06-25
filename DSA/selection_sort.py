def selection_sort(li:list):
    l=len(li)

    for i in range(l-1):
        min_index=i
        for j in range(i+1,l):
            if li[min_index]>li[j]:
                min_index=j
        val=li.pop(min_index)
        li.insert(i,val)
    return li

print(selection_sort([12,3,24,2,6,5,8,9,7,1,4]))
    
        
