import re
list = ["abc", "xyz", "test", 500, "month"]
s1 = "hello abc and how is xyz and what about the test in the year 500?";
for item in list:
	m1 = re.search(str(item), s1)
	if m1:
		print(item, "found with ", m1)
	else:
		print(item, ' not found');


