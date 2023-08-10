import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType
from html_templates import css

#A ser aprimorado para conseguir o resultado desejado
#Trabalhar com outros modelos de linguagem

def main():
    st.set_page_config(page_title="Agente Pandas")
    st.subheader("Chatbot usando OpenAI e Pandas")
    st.write("Faça o upload de um arquivo CSV ou XLSX e obtenha respostas de consulta a partir dos seus dados.")

    st.write(css, unsafe_allow_html=True)

    st.session_state.setdefault('chat_history', [])

    with st.sidebar:
        with st.expander("Configurações",  expanded=True):
            TEMP = st.slider(label="Temperatura do LLM", min_value=0.0, max_value=1.0, value=0.5)

    file =  st.file_uploader("Faça o upload do arquivo CSV",type=["csv","xlsx"])
    if not file: st.stop()

    data = pd.read_csv(file)

    st.write("Pré-visualização dos Dados:")
    st.dataframe(data.head()) 

    llm = OpenAI(temperature=TEMP)

    agent = create_pandas_dataframe_agent(llm, data, verbose=True) 

    query = st.text_input("Insira uma consulta:") 

    if st.button("Executar") and query:
        with st.spinner('Gerando resposta...'):
            try:
                prompt = f'''
                    Considerando os dados pandas carregados, responda de forma inteligente à entrada do usuário
                    \nHISTÓRICO DO CHAT: {st.session_state.chat_history}
                    \nENTRADA DO USUÁRIO: {query}
                    \nRESPOSTA DO AI AQUI:
                '''

                answer = agent.run(prompt)

                st.session_state.chat_history.append(f"USUÁRIO: {query}")
                st.session_state.chat_history.append(f"AI: {answer}")

                prev_author = None
                for message in reversed(st.session_state.chat_history):
                    author = message.split(": ")[0]
                    content = message.split(": ")[1]
                    if author == "AI" and prev_author == "AI":
                        st.markdown(content)
                    else:
                        st.markdown(f"**{author}:** {content}")
                    prev_author = author

            except Exception as e:
                st.error(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    load_dotenv()
    main()
