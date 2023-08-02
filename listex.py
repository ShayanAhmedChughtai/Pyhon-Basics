# list=[]
# 
# for i in range(1,11):
#     name=input("Enter name : ")
#     list.append(name)
# 
# print(list)
# for i in range(0,10,2):
#     print(list[i])

def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,3]))
