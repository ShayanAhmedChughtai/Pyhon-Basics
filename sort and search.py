# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
#  #list of odd numbers
# print(list) 
# num =("Enter any number from the above list  ")
# #selection of number 
# length = len(list)
# 
# def search(list , length, num): # to search the entered number in the list
#     for i in range(0, length):
#         if (list[i] == num):
#             return i
#     return 0
# 
# result = search(list, length, num) 
# if(result == 0):
#  print("Not found in the above list") 
# else:
#  print("found at index", result)
#  


























list=[2,4,6,8,7]
print(list)
num=4
length=len(list)

def search(list, num,length):
    for i in range(0,length):
        if(list[i]==num):
            return i
    return 0


result=search(list,num,length)
if(result==0):
    print("not found")
else:
    print("found at index",result)
