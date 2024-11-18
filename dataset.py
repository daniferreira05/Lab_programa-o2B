import csv
import numpy as np
import pandas as pd

# Dados fornecidos
dados = [
    ["2024-02-20", "Sul", "Produto B", 1, 71.8, 71.8],
    ["2024-02-09", "Norte", "Produto B", 13, 10.19, 132.47],
    ["2024-02-09", "Oeste", "Produto C", 19, 76.88, 1460.72],
    ["2024-02-26", "Leste", "Produto B", 20, 55.72, 1114.4],
    ["2024-02-02", "Norte", "Produto A", 17, 31.28, 531.76],
    ["2024-03-21", "Sul", "Produto A", 10, 78.51, 785.1],
    ["2024-03-28", "Leste", "Produto C", 7, 81.88, 573.16],
    ["2024-01-04", "Leste", "Produto A", 1, 72.4, 72.4],
    ["2024-02-21", "Sul", "Produto B", 18, 21.01, 378.18],
    ["2024-02-02", "Oeste", "Produto C", 4, 76.65, 306.6],
    ["2024-03-11", "Oeste", "Produto A", 9, 53.19, 478.71],
    ["2024-02-17", "Leste", "Produto B", 6, 33.08, 198.48],
    ["2024-03-05", "Leste", "Produto B", 15, 17.12, 256.8],
    ["2024-01-29", "Sul", "Produto C", 11, 82.58, 908.38],
    ["2024-03-17", "Norte", "Produto C", 20, 83.41, 1668.2],
    ["2024-02-13", "Norte", "Produto C", 16, 11.96, 191.36],
    ["2024-03-06", "Oeste", "Produto B", 1, 84.84, 84.84],
    ["2024-02-07", "Sul", "Produto C", 17, 74.98, 1274.66],
    ["2024-01-02", "Sul", "Produto A", 17, 32.44, 551.48],
    ["2024-03-09", "Oeste", "Produto C", 5, 34.66, 173.3],
    ["2024-03-19", "Leste", "Produto C", 7, 38.42, 268.94],
    ["2024-02-01", "Norte", "Produto A", 17, 25.81, 438.77],
    ["2024-02-04", "Sul", "Produto B", 11, 20.93, 230.23],
    ["2024-02-19", "Norte", "Produto A", 12, 44.55, 534.6],
    ["2024-03-15", "Norte", "Produto B", 8, 91.92, 735.36],
    ["2024-01-01", "Leste", "Produto A", 5, 43.98, 219.9],
    ["2024-02-02", "Norte", "Produto A", 15, 53.19, 797.85],
    ["2024-01-13", "Oeste", "Produto A", 20, 61.16, 1223.2],
    ["2024-02-28", "Leste", "Produto A", 4, 13.56, 54.24],
    ["2024-03-17", "Oeste", "Produto A", 16, 61.35, 981.6],
    ["2024-01-22", "Norte", "Produto B", 12, 86.85, 1042.2],
    ["2024-02-22", "Leste", "Produto A", 16, 51.42, 822.72],
    ["2024-01-10", "Sul", "Produto A", 17, 82.49, 1402.33],
    ["2024-01-27", "Leste", "Produto B", 11, 52.95, 582.45],
    ["2024-03-04", "Sul", "Produto A", 2, 38.05, 76.1],
    ["2024-03-30", "Norte", "Produto C", 5, 73.39, 366.95],
    ["2024-02-15", "Oeste", "Produto B", 17, 14.46, 245.82],
    ["2024-02-20", "Leste", "Produto A", 16, 58.57, 937.12],
    ["2024-02-21", "Oeste", "Produto B", 13, 68.7, 893.1],
    ["2024-02-03", "Norte", "Produto A", 14, 25.2, 352.8],
    ["2024-01-31", "Sul", "Produto A", 14, 37.83, 529.62],
    ["2024-03-23", "Sul", "Produto B", 1, 88.96, 88.96],
    ["2024-01-04", "Oeste", "Produto A", 3, 88.68, 266.04],
    ["2024-03-02", "Norte", "Produto C", 18, 95.58, 1720.44],
    ["2024-02-13", "Oeste", "Produto B", 9, 61.05, 549.45],
    ["2024-03-22", "Norte", "Produto B", 13, 85.96, 1117.48],
    ["2024-02-20", "Sul", "Produto B", 18, 51.13, 920.34],
    ["2024-02-20", "Leste", "Produto A", 12, 69.31, 831.72],
    ["2024-01-26", "Norte", "Produto C", 14, 13.4, 187.6],
    ["2024-01-23", "Norte", "Produto C", 14, 41.48, 580.72],
    ["2024-03-01", "Oeste", "Produto C", 10, 87.69, 876.9],
    ["2024-03-23", "Oeste", "Produto B", 19, 31.91, 606.29],
    ["2024-02-02", "Sul", "Produto C", 15, 43.35, 650.25],
    ["2024-01-15", "Sul", "Produto B", 7, 91.2, 638.4],
    ["2024-02-08", "Norte", "Produto C", 10, 38.66, 386.6],
    ["2024-03-25", "Sul", "Produto A", 2, 56.14, 112.28],
    ["2024-03-03", "Sul", "Produto B", 2, 85.75, 171.5],
    ["2024-03-23", "Oeste", "Produto B", 2, 22.3, 44.6],
    ["2024-01-13", "Leste", "Produto A", 6, 43.89, 263.34],
    ["2024-02-10", "Oeste", "Produto B", 5, 96.29, 481.45],
    ["2024-01-01", "Norte", "Produto B", 20, 17.26, 345.2],
    ["2024-02-07", "Oeste", "Produto B", 6, 88.46, 530.76],
    ["2024-02-28", "Sul", "Produto A", 7, 76.36, 534.52],
    ["2024-01-30", "Leste", "Produto B", 15, 14.3, 214.5],
    ["2024-02-19", "Oeste", "Produto B", 1, 50.62, 50.62],
    ["2024-03-09", "Norte", "Produto C", 3, 67.34, 202.02],
    ["2024-02-23", "Sul", "Produto C", 10, 50.49, 504.9],
    ["2024-02-11", "Oeste", "Produto C", 20, 98.8, 1976],
    ["2024-02-21", "Norte", "Produto A", 16, 53.62, 857.92],
    ["2024-03-27", "Leste", "Produto C", 18, 25.14, 452.52],
    ["2024-02-25", "Leste", "Produto B", 14, 53.63, 750.82],
    ["2024-03-02", "Norte", "Produto A", 4, 92.37, 369.48],
    ["2024-03-03", "Oeste", "Produto B", 16, 52.15, 834.4],
    ["2024-03-04", "Oeste", "Produto C", 13, 90.38, 1174.94],
    ["2024-01-13", "Oeste", "Produto B", 3, 92.16, 276.48],
    ["2024-03-18", "Oeste", "Produto C", 1, 20.2, 20.2],
    ["2024-01-02", "Norte", "Produto B", 10, 26.77, 267.7],
    ["2024-01-11", "Oeste", "Produto A", 15, 32.2, 483],
    ["2024-03-06", "Sul", "Produto A", 20, 14.52, 290.4],
    ["2024-01-01", "Leste", "Produto C", 6, 18.06, 108.36],
    ["2024-02-05", "Oeste", "Produto B", 7, 78.24, 547.68],
    ["2024-02-14", "Norte", "Produto A", 5, 69.41, 347.05],
    ["2024-02-08", "Norte", "Produto A", 6, 14.61, 87.66],
    ["2024-01-16", "Oeste", "Produto C", 5, 88.18, 440.9],
    ["2024-01-17", "Norte", "Produto C", 13, 66.38, 862.94],
    ["2024-01-05", "Oeste", "Produto C", 9, 73.5, 661.5],
    ["2024-03-13", "Norte", "Produto A", 7, 58.8, 411.6],
    ["2024-02-12", "Norte", "Produto B", 8, 39.41, 315.28],
    ["2024-02-24", "Oeste", "Produto B", 19, 58.66, 1114.54],
    ["2024-02-29", "Leste", "Produto C", 6, 64.19, 385.14],
    ["2024-03-02", "Norte", "Produto B", 18, 15.99, 287.82],
    ["2024-01-04", "Leste", "Produto C", 9, 23.26, 209.34],
    ["2024-02-16", "Oeste", "Produto C", 10, 45.72, 457.2],
    ["2024-02-22", "Leste", "Produto B", 4, 16.25, 65],
    ["2024-03-20", "Leste", "Produto C", 20, 12.94, 258.8],
    ["2024-01-25", "Leste", "Produto B", 8, 63.19, 505.52],
    ["2024-01-11", "Leste", "Produto A", 2, 83.02, 166.04],
    ["2024-03-16", "Sul", "Produto C", 7, 49.67, 347.69],
    ["2024-03-21", "Oeste", "Produto A", 4, 25.16, 100.64],
    ["2024-03-02", "Sul", "Produto C", 6, 85.14, 510.84]
]

