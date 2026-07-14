# Agenda de Contatos

> Agenda de contatos em Python puro, executada via terminal.

## Funcionalidades

- Adicionar novos contatos (nome, telefone e email)
- Visualizar todos os contatos salvos
- Editar nome, telefone ou email de um contato existente
- Marcar ou desmarcar um contato como **favorito**
- Listar apenas os contatos favoritos
- Remover contatos da lista

## Conceitos aplicados

| Conceito | Onde é aplicado |
|---|---|
| Manipulação de listas e dicionários | Cada contato é um dicionário armazenado em uma lista, atualizado pelas funções de edição |
| Modularização | Cada ação (adicionar, editar, favoritar, remover) é isolada em sua própria função |
| Controle de fluxo | Validação de índices e opções do menu com condicionais e tratamento de `ValueError` |

## Como usar

```bash
git clone git@github.com:kxyke/agenda-contatos.git
cd agenda-contatos
python agenda.py
```

Certifique-se de ter o Python instalado. Caso não tenha, baixe em [python.org/downloads](https://www.python.org/downloads/).

O menu no terminal guia pelas opções: adicionar, visualizar, editar, favoritar, listar favoritos, apagar ou sair.

## Tecnologias

- Python 3

## Estrutura do projeto

```
├── agenda.py       # Lógica da agenda e menu do terminal
└── README.md       # Documentação do projeto
```
