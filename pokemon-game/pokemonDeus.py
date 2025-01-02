from pokemon import Pokemon

class PokemonDeus(Pokemon):
    tipo = "???"

    def atacar(self, pokemon):
        print("{} lançou um raio de desintegração em {}".format(self, pokemon))
        return super().atacar(pokemon)