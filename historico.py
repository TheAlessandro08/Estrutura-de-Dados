historico=[]

def visitar_pagina(url):
    print(f"Visitando: {url}")
    historico.append(url)

def botao_voltar():
    if len(historico)>1:
        pagina_atual=historico.pop()
        print(f"<- Voltando de: {pagina_atual}")
        print(f"Agora você está em: {historico[-1]}")
    else:
        print("! Não há mais páginas para voltar.")

visitar_pagina("google.com")
visitar_pagina("youtube.com/JorgimGameplays")
visitar_pagina("github.com/TheAlessandro08")

print(f"\nHistórico atual (Pilha): {historico}\n")

botao_voltar()
botao_voltar()
    