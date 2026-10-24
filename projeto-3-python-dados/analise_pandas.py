import pandas as pd

df = pd.read_csv("produtos.csv")

print(df)

print("\nProdutos do mais barato ao mais caro:")

print(df.sort_values("preco"))

print("\nProdutos do mais caro ao mais barato:")
print(df.sort_values("preco", ascending=False))

print("\nProdutos com preço maior que R$ 1000:")

print(df[df["preco"] > 1000])

print("\nProdutos da categoria informatica:")
print(df[df["categoria"] == "informatica"])

print("\nQuantidade de produtos por categoria:")
print(df["categoria"].value_counts())

print("\nPreço médio dos produtos:")
print(df["preco"].mean())

print("\nMenor preço:")
print(df["preco"].min())

print("\nProduto mais caro:")
print(df.loc[df["preco"].idxmax()])

print("\nProdutos da categoria eletronicos:")
print(
    df[df["categoria"] == "eletronicos"]
    .sort_values("preco", ascending=False)
)

df.to_csv("produtos_ordenados.csv", index=False)

df[df["categoria"] == "eletronicos"] \
    .sort_values("preco", ascending=False) \
    .to_csv("eletronicos.csv", index=False)