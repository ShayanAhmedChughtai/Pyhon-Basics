def country_visit1():
    print("I will go to China")

def country_visit2():
    print("I will go to Japan")

def country_visit3():
    print("I will go to Canada")

def country_visit4():
    print("I will go to Saudi Arabia")

choice = 0
while choice != 5:
    print("\n1. China\n2. Japan\n3. Canada\n4. Saudi Arabia\n5. Exit")
    choice = int(input("Enter the country you want to visit: "))
    
    if choice == 1:
        country_visit1()
    elif choice == 2:
        country_visit2()
    elif choice == 3:
        country_visit3()
    elif choice == 4:
        country_visit4()
    elif choice == 5:
        print("Program Terminated")
    else:
        print("Invalid choice. Please select a valid option.")
