import re
pattern = r"Colour"
if re.match(pattern,"Colour is a colour,I love red colour"):
    print("Match")
else:
    print("Not Matched")
