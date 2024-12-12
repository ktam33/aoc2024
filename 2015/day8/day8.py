import re

with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

answer = 0
for line in lines:
    line_len = len(line)
    string_len = line_len - 2
    string_len -= len(re.findall(r"\\x[0-9a-f]{2}", line)) * 3
    string_len -= len(re.findall(r"\\[\\\"]", line))
    print(f"{line}: {line_len}, {string_len}")
    answer += line_len - string_len

print(answer)