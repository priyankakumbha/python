import re

m1 = re.finditer('\D', 'Java1.8 & Python3.0 are most using versions @ World wide')
for exp in m1:
	print('search str==>', exp.group(), 'start:', exp.start(), 'end:', exp.end(), )
