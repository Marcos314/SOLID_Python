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

**A violação do Single Responsibility Principle pode gerar alguns problemas, sendo eles:**

**Falta de coesão** — uma classe não deve assumir responsabilidades que não são suas;
**Alto acoplamento** — Mais responsabilidades geram um maior nível de dependências, deixando o sistema engessado e frágil para alterações;
**Dificuldades na implementação de testes automatizados** — É difícil de “mockar” esse tipo de classe;
**Dificuldades para reaproveitar o código;**

**Exemplos de responsabilidades da função**:
- Obter dados de um banco de dados é uma responsabilidade;
- Filtrar, classificar ou transformar esses dados é outra responsabilidade.
- Armazenar dados é uma responsabilidade diferente.
- O mesmo acontece com a apresentação desses dados ao usuário.

Curiosidades:
**_God Class_**:  Na programação orientada a objetos, é uma classe que sabe demais ou faz demais. O principal problema com um **_God Class_** são suas múltiplas funcionalidades ou responsabilidades concentradas em um único objeto ou classe. 



## Anotações Filipe Deschamps
#### Porque programar dessa forma? (SRP)
- Escopo fechado a escopo fechado para encontrar bugs;

Onde começa e termina a responsabilidade de um determinado componente?
Design prematuro?

## Referências

[The S.O.L.I.D Principles in Pictures](https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898)

Goal: This principle aims to separate behaviours so that if bugs arise as a result of your change, it won’t affect other unrelated behaviours.