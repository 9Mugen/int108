import re
mystring = "The alternate email address is victory@ct.com"
match = re.search('(\w+)@(\w+).(\w+)', mystring)
print(match)
if match:
	print("Full match:", match.group())
	print("Group 1:", match.group(1))
	print("Group 2:", match.group(2))
	print("Group 3:", match.group(3))
