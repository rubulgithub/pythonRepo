####Faulty Calculator

print("Enter number 1")
number1=int(input())
print("Enter number 2")
number2=int(input())
print("Choose Operator")
operator=input()
if operator=='*':
    if number1==43 and number2==3 :
        print("555")
    else:
        print(number1*number2)
elif operator=='/':
    if number1==56 and number2==6:
        print("4")
    else:
        print(number1/number2)
elif operator=='+':
    if number1==56 and number2==9:
        print("77")
    else:
        print(number1+number2)
elif operator == '-':
    print(number1-number2)

