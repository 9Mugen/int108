try:
   print("outer try block")
   print(10/0)
   try:
       print("Inner try block")
   except ZeroDivisionError:
       print("Inner except block")
   finally:
       print("Inner finally block")
except:
   print("outer except block")
finally:
   print("outer finally block")