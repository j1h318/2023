import pandas as pd
import numpy as np
import streamlit as st

st.title ("최고의 수업, OSS 개발에서 배운 Streamlit")


df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)
