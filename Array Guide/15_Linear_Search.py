def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return 0
    

arr=[1,2,3,4,5,6,7,8,9]

key=int(input("Enter key: "))
result=linear_search(arr,key)
if key!=-1:
    print("The Element is Found at index: ",result)
else:
    print("Element is not Found")