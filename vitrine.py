TAMANHOS = ("PP", "P", "M", "G", "GG")

vitrine = [
    {"nome": "Camiseta básica", "preco": 39.90, "tamanho": "M"},
    {"nome": "Calça jeans", "preco": 129.90, "tamanho": "G"},
    {"nome": "Moletom", "preco": 159.90, "tamanho": "P"},
]

carrinho = [("Camiseta básica", 3), ("Calça jeans", 1)]

preco = {}
for produto in vitrine:
    preco[produto["nome"]] = produto["preco"]

total = 0
for nome, quantidade in carrinho:
    total = total + preco[nome] * quantidade

print("Peças na vitrine:", len(vitrine))
print("Total do carrinho: R$", round(total, 2))

print(vitrine[1]["preco"])
print(TAMANHOS[-1])
print(len(carrinho))
print(preco["Moletom"] * 2)