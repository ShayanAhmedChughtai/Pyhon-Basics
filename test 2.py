import math

def add(num1,num2):
    print("Addition of ",num1,"&",num2,"=",num1+num2)

def sub(num1,num2):
    print("Substraction of ",num1,"&",num2,"=",num1-num2)

def div(num1,num2):
    print("Division of ",num1,"&",num2,"=",num1/num2)

def mul(num1,num2):
    print("Multiplication of ",num1,"&",num2,"=",num1*num2)

def power(num1,num2):
    print("Power of ",num1,"&",num2,"=",num1**num2)

def sqrt(num1):
    print("SQRT of ",num1,"=",math.sqrt(num1))

def floor(num1):
    print("Floor of ",num1,"=",math.floor(num1))

def ceil(num1):
    print("Ceil of ",num1,"=",math.ceil(num1))

def sin(num1):
    print("Sin of ",num1,"=",math.sin(math.radians(num1)))

def cos(num1):
    print("Cos of ",num1,"=",math.cos(math.radians(num1)))

def tan(num1):
    print("Tan of ",num1,"=",math.tan(math.radians(num1)))




choice=0
while choice<12:
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
    
    print("\n1.Addition \n2.Subtraction \n3.Division \n4.Multiplication \n5.Power \n6.Under Root \n7.Floor \n8.Ceil \n9.Sin \n10.Cos \n11.Tan \n12.Exit")
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        add(num1,num2)
    elif choice==2:
        sub(num1,num2)
    elif choice==3:
        div(num1,num2)
    elif choice==4:
        mul(num1,num2)
    elif choice==5:
        power(num1,num2)
    elif choice==6:
        sqrt(num1)
    elif choice==7:
        floor(num1)
    elif choice==8:
        ceil(num1)
    elif choice==9:
        sin(num1)
    elif choice==10:
        cos(num1)
    elif choice==11:
        tan(num1)
    else:
        print("Program terminated")