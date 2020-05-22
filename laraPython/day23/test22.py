import re

m1 = re.finditer('a?', 'a1aabcaaa234aaaahelloaaaaatest')
for exp in m1:
	print('search str==>', exp.group(), 'start:', exp.start(), 'end:', exp.end(), )
