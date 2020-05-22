a = 10
while a < 20:
    print('outer loop begin')
    b = 50
    while b <= 52:
        print('inner loop',a , b)
        b += 1
        print('inner loop begin')
        print('inner loop end')
        a += 1

print('done')
