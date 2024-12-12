from tqdm import tqdm
import functools
import math
import time

@functools.cache
def first_n_digits(num, n):
    return int(num // 10 ** (int(math.log10(num)) - n + 1))

@functools.cache
def last_n_digits(num, n):
    return int(num % (10 ** n))

@functools.cache
def get_num_digits(num):
    return int(math.log10(num))+1



class Stone():
    def __init__(self, value):
        self.value = value
        self.next = None

def add_to_nums(nums, key, value):
    if key not in nums:
        nums[key] = 0
    nums[key] += value

def blink(nums):
    new_nums = {}
    for num in nums:
        if num == 0:
            add_to_nums(new_nums, 1, nums[num])
        elif get_num_digits(num) % 2 == 0:
            midpoint = get_num_digits(num)/2
            left = first_n_digits(num, midpoint)
            right = last_n_digits(num, midpoint)
            add_to_nums(new_nums, left, nums[num])
            add_to_nums(new_nums, right, nums[num])
        else:
            add_to_nums(new_nums, num * 2024, nums[num])

    return new_nums
            

def main():
    input = "8435 234 928434 14 0 7 92446 8992692"
    # input = "125 17"
    stones = [int(x) for x in input.split(" ")]

    nums = {}

    for stone in stones:
        nums[stone] = 1

    curr_length = len(stones)
    for i in range(75):
        nums = blink(nums)

    answer = 0
    for num in nums:
        answer += nums[num]
    print(answer)

main()
