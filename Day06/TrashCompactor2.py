import numpy as np

with open('trashCompactorInput.txt', 'r') as file:
    numbers = []
    
    lines = file.readlines()

    operations = lines.pop(-1).split()

    operations = operations[::-1]

    eqn = []
    for j in range(len(lines[0].rstrip('\n')) - 1, -1, -1):
        num = ''
        for i in range(len(lines)):
            num = num + lines[i][j]
        if num.strip() == '':
            numbers.append(eqn)
            eqn = []
        else:
            eqn.append(num.strip())
    if numbers:
        numbers.append(eqn)

    running_total = 0
    for i in range(len(numbers)):
        operation = operations[i]
        if operation == '+':
            total = sum(int(x) for x in numbers[i])
        elif operation == '*':
            total = 1
            for x in numbers[i]:
                total *= int(x)
        else:
            print("Unknown operation:", operation)
            exit(1)
        running_total += total

print(running_total)
    
    