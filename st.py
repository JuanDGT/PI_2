# -*- coding: utf-8 -*-
import pandas as pd
#from sodapy import Socrata
import streamlit as st
import numpy as np
import datetime as dt
from datetime import datetime
from dateutil.relativedelta import relativedelta
#import matplotlib.pyplot as plt
#import seaborn as sns
#sns.set()
from IPython.display import clear_output

st.title("Covid 19 en USA")
df_data = pd.read_csv('COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv', delimiter= ",")
df_data.date = pd.to_datetime(df_data.date)
st.subheader('Datos')
st.write(df_data)

st.map(df_data)