x = [10, 200, 15, 35, 40, 200, 150, 40, 65];
print(x)

def calculateRemainder(a):
    return a % 2

for b in x:
    if(calculateRemainder(b) == 0):
        print(b, "is even")
    else:
        print(b, "is odd")
