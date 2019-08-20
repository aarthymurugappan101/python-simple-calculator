def add (a,b):
    return a+b

def subtract (a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide (a,b):
    return x/y

def mainmenu():
    print("select operation \n 1.Add\n 2.Subtract\n 3.Multiply\n4.Divide")
    choice = input("enter the choice(1/2/3/4)")
    num1 = int(input("enter the first number"))
    num2 = int(input("enter the second number"))


    if choice == "1":
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == "2":
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice == "3":
        print(num1,"x",num2,"=",multiply(num1,num2))
    elif choice == "4":
        print(num1,"/",num2,"=",divide(num1,num2))
    else:
        print("invalid input")

mainmenu()
