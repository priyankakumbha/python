import re
s1 = "hello abc and how is abc and what about the abc in the year 700";
print(s1)
r1 = re.findall('abc', s1);
print(r1)
for item in r1:
	print(item);


