from functions import *

no_of_students = int(input('How many students do you have? '))
i = 0

while i < no_of_students:
    name = input(f'Name of student {i + 1}? ')
    score = float(input("Score? "))
    scores(score)
    i = i + 1
