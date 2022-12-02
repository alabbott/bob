import re

# Define the regex pattern
pattern = r"(\d+) (?:calories|pounds) (?:of|from) (a|an|\d+)\s(\w+)"

# Extract the relevant information from the sentence
sentence = ""
match = re.search(pattern, sentence)
if match:
    amount = int(match.group(1))
    unit = match.group(2)
    food = match.group(3)
    print(f"{amount} {unit}")
    print(f"{food}")
    # Output:
    # 300 calories
    # a banana