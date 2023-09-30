import streamlit as st
# import polars as pl
import pandas as pd

import os
import sys
import wget
# import tarfile
import platform


############### Setting Configuration ###############

st.set_page_config(page_title="OS Java install",
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


############################## CREATING HEADER ##############################

header_left,header_mid,header_right = st.columns([1,8,1],gap = "small")

with header_mid:
    # https://docs.streamlit.io/library/get-started/create-an-app
    st.title("Testing OS")
  
    # https://stackoverflow.com/questions/59478429/downloading-and-installing-a-program-using-python
    st.write("Checking platform: ",platform.system())
  
    st.write("Current Directory: ",os.getcwd())
    st.write("Directory list: ",os.listdir())
    #st.write(f)
    #st.write(os.path.abspath(f))

############################## HEADER DONE ##############################


st.write("Installing Java")

# from: https://stackoverflow.com/questions/49484772/install-rpm-or-msi-file-through-python-script
!pip install rpm
import rpm
import subprocess
package_path = '/mount/src/os_explore/jdk-11.0.2_linux-x64_bin.rpm'
# command = ['rpm', '-Ivh', package_path]
command = ['rpm', '-ivh', package_path]
p = subprocess.Popen(command)
p.wait()
if p.returncode == 0:
    print("OK")
else:
    print("Something went wrong")


  ####################### Java installation tar.gzp file #######################

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

  ####################### Java installation tar.gzp file #######################

st.write(os.listdir())
