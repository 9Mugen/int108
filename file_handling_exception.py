try:
   fh = open("testfile1.txt", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("File already existing-->Change the file name")
else:
   print("Content written successfully")