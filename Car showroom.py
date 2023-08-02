id=input("Enter the id : ")
ps=input("Enter the ps : ")


if(id=="admin" and ps=="admin"):
    print("***Login Accepted***")
    
    car=input("Enter the car name")
    if(car=="Corolla"):
        print("Make:Toyota")
    
    elif(car=="Civic"):
        print("Make:Honda")
    
    elif(car=="Huracan"):
        print("Make:Lamborghini")
        
    else:
        print("the car is not available")
else:
    print("Access Denied")
#

num=int(input("Enter you num"))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")
#     
#     
#     
#       
#        
# 
#         
#



num=int(input('Enter the num'))

if(num%5==0):
    print('Hello')
else:
    print("Bye")



unit=int(input("Enter the unit"))
cost=0
if(unit<=100):
    print("No charge")

elif(unit>100 and unit<200):
    cost=(unit-100)*5
    print("your total bill is RS.",cost)
else:
    cost=500+((unit-100)*10)
    print("your total bill is RS.",cost)


unit=int(input("Enter the unit : "))
cost=0
if(unit<=50):
    cost=(unit)*15
    print("Your total bill is RS.",cost)

elif(unit>50 and unit<=150):
    cost=750+(unit)*25
    print("your total bill is RS.",cost)
else:
    cost=750+3750+((unit)*35)
    print("your total bill is RS.",cost)

   





