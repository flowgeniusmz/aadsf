import streamlit as st
from config import pagesetup as ps
from openai import OpenAI
from datetime import datetime

st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 0. Set Master Page Config (see config/pagesetup.py)
page = 1
ps.master_page_display(varPageNumber=page)

# 1. Set Variables
api_key = st.secrets.openai.apikey1
client = OpenAI(api_key=api_key)
assistant_id = st.secrets.openai.assistantid1
assistant = client.beta.assistants.retrieve(assistant_id=assistant_id)
thread = client.beta.threads.create()
thread_id = thread.id
chat_messages = [{"role": "assistant", "content": st.secrets.messageconfig.initialmessage1_daddy}]
log_messages = [{"assistant_id": None, "thread_id": None, "message_id": None, "role": "assistant", "run_id": None, "content": st.secrets.messageconfig.initialmessage1_daddy, "createddatetime": datetime.now(), "createdunixtime": None}]

# 2. Containers
main_container = st.container(border=True, height=400)
with main_container:
    cols = st.columns([3,1])
    with cols[0]:
        ps.get_gray_header(varText="Chat with Daddy")
        chat_container = st.container(border=True, height=375)
        with chat_container:
            for chatmsg in chat_messages:
                role = chatmsg['role']
                content = chatmsg['content']
                with st.chat_message(name=role):
                    st.markdown(body=content)
    with cols[1]:
        ps.get_gray_header(varText="The Bet Lab")
        status_container = st.container(border=True, height=375)
        
# 3. Prompt
if prompt := st.chat_input(placeholder="Ask Daddy and watch him cook..."):
    chat_messages.append({"role": "user", "content": prompt})
    with chat_container:
        with st.chat_message(name="user"):
            st.markdown("prompt")
    prompt_message = client.beta.threads.messages.create(thread_id=thread_id, role="user", content=prompt)
    prompt_message_id = prompt_message.id

