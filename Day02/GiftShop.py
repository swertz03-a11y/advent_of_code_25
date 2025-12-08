def int_len(n):
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length

running_total = 0

with open('giftShopInput.txt', 'r') as file:
    data = file.read()
    rows = data.split(',')
    for row in rows:
        row = row.strip()
        lower,upper = row.split('-')
        for i in range(int(lower), int(upper)+1):
            i_len = int_len(i)
            if(i_len % 2 == 1):
                continue
            first_half = i // (10**(i_len//2))
            second_half = i % (10**(i_len//2))
            # print(i, i_len, first_half, second_half)
            if first_half == second_half:
                running_total += i

print("Running total:", running_total)
