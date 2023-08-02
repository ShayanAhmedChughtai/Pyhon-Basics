


id=9
u_name="Shayan"
password=123

id2=int(input("Enter number :"))
u_name2=input("Enter u name :")
password_2=int(input("Enter the pass :"))

if( id2==id and u_name2==u_name and password_2==password):
    print("Welcome to Dashboard", id)
else:
    print("Login Error")