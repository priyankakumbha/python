x = input('enter a number:')
y = int(x)
z = 2;
Flag = True;
while(z <= (y/2)):
    if(y % z == 0):
        flag = False;
        break;

    z += 1

if flag:
    print(y, "is a prime number")
else:
    print(y, "is not a prime number")
