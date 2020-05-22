x = int(input("Enter First Number"))
y = int(input("Enter Second Number"))
z = 2
flag = True;
prime_count = 0;
while x < y:
    while(z <= (x/2)):
        if(x % z == 0):
            flag = False;
            break;
        z += 1

    if flag:
        print(x, end = ',')

    x += 1
    z = 2;
    flag = True;
