import re
s1 = "hello abc and how is abc and what about the abc in the year 700";
words = re.split('\s', s1)
for word in words:
	print(word)


