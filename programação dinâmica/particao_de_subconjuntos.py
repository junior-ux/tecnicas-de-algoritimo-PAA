# PROBLEMA:

# Determinar se um determinado conjunto pode ser particionado em 2 subconjuntos,
# de modo que a soma dos elementos, em ambos os subconjuntos sejam a mesma.
# Exemplo: [3, 2, 1] subconjunto seria [3] == [2+1]



# Retorna verdadeiro se arr[] puder ser particionado
# em dois subconjuntos de igual soma, caso contrário false
def findPartiion(arr, n):
	Sum = 0

	# Calcula a soma de todos os elementos
	for i in range(n):
		Sum += arr[i]
	if (Sum % 2 != 0):
		return 0
	part = [0] * ((Sum // 2) + 1)

	# Inicializa o part array como 0
	for i in range((Sum // 2) + 1):
		part[i] = 0

	# Preencha a tabela de partição de baixo para cima
	for i in range(n):

		# O elemento a ser incluído na soma não pode ser maior que a soma
		for j in range(Sum // 2, arr[i] - 1, -1):

			# Verifica se soma - arr[i] pode ser formado de um subconjunto usando elementos antes do índice i
			if (part[j - arr[i]] == 1 or j == arr[i]):
				part[j] = 1
	
	# Para imprimir o part
	for i in range(n):
		print(part[i])

	return part[Sum // 2]

# Código da unidade
arr = [3, 2, 1, 3, 1, 14]
n = len(arr)

# Chamada de função
if (findPartiion(arr, n) == 1):
	print("Pode ser dividido em dois subconjuntos de igual soma")
else:
	print("Não pode ser dividido em dois subconjuntos de igual soma")

