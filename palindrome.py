number=int(input("enter a number"))
original=number
reverse=0
while(number>0):
    remainder=number%10
    reverse=(reverse*10)+remainder
    number=number//10
if(original==reverse):
    print("number is palindrome")
else:
    print("number is not palindrome")
