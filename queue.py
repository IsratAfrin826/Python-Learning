from collections import deque

bank = deque(["Israt","Asma","Nitu"])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()


if not bank:
    print("No person left")