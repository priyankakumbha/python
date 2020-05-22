import re;
p = re.compile('\s')
m = p.finditer('ab1aba&bab')
for i in m:
	print(i.start(), i.group())