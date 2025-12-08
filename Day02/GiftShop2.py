running_total = 0

with open('giftShopInput.txt', 'r') as file:
    with open('test.txt', 'w') as test_file:
        data = file.read()
        rows = data.split(',')
        for row in rows:
            row = row.strip()
            lower,upper = row.split('-')
            for i in range(int(lower), int(upper)+1):
                i_str = str(i)
                i_len = len(i_str)
                for j in range(1, i_len):
                    if i_len%j != 0:
                        continue
                    substrs = []
                    repeating = True
                    start_ind = 0
                    for k in range(0, i_len//j):
                        substr = i_str[start_ind:start_ind + j]
                        # test_file.write(f"{i} {i_len} {start_ind} {j} {substr} {repeating} {k} {i_len//j}\n")
                        if substr not in substrs:
                            substrs.append(substr)
                        if len(substrs) > 1:
                            repeating = False
                            break
                        start_ind += j
                    if repeating:
                        # test_file.write(f"Adding {i}\n")
                        running_total += i
                        break     

print("Running total:", running_total)
