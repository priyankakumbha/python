for i in range(10):
    print('loop begin:', i);
    if i > 5:
        continue;
    print('loop middle:', i);
    print('loop end:', i);
print('done');
