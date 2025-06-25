def counting_sort(li:list):
    m=max(li)
    count=[0]*(m+1)
    l=len(li)
    while(l>0):
        temp=li.pop()
        count[temp]+=1 
        l-=1
    for i in range(len(count)):
        while count[i]>0:
            li.append(i)
            count[i]-=1
    return li

print(counting_sort([1,4,3,6,2,19,8,5]))
        
