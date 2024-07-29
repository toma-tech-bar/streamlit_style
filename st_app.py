import streamlit as st
import folium
from streamlit_folium import st_folium
import math

# 関数: 1km四方のメッシュを作成
def create_square(lat, lon, size_km):
    earth_radius = 6371.0  # 地球の半径 (km)
    d = size_km / (2 * earth_radius)
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    delta_lat = math.degrees(d)
    delta_lon = math.degrees(d / math.cos(lat_rad))
    
    top_left = (lat + delta_lat, lon - delta_lon)
    top_right = (lat + delta_lat, lon + delta_lon)
    bottom_right = (lat - delta_lat, lon + delta_lon)
    bottom_left = (lat - delta_lat, lon - delta_lon)
    
    return [top_left, top_right, bottom_right, bottom_left, top_left]

# Streamlitアプリの設定
st.set_page_config(
    page_title="1kmメッシュの可視化",
    page_icon="🗺️",
    layout="wide"
)

st.title("Streamlit Folium Mesh Example")

# 入力
latitude = st.number_input("緯度を入力", value=35.681236)
longitude = st.number_input("経度を入力", value=139.767125)
size_km = 1.0  # メッシュのサイズ (km)

# マップの初期化
map = folium.Map(location=[latitude, longitude], zoom_start=15)

# メッシュの作成
square_coords = create_square(latitude, longitude, size_km)

# メッシュを地図に追加
polygon = folium.Polygon(locations=square_coords, color='green', fill=True, fill_color='green', fill_opacity=0.25)
polygon.add_to(map)

# 中心点のマーカーを追加
folium.Marker(
    location=[latitude, longitude],
    popup="中心点",
    icon=folium.Icon(color="lightblue", icon="leaf")
).add_to(map)

# マップをStreamlitに表示
st_folium(map, width=800, height=400)

params = {
    "経度":longitude,
    "緯度":latitude
}

option_adress = st.selectbox("経度緯度の選択：", list(params.keys()))

if option_adress == "経度":
    st.write(f"経度の表示：{longitude}")
elif option_adress == "緯度":
    st.write(f"緯度の表示：{latitude}")


