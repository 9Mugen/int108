import re
txt="hello planet heo helo"
x=re.findall("he.+o",txt)
print(x)