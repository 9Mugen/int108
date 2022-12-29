# Sparse Matrix Representation using lists

def sparseMatrix(sparseMatrix, m, n):
	# initialize size as 0
	size = 0
	for i in range(m):
		for j in range(n):
			if (sparseMatrix[i][j] != 0):
				size += 1

	# number of columns in compressMatrix(size) should
	# be equal to number of non-zero elements in sparseMatrix
	rows, cols = (3, size)
	compressMatrix = [[0 for i in range(cols)] for j in range(rows)]

	k = 0
	for i in range(m):
		for j in range(n):
			if (sparseMatrix[i][j] != 0):
				compressMatrix[0][k] = i
				compressMatrix[1][k] = j
				compressMatrix[2][k] = sparseMatrix[i][j]
				k += 1

	print("Sparse representation:")
	for i in compressMatrix:
		print(i)

m = int(input("Enter row size: "))
n = int(input("Enter col size: "))
print("Enter elements:")
mat = [[int(input()) for x in range (n)] for y in range(m)]
print("Sparse matrix is:")
for i in range(m):
	for j in range(n):
		print(mat[i][j],end = " ")
	print()
sparseMatrix(mat, m, n)
