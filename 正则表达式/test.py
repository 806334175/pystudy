import re

string = "pythonp1234ythonpython"

res = re.findall("\d+",string)

print(res[0])