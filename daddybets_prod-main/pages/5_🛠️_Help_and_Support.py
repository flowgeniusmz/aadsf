import streamlit as st
from config import pagesetup as ps, sessionstates as ss
from assets.faqs import faq_app as fa, faq_prompts as fp
import requests

st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 0. Set Master Page Config (see config/pagesetup.py)
page = 4
ps.master_page_display(varPageNumber=page)



helpemail = "https://prod-109.westus.logic.azure.com:443/workflows/ffe43b3ca79b4143a9d6971528ea59c5/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=I4ma9GXheJjFg2OgaU8tLrmP9NmrSxww5TObTezHZUU"
bugemail = "https://prod-152.westus.logic.azure.com:443/workflows/2fe5da09a8154d65bcb27777279c4eac/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=NIlZe7YmX-q8jVBqkWHtx7nHVGP_PAxEmc1aSZ5X8nc"


def send_help_email(name: str, email: str, description: str, varType):
    if varType == "help":
        url = helpemail
    elif varType == "bug":
        url = bugemail
    else:
        url = helpemail

    data = {"email": email, "name": name, "description": description}
    response = requests.post(url=url, json=data)
    st.success(body="Your feedback or issue has been submitted! Please allow 24-48 hours for a response.")



# 1. Tabs
main_container = st.container(border=False, height=600)
with main_container:
    tab_names = ["Contact Support", "Report a Bug", "Prompt Tips and Tricks", "DaddyBets App FAQs"]
    tab1, tab2, tab3, tab4 = st.tabs(tabs=tab_names)
    with tab1:
        ps.get_gray_header(varText="Contact Support")
        con1 = st.container(border=False)
        with con1:
            scon1 = ps.container_styled2(varKey="helptab1")
            with scon1:
                cols1 = st.columns([1,20,1])
                with cols1[1]:
                    email = st.text_input(label="Email", key="_helpemail")
                    name = st.text_input(label="Name", key="helpname")
                    description = st.text_area(label="Question, Comment, or Concern", key="helpdescription", placeholder="Please enter your comments, questions or concerns here...")
                    submit = st.button(label="Submit", key="helpsubmitbutton")
                    if submit:
                        if name is not None and email is not None and description is not None:
                            send_help_email(name=name, email=email, description=description, varType="help")
    with tab2:
        ps.get_gray_header(varText="Report a Bug")
        con2 = st.container(border=False)
        with con2:
            scon2 = ps.container_styled2(varKey="helptab2")
            with scon2:
                cols2 = st.columns([1,20,1])
                with cols2[1]:
                    email = st.text_input(label="Email", key="bugemail")
                    name = st.text_input(label="Name", key="bugname")
                    description = st.text_area(label="Question, Comment, or Concern", key="bugdescription", placeholder="Please enter your comments, questions or concerns here...")
                    submit = st.button(label="Submit", key="bugsubmitbutton")
                    if submit:
                        if name is not None and email is not None and description is not None:
                            send_help_email(name=name, email=email, description=description, varType="bug")
                        else:
                            st.error(body="**Error:** Please complete all the fields in the form and try again")

    with tab3:
        ps.get_gray_header(varText="Prompt Tips and Tricks")
        con3 = st.container(border=False)
        with con3:
            scon3 = ps.container_styled2(varKey="helptab3")
            with scon3:
                content = fp.get_faq_prompts()
                st.markdown(content)
    with tab4:
        ps.get_gray_header(varText="DaddyBets App FAQs")
        con4 = st.container(border=False)
        with con4:
            scon4 = ps.container_styled2(varKey="helptab4")
            with scon4:
                content1 = fa.get_faq_app()
                st.markdown(body=content1)

