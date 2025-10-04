

def binary_search(arr,taregt):
    low=0
    high=len(arr)-1
    
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==taregt:
            return mid
        elif arr[mid]<taregt:
            low=mid+1
        else:
            high=mid-1
            
arr=[11,22,33,44,55,66,77,88,99]
target=88

found=binary_search(arr,target)
print("Found ",found)