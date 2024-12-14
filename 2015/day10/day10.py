import re
from tqdm import tqdm

def process_group(group):
    return str(len(group)) + group[0]


input = '3113322113'

for _ in tqdm(range(51)):
    groups = [m.group(0) for m in re.finditer(r"(\d)\1*", input)]
    new_groups = [process_group(group) for group in groups]
    input = "".join([process_group(group) for group in groups])

print(len(input))


