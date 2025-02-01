import re

# Define the regex pattern
pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
pattern2 = "don't\(\)|do\(\)"

# Initialize a list to store matches
matches = []
with open("data.txt", "r") as file:
    for line in file:
        matches.extend(re.findall(pattern, line)) 
        
collector = 0
skip = False
for pair in matches:
    # print(f"{pair[4:pair.index(',')]} : {pair[pair.index(',')+1 : -1]}")
    if "do()" in pair:
        skip = False
    elif "don't()" in pair:
        skip = True
    print(f"{skip = }, {pair}")
    if not skip and "mul" in pair:
        a = int(pair[4:pair.index(',')])
        b = int(pair[pair.index(',')+1 : -1])
        collector += a*b
        
    
print(f"{collector = }")