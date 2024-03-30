import streamlit as st
from config import pagesetup as ps, sessionstates as ss
from assets.terms import terms_content as terms
from forms import form_1_terms as ft, form_2_usertype as fu, form_3_existinguser as fe, form_3_newuser as fn, form_4_usersession as fg

# 1. Set Page Config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 2. Set Page Title
ps.set_title_manual(varTitle="DaddyBets", varSubtitle="Login / Registration", varDiv=True)

# 3. Session States
ss.initial_session_State()

ps.get_page_styling()
ps.display_background_image()






userflow_container = st.container(border=False)
with userflow_container:

# 6. Flow
    if st.session_state.userflow_complete:
        ps.switch_to_homepage()    
    elif not st.session_state.terms_complete:
        ps.get_gray_header(varText="Terms and Conditions")
        ft.TermsForm()
    elif not st.session_state.usertype_complete:
        ps.get_gray_header(varText="Select New or Existing User")
        fu.UserTypeForm()
    elif not st.session_state.usercheck:
        if st.session_state.usertype == "new": 
            ps.get_gray_header(varText="New User Registraiton")
            fn.NewUserForm()
        else:
            ps.get_gray_header(varText="Existing User Login")
            fe.ExistingUserForm()

        
        