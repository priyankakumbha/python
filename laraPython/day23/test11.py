import re

m1 = re.finditer('[a-ir-y]', 'java and python languages')
for exp in m1:
	print('search str==>', exp.group(), 'start:', exp.start(), 'end:', exp.end(), )
