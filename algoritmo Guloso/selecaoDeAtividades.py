# ALGORITMO GULOSO

# É um paradigma algorítmico que constrói uma solução peça por peça, 
# sempre escolhendo a próxima peça que oferece o benefício mais óbvio 
# e imediato. Algoritmos gulosos são usados ​​para problemas de otimização

# PROBLEMA

# O Problema de Seleção de Atividades é um problema de 
# otimização que lida com a seleção de atividades não 
# conflitantes que precisam ser executadas por uma única 
# pessoa ou máquina em um determinado período de tempo.

# COMPLEXIDADE

# O(N log N)

# CÓDIGO
def MaxActivities(arr, n):
	selected = []

	# Classifica os trabalhos de acordo com a hora de término
	Activity.sort(key=lambda x: x[1])

	# A primeira atividade sempre é selecionada
	i = 0
	selected.append(arr[i])

	for j in range(1, n):

		# Se esta atividade tiver horário de início maior ou
        # igual ao tempo de término do selecionado anteriormente
        # atividade, então selecione-a'''
		if arr[j][0] >= arr[i][1]:
			selected.append(arr[j])
			i = j
	return selected


# Código
if __name__ == '__main__':
	Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
	n = len(Activity)
	
	selected = MaxActivities(Activity, n)
	print("Seguintes atividades são selecionadas :")
	print(selected[0], end = "");
	for i in range (1, len(selected)):
		print(",", end = " ")
		print(selected[i], end = "")
