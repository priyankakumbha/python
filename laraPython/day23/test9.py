import re

m1 = re.finditer('[abcz3]', 'abc123abcxyzabchelloabc')
for exp in m1:
	print('search str==>', exp.group(), 'start:', exp.start(), 'end:', exp.end(), )
