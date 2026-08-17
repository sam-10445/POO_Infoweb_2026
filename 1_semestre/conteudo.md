# POO — 1º Semestre

## Conteúdos

### 01. Revisão de python

Revisou bem por cima o que aviamos visto de python no ano passado.

### 02. Introdução à Poo

- Explicar os conceitos de Entidade, Classificação e Abstração. 
- Introdução a **atributos e métodos** (ex. simples e introdutório de cálculo de triângulo) 

### 03. Criação de classes (sem e com encapsulamento)
### sets e gets

**Muito importante!:** criação de classes, primeiramente, sem encapsuladomento e posteriomente com encapsulamento com sets e gets.

> Introdução a @staticmethod

> Introdução a UI

### 04. Construtores e ToString

Explicação sobre construtores, com foco no __init__ e __str__ (ToString)

### 05. Estrutura básica (em um único arquivo)

1. **Class:** init, set, get, método (cálculo se houver), str (ToString)

2. **UI:** 
- main (op, while, op = UI.menu, if);
- menu (print, op = int(input), return op)
- operações (@staticmethod/classmethod)

3. UI.main()

### 06. Datas, Intervalos e Enumerações

- Datas: **datetime**
- Intervalos: **timedelta**
- Enumerações: **enum**

### 07. Dicionários

Salvar os cadastros com em um arquivo *.json* em formato de dicionário

*(para que não se tenha que fazer os cadastros do zero todas as vezes que rodar o programa)*
> Implementação as operações "def salvar (cls)" e "def abrir (cls)"

### 08. Programação em Camadas

Construção do programa em arquivos diferentes e conectados, por meio de uma Programação em Camadas.

> **Estrutura básica:**
> * class.py *(Objeto)*
> * classdao.py *(Amazenamento das informações)*
> * service.py *(Operações)*
> * ui.py *(Interface do Usuário)*
> 
> *Talvez eu tenha errado a função de alguma camada, por isso é sempre importante olhar no material oficial do GSA*