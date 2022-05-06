# S.O.L.I.D

* S: Single Responsability Principle
* O: Open-Closed Principle
* L: Liskov Substitution Principle
* I: Interface Segregation Principle
* D: Dependency Inversion Principle

****

## Single Responsabily Principle (SRP)

- Especialização de classes;
- Possuir apenas uma "responsabilidade" dentro do software;

**Exemplos de responsabilidades da função**
- Obter dados de um banco de dados é uma responsabilidade;
- Filtrar, classificar ou transformar esses dados é outra responsabilidade.
- Armazenar dados é uma responsabilidade diferente.
- O mesmo acontece com a apresentação desses dados ao usuário.
  
**A violação do Single Responsibility Principle pode gerar alguns problemas, sendo eles:**

- **Falta de coesão** — uma classe não deve assumir responsabilidades que não são suas;
- **Alto acoplamento** — Mais responsabilidades geram um maior nível de dependências, deixando o sistema engessado e frágil para alterações;
- **Dificuldades na implementação de testes automatizados** — É difícil de “mockar” esse tipo de classe;
- **Dificuldades para reaproveitar o código.**


**Meta**
Esse princípio visa separar comportamentos para que, se surgirem *bugs* como resultado de alguma alteração no código, isso não afete outros comportamentos não relacionados.

*"Um módulo deve ser responsável por um e apenas um, ator."*
...
*"Um módulo é apenas um conjunto coeso de funções e estruturas de dados."* 
**Bob Martin**

## Open-Closed Principle (OCP)

*"Classes, entidades ou funções devem ser abertas para extensão, mas fechadas para modificação"*


Para facilitar o entendimento, podemos fazer uma comparação com a instalação de um plugin em nosso navegador. A instalação do mesmo não vai modificar o código do navegador em si, vai apenas adicionar uma nova funcionalidade ao navegador.
Nesse exemplo o navegador está aberto (OPEN) para novas funcionalidades, mas o binário do navegador está fechado (CLOSED) para modificações.
- Exemplos
  - Plugins
  - ORMs

**Meta**
Este princípio visa estender o comportamento de uma classe sem alterar o comportamento existente dessa classe. Isso é para evitar causar bugs onde quer que a classe esteja sendo usada.


*"A essência é que para sistemas de software, para serem fáceis de mudar, eles devem ser projetados para permitir o comportamento desses sistemas a serem alterados pela adição de novo código, em vez de alterar o código existente."*
**Bom Martim**

## Liskov Substitution Principle (LSP)

Respeitar o LSP força o seu programa a ter as abstrações no nível certo e ser mais consistente.

## Interface Segregation Principle (ISP)

## Dependency Inversion Principle (DIP)


## Referências

[The S.O.L.I.D Principles in Pictures](https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898)
