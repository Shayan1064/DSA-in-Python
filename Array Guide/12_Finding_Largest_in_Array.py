def largest(arr):
    key=arr[0]
    for i in range(len(arr)):
        if arr[i]>key:
            key=arr[i]
    print("Largest Number in Array: ",key)

arr=[1,22,333,5,6,7]
largest(arr)
