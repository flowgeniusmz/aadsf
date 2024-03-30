import streamlit as st
import uuid
from datetime import datetime
import time
import json


def initial_session_State():
    if "userflow_complete" not in st.session_state:
        st.session_state.userflow_complete = False
        st.session_state.username = None
        st.session_state.credential = None
        st.session_state.usercheck = False
        st.session_state.payinfo = bool(st.query_params)
        st.session_state.fullname = None
    if "auth_complete" not in st.session_state:
        st.session_state.auth_complete = False
    if "usertype_complete" not in st.session_state:
        st.session_state.usertype_complete = bool(st.query_params)
        st.session_state.usertypes = ["New User Registration", "Existing User Login"]
        st.session_state.selected_usertype = "New User Registration" if st.query_params else None
        st.session_state.usertype = "new" if st.query_params else None
    if "terms_complete" not in st.session_state:
        st.session_state.terms_complete = bool(st.query_params)
        st.session_state.terms_acknowledged = bool(st.query_params)
        st.session_state.terms_accepted = bool(st.query_params)
    if "query_params" not in st.session_state:
        st.session_state.query_params = st.query_params
        st.session_state.query_params_empty = not bool(st.query_params)
    if "stripe_session" not in st.session_state:
        st.session_state.stripe_session = None
        st.session_state.stripe_session_id = st.query_params.get("session_id", None)
        st.session_state.stripe_customer_email = None
        st.session_state.customer_address_state = None
        st.session_state.customer_address_zip = None
        st.session_state.stripe_customer_name = None
        st.session_state.stripe_payment_status = None
        st.session_state.stripe_payment_intent = None
    if "geolocation_complete" not in st.session_state:
        st.session_state.geolocation_complete = False
        st.session_state.geolocation_response = None
        st.session_state.geolocation_json = None
        st.session_state.geolocation_location = None
        st.session_state.geolocation_siteexperience = None
        st.session_state.geolocation_isvpn = None
        st.session_state.geolocation_regionfull = None
        st.session_state.geolocation_region = None
        st.session_state.geolocation_regionlower = None
    if "usersession_complete" not in st.session_state:
        st.session_state.usersession_complete = False
        st.session_state.usersession_id = None
        st.session_state.usersession_datetime = None
        st.session_state.usersession_unixtime = None
    if "usersession_logged" not in st.session_state:
        st.session_state.usersession_logged = False
    if "userflow_stage" not in st.session_state:
        st.session_state.userflow_stage = 0
        
    
        
        
    