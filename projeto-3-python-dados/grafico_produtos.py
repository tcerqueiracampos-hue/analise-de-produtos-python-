import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("produtos.csv")

categorias = df.groupby("categoria")["preco"].sum()

plt.bar(categorias.index, categorias.values, color="hotpink")
for i, valor in enumerate(categorias.values):
    plt.text(i, valor, f"{valor:,.0f}", ha="center", va="bottom")

plt.xlabel("Categoria")
plt.ylabel("Valor Total")
plt.title("Valor Total por Categoria")
plt.savefig("grafico_produtos.png", dpi=300, bbox_inches="tight")
plt.show()