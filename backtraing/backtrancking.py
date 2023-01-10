# Tamanho do labirinto
n = 4

# Uma função utilitária para verificar se x, y é válido
# índice para N * N do labirinto


def isValid(n, maze, x, y, res):
	if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
		return True
	return False

# Uma função de utilidade recursiva para resolver o problema do labirinto

def RatMaze(n, maze, move_x, move_y, x, y, res):
	# se (x, y é o objetivo) retorna Verdadeiro
	if x == n-1 and y == n-1:
		return True
	for i in range(4):
		# Gerar novo valor de x
		x_new = x + move_x[i]

		# Gerar novo valor de y
		y_new = y + move_y[i]

		# Verifique se maze[x][y] é válido
		if isValid(n, maze, x_new, y_new, res):

			# marque x, y como parte do caminho da solução
			res[x_new][y_new] = 1
			if RatMaze(n, maze, move_x, move_y, x_new, y_new, res):
				return True
			res[x_new][y_new] = 0
	return False


def solveMaze(maze):
	# Criando uma lista 4 * 4 2-D
	res = [[0 for i in range(n)] for i in range(n)]
	res[0][0] = 1

	# matriz x para cada direção
	move_x = [-1, 1, 0, 0]

	# matriz y para cada direção
	move_y = [0, 0, -1, 1]

	if RatMaze(n, maze, move_x, move_y, 0, 0, res):
		for i in range(n):
			for j in range(n):
				print(res[i][j], end=' ')
			print()
	else:
		print('A solução não existe')


# Programa de driver para testar a função acima
if __name__ == "__main__":
	# inicializando o labirinto
	maze = [[1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1]]

	solveMaze(maze)
