'''
gas = 45
while gas > 0:
    print("Vroom")
    gas = gas-1
    if gas == 10:
        print ("Fill up!") 
        break #continue


ages = [18, 21, 16, 12]
for age in ages:
    if age >= 18:
        print("come in")
    elif age >= 16:
        print("Not there yet")
    else:
         print("get outta here")


adj = ["red", "big", "tasty"]
fruit = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruit:
        print(x, y)

for x in range(6):
    print(x)


number = 0
while number < 100:
    number = number +1
    if number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    elif number%3 and number%5 == 0:
        print("FizzBuzz")
    else:
        print(number)
    


number = 1
while number < 101:
    print(number)
    number = number +1
    if number == 100:
        print(number)
        

        count = number
        for x in count:
            if x%3==0:
                print("fizz")
'''
#list = [1,2,3,4,5,6,7,8,9]
import random 
number = random.randint(1, 10)

 print('I am thinking of a number between 1 and 10.')

guessesTaken = 3
