import re

m1 = re.finditer('[a-i2-7]', 'java8 and python3 are most using versions in 2020 ')
for exp in m1:
	print('search str==>', exp.group(), 'start:', exp.start(), 'end:', exp.end(), )
