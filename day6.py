'''
def greet(name):
    print("Hello", name)
    print("Whats going on?")

greet("Paul")
print("this is outside greet()")

def add_two_numbers(num1, num2):
    answer=num1 +num2
    return answer

first_number=int(input("Enter First number"))
second_number=int(input("Enter second number"))

solution= add_two_numbers(first_number,second_number)

print(first_number,"+", second_number,"=", solution)


def number(n):
    if n ==1:
        return 1
    else 
    return n*number (n-1)
'''


def palindrome(w):
    w = str (w)
    return w == w[::-1]
 
w = input("Check if its Palidrome\n")

ans = palindrome(w)
 
if ans:
    print("Well done")
else:
    print("Whaap Whaap")


