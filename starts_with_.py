import re
txt="hello planet"
x=re.findall("^hello",txt)
print(x)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")