import streamlit as st
import pandas as pd
import numpy as np

all_users = st.text_input("Movie title", "Life of Brian")
np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, len(all_users)), columns= all_users)

st.data_editor(data, height=250, use_container_width=True)

