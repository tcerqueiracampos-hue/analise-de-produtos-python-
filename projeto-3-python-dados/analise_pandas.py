import pandas as pd

# Lendo os dados
df = pd.read_csv("produtos.csv")


# Função para formatar valores em reais
def formatar_reais(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# Cabeçalho
print("\n" + "=" * 48)
print("              ANÁLISE DE PRODUTOS")
print("=" * 48)


# Visualização dos produtos
print("\n[ TODOS OS PRODUTOS ]")
print(df.to_string(index=False))


# Ordenação
print("\n[ PRODUTOS DO MAIS BARATO AO MAIS CARO ]")
print(df.sort_values("preco").to_string(index=False))

print("\n[ PRODUTOS DO MAIS CARO AO MAIS BARATO ]")
print(df.sort_values("preco", ascending=False).to_string(index=False))


# Filtros
print("\n[ PRODUTOS ACIMA DE R$ 1.000 ]")
print(df[df["preco"] > 1000].to_string(index=False))

print("\n[ PRODUTOS DE INFORMÁTICA ]")
print(df[df["categoria"] == "informatica"].to_string(index=False))

print("\n[ PRODUTOS ELETRÔNICOS ]")
eletronicos = df[df["categoria"] == "eletronicos"]
print(eletronicos.sort_values("preco", ascending=False).to_string(index=False))


# Quantidade por categoria
print("\n[ QUANTIDADE POR CATEGORIA ]")
print(df["categoria"].value_counts().to_string())


# Resumo financeiro
print("\n" + "=" * 48)
print("              RESUMO DOS PRODUTOS")
print("=" * 48)

print(f"\n  Média dos preços:       {formatar_reais(df['preco'].mean())}")
print(f"  Maior preço:            {formatar_reais(df['preco'].max())}")
print(f"  Menor preço:            {formatar_reais(df['preco'].min())}")
print(f"  Quantidade de produtos: {df['preco'].count()}")

produto_mais_caro = df.loc[df["preco"].idxmax()]

print(f"\n  Produto mais caro:      {produto_mais_caro['nome']}")

print("=" * 48)


# Exportação dos arquivos CSV
df.sort_values("preco").to_csv("produtos_ordenados.csv", index=False)

eletronicos.sort_values("preco", ascending=False).to_csv(
    "eletronicos.csv",
    index=False
)
print("\n[ PREÇO MÉDIO POR CATEGORIA ]")

print(
    df.groupby("categoria")["preco"].mean()
)
print("\n[ VALOR TOTAL POR CATEGORIA ]")

print(
    df.groupby("categoria")["preco"].sum()
)

print("\n[ RESUMO POR CATEGORIA ]")

print(
    df.groupby("categoria")["preco"].agg(
        ["count", "mean", "sum", "max", "min"]
    )
)

print("\n[ CATEGORIAS POR VALOR TOTAL ]")

print(
    df.groupby("categoria")["preco"]
    .sum()
    .sort_values(ascending=False)
)
print("\nArquivos CSV exportados com sucesso!")