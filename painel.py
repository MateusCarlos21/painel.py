import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Configuração geral do tema do seaborn
sns.set_theme(style="whitegrid", palette="muted")

# Cabeçalho do Dashboard
st.title("📊 Dashboard da Empresa AXIA")
st.markdown("Acompanhe a evolução do lucro e análise setorial")

# Carregar dados do primeiro arquivo
df = pd.read_excel("AXIA3_evolucao.xlsx")

# Filtrar dados do lucro
lucro_df = df[df["conta"] == "lucro"][["trimestre", "valor"]]

# Tabulação
tab1, tab2 = st.tabs(["Evolução do Lucro", "Análise Setorial"])

with tab1:
    nome = st.text_input("Digite seu nome:")
    st.header(f"Olá, {nome}!" if nome else "Informe seu nome para começar")

    # Gráfico do lucro ao longo do tempo
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=lucro_df, x="trimestre", y="valor", marker="o", ax=ax)
    ax.set_title("Evolução do Lucro por Trimestre", fontsize=16)
    ax.set_xlabel("Trimestre", fontsize=12)
    ax.set_ylabel("Valor (R$)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    # Mostrar tabela
    st.subheader("Dados completos")
    st.dataframe(df)

with tab2:
    # Carregar dados setor
    df_setor = pd.read_excel("planilhao_b3.xlsx")

    # Mostrar tabela
    st.subheader("Empresas por Setor")
    st.dataframe(df_setor)

    # Contagem por setor
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df_setor, y="setor", order=df_setor["setor"].value_counts().index, ax=ax, palette="coolwarm")
    ax.set_title("Número de Empresas por Setor", fontsize=16)
    ax.set_xlabel("Quantidade de Empresas", fontsize=12)
    ax.set_ylabel("Setor", fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)



