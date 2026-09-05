produtos = [
    {"nome": "Notebook", "preco": 2500.00, "categoria": "informatica"},
    {"nome": "PC", "preco": 8500.00, "categoria": "eletronicos"},
    {"nome": "livro", "preco": 23.00, "categoria": "papelaria"},
    {"nome": "blush", "preco": 15.99, "categoria": "beleza"},
    {"nome": "colar", "preco": 20.55, "categoria": "acessórios"},
    {"nome": "Mouse", "preco": 120.00, "categoria": "informatica"},
    {"nome": "Teclado", "preco": 180.00, "categoria": "informatica"},
    {"nome": "Celular", "preco": 3200.00, "categoria": "eletronicos"},
    {"nome": "Caderno", "preco": 35.00, "categoria": "papelaria"},
    {"nome": "Batom", "preco": 28.00, "categoria": "beleza"}

]
# contar produtos acima de R$ 500
contador = 0

for produto in produtos:
    print(produto["nome"], produto["preco"])

    if produto["preco"] > 500:
        print("Produto acima de R$ 500:", produto["nome"], produto["preco"])

        contador += 1

print("Quantidade de produtos acima de R$ 500:", contador)

# calcular o total dos produtos
def calcular_total(produtos):
    print("Calculando o total dos produtos...")
    total = 0

    for produto in produtos:
        total += produto["preco"]
    return total

print("Total dos produtos:", calcular_total(produtos))

# calcular a média dos produtos
def calcular_media(produtos):
    print("Calculando a média dos produtos...")
    total = calcular_total(produtos)
    media = total / len(produtos)
    return media

print("Média dos produtos:", calcular_media(produtos))

# encontrar o produto mais caro
def encontrar_maior_produto(produtos):
    print("Encontrando o produto mais caro...")
    maior_produto = produtos[0]

    for produto in produtos:
        if produto["preco"] > maior_produto["preco"]:
            maior_produto = produto
    return maior_produto

maior = encontrar_maior_produto(produtos)
print("Produto mais caro:", maior["nome"], maior["preco"])

# encontrar o produto mais barato
def encontrar_menor_produto(produtos):
    print("Encontrando o produto mais barato...")
    menor_produto = produtos[0]

    for produto in produtos:
        if produto["preco"] < menor_produto["preco"]:
            menor_produto = produto
    return menor_produto

menor = encontrar_menor_produto(produtos)
print("Produto mais barato:", menor["nome"], menor["preco"])

# calcular a quantidade de produtos por categoria
categorias = {
 produto["categoria"]: 0 for produto in produtos
}

for produto in produtos:
    categorias[produto["categoria"]] += 1

print("Quantidade de produtos por categoria:")
for categoria, quantidade in categorias.items():
    print(f"{categoria}: {quantidade}")

# preço por produto
precos_por_produto = {
    produto["nome"]: produto["preco"] for produto in produtos
}

print("preços pro produto:")
for nome, preco in precos_por_produto.items():
    print(f"{nome}: R$ {preco:.2f}")

# somar os preços por categoria
soma_por_categoria = {
    categoria: sum(produto["preco"] for produto in produtos if produto["categoria"] == categoria)
    for categoria in categorias
}
print("Soma dos preços por categoria:")
for categoria, soma in soma_por_categoria.items():
    print(f"{categoria}: R$ {soma:.2f}")

# calcular a quantidade de produtos por categoria
quantidade_por_categoria = {
    categoria: sum(1 for produto in produtos if produto["categoria"] == categoria)
    for categoria in categorias
}
print("Quantidade de produtos por categoria:")
for categoria, quantidade in quantidade_por_categoria.items():
    print(f"{categoria}: {quantidade}")

# calcular a média dos preços por categoria
media_por_categoria = {
    categoria: (soma_por_categoria[categoria] / quantidade_por_categoria[categoria]) 
     if quantidade_por_categoria[categoria] > 0 else 0
    for categoria in categorias
}
print("Média dos preços por categoria:")
for categoria, media in media_por_categoria.items():
    print(f"{categoria}: R$ {media:.2f}")

# encontrar produtos com preço acima da média
print("\nProdutos com preço acima da média:")
media_geral = calcular_media(produtos)
for produto in produtos:
    if produto["preco"] > media_geral:
        print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

# Encontrar a categoria com a maior média de preço
categoria_vencedora = None
maior_media = 0

for categoria, media in media_por_categoria.items():
    if media > maior_media:
        maior_media = media
        categoria_vencedora = categoria

print(f"\nCategoria com a maior média de preço: {categoria_vencedora} (R$ {maior_media:.2f})")
