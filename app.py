import streamlit as st
# import polars as pl
import pandas as pd

import os
import sys
import wget

f = wget.download("http://download.oracle.com/otn-pub/java/jdk/11+28/55eed80b163941c8885ad9298e6d786a/jdk-11_linux-x64_bin.tar.gz")

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
    st.write(f)
    st.write(os.path.abspath(f))

os.remove("jdk-11_linux-x64_bin.tar.gz")
os.remove("jdk-11_linux-x64_bin.tar (1).gz")
os.remove("jdk-11_linux-x64_bin.tar (2).gz")
os.remove("jdk-11_linux-x64_bin.tar (3).gz")
os.remove("jdk-11_linux-x64_bin.tar (4).gz")
os.remove("jdk-11_linux-x64_bin.tar (5).gz")
os.remove("jdk-11_linux-x64_bin.tar (6).gz")
os.remove("jdk-11_linux-x64_bin.tar (7).gz")
os.remove("jdk-11_linux-x64_bin.tar (8).gz")
os.remove("jdk-11_linux-x64_bin.tar (9).gz")

############################## HEADER DONE ##############################

if "jdk-11_linux-x64_bin.tar.gz" not in os.listdir():
  st.write("Checking execution steps")

  ####################### Java installation #######################
  #Name of tarfile (without the .tar.gz extension)
  file_name = "jdk-11_linux-x64_bin"

  #Target directory
  target_dir = "mydirectory"

  #Extract the tar file
  os.system("tar -xf " + file_name + ".tar.gz")

  #Move the tar files into your target folder
  os.system("mv " + file_name + " " + target_dir)

else: 
  st.write("Java file already exist")
  
#st.write(os.listdir())
