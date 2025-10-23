def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return None

numeros = [1, 3, 5, 7, 9]
print(busca_linear(numeros, 3))  # Saída: 1
print(busca_linear(numeros, -1)) # Saída: None
