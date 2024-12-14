import re

pwd = 'hepxcrrq'
pwd_chars = [char for char in pwd]

alpha = 'abcdefghijklmnopqrstuvwxyz'
triplets = set()
for i in range(len(alpha) - 2):
    triplets.add(alpha[i: i+3])

def find_next(pwd):
    is_valid = False
    while not is_valid:
        for i in range(7, -1, -1):
            if pwd_chars[i] == 'z':
                pwd_chars[i] = 'a'
                continue
            pwd_chars[i] = alpha[alpha.index(pwd_chars[i]) + 1] 
            break
        pwd = "".join(pwd_chars)

        has_triplet = False
        for i in range(5):
            if pwd[i: i + 3] in triplets:
                has_triplet = True
                break
        
        has_bad_char = False
        if 'i' in pwd or 'o' in pwd or 'l' in pwd:
            has_bad_char = True

        has_repeats = False
        if len(re.findall(r'(\w)\1', pwd)) > 1:
            has_repeats = True

        if has_triplet and not has_bad_char and has_repeats:
            is_valid = True 

    return pwd
    
print(find_next(pwd))
print(find_next(pwd))
