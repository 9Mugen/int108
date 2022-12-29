import random
# choice(seq) - This function returns a random element from the non-empty sequence.
# If seq is empty, interpreter raises an IndexError.

# seq = "abcdefghijklmn"
# seq1=[1,2,3,4]
# print(random.choice(seq)) # will print result as follows
# print(random.choice(seq1))

#shuffle(list) - This functions returns shuffled list.
# L1 = [10, 20, 2, 3, 1]
# random.shuffle(L1)
# print (L1) # will print result as follows

# randint(a, b) - This function returns a random integer between a and b inclusive
# print(random.randint(1, 5))


# seed() - This function always returns the same random value.

# for i in range(10):
# 	random.seed(20)
# 	print(random.randint(1, 1000))

# random() -using random() get the next random number in the range (0.0, 1.0)
# means a random float value f, such that 0 is less than or equal to f
# and f is less than 1.

#print(random.random())

# randrange(start, stop, step) - This function returns random values in the given
# sequence based on step.

# print(random.randrange(2, 10))
# print(random.randrange(2, 10, 4))