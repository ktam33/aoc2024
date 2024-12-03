def is_safe(numbers):
    is_ascending = numbers[1] > numbers[0]

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        if is_ascending and diff <= 0:
            return False
        if not is_ascending and diff >= 0:
            return False
        if abs(diff) > 3:
            return False

    return True

# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

safe_count = 0
for line in lines:
    # split up the line into a list of numbers
    numbers = [int(x) for x in line.split(' ')]
    if is_safe(numbers):
        safe_count += 1
    else:
        for i in range(len(numbers)):
            numbers_copy = numbers.copy()
            del numbers_copy[i]
            if is_safe(numbers_copy):
                safe_count += 1
                break

print(safe_count)