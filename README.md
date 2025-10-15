# Sistema de Gestão de Reservas de Hotel com Git e GitHub
Projeto que aplica práticas de controle de versões no desenvolvimento de um sistema simples em Python para gerir reservas, quartos e clientes."
# gestao-hotel-git

## Autora
- Ana Luiza Dornas

## Descrição Geral
Este projeto consiste na criação de um sistema simples em Python para gerir reservas, quartos e clientes de um hotel, com foco na organização com Git e GitHub.

## Funções Principais do Sistema
- Registo e listagem de clientes.
- Gestão de quartos (disponíveis/ocupados).
- Criação e cancelamento de reservas.

# Relatório do Projeto

## Organização do Trabalho
Trabalhei criando branches por funcionalidade (clientes, quartos, reservas) implementando o código em etapas e integrando com merges.

## Problemas e Conflitos
O main local estava desatualizado, e os commits de quartos estavam em main.

Erro de importação em reservas.py devido à ausência de funções em quartos.py.

Conflito em quartos.py entre feature-reservas e main na função listar_quartos.

Necessidade de tratar casos de quartos ocupados em reservas.py.

Mensagem de saudacao não aparecia devido a falta de aplicacao da correcao em app.py.

Ajustes de imports entre módulos (corrigidos verificando a ordem de importação e caminhos).


## Resolução com Git
Recriei manualmente os commits em feature-quartos e fiz push.

Recriei manualmente as funções em quartos.py em feature-quartos e fiz push.

Usei git merge para detectar os conflitos, editei manualmente quartos.py para combinar as versões de listar_quartos e finalizei o merge.

Modifiquei reservas.py em feature-reservas para exibir 'Quarto ocupado' e fiz push.

Garanti a inclusao de saudacao em app.py e fiz push da correcao.

Usei git merge para integrar branches e editei manualmente os arquivos necessários.

Criei tag v1.0 com git tag -a v1.0 -m "Versão final" e git push origin v1.0.


