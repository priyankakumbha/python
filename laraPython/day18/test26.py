import json
data1 = [10, "abc", True]
data2 = (10, "abc", False, None)
data3 = {"k1": "Hello", "k2": "java", "k3": 100, "k4": False, "k5": None}
data4 = [data1, data2, data3];
print(type(data1), data1);
print(type(data2), data2);
print(type(data3), data3);
print(type(data4), data4);
print("-------------")
with open('d4.json', 'w') as f1:
	json.dump(data4, f1);

with open('d4.json', 'r') as f2:
	x = json.load(f2);
print(type(x), x);
print(type(x[0]), x[0]);
print(type(x[1]), x[1]);
print(type(x[2]), x[2]);
