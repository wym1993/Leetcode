def maxWeightPath(mat):

	if not mat or not mat[0]:
		return 0;

	for i in range(1, len(mat)):
		for j in range(len(mat[0])):
			if j==0:
				mat[i][j]+=mat[i-1][j];
			else:
				mat[i][j]+=max(mat[i-1][j], mat[i-1][j-1])

	return max(mat[len(mat)-1])

mat = [[4,2,3,4,1], [2,9,1,10,5], [15, 1, 3, 0, 20], [16, 92, 41, 44, 1], [8, 142, 6, 4, 8]]
print maxWeightPath(mat)