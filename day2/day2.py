def is_safe(line):
    numbers = [int(x) for x in line.split(' ')]
    is_ascending = numbers[0] < numbers[1]
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if is_ascending and diff < 0:
            return False
        if not is_ascending and diff > 0:
            return False
        abs_diff = abs(diff)
        if abs_diff < 1 or abs_diff > 3:
            return False 
    return True

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

safe_count = 0
for line in lines:
    if is_safe(line):
        safe_count += 1

print(safe_count)