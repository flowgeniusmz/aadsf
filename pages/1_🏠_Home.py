import streamlit as st
from config import pagesetup as ps

st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 0. Set Master Page Config (see config/pagesetup.py)
page = 0

ps.master_page_display_styled(varPageNumber=page)




