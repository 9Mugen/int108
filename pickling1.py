import pickle

animalDict = { 'Cat': 2, 'Dog': 7, 'Lion': 4, 'Tiger': 9, 'Leopard': 11, 'Bear': 8, 'Elephant': 15 }
outfile = open('animals','wb')
pickle.dump(animalDict, outfile)
outfile.close()
fst = open("animals", 'rb')				# Open the file as input binary
data = pickle.load(fst)			         # Read the first record
try:					# The Endof file is indicated as EOFError exception, we need to catch this exception
   while(True):
    print(data)
    data = pickle.load(fst)
except:
   print("Bye")