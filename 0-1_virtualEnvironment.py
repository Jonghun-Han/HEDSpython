#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Virtual Environment
@author: Roberto Gentile
@module: Humanitarian Engineering and Data Science
"""

# download and install Anaconda
# After installing it, the folder "userName/opt/anaconda3" should be created


# In the terminal (for Linux/Mac) or CMD (for Windows) run:
conda create -n HEDSenv -y
conda activate HEDSenv
conda install spyder-kernels=2.3 numpy pandas matplotlib scikit-learn
# After these commands, you should have the folder 
# "userName/opt/anaconda3/envs/HEDSenv/bin/python"

# If spyder-kernels 2.3 is not available run:
conda install -c conda-forge spyder-kernels=2.3


# go to Spyder preferences / Python Interpreter
# Select "use the following python interpreter"

# in spyder, restart the kernel