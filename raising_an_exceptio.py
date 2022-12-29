def checkage(age):
	if age < 0:
		raise ValueError("invalid age","please enter positive age")
	print("age is valid")
try:
	age = int(input("age: "))
	checkage(age)
except ValueError as err:
	print(" ".join(err.args))
finally:
	print("executed in any condition")