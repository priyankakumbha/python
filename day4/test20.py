for a in range(10):
    print('outer', a)
    for b in range(15, 18):
        print('inner',a, b);
        if b == 16:
            continue;
            print('outer end',a)
