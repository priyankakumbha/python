import pickle

f1 = open('hello11.ser', 'wb')
i = 20;
j = 40;
pickle.dump(i, f1)
pickle.dump(j, f1)
f1.close()

f2 = open('hello11.ser', 'rb')
x = pickle.load(f2)
y = pickle.load(f2)
f2.close()

print(x);
print(y);
