print("Simple Calculator by Muhammad Saleem")
print("-"*40)
while True :
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    choice = input("Select an Option : (/, *, +, -) : ")
    if choice == '/':        
        if num1 == 0 :
            print("can't divided by zero")
            break
        else :
            div = num2/num1
            print("Division : ", div)
    elif choice == '*':
        mul = num1*num2
        print("Multiplication : ", mul)
    elif choice == '+':
        add = num1+num2
        print("Addition : ", add)
    elif choice == '-':
        sub = num1-num2
        print("Substraction : ", sub)
    else : print("Invalid Input")

    exit = input("Enter Yes / No :")
    if exit == "Yes":
        break

