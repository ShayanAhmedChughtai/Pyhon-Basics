def km_to_m():
    kilometer=float(input(" kilometer to meter convertor : "))
    meter=kilometer * 1000
    print(meter)
 
def m_to_km():
    meter=float(input(" meter to kilometer convertor: "))
    kilometer=meter / 1000
    print(kilometer)

def m_to_cm():
    meter=float(input("meter to centimeter : "))
    centimeter=meter * 100
    print(centimeter)

def cm_to_m():
    centimeter=float(input("centimeter to meter : "))
    meter=centimeter / 100
    print(meter)

def cm_to_mm():
    centimeter=float(input(" centimeter to milimeter convertor : "))
    milimeter=centimeter * 10
    print(milimeter)

def mm_to_cm():
    milimeter=float(input(" milimeter to centimeter convertor : "))
    centimeter=milimeter / 10
    print(centimeter)


choice = 0
while choice != 7:
    print("\n1.km to m convertor \n2.m to km convertor \n3.m to cm convertor \n4.cm to m convertor \n5.cm to mm convertor \n6.mm to cm convertor \n7.Exit")
    choice=int(input("Enter your choice : "))
    
    if choice==1:
        km_to_m()
    elif choice==2:
        m_to_km()
    elif choice==3:
        m_to_cm()
    elif choice==4:
        cm_to_m()
    elif choice==5:
        cm_to_mm()
    elif choice==6:
        mm_to_cm()
    else:
         print("Program Terminated")
 
 
 
 
 
