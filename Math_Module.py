# Number-theoretic and representation functions:
# floor(),fmod(),ceil(),fabs(),factorial(),gcd(),trunc()
import math

# x=12.34
# print(math.floor(x))

x,y=43.50,4.5
print(math.fmod(x,y))
#
# x=12.34
# print(math.ceil(x))

# x=-12
# y=-12.34
# print(math.fabs(x))
# print(math.fabs(y))
#
# x=5
# print(math.factorial(x))
#
# x,y,z=16,12,8
# print(math.gcd(x,y,z))
#
# x=89.76
# print(math.trunc(x))

# Power and Logarithmic functions:
# exp(),log(),log10(),pow(),sqrt()

# print(math.exp(2))
# print(math.log(3))
# print(math.log10(5))
# print(math.pow(2,3))
# print(math.sqrt(16))

# Trignometric functions:
# sin(x),cos(x),tan(x),hypot(x,y)
# print(math.sin(math.radians(30))) # sin 30 degree:1/2
# print(math.cos(math.radians(0)))  # cos 0 degree:1
# print(math.tan(math.radians(45))) # tan 45 degree:1
# print(math.hypot(4,2))

# Angular conversion functions:
# degree(), radians()
# degrees() :- This function is used to convert argument value from radians to degrees.
# radians() :- This function is used to convert argument value from degrees to radians.
# print(math.radians(1)) # 0.017...[Degrees to radians]
# print(math.degrees(1)) # 57.295...Radians to degrees]

# Mathmatical constants
# pi,e,tau,inf
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

print(type(math.pi))
print(type(math.e))
print(type(math.tau))
print(type(math.inf))
print(type(math.nan))