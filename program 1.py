print("***\tInvitation to the Guests\t***\n")

guest_list=["Talal ","Abdul Moiz Khan","Shaheer","Owais Ahmed"]

for i in guest_list:
 print("->",i,"I invite u on dinner at 10:00 clock ")

#A guest cannot come to the dinner
print("\n\n>>>",guest_list[3],"can't come at dinner <<<\n\n")

#adding a guest to the list and removing the old guest
guest_list[guest_list.index("Owais Ahmed")]="Naveed"

print("***\tResending Invitation to the Guests\t***\n")

for x in guest_list:
 print("->",x,"I invite u on dinner at 10:00 clock")
