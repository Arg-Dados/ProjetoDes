import pandas as pd
from config import OUTPUT_DIR

def save_results(produto_vendas_total, canal_vendas_total, pais_regiao_vendas_total, vendas_mensais_total):
    print("Salvando resultados...")

    if produto_vendas_total is not None:
        df_produto_canal = pd.DataFrame({
            'Produto': produto_vendas_total.index,
            'Quantidade Vendida': produto_vendas_total.values
        })
        df_produto_canal.to_excel(f'{OUTPUT_DIR}/produto_canal_vendas.xlsx', index=False)
        print("Arquivo produto_canal_vendas.xlsx salvo.")
    
    if canal_vendas_total is not None:
        df_canal_vendas = pd.DataFrame({
            'Canal de Vendas': canal_vendas_total.index,
            'Valor Total de Vendas': canal_vendas_total.values
        })
        df_canal_vendas.to_excel(f'{OUTPUT_DIR}/pais_regiao_vendas.xlsx', index=False)
        print("Arquivo pais_regiao_vendas.xlsx salvo.")
    
    if pais_regiao_vendas_total is not None:
        df_pais_regiao = pd.DataFrame({
            'País/Região': pais_regiao_vendas_total.index,
            'Valor Total de Vendas': pais_regiao_vendas_total.values
        })
        df_pais_regiao.to_excel(f'{OUTPUT_DIR}/vendas_mensais_produto.xlsx', index=False)
        print("Arquivo vendas_mensais_produto.xlsx salvo.")
    
    if vendas_mensais_total is not None:
        df_vendas_mensais = vendas_mensais_total.reset_index()
        df_vendas_mensais.columns = ['Produto', 'Mês', 'Média de Vendas']
        df_vendas_mensais.to_excel(f'{OUTPUT_DIR}/vendas_mensais_produto.xlsx', index=False)
        print("Arquivo vendas_mensais_produto.xlsx salvo.")
