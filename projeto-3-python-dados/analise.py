arquivo = open("produtos.csv", "r")

linhas = arquivo.readlines()

produtos = [linhas[i].split(",") for i in range(1, len(linhas))]

for i in range(len(produtos)):
    produtos[i] = {
        "nome": produtos[i][0],
        "preco": int(produtos[i][1]),
        "categoria": produtos[i][2].strip()
    }

print(produtos[3]["nome"],
      produtos[3]["preco"],
      produtos[3]["categoria"])

for produto in produtos:
    if produto["categoria"] == "eletronicos":
        print(f"Nome: {produto['nome']} | Preço: R${produto['preco']}")


def calcular_total(produtos):
    print("Calculando o total dos produtos...")
    total = 0

    for produto in produtos:
        total += produto["preco"]
    return total

print("Total dos produtos:", f"R$ {calcular_total(produtos)}")

def calcular_media(produtos):
    print("Calculando a média dos produtos...")
    total = calcular_total(produtos)
    media = total / len(produtos)
    return media

print("Média dos produtos:", f"R$ {calcular_media(produtos)}")

arquivo.close()