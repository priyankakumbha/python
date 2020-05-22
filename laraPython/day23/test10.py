import re

m1 = re.finditer('[a-p]', 'java and python languages')
for exp in m1:
	print('search str==>', exp.group(), 'start:', exp.start(), 'end:', exp.end(), )
