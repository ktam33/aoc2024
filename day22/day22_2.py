import math
from tqdm import tqdm

def get_combos():
    for i in range(-9, 10):
        for j in range(-9, 10):
            for k in range(-9, 10):
                for l in range(-9, 10):
                    yield (i,j,k,l)

def get_next_secret(number):
    prune_num = 16777216
    a = ((number * 64) ^ number) % prune_num
    b = (math.floor(a/32) ^ a) % prune_num
    return ((b * 2048) ^ b) % prune_num

def get_prices(number):
    curr_secrets = []
    curr_prices = {}
    curr_secrets.append((number, number % 10, 0))
    for i in range(1, 2000):
        number = get_next_secret(number)
        price = number % 10
        curr_secrets.append((number, price, price - curr_secrets[i - 1][1]))
        if i > 3:
            key = (
                curr_secrets[i - 3][2],
                curr_secrets[i - 2][2],
                curr_secrets[i - 1][2],
                curr_secrets[i][2],
            )
            if key not in curr_prices:
                curr_prices[key] = price
    return curr_prices

with open('input.txt', 'r') as file:
    secrets = [int(line.strip()) for line in file]

secret_prices = {}
for secret in secrets:
    secret_prices[secret] = get_prices(secret)

max_bananas = 0
curr_combo = None
for combo in tqdm(list(get_combos())):
    curr_bananas = 0
    for secret in secret_prices:
        if combo in secret_prices[secret]:
            curr_bananas += secret_prices[secret][combo]
    if curr_bananas > max_price:
        max_price = max_bananas
        curr_combo = combo

print(curr_combo)
print(max_price)