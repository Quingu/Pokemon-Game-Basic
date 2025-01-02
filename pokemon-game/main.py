import pickle

from pokemon import Pokemon
from pokemonEletrico import PokemonEletrico
from pokemonFogo import PokemonFogo
from pokemonAgua import PokemonAgua
from pessoa import Pessoa
from players import Players
from inimigos import Inimigo
from pokemonDeus import PokemonDeus

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player,arquivo)
            print("Jogo salvo com sucesso")
    except Exception as e:
        print("Erro ao salvar")
        print(e)
        

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso")
            return player
    except Exception as e:
        print("Save não encontrado")
        print(e)
        

def escolher_pokemon_principal(player):
    print("{} você poderá escolher 1 pokemon para te acompanhar em sua jornada, escolha com sabedoria, pois ele será seu parceiro!".format(player))
    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)  
    
    print("Você pode escolher entre esses 3:")
    print("1 -", pikachu)
    print("2 -", charmander)
    print("3 -", squirtle)
    
    while True:
        escolha = input("Escolha seu Pokemon: ")
        
        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha um, senão vai se sentir solitário")
 
if __name__ == "__main__": # = a classe main do java
    
    player = carregar_jogo()
    
    if not player:
        print("-------------------------------------------------------------------") 
        print("Seja bem vindo ao mundo Pokemon, nele você poderá se aventurar e participar de batalhas pokemon")
        print("-------------------------------------------------------------------") 
        nome = input("Antes disso, qual é seu nome? ")
        player = Players(nome)
        print("Olá {} ".format(player))
        player.mostrar_dinheiro()
        print("-------------------------------------------------------------------") 
        
        if player.pokemons:
            print("Vi que você já possui pokemons")
            player.mostrar_pokemons()
        else:
            print("Pelo que parece você não possui nenhum pokemon")
            escolher_pokemon_principal(player)
        print("-------------------------------------------------------------------")   
        print("Que tal como aquecimento você batalhar contra mim? vou pegar leve")
        Deus = Inimigo(nome="Deus", pokemons=[PokemonDeus("Arceus", level=1000)])
        player.batalhar(Deus)
        salvar_jogo(player)
        
    
    while True:
        print("-------------------------------------------------------------------") 
        print("O que você deseja fazer?")
        print("1 - Explorar o mapa")
        print("2 - iniciar uma batalhar")
        print("3 - revanche contra Deus")
        print("4 - Ver Pokedez")
        print("0 - sair do jogo")
        escolha = input("Qual sua escolha?: ")
        print("-------------------------------------------------------------------") 
        
        if escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            print("Certeza? ok,vamos lá")
            Deus = Inimigo(nome="Deus", pokemons=[PokemonDeus("Arceus", level=100)])
            player.batalhar(Deus)
            salvar_jogo(player)
        elif escolha == "4":
            player.mostrar_pokemons()
        elif escolha == "0":
            print("Saindo do jogo...")
            break
        else:
            print("Escolha inválida")
            
    
    
    
    
    
    
    
    """       
    player = Players("Gustavo")
    player.capturar(PokemonEletrico("Pikachu", level=1))
    #escolher_pokemon_principal(player)

    player.mostrar_pokemons()

    inimigo1 = Inimigo(nome="Gary", pokemons=[PokemonFogo("Charmander", level=1)])

    player.batalhar(inimigo1)

    player.explorar()

    player.mostrar_pokemons()
    """
