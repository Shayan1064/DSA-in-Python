arr = [3, 4, 2, 1, 9, 3, 0, 7]
n = len(arr)


for i in range(n):
    for j in range(n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]


print("Sorted: ",arr)

# After pass 1: [3, 2, 1, 4, 3, 0, 7, 9]
# After pass 2: [2, 1, 3, 3, 0, 4, 7, 9]
# After pass 3: [1, 2, 3, 0, 3, 4, 7, 9]
# After pass 4: [1, 2, 0, 3, 3, 4, 7, 9]
# After pass 5: [1, 0, 2, 3, 3, 4, 7, 9]
# After pass 6: [0, 1, 2, 3, 3, 4, 7, 9]
# After pass 7: [0, 1, 2, 3, 3, 4, 7, 9]
# After pass 8: [0, 1, 2, 3, 3, 4, 7, 9]
