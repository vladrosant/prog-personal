# task 3

number = int(input('Please enter an integer number: '))
while (number<0):
    number = int(input('Make sure the number is positive: '))
if number == 0:
    print(f"{number}! = 1")
else:
    factorial = 1
    for i in range(2, number+1):
        factorial = i*factorial
    print(f"{number}! = {factorial}.")