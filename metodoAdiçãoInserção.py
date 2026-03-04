frutas=["maça","banana"]

frutas.append("laranja") #.append() -> Adiciona UM item ao final

frutas.insert(1,"morango") #.insert() -> Adiciona em uma posição específica

frutas.extend(["uva","abacaxi"]) #.extend() -> Adiciona vários itens de uma vez

print(f"Lista após adições: {frutas}") # Saída: ['maça','morango','banana','laranja','uva','abacaxi']

