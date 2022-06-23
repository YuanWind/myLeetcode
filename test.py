
def generateMatrix(n):
	"""
	:type n: int
	:rtype: List[List[int]]
	"""
	ans = [[0]*n for _ in range(n)]
	i,j = 0,0
	# 左上角为零点，向右为x轴递增，向下为y轴递增，定义方向为：右，下，左，上
	directions = [[0,1],[1,0],[0,-1],[-1,0]] 

	def go(a,direction,table):
		# 从a点坐标按照direction走到b点，返回b点坐标, 超出边界或已经存在值则返回 False
		x = a[0]+direction[0]
		y = a[1]+direction[1]
		if x >= len(table) or y >= len(table[0]):
			return False
		elif table[x][y] != 0:
			return False
		return [x, y]

	location = [0,-1]
	num = 1
	while True:
		for i in range(4):
			flag = True
			while flag:
				flag = go(location, directions[i], ans)
				if flag is not False:
					location = flag
					ans[location[0]][location[1]] = num
					num += 1
				
				if num > n*n:
					break
			if num > n*n:
				break
		if num > n*n:
			break
	return ans

ans = generateMatrix(3)
print(ans)