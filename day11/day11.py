from tqdm import tqdm

input = "8435 234 928434 14 0 7 92446 8992692"
# input = "125 17"
stones = input.split(" ")

def blink(stones, iteration, l):
    i = 0 
    with tqdm(total = l) as pbar:
        pbar.set_description(f'Processing iteration {iteration}')
        while i < l:
            if stones[i] == "0":
                stones[i] = "1"
            elif len(stones[i]) % 2 == 0:
                midpoint = int(len(stones[i])/2)
                stones.insert(i + 1, str(int(stones[i][midpoint:])))
                stones[i] = str(int(stones[i][:midpoint]))
                i += 1
            else:
                stones[i] = str(int(stones[i]) * 2024)
            i += 1
            pbar.update(1)

for i in range(25):
    blink(stones, i, len(stones))

print(len(stones))
