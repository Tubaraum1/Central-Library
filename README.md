# Central-Library
Este repositório contém um exemplo de refatoração de código seguindo os princípios S.O.L.I.D.
As classes Livro e Usuario foram criadas para representar entidades separadas, isso facilita a manutenção e a compreensão do código, pois cada classe tem uma responsabilidade clara.
Também, a lógica de empréstimo foi separada em uma classe abstrata Emprestimo e sua implementação EmprestimoBiblioteca, podendo novas regras de empréstimo ser facilmente adicionadas e permitindo que diferentes tipos de empréstimos sejam implementados sem alterar a lógica existente.
Outro ponto, foi a devolução é gerenciada por uma classe separada Devolucao, para cada classe lidra com uma única parte da lógica, facilitando a manutenção e testes.
classe BibliotecaApp depende de abstrações em vez de implementações concretas -> Permite que diferentes implementações de empréstimo sejam utilizadas sem modificar a lógica da biblioteca, promovendo um design desacoplado.
