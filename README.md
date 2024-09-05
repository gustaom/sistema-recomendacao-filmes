# Sistema de Recomendação de Filmes

Este projeto implementa um sistema de recomendação de filmes com base em conteúdo. O sistema utiliza dados de filmes e avaliações para sugerir filmes aos usuários com base em suas preferências.

## Funcionalidades

- **Recomendação baseada em similaridade de conteúdo**: Utiliza a similaridade de gêneros dos filmes para sugerir títulos.
- **Exploração de dados**: Análise dos dados de filmes e avaliações para melhor entendimento do conjunto de dados.

## Estrutura do Projeto

├── data/ # Diretório contendo os datasets 
  ├── movies.dat # Arquivo com dados dos filmes 
  │ └── ratings.dat # Arquivo com dados de avaliações 
├── src/ # Diretório contendo scripts de processamento de dados 
  ├── load_data.py # Funções para carregar e processar os dados 
  ├── explore_data.py # Funções para explorar os dados 
  │ └── recommendation.py # Funções para gerar recomendações de filmes 
├── main.py # Script principal para executar o sistema de recomendação


## Instruções para Executar o Projeto

### Pré-requisitos

- Python 3.x
- Bibliotecas listadas em `requirements.txt`

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/gustaom/sistema-recomendacao-filmes.git
   cd sistema-recomendacao-filmes
   ```
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Executando o Sistema
Carregue os dados de filmes e avaliações e faça as recomendações:
```bash
python main.py
