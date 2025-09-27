import streamlit as st
from openai import OpenAI

import openai_api_key


client = OpenAI(
    api_key=openai_api_key.get()
)

st.write("## Python Dev | chatbot com IA")

# se não existir histórico de mensagens na sessão, cria o histórico de mensagens
if not "messages_historic" in st.session_state:
    st.session_state["messages_historic"] = []

# exibe as mensagens do histórico no chat
for msg in st.session_state["messages_historic"]:
    st.chat_message(msg["role"]).write(msg["content"])

user_msg = st.chat_input("Mensagem...")

if user_msg:
    st.chat_message("user").write(user_msg)
    # armazenar a mensagem do usuário no histórico
    st.session_state["messages_historic"].append(
        {
            "role": "user",
            "content": user_msg
        }
    )

    # todo ~> pegar a resposta de IA
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state["messages_historic"]
    )
    assistant_msg = completion.choices[0].message.content

    st.chat_message("assistant").write(assistant_msg)
    # armazenar a resposta da IA no histórico
    st.session_state["messages_historic"].append(
        {
            "role": "assistant",
            "content": assistant_msg
        }
    )
