import re

p1 = re.compile('a')
m1 = p1.finditer('abcahelloatesta123')
for exp in m1:
	print('start:', exp.start(), 'end:', exp.end(), 'search str:', exp.group())
