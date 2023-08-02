#Electricity bill

unit=int(input("Enter the unit : "))
cost=0
if(unit<=50):
    cost=(unit)*15
    print("Your total bill is RS.",cost)

elif(unit>50 and unit<=150):
    cost=750+(unit)*25
    print("your total bill is RS.",cost)
else:
    cost=3250+((unit)*35)
    print("your total bill is RS.",cost)

  