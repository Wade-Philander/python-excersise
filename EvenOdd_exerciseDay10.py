listOne = [3, 6, 9, 12, 15, 18, 21]         #Making my first List
listTwo = [4, 8, 12, 16, 20, 24, 28]        #making a second list
listThree = []                             #Making a third empty list to move all my values.

for i in range(len(listOne)):              # Allowing the for loop to run through listOne regardless of the length and give it the value i
        if i%2==1:                              # Check if i (which is the numbers within my list) is divisable by 2 with a remainder(odd numbers) and removes it automatically.
                listThree.append(listOne[i])       # Append/Move the result to empty listThree which will give you all the even numbers because that is all that remains inside listOne.

print(listThree)                        # Print the numbers (that doesn't give a remainder) that has been moved to listThree.

for i in range(len(listTwo)):        #repeat the steps for listTwo
    if i%2==0:                          #Check if i is again divisable by 2 however if it doesn't give a remainder(even number) removes it automatically
        listThree.append(listTwo[i])    #Append/Move the result again to listThree

print(listThree)                        #Print listThree which is a combination of the result of listOne & listTwo.


#***************************************************************************************************************************************
 # QUESTION 2

list = [54, 44, 27, 79, 91, 41]             # Makeing my list
print("Initial", list, "\n")

x = list.pop(4)                             #using the built in pop() method to remove the 4th placed index but at the sametime giving the removed index a variable
print("After the removal of index 4", list)     #print out the list without the 4th index

list.insert(2, x)                                   #using the variable name to insert() the initial removed index and replacing it at the second index
print("Relocate at index 4 to index 2", list)       

list.append(x)                                          # Append the variable to add in again for the second time to the list however it will automatically be add to the back of the list because there is no index specification before appending.
print("Add the initial index again at the end of the list", list, "\n") # print final list.

#****************************************************************************************************************************************

# QUESTION 3

anotherlist = [11, 45, 8, 23, 14, 12, 78, 45, 89] #Original list
print(anotherlist)

polony = anotherlist[0:3]               # Gave the first 3 index a variable name

(range(len((polony))))             # use the function of range(len) to run through the specific index in the Variable.
print("first half", polony,"\n","Reverse first half",polony[::-1],"\n")  # print the findings of the above index and again (print twice) but in reverse using ::-1 in a new line

sasuage = anotherlist[3:6]              # Gave the second 3 index a variable name of Sasuage

(range(len((sasuage))))                                                     # Repeat
print("Second half", sasuage,"\n","Reverse second half",sasuage[::-1],"\n")  # Repeat

kalamari = anotherlist[6:9]                     # Gave the third 3 index a variable named kalamari

(range(len((kalamari))))                        # Repeat
print("Third half", kalamari,"\n","Reverse third half" ,kalamari[::-1],"\n")            # Repeat

#*****************************************************************************************************************************************

# QUESTION 4

againlist = [11, 45, 8, 11, 23, 45, 23, 45, 89]

dict = dict() 

for num in againlist:       
    if(num in dict):
        dict[num] +=1
    else:
        num = 1
print(dict)

# ******************************************************************************************************************************************

# Question 5 

list1 = [2, 3, 4, 5, 6, 7, 8]       #Making a list
print(list1)

list2 = [4, 9, 16, 25, 36, 49, 64] # Making another list
print(list2)

i = zip(list1, list2)       # use zip function to combine the two list as a itarators
print(set(i))               # print out the itarators inside a set.

#********************************************************************************************************************************************

# QUESTION 6.

# **********************************************************************************************************************

# QUESTION 7.

set1 = {27, 43, 34}
set2 = {34, 93, 22, 27, 43, 53, 48}

if (set1.issuperset(set2)) :                # Use the built in .issuperset() method to determine if set2 is  is within set1.
    print("True - This is the Superset")    # If True, set1 is the superset.
else :
    print("False - This is the subset")     # If False, set1 is the subset.

if (set1.issubset(set2)) :                  # Use the built in .issubset() method to determine if set2 is a 'smaller' or a cut version from set1.
    print("True - This is the Subset")      # If true, set1 is the subset
else :
    print("False - This is the superset")   # If false, set1 is the superset.


# ***************************************************************************************************************


# QUESTION 8.

rollNumber  = [47, 64, 69, 37, 76, 83, 95, 97]
val = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

a = []                              # empty list

for x,y in val.items():         #Determining the value and index as x,y in dictionary 
    for i in rollNumber:        # Determining i index in list
        if i==y:                # Comparing the index in the list rollNumber to the value in dictionary to check if the value are in both list and dict.
            a.append(i)         # Move the result to my empty list.

print(a)            #print my empty list to show all the values that were in both rollNumber & val.
        
#****************************************************************************************************************

#   QUESTION 9

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

b = list(dict.fromkeys(speed.values())) 

print(b)

# ******************************************************************************************************************************

