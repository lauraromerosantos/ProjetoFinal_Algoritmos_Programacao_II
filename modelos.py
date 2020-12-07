class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas

vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
birdbox = Filme ('Bird Box', 2018, 124 )
bly = Serie('A Maldição da Mansão Bly', 2020, 1)
interestelar = Filme('Interestelar', 2014, 169)
crown = Serie('The Crown', 2016, 4)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
interestelar.dar_likes()
interestelar.dar_likes()
bly.dar_likes()
bly.dar_likes()
birdbox.dar_likes()
birdbox.dar_likes()
birdbox.dar_likes()
crown.dar_likes()
crown.dar_likes()

listinha = [bly, vingadores, interestelar, birdbox, crown]
minha_playlist = Playlist('fim de semana', listinha)
print('_'*60)
print('Playlist da Laura - Fim de Semana')
print('*'*60)
for programa in minha_playlist:
    print(programa)
print('*'*60)
print(f'Tamanho da playlist: {len(minha_playlist.listagem)}')
print('_'*60)
