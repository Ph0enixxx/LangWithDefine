import re
from conf import conf

file = "test.py"

fp = open(file).readlines()
fp = "".join(fp)
for k,v in conf.items():
	fp = fp.replace(str(k),str(v))
print(fp)