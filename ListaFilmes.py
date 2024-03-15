#Descrição do Exercício a ser solucionado.
#- Implemente uma lista circular com nomes de filmes a qual tenha as seguintes características:
#	- Alocação de memória dinâmica para os filmes inseridos
#	- Uma função de busca de filmes por nomes
#	- Contagem da quantidade de filmes presentes na lista
#	- Remoção de filmes
#	- Adição de filmes
#	- O último filme aponta para o primeiro filme da lista.
#Resolução do Exercício  - Codificação: 
class Filme:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class ListaCircularFilmes:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.quantidade = 0

    def adicionar_filme(self, nome):
        novo_filme = Filme(nome)
        if self.quantidade == 0:
            self.primeiro = novo_filme
            novo_filme.proximo = novo_filme  # O último aponta para o primeiro
        else:
            novo_filme.proximo = self.primeiro
            self.ultimo.proximo = novo_filme
        self.ultimo = novo_filme
        self.quantidade += 1

    def remover_filme(self, nome):
        if self.quantidade == 0:
            return

        filme_atual = self.primeiro
        filme_anterior = None

        while filme_atual.nome != nome:
            filme_anterior = filme_atual
            filme_atual = filme_atual.proximo
            if filme_atual == self.primeiro:
                return

        if filme_anterior:
            filme_anterior.proximo = filme_atual.proximo
            if filme_atual == self.primeiro:
                self.primeiro = filme_atual.proximo
            if filme_atual == self.ultimo:
                self.ultimo = filme_anterior
        else:
            self.primeiro = filme_atual.proximo
            self.ultimo.proximo = self.primeiro

        self.quantidade -= 1

    def buscar_filme(self, nome):
        if self.quantidade == 0:
            return None

        filme_atual = self.primeiro

        while filme_atual.nome != nome:
            filme_atual = filme_atual.proximo
            if filme_atual == self.primeiro:
                return None

        return filme_atual

    def contar_filmes(self):
        return self.quantidade

    def listar_filmes(self):
        if self.quantidade == 0:
            return

        filme_atual = self.primeiro

        for _ in range(self.quantidade):
            print(filme_atual.nome)
            filme_atual = filme_atual.proximo

# Exemplo de uso:
lista_filmes = ListaCircularFilmes()
lista_filmes.adicionar_filme("Avangers")
lista_filmes.adicionar_filme("Sherk")
lista_filmes.adicionar_filme("Jujutsu Kaisen")

print("Lista de filmes:")
lista_filmes.listar_filmes()

print(f"Quantidade de filmes: {lista_filmes.contar_filmes()}")

filme_buscado = lista_filmes.buscar_filme("Sherk")
if filme_buscado:
    print(f"Filme encontrado: {filme_buscado.nome}")

lista_filmes.remover_filme("Sherk")
print("Lista de filmes após a remoção:")
lista_filmes.listar_filmes()

#Descrição da aprendizagem obtida através do exercicío :
#Com este exercicío eu aprendi mais sobre a alocação de memória dinâmica. 
#Como o ponteiro funciona, quando o último elemento da lista aponta para o primeiro.
#Sobre métodos tambem quando ele adiciona filmes, remove filmes, busca filmes por nome, conta a quantidade de filmes na lista e lista os filmes.
#Sobre manipulação de lista em como ele adiciona elementos a uma lista circular, remove elementos dela e procura por elementos específicos.
