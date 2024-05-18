# ETL em Python

## Descrição
Este projeto de ETL (Extract, Transform, Load) em Python extrai dados de arquivos Excel em uma pasta, transforma-os e carrega-os em um novo arquivo Excel.

### Processo ETL

1. **Extração (Extract):**
   - Os dados são extraídos dos arquivos Excel na pasta especificada usando a biblioteca `glob`.

2. **Transformação (Transform):**
   - Adiciona uma coluna com o nome do arquivo de origem.
   - Adiciona uma coluna com a localização, determinada pelo nome do arquivo.
   - Extrai o nome da campanha da coluna `utm_link` e adiciona uma nova coluna com este nome.
   - Combina todos os DataFrames em um único DataFrame.

3. **Carregamento (Load):**
   - Salva o DataFrame resultante em um novo arquivo Excel na pasta de saída.

## Tecnologias Utilizadas
- Python
- Pandas
- os
- glob

## Estrutura do Projeto
- **src/**: Pasta principal do projeto
  - **data/**: Pasta para os arquivos de entrada e saída
    - **raw/**: Contém os arquivos Excel de entrada
    - **ready/**: Onde o arquivo Excel resultante será salvo
  - **main.py**: Script Python com o código do ETL

## Execução do Projeto
1. Coloque os arquivos Excel de entrada em `data/raw`.
2. Execute o script `main.py`.
3. Certifique-se de ter permissão de escrita em `data/ready` para salvar o arquivo resultante.

## Observações
Este é um exemplo simples de um processo ETL em Python e pode ser expandido conforme necessário para atender a requisitos adicionais.

