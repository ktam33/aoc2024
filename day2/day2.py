def is_safe(line):
    return True

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

safe_count = 0
for line in lines:
    if is_safe(line):
        safe_count += 1

print(safe_count)