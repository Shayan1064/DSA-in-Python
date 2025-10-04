

def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    else:
        mid=len(arr)//2
        left_side=arr[:mid]
        Right_side=arr[mid:]
        left_sorted=merge_sort(left_side)
        Right_sorted=merge_sort(Right_side)
        return merge(left_sorted, Right_sorted)
    
def merge(left,right):
    sorted_array=[]
    i=j=0
    while i< len(left) and j <len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i+=1
        else:
            sorted_array.append(right[j])
            j+=1
    
    while i < len(left):
        sorted_array.append(left[i])
        i+=1
        
    while j < len(right):
        sorted_array.append(right[j])
        j+=1
    return sorted_array
    
arr=[3,4,7,9,8,7,3,5,0,8,2,3,5]
print("Unsorted array:", arr)

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)