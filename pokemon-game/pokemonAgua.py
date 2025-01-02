from pokemon import Pokemon

class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, pokemon):
        print("{} lançou um jato d'água em {}".format(self, pokemon))
        return super().atacar(pokemon)