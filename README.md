# Projeto Final - Algoritmos e Programação II - 2020/2

## Requisito - Projeto Final
O projeto terá um requisito obrigatório: **Orientação a Objetos** e conceitos que a integram **(classe, objeto, atributos, Herança, Polimorfismo, Encapsulamento).**

## Proposta - Projeto Final
A ideia deste projeto é criar uma aplicação que tenha um controle de playlist dos programa de TV (filmes, séries e documentários).

A classe Filme terá o inicializador “init" que recebe "self", e também terá outros atributos: nome, ano e duração. A classe Série, por sua vez, irá possuir nome, ano e temporadas. Também será criado um método com a utilidade de dar like aos filmes e séries, sem receber parâmetros e que, no fim, adicionará +1 à contagem de likes.

Para isso será aplicado o conceito de herança visto em aula onde será criado uma classe que representará a ideia genérica, que será a classe Programa, já que irá conter programas de TV. Todo programa de TV terá nome, ano e likes. A herança na verdade é uma ligação que essas classes terão, e que vão representar que Filme contém informações do programa, porque ele herdará Programa. Da mesma forma, Série terá informações do mesmo.

Será utilizado o encapsulamento para proteger o atributo nome do Filme ou Série e para proteger os likes. Os elementos que não precisam de proteção, sem nenhuma lógica, ficarão públicos.

Também será utilizado o conceito de polimorfismo para criar a playlist de programas que terá terá um nome específico, temático ou não, uma lista de forma ordenada e seu tamanho.

Além disso, será utilizado property ao invés de métodos getters e setters, por que se não todos os lugares que já acessam a classe iriam precisar mudar.

Para realizar este projeto será utilizado a linguagem Python, que foi estudada durante este semestre devido a familiaridade e facilidade com esta linguagem. 
