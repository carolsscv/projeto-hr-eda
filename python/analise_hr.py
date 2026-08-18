"""
Análise Exploratória de Dados - HR
Projeto de Recuperação Módulo 1 - Semana 14

Este arquivo lê os dois CSVs gerados pelas consultas SQL,
faz uma análise exploratória simples e cria gráficos.
"""

import pandas as pd
import matplotlib.pyplot as plt


# 1. Leitura dos arquivos CSV
df_salarios = pd.read_csv("data/query_01.csv")
df_localidade = pd.read_csv("data/query_02.csv")


# 2. Visão inicial dos dados
print("\n--- QUERY 1: SALÁRIOS ---")
print("Linhas e colunas:", df_salarios.shape)
print(df_salarios.head())

print("\nTipos de dados:")
print(df_salarios.dtypes)

print("\nValores ausentes:")
print(df_salarios.isnull().sum())


print("\n--- QUERY 2: LOCALIDADES ---")
print("Linhas e colunas:", df_localidade.shape)
print(df_localidade.head())

print("\nValores ausentes:")
print(df_localidade.isnull().sum())


# 3. Estatísticas básicas dos salários
media = df_salarios["SALARY"].mean()
mediana = df_salarios["SALARY"].median()
minimo = df_salarios["SALARY"].min()
maximo = df_salarios["SALARY"].max()

print("\n--- ESTATÍSTICAS DOS SALÁRIOS ---")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Mínimo: {minimo:.2f}")
print(f"Máximo: {maximo:.2f}")


# 4. Salário médio por departamento
print("\n--- MÉDIA SALARIAL POR DEPARTAMENTO ---")
media_departamento = (
    df_salarios.groupby("DEPARTMENT_NAME")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)
print(media_departamento)


# 5. Salário médio por cargo
print("\n--- MÉDIA SALARIAL POR CARGO ---")
media_cargo = (
    df_salarios.groupby("JOB_TITLE")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)
print(media_cargo)


# 6. Funcionários por região, país e cidade
print("\n--- FUNCIONÁRIOS POR REGIÃO ---")
print(df_localidade["REGION_NAME"].value_counts())

print("\n--- FUNCIONÁRIOS POR PAÍS ---")
print(df_localidade["COUNTRY_NAME"].value_counts())

print("\n--- FUNCIONÁRIOS POR CIDADE ---")
print(df_localidade["CITY"].value_counts())


# 7. Identificação de outliers usando o IQR
q1 = df_salarios["SALARY"].quantile(0.25)
q3 = df_salarios["SALARY"].quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers = df_salarios[
    (df_salarios["SALARY"] < limite_inferior)
    | (df_salarios["SALARY"] > limite_superior)
]

print("\n--- OUTLIERS ---")
print(f"Q1: {q1:.2f}")
print(f"Q3: {q3:.2f}")
print(f"IQR: {iqr:.2f}")
print(f"Limite inferior: {limite_inferior:.2f}")
print(f"Limite superior: {limite_superior:.2f}")
print(f"Quantidade de outliers: {len(outliers)}")
print(outliers[
    ["EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY",
     "DEPARTMENT_NAME", "JOB_TITLE"]
])


# 8. Histograma
plt.figure(figsize=(9, 5))
plt.hist(df_salarios["SALARY"], bins=10, edgecolor="black")
plt.title("Distribuição dos salários")
plt.xlabel("Salário")
plt.ylabel("Quantidade de funcionários")
plt.tight_layout()
plt.savefig("graficos/histograma_salarios.png", dpi=150)
plt.show()


# 9. Boxplot
plt.figure(figsize=(8, 4.5))
plt.boxplot(df_salarios["SALARY"], vert=False)
plt.title("Boxplot dos salários")
plt.xlabel("Salário")
plt.tight_layout()
plt.savefig("graficos/boxplot_salarios.png", dpi=150)
plt.show()


# 10. Média salarial por departamento
plt.figure(figsize=(9, 6))
plt.barh(media_departamento.index, media_departamento.values)
plt.title("Média salarial por departamento")
plt.xlabel("Salário médio")
plt.ylabel("Departamento")
plt.tight_layout()
plt.savefig("graficos/media_salarial_departamento.png", dpi=150)
plt.show()


# 11. Funcionários por região
quantidade_regiao = df_localidade["REGION_NAME"].value_counts().sort_values()

plt.figure(figsize=(7, 4.5))
plt.barh(quantidade_regiao.index, quantidade_regiao.values)
plt.title("Funcionários por região")
plt.xlabel("Quantidade de funcionários")
plt.ylabel("Região")
plt.tight_layout()
plt.savefig("graficos/funcionarios_regiao.png", dpi=150)
plt.show()
