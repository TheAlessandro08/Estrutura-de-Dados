//1. O molde de cada item (Nó)

class No{
    constructor(valor){
        this.valor=valor;
        this.proximo=null;
    }
}

// A estrutura da Lista
class ListaLigada{
    constructor(){
        this.cabeca=null;
        this.tamanho=0;
    }

    //Método para inserir no final
    adicionar(valor){
        const novoNo=new No(valor);

        if(!this.cabeca){
            //Se a lista está vazia, o novo nó vira a cabeça
            this.cabeca=novoNo;
        }else{
            //Se não, percorre até o último
            let atual=this.cabeca;
            while(atual.proximo){
                atual=atual.proximo;
            }
            atual.proximo=novoNo;
        }
        this.tamanho++;
        console.log(`Adicionado: ${valor}`);
    }

    //Método para imprimir a lista de forma visual
    imprimir(){
        if(!this.cabeca){
            console.log("A lista está vazia.");
            return;    
        }

        let atual=this.cabeca;
        let resultado="";

        while(atual){
            resultado+= `${atual.valor} -> `;
            atual=atual.proximo;
        }
        console.log(resultado + "null");
    }
}

// --- TESTANDO O PROGRAMA ---
const minhaLista=new ListaLigada();

minhaLista.adicionar("Café");
minhaLista.adicionar("Código");
minhaLista.adicionar("Sucesso");

console.log("\n--- Estrutura Final ---");
minhaLista.imprimir();
console.log(`Itens totais: ${minhaLista.tamanho}`);