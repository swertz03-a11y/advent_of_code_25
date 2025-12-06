def isFresh(fresh_ranges, ingredient):
    for start, end in fresh_ranges:
        if start <= ingredient <= end:
            return True
    return False

fresh_count = 0

with open('cafeteriaInput.txt', 'r') as file:
    fresh_ranges = []
    line = file.readline().strip()
    while line:
        parts = line.split('-')
        fresh_ranges.append((int(parts[0]), int(parts[1])))
        line = file.readline().strip()
    
    ingredients = []
    for line in file.readlines():
        ingredient = int(line.strip())
        ingredients.append(ingredient)
    
    for ingredient in ingredients:
        if isFresh(fresh_ranges, ingredient):
            fresh_count += 1
    
print("Fresh count:", fresh_count)
    