def quick(arr):
    if len(arr)<=1:
        return arr
    pavit=arr[0]
    left=[x for x in arr[1:] if x<=pavit]
    right=[x for x in arr[1:] if x>pavit]
    return quick(left)+[pavit]+quick(right)

arr=[3,8,9,7,5,1,2,6]
print("Sorted Array: ",quick(arr))