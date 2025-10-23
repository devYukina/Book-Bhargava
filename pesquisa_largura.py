from collections import deque

def pessoa_e_vendedor(nome):
    return nome.endswith('m')

def pesquisa(nome):
    fila = deque()
    fila += grafo[nome]
    visitados = []

    while fila:
        pessoa = fila.popleft()
        if pessoa not in visitados:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de manga!")
                return True
            else:
                fila += grafo[pessoa]
                visitados.append(pessoa)
    return False

grafo = {
    "voce": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

pesquisa("voce")
