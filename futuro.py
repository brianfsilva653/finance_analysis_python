import pandas as pd

saldo_inicial = 2216.48
aporte_mensal = 600.00
mes_de_inicio = 5
mes_final = 12 
meses = range(mes_de_inicio, mes_final + 1)
projecao = []
saldo_acumulado = saldo_inicial

for mes in meses:
    saldo_acumulado += aporte_mensal
    
    projecao.append({
        'Mês': mes,
        'Aporte Mensal': aporte_mensal,
        'Saldo Acumulado': round(saldo_acumulado, 2)
    })
df_futuro = pd.DataFrame(projecao)

print("PROJEÇÃO DE INVESTIMENTOS: FUTURO")
print(df_futuro)

# 4. (Opcional) Salvar em uma planilha Excel
df_futuro.to_excel("futuro_py.xlsx", index=False)
valor_final = df_futuro.iloc[-1]['Saldo Acumulado']
print(f"\nNo final do ano, você terá aproximadamente: R$ {valor_final}")