import streamlit as st
from openai import OpenAI

import openai_api_key


def init_messages_historic() -> None:
    st.session_state["messages"] = list[dict[str, str]]
    st.session_state["messages"] = []
    add_message({
        "role": "assistant",
        "content": "Olá! No que posso ajudar?"
    })


def show_messages() -> None:
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])


def add_message(msg: dict[str, str]) -> None:
    st.session_state["messages"].append(msg)


def get_assistant_response(model: str = "gpt-4o") -> dict[str, str]:
    completion = client.chat.completions.create(
        model=model,
        messages=st.session_state["messages"]
    )

    return {
        "role": "assistant",
        "content": str(completion.choices[0].message.content)
    }


if __name__ == "__main__":
    client = OpenAI(api_key=openai_api_key.get())

    if not "messages" in st.session_state:
        init_messages_historic()

    st.set_page_config(page_title="Python Dev | Chatbot com IA")

    show_messages()

    user_msg_content = st.chat_input("Digite alguma coisa...")

    if user_msg_content:
        st.chat_message("user").write(user_msg_content)
        add_message({
            "role": "user",
            "content": user_msg_content
        })

        assistant_response = get_assistant_response()
        st.chat_message(
            assistant_response["role"]).write(
            assistant_response["content"]
        )
        add_message(assistant_response)
