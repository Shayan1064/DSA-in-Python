


# Checking plindrome

num1=121
result=0
original=num1
while(num1>0):
    last_digit=num1%10
    result=(result*10)+last_digit
    num1//=10
    
print(result)
num2=result

if(original==num2):
    print("Yes Plindrome")
else:
    print("Not Plindrome")