


# Checking Arm-Strong
# what is Arm-Strong

# number=153 and 1^3 + 5^3 + 3^3 =153 then it is called
# number=1537 and 1^4 + 5^4 + 3^4 =1537 then it is called 


number=153
original=number
total=0

while(number>0):
    digit=number%10
    digit=digit*digit*digit
    total+=digit
    number//=10
    
if original==total:
    print("Arm-Strong")
else:
    print("Arm-Strong")