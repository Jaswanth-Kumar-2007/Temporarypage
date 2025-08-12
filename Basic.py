print("Welcome to Calculator")
s = input("Are you Want to Continue(y or n):")

while s=="y":
    num1 = input("Enter num1:")
    num2 = input("Enter num2:")
    operand = input("Select Operand(+,-,*,/):")
    if (operand=="+"):
        print(num1+num2)
    elif(operand=="-"):
        print(num1-num2)
    elif(operand=="*"):
        print(int(num1)*int(num2))
    elif(operand=="/"):
        print(int(int(num1)/int(num2)))
    else:
        print("invalid operand")
        
    s = input("Are you Want to Continue(y or n):")
else:
              print("Thanks for Using me")

        
