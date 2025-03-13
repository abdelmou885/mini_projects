#First solution
n = int(input())
y = 0

for _ in range(n):
    x = input().strip()

    if "++" in x:
        y += 1
    elif "--" in x:
        y -= 1

print(y)
# Second solution
n = int(input())
y = 0

for _ in range(n):
    x = input().strip()

    if "++" in x:
        y += 1
    elif "--" in x:
        y -= 1

print(y)