#create a list of numbers (1-20)

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
print(list)
length=len(list)
oddlist=[]
evenlist=[]

def oddnumbers():
    for i in range(1,length+1,2):
        oddlist.append(i)
    print(oddlist)

def evennumbers():
    for i in range(2,length+1,2):
        evenlist.append(i)
    print(evenlist)

def search(list, num,length):
    for i in range(0,length):
        if(list[i]==num):
            return i
    return 0
choice=0
while choice != 4:
    print("enter choice\n 1.odd\n 2.even \n 3.index of 15 \n4. exit")
    choice=int(input("Enter Choice"))
    if choice ==1:
        oddnumbers()
    elif choice == 2:
        evennumbers()
    elif choice == 3:
        num=int(input("enter number"))
        result=search(list,num,length)
        if(result==0):
            print("not found")
        else:
            print("found at index",result)
    else:
        print("program terminated")
        
