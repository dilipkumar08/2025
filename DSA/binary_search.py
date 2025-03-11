#binary search

def binary_search(target,arr):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=low+high//2
    if arr[mid]>target:
      high=mid-1
    elif arr[mid]<target:
      low=mid+1
    else:
      return mid

print(binary_search(1,[1,2,3,4,5,6,7,8]))
