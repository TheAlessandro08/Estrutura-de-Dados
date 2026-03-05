class Musica:
    def __init__(self,nome):
        self.nome=nome
        self.proxima=None

class Playlist:
    def __init__(self):
        self.primeira=None

    def adicionar_musica(self,nome):

        nova=Musica(nome)

        nova.proxima=self.primeira

        self.primeira=nova
        print(f"♫ {nome} adicionada à playlist!")

    def toccar_proxima(self):

        if self.primeira is None:
            print("🎧 A playlist está vazia.")
            return

        tocando=self.primeira.nome
        print(f"▶️ Tocando agora: {tocando}")

        self.primeira=self.primeira.proxima 
    
    def mostrar_fila(self):
        atual=self.primeira
        print("\n--- FILA ATUAL ---")
        while atual:
            print(f"Track: {atual.nome}")
            atual=atual.proxima
        print("----------------\n")

minha_vibe=Playlist()
minha_vibe.adicionar_musica("Red Hot Chilli Peppers")
minha_vibe.adicionar_musica("D-Devils - 6th Gate")
minha_vibe.adicionar_musica("ABBA - Dancing Queen")
minha_vibe.mostrar_fila()


