import pandas as pd

def process_chunk(chunk):
    produto_vendas = chunk.groupby('Item Type')['Units Sold'].sum()
    
    chunk['Total Revenue'] = chunk['Units Sold'] * chunk['Unit Price']
    canal_vendas = chunk.groupby('Sales Channel')['Total Revenue'].sum()
    pais_regiao_vendas = chunk.groupby('Country')['Total Revenue'].sum()
    
    chunk['Order Date'] = pd.to_datetime(chunk['Order Date'])
    vendas_mensais = chunk.groupby([chunk['Item Type'], chunk['Order Date'].dt.to_period('M')])['Total Revenue'].mean()

    return produto_vendas, canal_vendas, pais_regiao_vendas, vendas_mensais

def aggregate_results(results, current_totals):
    if current_totals is None:
        return results
    else:
        return current_totals.add(results, fill_value=0)
