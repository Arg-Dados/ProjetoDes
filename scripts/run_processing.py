# scripts/run_processing.py
print("Iniciando o processamento dos dados...")

from data_ingestion import ingest_data
from data_processing import process_chunk, aggregate_results
from data_storage import save_results

if __name__ == '__main__':
    produto_vendas_total = None
    canal_vendas_total = None
    pais_regiao_vendas_total = None
    vendas_mensais_total = None

    for chunk in ingest_data():
        produto_vendas, canal_vendas, pais_regiao_vendas, vendas_mensais = process_chunk(chunk)

        produto_vendas_total = aggregate_results(produto_vendas, produto_vendas_total)
        canal_vendas_total = aggregate_results(canal_vendas, canal_vendas_total)
        pais_regiao_vendas_total = aggregate_results(pais_regiao_vendas, pais_regiao_vendas_total)
        vendas_mensais_total = aggregate_results(vendas_mensais, vendas_mensais_total)

    save_results(produto_vendas_total, canal_vendas_total, pais_regiao_vendas_total, vendas_mensais_total)
    print("Processamento e armazenamento dos dados concluído.")
