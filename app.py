import streamlit as st
# import polars as pl
import pandas as pd

import os
import sys

print(os.getcwd())
print(os.listdir())




############### Setting Configuration ###############

st.set_page_config(page_title="Political Parties Crime Record Analysis",
                    layout='wide',
                    initial_sidebar_state="expanded")


# Setting configuration to diable plotly zoom in plots
config = dict({'scrollZoom': False})

############### Setting Configuration Ends ###############





############################## CREATING HEADER ##############################

header_left,header_mid,header_right = st.columns([1,8,1],gap = "small")

with header_mid:
    # https://docs.streamlit.io/library/get-started/create-an-app
    st.title("Testing OS")
    st.write(os.getcwd())

    st.write(os.listdir())

############################## HEADER DONE ##############################



