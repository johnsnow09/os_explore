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


st.write(os.getcwd())
