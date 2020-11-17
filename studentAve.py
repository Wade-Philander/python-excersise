mark = []

student = input("Enter in you full name: ")

for i in range(3):
    i = float(input("Please enter you marks for your Tests:"))
    print("Thank you")
 
    mark.append(i)

print("Your Test marks are", mark)
print("-----------------------------------------------------------------------------")
ave = sum(mark)/3,
print("Your average mark is", ave, "%")

print("------------------------------------------------------------------------------")
if ave >=50:
    print("Well Done", student, "you passed")
if ave <50:
    print("Unlucky", student, "you failed")
