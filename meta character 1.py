import re
pattern = r"^colo.r$"                     # (dot)(any character)
if re.match(pattern,"colour"):      #^$
    print("Matched")


pattern = r"a*"                           # * (0 or more)
if re.match(pattern,"colour"):
    print("Matched")


pattern = r"a+"                            # + (1 or more)
if re.match(pattern,"a"):
    print("Matched")

pattern = r"ice(-)?cream"                   # ? ( 0 or 1)
if re.match(pattern,"ice-cream"):
    print("Matched")


pattern = r"a{1,3}$"                          # {and}
if re.match(pattern,"aaa"):
    print("Matched")