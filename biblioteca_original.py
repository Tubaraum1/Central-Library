class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, titulo):
        self.livros.append({'titulo': titulo, 'disponivel': True})

    def registrar_usuario(self, nome):
        self.usuarios.append({'nome': nome})

    def emprestar_livro(self, titulo, usuario_nome):
        for livro in self.livros:
            if livro['titulo'] == titulo and livro['disponivel']:
                livro['disponivel'] = False
                print(f"{usuario_nome} pegou emprestado {titulo}.")
                return
        print(f"{titulo} não está disponível.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro['titulo'] == titulo:
                livro['disponivel'] = True
                print(f"{titulo} foi devolvido.")
                return
        print(f"{titulo} não pertence à biblioteca.")
    
    def listar_livros(self):
        for livro in self.livros:
            status = "Disponível" if livro['disponivel'] else "Indisponível"
            print(f"{livro['titulo']} - {status}")
