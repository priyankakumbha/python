for i in range(10):
    print('outer loop begin:', i);
    for j in range (15,20):
        print('inner loop', i, j)
    print('outer loop begin:', i);
    print('outer loop end:', i);
print('done');
