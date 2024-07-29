import streamlit as st
import pandas as pd
import numpy as np

# データの作成（例としてランダムデータを生成）
np.random.seed(0)
dates = pd.date_range(start="2023-06-01", end="2024-07-30")
temperatures = np.random.normal(loc=20, scale=5, size=len(dates))
precipitations = np.random.normal(loc=5, scale=2, size=len(dates))

# DataFrameに変換
data = pd.DataFrame({
    'date': dates,
    'temperature': temperatures,
    'precipitation': precipitations
})

# Streamlitのアプリケーションの設定
st.title("Select Values from DataFrame Columns with Session State")

# セッションステートに選択した値を保存するための初期化
if 'selected_date' not in st.session_state:
    st.session_state.selected_date = dates[0]

if 'selected_temperature' not in st.session_state:
    st.session_state.selected_temperature = temperatures[0]

if 'selected_precipitation' not in st.session_state:
    st.session_state.selected_precipitation = precipitations[0]

# 各カラムから一つの値を選択するためのselectboxを作成
selected_date = st.selectbox("Select Date", data['date'], index=list(data['date']).index(st.session_state.selected_date))
selected_temperature = st.selectbox("Select Temperature", data['temperature'], index=list(data['temperature']).index(st.session_state.selected_temperature))
selected_precipitation = st.selectbox("Select Precipitation", data['precipitation'], index=list(data['precipitation']).index(st.session_state.selected_precipitation))

# 選択した値をセッションステートに保存
st.session_state.selected_date = selected_date
st.session_state.selected_temperature = selected_temperature
st.session_state.selected_precipitation = selected_precipitation

# 選択した値を表示
st.write(f"Selected Date: {selected_date}")
st.write(f"Selected Temperature: {selected_temperature:.2f} °C")
st.write(f"Selected Precipitation: {selected_precipitation:.2f} mm")

# DataFrameを表示
st.write("DataFrame:")
st.dataframe(data)
