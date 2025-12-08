with open('laboratoriesInput.txt', 'r') as file:
    beams = []
    split_count = 0
    
    line = file.readline()
    beams = {line.find('S'): 1}
    for line in file.readlines():
        new_beams = {}
        for beam in beams.keys():
            if line[beam] == '^':
                if beam - 1 not in new_beams:
                    new_beams[beam - 1] = beams[beam]
                else:
                    new_beams[beam - 1] += beams[beam]
                
                if beam + 1 not in new_beams:
                    new_beams[beam + 1] = beams[beam]
                else:   
                    new_beams[beam + 1] += beams[beam]
            else:
                if beam not in new_beams:
                    new_beams[beam] = beams[beam]
                else:
                    new_beams[beam] += beams[beam]
        
        beams = new_beams
    
print(sum(beams.values()))