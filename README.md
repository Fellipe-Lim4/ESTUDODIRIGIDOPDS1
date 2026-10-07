# PDS - Parte 1: Processamento Digital de Sinais

Este repositório contém o estudo dirigido, relatórios, códigos e simulações desenvolvidos para a disciplina de Processamento Digital de Sinais do Instituto Federal da Paraíba (IFPB).

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

* **relatorio/**: Documentação teórica, deduções matemáticas e discussões dos resultados.
* **simulacoes/**: Scripts em Python separados por tópicos fundamentais da disciplina (Sinais, Amostragem, Quantização, Sistemas e Convolução).
* **mini-projeto/**: Simulação completa de um Sistema de Aquisição e Processamento de Sinais aplicado a um Eletrocardiograma (ECG) simplificado.
  * `codigo/`: Script principal do projeto.
  * `dados/`: Datasets gerados pela simulação.
  * `figuras/`: Gráficos comparativos gerados pelo sistema LTI.
* **resultados/**: Imagens e saídas de terminal das simulações menores.

## Dependências

Para executar os códigos contidos na pasta `simulacoes` e `mini-projeto/codigo`, você precisará do Python instalado e das seguintes bibliotecas:
* NumPy
* Matplotlib

Você pode instalá-las rodando:
pip install numpy matplotlib

## Como executar
Basta navegar até a pasta do código desejado e executar com o Python. Exemplo:
python simulacoes/convolucao/filtro_media_movel.py
