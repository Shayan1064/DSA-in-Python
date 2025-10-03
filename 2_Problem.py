

#        Sum of Every digit in Whole Number

n=5873
sum=0
while(n>0):
    digit=n%10
    sum+=digit
    n//=10
print(sum) 