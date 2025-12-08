with open('laboratoriesInput.txt', 'r') as file:
    beams = []
    split_count = 0

    line = file.readline()
    beams.append(line.find('S'))
    for line in file.readlines():
        new_beams = []
        for beam in beams:
            
            if line[beam] == '^':
                if beam - 1 not in new_beams:
                    new_beams.append(beam - 1)
                if beam + 1 not in new_beams:
                    new_beams.append(beam + 1)
                split_count += 1
            else:
                if beam not in new_beams:
                    new_beams.append(beam)
        
        beams = new_beams
    
print(split_count)