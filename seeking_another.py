obj=open("Demo.txt","w+")
obj.write("Hello World")
obj.seek(3) #Move to 4th Byte
print(obj.tell()) #Gives the byte number(in terms of index
print(obj.read())
obj.seek(2,0)#Move 2 bytes further from beginning(0[First character at 0]+2=2)
print(obj.read())
obj.close()
obj=open("Demo.txt","rb")
obj.seek(1)
obj.seek(5,1)#Move 5 bytes further from current position[1[Currently at 2nd byte]+5=6]
print(obj.read().decode("utf-8"))
obj.seek(3)
obj.seek(-2,1)#Move 2 bytes back from current position
print(obj.read().decode("utf-8"))
obj.seek(-3,2) #Move 3 bytes backward[Reference position is from end]
print(obj.read().decode("utf-8"))