# Definir o nome do arquivo
nome_arquivo = 'vendas.csv'

# Escrever os dados no arquivo CSV
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["Data", "Região", "Produto", "Quantidade Vendida", "Preço Unitário", "Valor Total"])

    writer.writerows(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")



'''
1- Leitura e Preparação dos Dados:

Carregue os dados do arquivo CSV para um array numpy. Cada linha do dataset deve ser representada por um array unidimensional, e o dataset completo deve ser uma matriz 2D.
Certifique-se de converter as colunas de data, quantidade e preço para tipos apropriados (data como string ou datetime, quantidade e preço como numéricos).

'''


df = pd.read_csv('vendas.csv')

# Converter as colunas para os tipos apropriados
df['Data'] = pd.to_datetime(df['Data'])  
df['Quantidade Vendida'] = pd.to_numeric(df['Quantidade Vendida'], errors='coerce')  
df['Preço Unitário'] = pd.to_numeric(df['Preço Unitário'], errors='coerce')  

# Converte o DataFrame para um array numpy
dataset = df.to_numpy()

# Exibir o array resultante
print(dataset)


'''
2- Análise Estatística:

Calcule a média, mediana e desvio padrão do Valor Total das vendas.
Encontre o produto com a maior quantidade vendida e o produto com o maior valor total de vendas.
Calcule o valor total de vendas por região.
Determine a venda média por dia.

'''

# Calcular o valor total de cada venda (quantidade * preço)
df['valor_total'] = df['Quantidade Vendida'] * df['Preço Unitário']

# Cálculo da média, mediana e desvio padrão do valor total das vendas
media_valor_total = df['valor_total'].mean()
mediana_valor_total = df['valor_total'].median()
desvio_padrao_valor_total = df['valor_total'].std()

# Encontrar o produto 
produto_maior_quantidade = df.groupby('Produto')['Quantidade Vendida'].sum().idxmax()
produto_maior_valor_total = df.groupby('Produto')['valor_total'].sum().idxmax()
vendas_por_regiao = df.groupby('Região')['valor_total'].sum()
venda_media_diaria = df.groupby(df['Data'].dt.date)['valor_total'].sum().mean()


print(f'Média do valor total das vendas: R${media_valor_total:.2f}')
print(f'Mediana do valor total das vendas: R${mediana_valor_total:.2f}')
print(f'Desvio padrão do valor total das vendas: R${desvio_padrao_valor_total:.2f}')
print(f'Produto com a maior quantidade vendida: {produto_maior_quantidade}')
print(f'Produto com o maior valor total de vendas: {produto_maior_valor_total}')
print(f'Valor total de vendas por região:\n{vendas_por_regiao}')
print(f'Venda média por dia: R${venda_media_diaria:.2f}\n')

'''
3- Análise Temporal:

a) Determine o dia da semana com maior número de vendas.
b) Calcule a variação diária no valor total de vendas, ou seja, a diferença entre as vendas de um dia e o dia seguinte.

'''
df['Dia da Semana'] = df['Data'].dt.day_name()
vendas_por_dia_semana = df.groupby('Dia da Semana')['Quantidade Vendida'].sum()
print(vendas_por_dia_semana)

df_sorted = df.sort_values(by='Data')
df_sorted['Variação Diária'] = df_sorted['Valor Total'].diff()
print("\nVariação Diária no Valor Total de Vendas:")
print(df_sorted[['Data', 'Valor Total', 'Variação Diária']])
df['Dia da Semana'] = df['Data'].dt.day_name()




def total_vendas_por_regiao_produto(regiao, produto):
    filtro = df[(df['Região'] == regiao) & (df['Produto'] == produto)]
    if filtro.empty:
        return f"Não há vendas para a combinação Região: {regiao} e Produto: {produto}."
    total_vendas = filtro['Valor Total'].sum()
    return total_vendas

df['Ano-Mês'] = df['Data'].dt.to_period('M')

'''
4- Desafios Adicionais (Opcional):

Crie uma função que, dada uma região e um produto, retorne o total de vendas dessa combinação.
Implemente uma análise de crescimento das vendas ao longo do tempo, ou seja, compare o total de vendas entre dois períodos (ex: janeiro de 2024 e fevereiro de 2024) e calcule o aumento ou diminuição percentual.
'''

def crescimento_vendas_periodo(mes_ano_inicial, mes_ano_final):
    # Certificando-se de que a coluna 'Ano-Mês' existe
    if 'Ano-Mês' not in df.columns:
        return "A coluna 'Ano-Mês' não foi criada corretamente."
    
    # Filtrando as vendas por período
    vendas_inicial = df[df['Ano-Mês'] == mes_ano_inicial]['Valor Total'].sum()
    vendas_final = df[df['Ano-Mês'] == mes_ano_final]['Valor Total'].sum()
    
    if vendas_inicial == 0:
        return f"Vendas no período {mes_ano_inicial} são zero, não é possível calcular a variação percentual."
    
    # Calculando a variação percentual
    variacao_percentual = ((vendas_final - vendas_inicial) / vendas_inicial) * 100
    return (f"Vendas no período {mes_ano_inicial}: R${vendas_inicial:.2f}\n"
            f"Vendas no período {mes_ano_final}: R${vendas_final:.2f}\n"
            f"Crescimento/Diminuição Percentual: {variacao_percentual:.2f}%")

# Função para pedir dados ao usuário
def pedir_dados_usuario():
    # Receber input do usuário para os períodos
    while True:
        mes_ano_inicial = input("\nDigite o período inicial (no formato YYYY-MM, ex: 2024-01): ").strip()
        mes_ano_final = input("Digite o período final (no formato YYYY-MM, ex: 2024-02): ").strip()

        # Verificar se os períodos são válidos
        if mes_ano_inicial in df['Ano-Mês'].astype(str).unique() and mes_ano_final in df['Ano-Mês'].astype(str).unique():
            break
        else:
            print("Períodos inválidos, por favor insira novamente.")
    
   
    crescimento = crescimento_vendas_periodo(mes_ano_inicial, mes_ano_final)
    print("\nAnálise de Crescimento de Vendas:")
    print(crescimento)

# Chamar a função para pedir dados do usuário e exibir o crescimento de vendas
pedir_dados_usuario()
