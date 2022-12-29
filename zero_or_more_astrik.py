import re
txt="hello helo planet heo"
x=re.findall("he.*o",txt)
print(x)