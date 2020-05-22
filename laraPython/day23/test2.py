import re

p1 = re.compile('a')
print(type(p1))
m1 = p1.finditer('abcahelloatesta123')
print(type(m1))
for exp in m1:
	print(exp.start())
	print(type(m1))
	print('-----')
