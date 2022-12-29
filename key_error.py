marks={'Rahul':50, 'Harsh':60,'Suresh':70}
name=input("enter name:")
try:
       print ('marks:',marks[name])
except KeyError:
       print ('name {} not in the list'.format(name))
print ("end of program")