let nomeCliente = "Amoeba Contadores LTDA"; //Declarando o nome do cliente
console.log("Iniciando fechamento do cliente: " + nomeCliente); // Imprimindo mensagem com concatenação do nome do cliente

let despesas = ["Aluguel do Escritório", "Energia Elétrica", "Internet", "Folha de Pagamento"]; //Declarando um array com as despesas do escritório

// Função que recebe o nome da despesa como um parâmetro
function registrarNovaDespesa(nomeDespesa) {
    despesas.push(nomeDespesa); // Adiciona no final da lista
    console.log("Nota fiscal registrada com sucesso: " + nomeDespesa); // Imprimindo mensagem de sucesso com concatenação do nome da despesa
}

console.log("Prioridade 1: " + despesas[0]); //Imprimindo a primeira posição do arraay

console.log("Chegaram notas fiscais de última hora. Processando..."); //Imprimindo mensagem de carregamento

// Chamando a função registrarNovaDespesa para adicionar novas despesas
registrarNovaDespesa("Conserto de Impressora");
registrarNovaDespesa("Compra de Toner e Papel");
registrarNovaDespesa("Taxa do Motoboy");

console.log("Atenção: O cliente possui " + despesas.length + " despesas processadas neste mês."); // Imprimindo uma mensagem com o tamanho do array(nº de despesas)
console.table(despesas); //Imprime as despesas em formato de tabela, mostrando os índices