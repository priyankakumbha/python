import json
data1 = [10, "abc", True]
data2 = (10, "abc", False, None)
data3 = {"k1": "Hello", "k2": "java", "k3": 100, "k4": False, "k5": None}
print(type(data1), data1);
print(type(data2), data2);
print(type(data3), data3);
print("-------------")
with open('d3.json', 'w') as f1:
	json.dump(data1, f1);
	json.dump(data2, f1);
	json.dump(data3, f1);

with open('d3.json', 'r') as f2:
	x = json.load(f2);
print(type(x), x);
