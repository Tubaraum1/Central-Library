from abc import ABC, abstractmethod

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True

class Usuario:
    def __init__(self, nome):
        self.nome = nome

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

class Emprestimo(ABC):
    @abstractmethod
    def emprestar(self, titulo, usuario):
        pass

class EmprestimoBiblioteca(Emprestimo):
    def emprestar(self, titulo, usuario):
        for livro in biblioteca.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"{usuario.nome} pegou emprestado {titulo}.")
                return
        print(f"{titulo} não está disponível.")

class Devolucao:
    @staticmethod
    def devolver(biblioteca: Biblioteca, titulo):
        for livro in biblioteca.livros:
            if livro.titulo == titulo:
                livro.disponivel = True
                print(f"{titulo} foi devolvido.")
                return
        print(f"{titulo} não pertence à biblioteca.")

class BibliotecaApp:
    def __init__(self, biblioteca: Biblioteca, emprestimo: Emprestimo):
        self.biblioteca = biblioteca
        self.emprestimo = emprestimo

    def listar_livros(self):
        for livro in self.biblioteca.livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"{livro.titulo} - {status}")

biblioteca = Biblioteca()
emprestimo = EmprestimoBiblioteca(biblioteca)
biblioteca_app = BibliotecaApp(biblioteca, emprestimo)

livro1 = Livro("1984")
livro2 = Livro("Brave New World")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

usuario1 = Usuario("Alice")
biblioteca.registrar_usuario(usuario1)

biblioteca_app.listar_livros()
emprestimo.emprestar("1984", usuario1)
biblioteca_app.listar_livros()
Devolucao.devolver(biblioteca, "1984")
biblioteca_app.listar_livros()
