import re
pattern = r"colour"
text1 = "My favourite colour is red.I love blue colour."
text2 = re.sub(pattern,"color",text1)
print (text2)