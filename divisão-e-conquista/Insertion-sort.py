
def insertionSort(arr):
 
    # percorre o array elemento por elemento
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Mover elementos da matriz [0..i-1], que são
        # maior que a chave, para uma posição à frente
        # da sua posição actual
        j = i-1 # Volta ao elemento anterior para comparar com os anteriores 
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key # Atribue o valor de troca de posição temporariamente

arr = [12, 11, 13, 5, 6] # array a ser testado acima
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
