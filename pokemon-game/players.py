import random

from pessoa import Pessoa
from pessoa import POKEMONS

class Players(Pessoa):
    tipo = "player"
    
    def capturar(self, pokemons):
        self.pokemons.append(pokemons)
        print("{} capturou {} com sucesso".format(self, pokemons))
        
        
    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                escolha = int(input("Escolha seu pokemon: "))
                try:
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("Esse jogador não possui nenhum pokemon para ser escolhido!!")
            
            
    def explorar(self):
        if random.random() <=0.3:
            pokemon = random.choice(POKEMONS)
            print("{} apareceu".format(pokemon))
            escolha = input("Você deseja capturar? s/n: ")
            if escolha == "s":
                if random.random() >= 0.3:
                    self.capturar(pokemon)
                else:
                    print("{} fugiu, que pena!!".format(pokemon))
            else:
                print("Boa viagem")
        else:
            print("Essa exploração não deu em nada")