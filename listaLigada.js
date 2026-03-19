//Classe nó: Representa cada "item" individual da sua lista
class No{
    constructor(tarefa){ //O construtor recebe a string tarefa
        this.tarefa=tarefa; //Armazena a string(ex: "Estudar JavaScript")
        this.proximo=null; //Por padrão, um novo nó não aponta para ninguém
    }
}

// A classe lista, o construtor inicia a lista vazia, sem cabeça
class ListaDeTarefas{
    constructor(){
        this.cabeca=null; //A lista começa vazia, sem nenhuma tarefa
    }

    // Método Adicionar: Insere uma tarefa sempre no final da corrente
    adicionar(nomeDaTarefa){ 
        const novoNo=new No(nomeDaTarefa); //Cria o novo objeto nó

        //Se a lista estiver vazia (sem cabeça), a nova tarefa vira a cabeça
        if(!this.cabeca){
            this.cabeca=novoNo;
        }
        //Se já houver tarefas, precisamos encontrar a última
        else{
            let atual=this.cabeca;

            //Percorre a lista: enquanto houver um "próximo", a gente pula para ele
            while(atual.proximo){
                atual=atual.proximo;
            }

            //Quando sair do while, 'atual' é o último nó.
            //Agora dizemos que o próximo do último é o nosso novo nó.
            atual.proximo=novoNo;
        }
    } 

    //Método mostrar: Transforma a estrutura de objetos em uma linha legível
    mostrar(){
        let atual=this.cabeca; //Começa do início
        let visual="INÍCIO ->";

        //Diferente do adicionar, aqui vamos ATÉ o null (incluindo o último nó)
        while(atual){
            visual += "[${atual.tarefa}] -> "; //Concatena o texto da tarefa
            atual = atual.proximo; //Move o ponteiro para o próximo item
        }

        //Quando 'atual' for null, o loop para e imprimimos o resultado final
        console.log(visual+"FIM");
    }
}

// --- EXECUÇÃO ---
const minhasTarefas=new ListaDeTarefas();

//Adicionando itens (Cada chamada percorre a lista do início ao fim)
minhasTarefas.adicionar("Estudar JavaScript");
minhasTarefas.adicionar("Entender de funções");
minhasTarefas.adicionar("Criar lista ligada");
minhasTarefas.adicionar("Pausa para descansar");
minhasTarefas.adicionar("Estudar SQL");
minhasTarefas.adicionar("Estudar C++");
minhasTarefas.adicionar("Estudar Azure");
minhasTarefas.adicionar("Estudar Big Data");
minhasTarefas.adicionar("Estudar IA");
minhasTarefas.adicionar("Lanchar");

//Imprime: INÍCIO -> [Estudar JavaScript] -> [Entender de funções] -> [Criar lista ligada]
minhasTarefas.mostrar();