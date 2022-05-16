import numpy as np

caso_de_teste1_numeros_aleatorios = np.array(np.random.randint(0, 1000, 10))

def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid].copy()
        right = lista[mid:].copy()

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              lista[k] = left[i]
              # Move the iterator forward
              i += 1
              
            else:
                lista[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k]=right[j]
            j += 1
            k += 1

        return lista
    
    else:
        return lista
        


print(caso_de_teste1_numeros_aleatorios)
mergeSort(caso_de_teste1_numeros_aleatorios)
print(caso_de_teste1_numeros_aleatorios)



