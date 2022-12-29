import os.path

if os.path.isfile("myfile1.txt"):
    print("myfile.txt exists")
else:
    print("myfile.txt does not exists")
# os.rename("myfile1.txt","newname1.txt")
# os.remove("newname1.txt")