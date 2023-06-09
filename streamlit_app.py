import openai
import streamlit as st
from streamlit_chat import message
import os 

# openai.api_key = os.getenv('API_KEY')
openai.api_key = "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"


def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        stop=None,
        temperature=0,
        top_p=1,
    )
 
    message = completions["choices"][0]["text"].replace("\n", "")
    return message
 
 
st.header("🤖ARON's ChatGPT-3 (Demo)")

st.markdown("[Be Original](https://github.com/L22AR5N/chat_gpt_test1/)")
 
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
 
if submitted and user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
 
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
