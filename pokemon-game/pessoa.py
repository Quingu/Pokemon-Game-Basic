import random

from pokemon import Pokemon
from pokemonEletrico import PokemonEletrico
from pokemonFogo import PokemonFogo
from pokemonAgua import PokemonAgua
from pokemonDeus import PokemonDeus

NOMES = [
    "Ash Ketchum", "Misty", "Brock", "Professor Oak", "Tracey Sketchit",
    "May", "Max", "Dawn", "Serena", "Clemont",
    "Bonnie", "Lillie", "Kiawe", "Sophocles", "Mallow",
    "Gladion", "Professor Kukui", "Nessa", "Leon", "Hop"
]

POKEMONS = [
    # Pokémon do tipo Fogo
    PokemonFogo("Charmander"), PokemonFogo("Flareon"), PokemonFogo("Charmeleon"),
    PokemonFogo("Vulpix"), PokemonFogo("Ninetales"), PokemonFogo("Growlithe"),
    PokemonFogo("Arcanine"), PokemonFogo("Ponyta"), PokemonFogo("Rapidash"),
    PokemonFogo("Magmar"), PokemonFogo("Cyndaquil"), PokemonFogo("Quilava"),
    PokemonFogo("Typhlosion"), PokemonFogo("Torchic"), PokemonFogo("Combusken"),
    PokemonFogo("Blaziken"), PokemonFogo("Torkoal"), PokemonFogo("Chimchar"),
    PokemonFogo("Monferno"), PokemonFogo("Infernape"),

    # Pokémon do tipo Elétrico
    PokemonEletrico("Pikachu"), PokemonEletrico("Raichu"), PokemonEletrico("Magnemite"),
    PokemonEletrico("Magneton"), PokemonEletrico("Electabuzz"), PokemonEletrico("Jolteon"),
    PokemonEletrico("Zapdos"), PokemonEletrico("Chinchou"), PokemonEletrico("Lanturn"),
    PokemonEletrico("Mareep"), PokemonEletrico("Flaaffy"), PokemonEletrico("Ampharos"),
    PokemonEletrico("Elekid"), PokemonEletrico("Raikou"), PokemonEletrico("Manectric"),
    PokemonEletrico("Plusle"), PokemonEletrico("Minun"), PokemonEletrico("Shinx"),
    PokemonEletrico("Luxio"), PokemonEletrico("Luxray"),

    # Pokémon do tipo Água
    PokemonAgua("Squirtle"), PokemonAgua("Magikarp"), PokemonAgua("Wartortle"),
    PokemonAgua("Blastoise"), PokemonAgua("Psyduck"), PokemonAgua("Golduck"),
    PokemonAgua("Poliwag"), PokemonAgua("Poliwhirl"), PokemonAgua("Poliwrath"),
    PokemonAgua("Tentacool"), PokemonAgua("Tentacruel"), PokemonAgua("Slowpoke"),
    PokemonAgua("Slowbro"), PokemonAgua("Seel"), PokemonAgua("Dewgong"),
    PokemonAgua("Shellder"), PokemonAgua("Cloyster"), PokemonAgua("Horsea"),
    PokemonAgua("Seadra"), PokemonAgua("Lapras"),
    
    PokemonDeus("Arceus")
]

class Pessoa:
    
    def __init__(self,nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES) 
            
        
        self.pokemons = pokemons
        
        self.dinheiro = dinheiro
        
    
    def __str__(self):
        return self.nome
    
    
    def mostrar_pokemons(self):
        if self.pokemons:
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não possui nem pokemon, capture!".format(self))
    
            
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Esse jogador não possui nenhum pokemon para ser escolhido!!")
            
            
    def mostrar_dinheiro(self):
        print("Você possui ${}".format(self.dinheiro))
            
            
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("você ganhou ${}".format(quantidade))
        self.mostrar_dinheiro()
           
            
    def batalhar(self, pessoa):
        print("_________________")
        print("{} iniciou uma batalha com {}".format(self, pessoa))
        print("_________________")
        print("{} tem um: ".format(pessoa))
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
        print("_________________")
        seu_pokemon = self.escolher_pokemon()
        if seu_pokemon and pokemon_inimigo:
            while True:
                vitoria = seu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(seu_pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    break
        else:
            print("Essa batalha não pode ocorrer")
        