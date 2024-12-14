import re

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

answer = 0
for line in lines:
    line_len = len(line)
    string_len = line_len + 2
    string_len += len(re.findall(r"[\\\"]", line))
    print(f"{line}: {line_len}, {string_len}")
    answer += string_len - line_len

print(answer)