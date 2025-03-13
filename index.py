from functions import *
while True:
    try:
        no_of_students = int(input('How many students do you have? '))
        i = 0
        break
    except:
        print('Please input a number')

while i < no_of_students:
    while True:
        try:
            name = input(f'Name of student {i + 1}? ')
            score = float(input("Score? "))
            scores(score)
            i = i + 1
            break
        except:
            print("Invalid input")