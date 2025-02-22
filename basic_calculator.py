#====CALCULATOR====

def calculator():
    num1 = float(input("Enter the 1st number : "))
    num2 = float(input("Enter the 2nd number : "))
    operation = input("Choose the operator (+  , -  , * , / , % , **) : ")

    if (operation == "+") :
        result = num1+num2
        print(f"The addition of {num1} and {num2} = {result} ")
    
    elif (operation == "-") :
        result = num1-num2
        print(f"The subtraction of {num1} and {num2} = {result}")

    elif (operation == "*") :
        result = num1*num2
        print(f"The multiplication of {num1} and {num2} = {result}")

    elif (operation == "/") :
        if (num2 != 0) :
            result  = num1/num2
            print(f"The division of {num1} and {num2} = {result}")
        else:
            print("ERROR : Division by 0 is not possible!!")

    elif (operation == "%") :
        result = num1%num2
        print(f"The remainder from dividing {num1} and {num2} = {result}")

    elif (operation == "**") :
        result = num1**num2
        print(f"The power of {num1} , {num2} times = {result}")

    else:
        print("Invalid operator! Try again!...")

    
print(calculator())