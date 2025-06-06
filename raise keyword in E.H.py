def voter(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "you are allowed to vote"

try:
    print (voter(16))
except ValueError as e:
    print(e)