

salary=int(input("Enter Salary : "))
if salary>1 and salary < 24999 :
    print("Designation : Junor Developer")
elif salary>24999 and salary< 34999:
    print("Designation:Associate Software Engineer")
elif salary>34999 and salary< 44999:
    print("Designation:Software Enigineer")
elif salary>44999 and salary< 69999:
    print("Designation:Senior Developer")
elif salary>69999 and salary< 150000:
    print("Principle Developer")
else:
    print("You are not qualified")
    



