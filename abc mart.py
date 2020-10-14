a = int()
b = int()
c = int()

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            num1 = (100*a)+(10*b)+c
            num2 = (100*c)+(10*c)+a
            result = num1 + num2
            if result == (1000+(100*a)+(10*b)+2):
                print(a, b, c)