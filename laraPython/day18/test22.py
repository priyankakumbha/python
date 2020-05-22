import json
with open('data.json') as f1:
	s1 = json.load(f1)
print(s1);
print(s1['emp']);
print(s1['emp'][0]);
print(s1['emp'][1]);
print(s1['country']);
