


# What is Recursion

count=0

def info():
    global count
    if  count==10:
        return
    print("Shayan Hassan")
    count+=1
    info()
info()

#-------------------------------------------------------

# Rescursion using parameters

def factorial(number):
    if(number==0 or number==1):
        return 1
    else:
        return number*(factorial(number-1))
    

number=int(input("Enter Number: "))
result=factorial(number)
print("The result is: ",result)