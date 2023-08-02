choice=0

while choice<5:
    print("\n1. Celsius to Fahrenhiet \n2. Fahrenhiet to Celsuis \n3. Celsuis to Kelvin \n4. Average of Numbers \n5. Exit")
    choice=int(input("Enter your choice : "))

    if choice == 1:
        tc=int(input("Enter temperature in Celsius : "))
        tf=(tc+32)*(9/5)
        print(tc,"Celsius is equal to ",tf,"Fahrenhiet")
    
    elif choice==2:
        tf=int(input("Enter temperature in Fahrenhiet : "))
        tc=(tf-32)*(5/9)
        print(tf,"Fahrenhiet is equal to ",tc,"Celsius")
    
    elif choice==3:
        tc=int(input("Enter temperature in Celsius : "))
        tk=(tc+273)
        print(tc,"Celsuis is equal to ",tk,"Kelvin")
    
    elif choice==4:
        numbers = [1, 2, 34, 56, 7, 23, 23, 12, 1, 2, 3, 34, 56]
        sumOfNums = 0
        count = 0
        for number in numbers:
            sumOfNums += number
            count += 1
        average = sumOfNums / count
        print("The list of numbers is:", numbers)
        print("The average of all the numbers is:", average)
    else:
        print("Program Terminated")

        
        
        











