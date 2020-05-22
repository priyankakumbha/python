x = 2
z = 2;
flag = True;
prime_count = 0;
while prime_count < 10:
    while(z <= (x/2)):
        if(x % z == 0):
            flag = False;
            break;
        z += 1

    if flag:
        print(x, end = ',')
        prime_count += 1;

    x += 1
    z = 2;
    flag = True;
