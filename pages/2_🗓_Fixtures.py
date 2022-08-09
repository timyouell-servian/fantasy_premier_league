#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 15:57:08 2022

@author: timyouellservian
"""

import streamlit as st
import pandas as pd
import requests

base_url = 'https://fantasy.premierleague.com/api/'

st.set_page_config(page_title='Fixtures', page_icon=':calendar:', layout='wide')


st.sidebar.subheader('About')
st.sidebar.write("""This website is designed to help you analyse and
                 ultimately pick the best Fantasy Premier League Football
                 options for your team.""")
st.sidebar.write('[Github](https://github.com/TimYouell15)')