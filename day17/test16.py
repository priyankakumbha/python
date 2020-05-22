print(1)
try:
    print(2)
    y = 10 / 0
    x = 20
    print(3)

except:
    print("except begin", x)
    print("except end")

print(4, x)
