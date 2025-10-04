arr=[5,3,8,9,1,0]

for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
    
print("Sorted array:", arr)


# Q: What is Insertion Sort?
# 👉 It’s a sorting method that puts each element in its correct place, one by one — like sorting playing cards in your hand.

# Q: How does it work?
# 👉 It takes one element, compares it with the left side, and keeps moving it left until it’s in the right spot.

# Example:
# [5, 3, 4, 1] → [3, 5, 4, 1] → [3, 4, 5, 1] → [1, 3, 4, 5]