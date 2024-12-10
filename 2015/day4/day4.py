import hashlib

key = "bgvyzdsv"

num = 0

answer_1 = None
answer_2 = None
while answer_1 == None or answer_2 == None:
    combined = key + str(num)
    result = hashlib.md5(combined.encode()).hexdigest()
    if result[0:5] == '00000' and answer_1 == None:
        answer_1 = num
    if result[0:6] == '000000' and answer_2 == None:
        answer_2 = num
    num += 1

print(f'part1: {answer_1}')
print(f'part2: {answer_2}')