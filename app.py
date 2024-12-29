
import streamlit as st
import neurokit2 as nk
import pandas as pd

st.title("Analisador de Eletrocardiograma (ECG)")

# Upload de arquivo
uploaded_file = st.file_uploader("Faça upload do arquivo de ECG (.csv ou .txt)", type=["csv", "txt"])

if uploaded_file is not None:
    # Carregar o arquivo de ECG
    try:
        ecg_data = pd.read_csv(uploaded_file, header=None)
        signal = ecg_data[0].values

        # Processar o sinal de ECG
        processed_ecg = nk.ecg_process(signal, sampling_rate=500)  # Ajuste a taxa de amostragem conforme necessário
        report = nk.ecg_report(processed_ecg)

        # Mostrar resultados
        st.subheader("Relatório de Análise")
        st.text(report)

        # Gráfico do ECG
        st.subheader("Gráfico do ECG")
        nk.ecg_plot(processed_ecg)
        st.pyplot()

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
