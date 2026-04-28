import pandas as pd

def gerar_planejamento():
    # Dados de entrada
    fluxo_inicial = 1695.94
    
    # Estrutura dos dados das despesas
    itens = [
        {"Descrição": "Fluxo de Caixa Inicial", "Valor": fluxo_inicial, "Tipo": "Entrada"},
        {"Descrição": "Faculdade", "Valor": 317.00, "Tipo": "Saída"},
        {"Descrição": "Investimentos", "Valor": 600.00, "Tipo": "Saída"},
        {"Descrição": "Casa", "Valor": 250.00, "Tipo": "Saída"},
        {"Descrição": "Lazer Pessoal", "Valor": 180.00, "Tipo": "Saída"},
        {"Descrição": "Transporte Facul", "Valor": 70.00, "Tipo": "Saída"},
    ]

    # Criação do DataFrame inicial
    df = pd.DataFrame(itens)

    # Cálculos
    total_despesas = df[df["Tipo"] == "Saída"]["Valor"].sum()
    saldo_final = fluxo_inicial - total_despesas

    # Adicionando as linhas de resumo ao DataFrame
    resumo = pd.DataFrame([
        {"Descrição": "TOTAL DE DESPESAS", "Valor": total_despesas, "Tipo": "Resumo"},
        {"Descrição": "SALDO LÍQUIDO FINAL", "Valor": saldo_final, "Tipo": "Resultado"}
    ])

    df_final = pd.concat([df, resumo], ignore_index=True)

    # Exportação para Excel
    nome_arquivo = "planejamento_py.xlsx"
    try:
        df_final.to_excel(nome_arquivo, index=False)
        print(f"Sucesso! O arquivo '{nome_arquivo}' foi gerado.")
    except Exception as e:
        print(f"Erro ao gerar a planilha: {e}")

if __name__ == "__main__":
    gerar_planejamento()
