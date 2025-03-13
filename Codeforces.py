n = int(input())
z = 0
for _ in range(n):
    y=0
    x = input()
    for i in x:
        if i == "1":
            y += 1
    if y > 1:
        z += 1
print(z)



