import re
s1 = "hello abc and how is abc and what about the abc in the year 700";
print(s1)
r1 = re.match('hello', s1);
print(r1)
r2 = re.match('abc', s1);
print(r2)


