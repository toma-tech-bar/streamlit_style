import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DayLocator
from datetime import datetime, timedelta

# データの作成（例としてランダムデータを生成）
np.random.seed(0)
dates = pd.date_range(start=datetime.now().date() - timedelta(days=30), end=datetime.now().date())
temperatures = np.random.normal(loc=20, scale=5, size=len(dates))
precipitations = np.random.normal(loc=5, scale=2, size=len(dates))

# DataFrameに変換
data = pd.DataFrame({
    'date': dates,
    'temperature': temperatures,
    'precipitation': precipitations
})

# Streamlitのアプリケーションの設
st.set_page_config(
    page_title="背景色付きグラフ",
    page_icon="📈",
    layout="wide"
)

st.title("Temperature Time Series with Background Color")

# 今日の日付
today = datetime.now().date()

# グラフを横並びに表示するためのカラム設定
col1, col2 = st.columns(2)

# 気温のプロット
with col1:
    fig, ax = plt.subplots(figsize=(12, 5))

    # データのプロット
    ax.plot(data['date'], data['temperature'], label='Temperature')

    # 背景色の設定
    nine_days_ago = today - timedelta(days=10)
    ax.axvspan(nine_days_ago, today, color='red', alpha=0.3, label='Today ~ 10 days ago')

    twenty_six_days_ago = today - timedelta(days=20)
    ax.axvspan(twenty_six_days_ago, nine_days_ago, color='yellow', alpha=0.3, label='10 ~ 20 days ago')

    ax.axvspan(data['date'].min(), twenty_six_days_ago, color='green', alpha=0.3, label='More than 20 days ago')

    # 軸ラベルとタイトルの設定
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Time Series')

    # 凡例の設定
    ax.legend()

    # 日付フォーマットの設定（毎日表示）
    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45, fontsize=8)  # 日付ラベルを回転させてフォントサイズを小さく

    # プロットのレイアウト調整
    plt.subplots_adjust(bottom=0.2)

    # Streamlitでプロットを表示
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(10, 5))  # プロットサイズを調整

    # データのプロット
    ax.plot(data['date'], data['precipitation'], label='Precipitation', color='blue')

    # 背景色の設定
    ax.axvspan(nine_days_ago, today, color='red', alpha=0.3, label='Today ~ 10 days ago')

    ax.axvspan(twenty_six_days_ago, nine_days_ago, color='yellow', alpha=0.3, label='10 ~ 20 days ago')

    ax.axvspan(data['date'].min(), twenty_six_days_ago, color='green', alpha=0.3, label='More than 20 days ago')

    # 軸ラベルとタイトルの設定
    ax.set_xlabel('Date')
    ax.set_ylabel('Precipitation (mm)')
    ax.set_title('Precipitation Time Series')

    # 凡例の設定
    ax.legend()

    # 日付フォーマットの設定（毎日表示）
    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45, fontsize=8)  # 日付ラベルを回転させてフォントサイズを小さく

    # プロットのレイアウト調整
    plt.subplots_adjust(bottom=0.2)

    # Streamlitでプロットを表示
    st.pyplot(fig)
