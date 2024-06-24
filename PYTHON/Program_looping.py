# For Loop (Perulangan)
print("For Loop:")
name = ["ridho", "chelly", "adam"]
for name in name:
    print(name)

# While Loop (Perulangan memiliki kondisi agar bisa berjalan terus)
print("While Loop:")
x = 0
while x < 11:
    print(x)
    x += 1

# Nested Loop (Perulangan yang tedapat perulangan lagi)
print("Nested Loop:")
for y in range(1, 11):
    for x in range(1, 11):
        for z in range(1, 11):
            print(f"({x}, {y}, {z})")

# Loop with Break (Perulangan yang dapat di hentian secara paksa sesuai statement yang di inginkan)
print("Loop Break:")
for x in range(1, 6):
    if x == 6:
        break
    print(x)

# Loop with Continue
print("Loop Continue:")
for x in range(1, 11):
    if x == 11:
        continue
    print(x)

# Loop with Else
print("Loop Else:")
for x in range(1, 6):
    print(x)
else:
    print("Loop selesai")