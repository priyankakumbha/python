import re
s1='hello abc 123 abc';
print('source:', s1)
m1 = re.search('abc', s1)
print(m1)
