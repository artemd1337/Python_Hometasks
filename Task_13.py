a = ["let", "me", "die"]
b = ["z", "x", "c"]

for i in range(len(a)):
    print(i, (a[i], b[i]))

for elem in enumerate(zip(a, b)):
    print(*elem)
