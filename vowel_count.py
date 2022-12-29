count=0
obj=open("source.txt","w")
str1=input("Enter file data...")
obj.write(str1)
obj.close()
obj=open("source.txt","r")
data=obj.read()
for char in data:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        count+=1
obj.close()
obj=open("Target.txt","w")
obj.write(str(count))


