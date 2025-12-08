total_zeroes = 0
safe_place = 50
total_zero_passes = 0

with open('secretEntranceInput.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            passing_line = ""
            line = line.strip()
        
            if len(line) < 2:
                continue
            
            turn = int(line[1:])

            total_zero_passes += turn // 100

            turn %= 100

            if line.startswith('L'):    
                if safe_place - turn < 0:
                    passing_line = "Passing\n"
                    total_zero_passes += 1
                safe_place -= turn
            else:
                if safe_place == 0:
                    total_zero_passes += 1
                if safe_place + turn > 100:
                    passing_line += "Passing\n"
                    total_zero_passes += 1
                safe_place += turn

            safe_place %= 100
            
            if safe_place == 0:
                total_zeroes += 1

print("Total zeroes", total_zeroes)
print("Total zero passes:", total_zero_passes)