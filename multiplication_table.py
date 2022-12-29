import random
num=random.randint(1,9)
obj=open("multiplication.txt","w")
for i in range(1,11):
    result=num*i
    value=str(num)+"X"+str(i)+"="+str(result)
    obj.write(value)
    obj.write("\n")
obj.close()
obj=open("multiplication.txt","r")
print(obj.read())