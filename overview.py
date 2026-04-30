"""
Object Oriented Programming é uma forma de programar baseada em construir objetos que podem contem dados e códigos
Beneficios: Escalabilidade, Eficiencia e Reusabilidade.

Oque são objetos?
    Há varios objetos ao nosso redor: arvores, casas, meus gatos...

Todos os objetos precisam ter atributos e metodos
Atributos: oque é
Metodos: oque faz

Ex:
class Dog:
    legs: int = 4
    ears: int = 2
    type: str = 'Goldendoodle'
    age: int = 5
    color: str = 'blue'

Há 4 pilares que devem ser aprendidos em OOP:
    - Encapsulation
    - Abstraction
    - Inheritance
    - Polymorphism


Abstraction:
    - Pensar como uma lampada que acende e desliga a luz. Nós não nos importamos como a luz liga e desliga dentro da lam
    pada apenas sabemos do seu estado atual

Constructors:
    - São chamadas as classes que executam ou não valores iniciais: def __init__(self): é um exemplo de contructor que
    ao chamar a classe, é executado o init

Encapsulation:
    - Classificar se as variaveis são publicas ou privadas. Para transformar uma variavel em privada usasse o self.__no
    me_variavel se tornando impossivel a alteração do valor. Mas para alterar é usado Setters encapsulation e visualizar
    Getters encapsulation.

Inheritance:
    - Herdar os metodos e atributos de uma classe. Parent class > Child class.
    Method override:
        - Quando existe 2 metodos iguais no Parent e Child a funcao executada sera do Child
    Method overriding:
        - Quando a Child class ja tem seu proprio metodo

Self vs Super:
    - Self usado para definir as variaveis da propria classe
    - Super usado para definir as variaveis da parent classe

Polymorphism:
    - Ter metodos iguais em cada Child class para cada um ter sua particularidade


POST - Metodo
    - usado para criar dados
    - deve ter um Body para adição dos dados, GET não deve
PUT - Metodo
    - usado para criar dados
    - pode ter um Body para adição dos dados, GET não deve

Oque é Pydantics?
    - É uma biblioteca de validação de dados, usada para criar modelos de dados e validar os dados de entrada em APIs. Ele é usado para garantir que os dados recebidos em
    uma API estejam no formato correto e atendam aos requisitos especificados.
    Ele é amplamente utilizado em frameworks como FastAPI para facilitar a criação de APIs robustas e seguras.
"""