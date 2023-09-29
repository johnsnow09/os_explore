import streamlit as st
# import polars as pl
import pandas as pd

import os
import sys
import wget
import tarfile
import platform


############### Setting Configuration ###############

st.set_page_config(page_title="Political Parties Crime Record Analysis",
                    layout='wide',
                    initial_sidebar_state="expanded")


# Setting configuration to diable plotly zoom in plots
config = dict({'scrollZoom': False})

############### Setting Configuration Ends ###############


# if "jdk-11_linux-x64_bin.tar.gz" not in os.listdir():
if "jdk-11.0.2_linux-x64_bin.rpm" not in os.listdir():
  
  st.write("Starting downloading Java & execution steps")
  #f = wget.download("http://download.oracle.com/otn-pub/java/jdk/11+28/55eed80b163941c8885ad9298e6d786a/jdk-11_linux-x64_bin.tar.gz")

  # for linux from: https://crunchify.com/where-is-java-installed-on-my-mac-osx-system/
  f = wget.download("https://download.oracle.com/otn-pub/java/jdk/11.0.2+9/f51449fcd52f4d52b93a989c5c56ed3c/jdk-11.0.2_linux-x64_bin.rpm")
  st.write(" Java Downloaded")

else: 
  st.write("Java file already exist")
  
#print("Current Directory: ",os.getcwd())
#print("Directory list: ",os.listdir())



############################## CREATING HEADER ##############################

header_left,header_mid,header_right = st.columns([1,8,1],gap = "small")

with header_mid:
    # https://docs.streamlit.io/library/get-started/create-an-app
    st.title("Testing OS")
    st.title("Checking platform: ",platform.system())
    st.write("Current Directory: ",os.getcwd())

    st.write("Directory list: ",os.listdir())
    #st.write(f)
    #st.write(os.path.abspath(f))

############################## HEADER DONE ##############################



  ####################### Java installation tar.gzp file #######################
st.write("Installing Java")

#Name of tarfile (without the .tar.gz extension)
#file_name = "jdk-11_linux-x64_bin"

#Target directory
#target_dir = "mydirectory"

#Extract the tar file
#os.system("tar -xf " + file_name + ".tar.gz")

#file = tarfile.open('jdk-11_linux-x64_bin.tar.gz')
  
# extracting file
#file.extractall('./mydirectory')
#file.close()

#Move the tar files into your target folder
#os.system("mv " + file_name + " " + target_dir)

#st.write("Ending execution steps")

if os.path.exists("jdk-11_linux-x64_bin.tar.gz") == True:
  os.remove("jdk-11_linux-x64_bin.tar.gz")
  #os.remove("jdk-11_linux-x64_bin.tar (1).gz")


st.write(os.listdir())
