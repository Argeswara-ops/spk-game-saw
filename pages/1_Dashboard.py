import pandas as pd
import streamlit as st

from src.custom_dataset import render_dataset_source
from src.dataset import format_price
from src.ui import apply_steam_theme, render_steam_header, render_steam_title

apply_steam_theme("Dashboard - SPK Game PC")
data, dataset_name = render_dataset_source()

render_steam_header(
    "Dashboard Analytics",
    f"Ringkasan statistik & visualisasi dataset aktif: {dataset_name}.",
    tag="DASHBOARD ANALYTICS",
)

if data.empty:
    st.info("Pilih dataset Steam atau upload CSV melalui sidebar untuk melihat dashboard.")
    st.stop()

total_games = len(data)
total_genres = (
    data["Genre"].str.split(";").explode().str.strip().replace("", pd.NA).nunique()
    if "Genre" in data
    else 0
)
average_price = data["Harga"].mean()
free_games = int((data["Harga"] == 0).sum())

metric_columns = st.columns(4)
metric_columns[0].metric("Total Game", f"{total_games:,}".replace(",", "."))
metric_columns[1].metric("Kategori Genre", f"{total_genres:,}".replace(",", "."))
metric_columns[2].metric("Rata-Rata Harga", format_price(average_price))
metric_columns[3].metric("Game Gratis (Free)", f"{free_games:,}".replace(",", "."))

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns(2)
with left:
    if "Genre" in data and data["Genre"].str.strip().ne("").any():
        genre_counts = (
            data.assign(Genre=data["Genre"].str.split(";"))
            .explode("Genre")
            .assign(Genre=lambda frame: frame["Genre"].str.strip())
            .query("Genre != ''")["Genre"]
            .value_counts()
            .head(10)
            .sort_values()
        )
        render_steam_title("Top 10 Genre Game", "chart")
        st.bar_chart(genre_counts, color="#66c0f4")
    else:
        st.info("Kolom genre tidak tersedia pada dataset ini.")

with right:
    render_steam_title("Distribusi Sebaran Harga", "chart")
    price_counts = data["Harga"].value_counts().sort_index().rename("Jumlah Game")
    st.line_chart(price_counts, color="#199fff")

st.markdown("<br>", unsafe_allow_html=True)
render_steam_title("Ringkasan Statistik Harga", "dollar")

price_columns = st.columns(4)
price_columns[0].metric("Harga Minimum", format_price(data["Harga"].min()))
price_columns[1].metric("Harga Median", format_price(data["Harga"].median()))
price_columns[2].metric("Harga Maksimum", format_price(data["Harga"].max()))
price_columns[3].metric("Total Game Gratis", f"{free_games:,}".replace(",", "."))
