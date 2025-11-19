def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
        return -1
arr=[0,1,2,4,9]
target=int(input('enter element to search:'))
result=binary_search(arr,target)
if result!=-1:
    print(f'elemeny {target} found at index {result}')
else:
    print(f'element {target} not found')
