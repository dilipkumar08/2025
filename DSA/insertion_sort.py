
def insertion_sort(li:list):
    l=len(li)
    for i in range(1,l):
        idx=i
        temp=li.pop(i)
        for j in range(i-1,-1,-1):
            if temp<li[j]:
                idx=j
        
        li.insert(idx,temp)
    return li   

print(insertion_sort([7,8,5,3,2,9,20,1,4]))
