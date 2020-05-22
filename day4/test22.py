for a in range(10):
    print('outer begin', a)
    flag = False
    for b in range(15, 18):
        print('inner',a, b);
        if b == 16:
            flag = True;
            break;
        print('inner end', a, b);
    print('outer end',a)
    if flag:
        break
