import tqdm
from datetime import datetime

input = "8435 234 928434 14 0 7 92446 8992692"
# input = "125 17"
stones = input.split(" ")

def blink(stones, iteration, l):
    i = 0 
    while i < len(stones):
        if stones[i] == "0":
            stones[i] = "1"
        elif len(stones[i]) % 2 == 0:
            midpoint = int(len(stones[i])/2)
            print(f'start {datetime.now()} {iteration}:{l}')
            stones.insert(i + 1, str(int(stones[i][midpoint:])))
            print(datetime.now())
            stones[i] = str(int(stones[i][:midpoint]))
            i += 1
        else:
            stones[i] = str(int(stones[i]) * 2024)
        i += 1

for i in tqdm.tqdm(range(75)):
    blink(stones, i, len(stones))

print(len(stones))
