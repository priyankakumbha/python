import json
data = [{"firstName": "Vijay", 
		"lastName": "B",
		"age": 22,
		"weight": 55.6,
		"address": {
			"houseNo": "123/M",
			"streetName": "BTM"
			},
		"city": "Bangalore"
		},
		{"firstName": "Mohan", 
		"lastName": "BTM",
		"age": 24,
		"weight": 65.6,
		"address": {
			"houseNo": "125/N",
			"streetName": "JPN"
			},
		"city": "Bangalore"
		}]
print(type(data), data);
print(type(data[0]), data[0]);
print("-------------")
with open('d2.json', 'w') as f1:
	json.dump(data, f1);

with open('d2.json', 'r') as f2:
	x = json.load(f2);
print(type(x), x);
print(type(x[0]), x[0]);


