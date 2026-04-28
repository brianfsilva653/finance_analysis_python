import pandas as pd

saldo_inicial = 2816.48
aporte_mensal = 600.00
mes_inicio = 5
mes_final = 12

# C.I.D.R (102% do CDI ~ 0.84% am)
taxa_mensal_bruta = 0.0084 
# I.D.R de 22,5% sobre o rendimento (em menos de 180 dias)
aliquota_ir = 0.225
taxa_mensal_liquida = taxa_mensal_bruta * (1 - aliquota_ir)

# Projeção
meses = range(mes_inicio, mes_final + 1)
projecao = []
saldo_acumulado = saldo_inicial

for mes in meses:
    rendimento_mes = saldo_acumulado * taxa_mensal_liquida
    saldo_acumulado += rendimento_mes + aporte_mensal
    
    projecao.append({
        'Mês': mes,
        'Aporte': aporte_mensal,
        'Rendimento Líquido (R$)': round(rendimento_mes, 2),
        'Saldo Acumulado': round(saldo_acumulado, 2)
    })
df_futuro = pd.DataFrame(projecao)
df_futuro.to_excel("futuro_py.xlsx", index=False)

print("PROJEÇÃO REALISTA (PICPAY 102% CDI)")
print(df_futuro)

total_juros = df_futuro['Rendimento Líquido (R$)'].sum()
print(f"\nTotal de juros 'limpos' ganhos até dezembro: R$ {round(total_juros, 2)}")
print(f"Saldo final estimado: R$ {round(saldo_acumulado, 2)}")
