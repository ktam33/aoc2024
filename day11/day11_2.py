from tqdm import tqdm


class Stone():
    def __init__(self, value):
        self.value = value
        self.next = None

def blink(first_stone, iteration, l):
    with tqdm(total = l) as pbar:
        pbar.set_description(f'Processing iteration {iteration}')
        curr_stone = first_stone
        while curr_stone != None:
            next_stone = curr_stone.next
            if curr_stone.value == "0":
                curr_stone.value = "1"
            elif len(curr_stone.value) % 2 == 0:
                midpoint = int(len(curr_stone.value)/2)
                curr_stone.next = Stone(str(int(curr_stone.value[midpoint:])))
                curr_stone.next.next = next_stone
                curr_stone.value = str(int(curr_stone.value[:midpoint]))
                all_stones.append(new_stone)
            else:
                curr_stone.value = str(int(curr_stone.value) * 2024)
            curr_stone = next_stone
            pbar.update(1)

input = "8435 234 928434 14 0 7 92446 8992692"
# input = "125 17"
stones = input.split(" ")

all_stones = []
previous_stone = None
for stone in stones:
    new_stone = Stone(stone)
    if previous_stone:
        previous_stone.next = new_stone
    all_stones.append(new_stone)
    previous_stone = new_stone


first_stone = all_stones[0]
for i in range(75):
    blink(first_stone, i, len(all_stones))

print(len(all_stones))
