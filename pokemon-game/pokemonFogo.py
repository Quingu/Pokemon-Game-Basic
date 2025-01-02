from pokemon import Pokemon

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabeça de {}".format(self, pokemon))
        return super().atacar(pokemon)