try:
       x=int(input('enter a number: '))
       if x not in range(1,101):
               raise Exception("Out of range")
except Exception as err:
       print (err)
else:
       print (x, "is within the allowed range")