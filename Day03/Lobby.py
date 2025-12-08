NUM_DIGITS = 12

running_total = 0

with open('lobbyInput.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        tens_dig = line[0]
        tens_dig_index = 0
        cur_ind = 0
        max_dig = line[0]
        max_dig_index = 0
        digits = []
        for i in range(NUM_DIGITS):
            max_dig = line[cur_ind]
            max_dig_index = cur_ind
            for j in range(cur_ind + 1, len(line) - (NUM_DIGITS - len(digits)) + 1):
                if line[j] > max_dig:
                    max_dig = line[j]
                    max_dig_index = j
            cur_ind = max_dig_index + 1
            digits.append(int(max_dig))
        
        for i in range(len(digits)):
            running_total += digits[i] * (10 ** (NUM_DIGITS - i - 1))

print("Running total:", running_total)