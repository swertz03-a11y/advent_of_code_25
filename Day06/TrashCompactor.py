import numpy as np

with open('trashCompactorInput.txt', 'r') as file:
    numbers = []
    for line in file.readlines():
        line = line.strip()
        equation = []
        for char in line.split():
            equation.append(char)
        numbers.append(equation)
    
    operations = numbers.pop(-1)


    running_total = 0
    for i in range(len(numbers[0])):
        operation = operations[i]
        if operation == '+':
            total = 0
        elif operation == '*':
            total = 1
        else:
            print("Unknown operation:", operation)
            exit(1)
        for j in range(len(numbers)):
            number = int(numbers[j][i])
            if operation == '+':
                total += number
            elif operation == '*':
                total *= number
            else:
                print("Unknown operation:", operation)
                exit(1)
        running_total += total

print(running_total)