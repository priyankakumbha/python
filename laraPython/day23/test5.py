import re

p1 = re.compile('abc')
m1 = p1.finditer('abc123abcxyzabchelloabc')
for exp in m1:
	print('search str==>', exp.group(), 'start:', exp.start(), 'end:', exp.end(), )
