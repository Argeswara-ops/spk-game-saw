import math

import streamlit as st

from src.custom_dataset import render_dataset_source
from src.dataset import format_price
from src.ui import (
    apply_steam_theme,
    render_steam_header,
    render_steam_table,
    render_steam_title,
)

apply_steam_theme("Dataset - SPK Game PC")
data, dataset_name = render_dataset_source()

render_steam_header(
    "Katalog & Search Dataset",
    f"Data aktif: {dataset_name}. Cari, saring, dan telusuri katalog alternatif game.",
    tag="DATABASE GAME",
)

if data.empty:
    st.info("Pilih dataset Steam atau upload CSV melalui sidebar untuk menampilkan data.")
    st.stop()

genre_values = []
if "Genre" in data:
    genre_values = sorted(
        {
            genre.strip()
            for value in data["Genre"].dropna()
            for genre in str(value).split(";")
            if genre.strip()
        }
    )

render_steam_title("Pencarian & Filter Dataset", "search")
search_column, genre_column = st.columns([2, 1])
search = search_column.text_input(
    "Cari Nama Game / Developer",
    placeholder="Contoh: Counter-Strike, Dota, Valve...",
)
selected_genre = genre_column.selectbox("Filter Genre", ["Semua Genre", *genre_values])

filtered = data.copy()
if search:
    searchable = ["Nama Game", "Genre", "Developer"]
    searchable = [column for column in searchable if column in filtered.columns]
    matches = filtered[searchable].fillna("").astype(str).apply(
        lambda column: column.str.contains(search, case=False, regex=False)
    )
    filtered = filtered[matches.any(axis=1)]

if selected_genre != "Semua Genre":
    filtered = filtered[
        filtered["Genre"].fillna("").map(
            lambda value: selected_genre
            in [genre.strip() for genre in str(value).split(";")]
        )
    ]

st.markdown("<br>", unsafe_allow_html=True)
p_col1, p_col2, p_col3 = st.columns([2, 1, 1])
with p_col1:
    st.caption(f"Menampilkan **{len(filtered)}** game yang sesuai dengan kriteria filter.")

page_size = p_col2.selectbox("Jumlah per halaman", [10, 25, 50], index=0)
total_pages = max(1, math.ceil(len(filtered) / page_size))
page = p_col3.selectbox("Halaman", list(range(1, total_pages + 1)))

start = (page - 1) * page_size
display = filtered.iloc[start : start + page_size].copy()
display["Harga"] = display["Harga"].map(format_price)
display = display.rename(columns={"Rating_Positif": "Rating Positif"})

render_steam_table(display)
