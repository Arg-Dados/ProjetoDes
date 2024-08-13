# Projeto de Processamento de Dados de Grande Volume

## Visão Geral

O objetivo deste projeto é avaliar suas habilidades em manipular e analisar grandes volumes de dados em Python, de forma eficiente e com consumo otimizado de recursos.

Você receberá um arquivo CSV de grande porte, denominado `vendas.csv`, com cerca de 5GB. O arquivo contém dados de vendas de uma cadeia de varejo. As colunas incluem: Data, Produto, Quantidade, Preço_Unitário, e Loja.

## Instruções para Implementação

1. **Leitura Eficiente dos Dados**:
   - Implemente uma solução para ler o arquivo `vendas.csv` de forma eficiente, considerando o grande volume de dados.
   - Utilize técnicas como leitura em partes (chunking) para garantir que o processamento possa ser realizado em uma máquina com memória limitada.

2. **Identificação do Produto Mais Vendido**:
   - Determine qual produto foi o mais vendido em termos de quantidade e canal de vendas.

3. **Determinação do Maior Volume de Vendas por País e Região**:
   - Identifique qual país e região teve o maior volume de vendas (em valor).

4. **Cálculo da Média de Vendas Mensais por Produto**:
   - Calcule a média de vendas mensais por produto, considerando o período dos dados disponíveis.

## Requisitos

- A solução deve ser capaz de rodar em uma máquina com memória limitada, sem carregar o arquivo inteiro na memória de uma vez.
- O uso de bibliotecas como Pandas é permitido e recomendado, especialmente com o recurso de leitura em chunks.
- Priorize a eficiência do processamento e o uso otimizado de recursos.
- Documente o código adequadamente e inclua comentários explicativos sobre suas escolhas de implementação.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **`config.py`**: Contém as configurações e variáveis globais, como os caminhos dos arquivos.
- **`data_ingestion.py`**: Responsável pela ingestão dos dados em chunks.
- **`data_processing.py`**: Realiza o processamento dos dados, como agregações e cálculos.
- **`data_storage.py`**: Gerencia o armazenamento dos resultados processados em arquivos Excel.
- **`utils/`**: Diretório que contém funções auxiliares para operações com arquivos e banco de dados.
  - **`file_utils.py`**: Funções para manipulação de arquivos.
  - **`db_utils.py`**: Funções para interação com bancos de dados.
- **`scripts/`**: Diretório que contém os scripts de automação do pipeline.
  - **`__main__.py`**: Script principal que executa a ingestão e o processamento dos dados.
- **`outfiles/`**: Diretório onde os arquivos de saída (Excel) são armazenados após o processamento.
- **`README.md`**: Este arquivo de documentação.
- **`requirements.txt`**: Lista de dependências do projeto.

## Requisitos de Software

Certifique-se de ter o Python 3 instalado e as seguintes bibliotecas Python:

- **Pandas**

Para instalar as dependências, execute o comando:

```bash
pip install -r requirements.txt
