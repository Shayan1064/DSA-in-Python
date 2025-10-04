
def second_larget(arr):
    first=second=-99999
    
    for num in arr:
        if num > first:
            second=first
            first=num
        elif num>second and num !=first:
            second=num
            
    return second
arr=[11,22,33,44,55]
scnd_lrgst=second_larget(arr)
print(scnd_lrgst)