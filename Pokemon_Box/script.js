const API_URL = "https://pokeapi.co/api/v2/pokemon";
const root = document.getElementById("root");
const form = document.getElementById("addPokemonForm");
// Dicionário de tradução dos tipos
const traducoesTipos = {
  normal: "normal",
  fire: "fogo",
  water: "agua",
  electric: "eletrico",
  grass: "planta",
  ice: "gelo",
  fighting: "lutador",
  poison: "venenoso",
  ground: "terra",
  flying: "voador",
  psychic: "psiquico",
  bug: "inseto",
  rock: "pedra",
  ghost: "fantasma",
  dragon: "dragao",
  dark: "sombrio",
  steel: "aço",
  fairy: "fada"
};

// Variáveis para controlar as caixas
let currentBox = null;
let pokemonCount = 0;
const POKEMON_PER_BOX = 30; // Limite de 6x5

// Função para criar uma nova caixa com o background
function createNewBox() {
  const box = document.createElement("div");
  box.className = "pokemon-box";
  root.appendChild(box);
  return box;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  
  // Converte para minúsculo para evitar erros na PokeAPI (ex: "Pikachu" falharia, "pikachu" funciona)
  const pokemonName = document.getElementById("pokemonName").value.toLowerCase().trim();

  fetch(`${API_URL}/${pokemonName}`)
    .then((response) => {
      if (!response.ok) throw new Error("Pokémon não encontrado!");
      return response.json();
    })
    .then((newPokemon) => {
      // Se for o primeiro Pokémon ou se a caixa atual já tem 30, cria uma nova caixa
      if (pokemonCount % POKEMON_PER_BOX === 0) {
        currentBox = createNewBox();
      }

      // Criação dos elementos da carta
      const div = document.createElement("div");
      const image = document.createElement("img");
      const name = document.createElement("h1");
      
      // NOVO: Container para os tipos
      const typesContainer = document.createElement("div");
      typesContainer.className = "types";

      div.className = "card";
      
      image.src = newPokemon.sprites.other['official-artwork'].front_default || newPokemon.sprites.front_default;
      name.textContent = newPokemon.name;
      
      // NOVO: Loop para pegar cada tipo do Pokémon na API
      // Loop para pegar cada tipo do Pokémon na API
      newPokemon.types.forEach((typeInfo) => {
        const typeSpan = document.createElement("span");
        
        // Pega o nome do tipo em inglês direto da API (ex: "fire")
        const tipoEmIngles = typeInfo.type.name;
        
        // Busca a tradução no nosso dicionário. 
        // O || tipoEmIngles é um "fallback": se a API adicionar um tipo novo que não tá no dicionário, ele mostra em inglês para não quebrar.
        const tipoEmPortugues = traducoesTipos[tipoEmIngles] || tipoEmIngles;

        // Mantém a CLASSE em inglês para o CSS pintar com a cor certa
        typeSpan.className = `type ${tipoEmIngles}`; 
        
        // Exibe o TEXTO na tela em português
        typeSpan.textContent = tipoEmPortugues; 
        
        typesContainer.appendChild(typeSpan);
      });
      
      // Inserindo na ordem: imagem, nome, e depois as tipagens
      div.appendChild(image);
      div.appendChild(name);
      div.appendChild(typesContainer); // NOVO
      
      currentBox.appendChild(div);
      pokemonCount++;
      document.getElementById("pokemonName").value = "";
    })
});