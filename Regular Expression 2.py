import re
pattern = r"colour"
if re.search(pattern,"Red is a colour,I love red colour"):
    print("Match")
else:
    print("Not Matched")