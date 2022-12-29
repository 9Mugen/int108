a=[10,20,30,40,50]
try:
       x=int(input('enter index: '))
       print ('number at index {} is {}'.format(x,a[x]))
except IndexError:
       print ("index is out of range")
except ValueError:
       print ("index should be an integer")