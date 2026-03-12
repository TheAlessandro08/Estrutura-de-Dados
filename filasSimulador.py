from collections import deque
import time

class SistemaLogistico:
    def __init__(self):        
        self.fila_pedidos=deque()
        self.historico_concluido=deque(maxlen=5) 
    
    def receber_pedido(self,id_pedido,cliente):
        """Adiciona um novo pedido ao final da fila (Enqueue)"""
        print(f"RECEBIDO: Pedido {id_pedido} - Cliente: {cliente}")
        self.fila_pedidos.append({"id": id_pedido, "cliente": cliente, "status": "Pendente"})

    def processar_proximo(self):
        """Remove e processa o primeiro pedido da fila (Dequeue)"""
        if not self.fila_pedidos:
            print("Fila vazia. Nenhum pedido para processar.")
            return
        
        #popleft() garante performance 0(1)
        pedido=self.fila_pedidos.popleft()
        print(f"PROCESSANDO: Separando itens do pedido {pedido['id']}...")

        #Simulando um tempo de processamento
        time.sleep(0.5)

        pedido["status"]="Enviado"
        self.historico_concluido.append(pedido)
        print(f"CONCLUÍDO: Pedido {pedido['id']} enviado para {pedido['cliente']}!")

    def mostrar_status(self):
        print(f"\n--- STATUS DO SISTEMA ---")
        print(f"Pedidos aguardando: {len(self.fila_pedidos)}")
        if self.fila_pedidos:
            print(f"Próximo da fila: {self.fila_pedidos[0]['id']}")
        print(f"Últimos enviados: {[p['id'] for p in self.historico_concluido]}")
        print("-" * 25 + "\n")

# --- Executando a Simulação ---

logistica=SistemaLogistico()

# 1. Chegada de pedidos
logistica.receber_pedido("001","Alice")
logistica.receber_pedido("002","Bob")
logistica.receber_pedido("003","Carlos")

logistica.mostrar_status()

# 2. Iniciando o processamento
logistica.processar_proximo()
logistica.processar_proximo()

# 3. Chega mais um pedido enquanto processamos
logistica.receber_pedido("004","Diana")

logistica.mostrar_status()

# 4. Finalizando o que restou
logistica.processar_proximo()
logistica.processar_proximo()
