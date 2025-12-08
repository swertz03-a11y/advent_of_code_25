fresh_count = 0

with open('cafeteriaInput.txt', 'r') as file:
    fresh_ranges = []
    line = file.readline().strip()
    while line:
        parts = line.split('-')
        fresh_ranges.append((int(parts[0]), int(parts[1])))
        line = file.readline().strip()
    
    fresh_ranges.sort(key=lambda x: x[0])
     
    merged_ranges = []
    for current in fresh_ranges:
        if not merged_ranges:
            merged_ranges.append(current)
        else:
            last = merged_ranges[-1]
            if current[0] <= last[1]:
                merged_ranges[-1] = (last[0], max(last[1], current[1]))
            else:
                merged_ranges.append(current)
    
    for range in merged_ranges:
        fresh_count += range[1] - range[0] + 1
    
print("Fresh count:", fresh_count)