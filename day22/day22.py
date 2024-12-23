import math

def get_next_secret(number):
    prune_num = 16777216
    a = ((number * 64) ^ number) % prune_num
    b = (math.floor(a/32) ^ a) % prune_num
    return ((b * 2048) ^ b) % prune_num

with open('input.txt', 'r') as file:
    secrets = [int(line.strip()) for line in file]

answer = 0
for secret in secrets:
    for _ in range(2000):
        secret = get_next_secret(secret)
    answer += secret

print(answer)
