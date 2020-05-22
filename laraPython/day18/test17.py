import pickle

f1 = open('hello10.ser', 'wb')
i = 20;
pickle.dump(i, f1)
f1.close()

f2 = open('hello10.ser', 'rb')
j = pickle.load(f2)
f2.close()

print(j);
