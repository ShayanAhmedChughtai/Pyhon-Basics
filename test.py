id=input("Enter the id : ")
ps=input("Enter the ps : ")


if(id=="admin" and ps=="admin"):
    print("\t\t***Welcome to percentage calculator***")
    
    maths=int(input("enter Maths number : "))
    eng=int(input("enter ENG number : "))
    urdu=int(input("enter urdu number : "))
    total=int(input("Enter total numbers"))
    
    per=(((maths+eng+urdu)/total)*100)
    
    
    if(per>=80 and per<=100):
        print("the percenatage is : ",per)
        print("the Grade is : A-1")
    elif(per>=70 and per<80):
        print("the percenatage is : ",per)
        print("the Grade is : A")
    elif(per>=60 and per<70):
        print("the percenatage is : ",per)
        print("the Grade is : B")
    else:
        print("Bacha Fail hogya")
    
else:
    print("Access Denied")
    