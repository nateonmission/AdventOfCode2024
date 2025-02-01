import re



# Define the regex pattern
pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)")
collector = 0
skip = False

# Initialize a list to store matches
matches = []
with open("data.txt", "r") as file:
    for line in file:
        for match in pattern.finditer(line):
            pair = match.group() 
            # print(f"{pair[4:pair.index(',')]} : {pair[pair.index(',')+1 : -1]}")
            if "do()" in pair:
                skip = False
            elif "don't()" in pair:
                skip = True
            elif not skip and pair.startswith("mul"):
                start = pair.index('(') + 1
                mid = pair.index(',')
                end = pair.index(')')
                a, b = int(pair[start:mid]), int(pair[mid+1:end])
                collector += a*b
        
    
print(f"{collector = }")