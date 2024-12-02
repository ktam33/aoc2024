def is_safe(numbers):
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

def is_safe_if_removed(line, index_to_remove):
    del line[index_to_remove]
    return is_safe(line)


# read file contents into a list called lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

safe_count = 0
for line in lines:
    numbers = [int(x) for x in line.split(' ')]
    if is_safe(numbers):
        safe_count += 1
    else:
        # for each number in the line, check if it is safe after removing the number
        for i in range(len(numbers)):
            numbers_copy = numbers.copy()
            del numbers_copy[i]
            if (is_safe(numbers_copy)):
                safe_count += 1
                break


print(safe_count)
