import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres

def main():
    
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Email do Vendedor:")
    data = st.date_input("Data da Compra:", datetime.now())
    hora = st.time_input("Hora da Compra:", value=time(9,0))
    valor = st.number_input("Valor da Venda:", min_value=0.0, format="%2.f")
    quantidade = st.number_input("Quantidade de Produtos:", min_value=1, step=1)
    produto = st.selectbox("Produto:", ["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])
    
    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )

            st.write(venda)
            salvar_no_postgres(venda)

        except ValidationError as e:
            st.error(f"Deu erro {e}")

if __name__=="__main__":
    main()