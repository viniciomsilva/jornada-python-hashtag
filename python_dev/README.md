# 🤖 Python Dev | Chatbot com IA

Chatbot with artificial intelligence in ChatGPT style. In it, the user sends a
message and the assistant responds.

## #1. Technologies Used

* Streamlit: library for building the web interface in Python
  * It has several ready-made components, easy to configure, aimed at AI
    integration
  * Here only a few web chat components are used
* OpenAI: library to access OpenAI's generative text AI

```bash
pip install pandas openai streamlit
```

> NOTE: If the installation of all requirements by the ` requirements.txt ` has
> already been done file, no longer need to install.

## #2. Project Flow

1. Build the web page
2. Capture the user's message
3. Send the user's message to the AI
4. Capture de AI's response
5. Display the response on the web chat

## #3. Starting the Project

To start the application, you need to call Streamlit in the terminal so it
creates a local server.

```bash
streamlit run ./python_dev/app.py
```

```bash
>>> Local URL: http://localhost:8501
>>> Network URL: http://192.168.0.6:8501
```

## #4. About the Data Structures

When the user asks a question to OpenAI's generative AI, it does not respond to
that specific question, but rather completes the context of the conversation.  
Therefore, for everything to work perfectly, it is necessary to store the
message history in the user's session, and when they ask a new question, the
history must be sent to the AI to respond.  
This is how it manages to "understand" and "remember" the conversation topic.

Thus, this project manipulates two important data structures: the user's
navigation session (where the message history will be stored) and the messages.

**Streamlit Session State:**  
Every web application, when the page state changes due to user interaction, is
reloaded. However, the user's session information remains saved. This is the
structure where the user's message history should be kept.  
The Streamlit Session State is a Python dictionary with key and value. And the
message history is a list.

```python
  st.session_state["messages"] = list
```

**Message:**  
In this project, a message is a Python dictionary with the keys:

* Role: function within the conversation (user or assistant)
* Content: message content

```python
msg = {
  "role": "assistant"
  "content": "Hello World!"
}
```

## #5. About the Script

```python
# script app.py

# initialize message history
def init_messages_historic() -> None:
    st.session_state["messages"] = []

# show the messages from the history as chat messages
def show_messages() -> None:
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

# add a message to the history
def add_message(msg: dict[str, str]) -> None:
    st.session_state["messages"].append(msg)

# send the message history to the AI to complete
# return the formatted response for this system
def get_assistant_response(model: str = "gpt-4o") -> dict[str, str]:
    completion = client.chat.completions.create(
        model=model,
        messages=st.session_state["messages"]
    )

    return {
        "role": "assistant",
        "content": str(completion.choices[0].message.content)  # structure that contains the AI's response
    }

if __name__ == "__main__":
    client = OpenAI(api_key="")

    # when the user sends a message, the app state changes
    user_msg_content = st.chat_input("Digite alguma coisa...")

    # when this changes happens
    if user_msg_content:
        # show the user's message in the chat
        st.chat_message("user").write(user_msg_content)
        
        # add it to the history
        add_message({
            "role": "user",
            "content": user_msg_content
        })

        # get the AI's response
        assistant_response = get_assistant_response()
        
        # show the AI's response in the chat
        st.chat_message(
            assistant_response["role"]).write(
            assistant_response["content"]
        )
        
        # add it to the history
        add_message(assistant_response)
```
