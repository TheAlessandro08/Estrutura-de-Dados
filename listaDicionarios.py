usuarios=[
    {"nome":"alice","idade":25},
    {"nome":"pedro","idade":12},
    {"nome":"ANA","idade":30},
]

usuarios.append({"nome":"Beto","idade":12})

print("--- Usuários Maiores de Idade ---") 
for u in usuarios:
    nome_limpo=u["nome"].strip().title()

    if u["idade"] >= 18:
        print(f"Nome: {nome_limpo} | Idade: {u['idade']}")

print(f"\nTotal de cadastros: {len(usuarios)}")