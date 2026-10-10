import streamlit as st

from src.custom_dataset import render_dataset_source
from src.ui import (
    SVG_ICONS,
    apply_steam_theme,
    render_steam_header,
    render_steam_table,
    render_steam_title,
)

apply_steam_theme("SPK Game PC - Steam Client")
data, dataset_name = render_dataset_source()

render_steam_header(
    "SPK Pemilihan Game PC",
    "Sistem Pendukung Keputusan Pemilihan Game Steam Menggunakan Metode Simple Additive Weighting (SAW).",
    tag="STEAM SAW ENGINE",
)

st.markdown(
    """
    Selamat datang di platform **Decision Support System Pemilihan Game Steam**.
    Gunakan menu navigasi di sidebar untuk mengeksplorasi dataset, menyesuaikan bobot kriteria,
    melihat kalkulasi matriks SAW secara transparan, dan menentukan rekomendasi game PC terbaik sesuai preferensi Anda.
    """
)

st.markdown("<br>", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
m1.metric("Sumber Dataset", dataset_name)
m2.metric("Total Game Siap Dihitung", f"{len(data):,}".replace(",", "."))
m3.metric("Metode SPK", "SAW (Simple Additive Weighting)")

st.markdown("<br>", unsafe_allow_html=True)

if data.empty:
    st.info("Pilih dataset Steam atau upload CSV melalui panel di sidebar untuk memulai.")
else:
    render_steam_title("Pratinjau Katalog Game", "game")
    preview_df = (
        data[["Nama Game", "Harga", "Metacritic", "Rating_Positif", "Playtime"]]
        .head(5)
        .rename(columns={"Rating_Positif": "Rating Positif", "Playtime": "Playtime (Menit)"})
    )
    render_steam_table(preview_df)

st.markdown("<br>", unsafe_allow_html=True)
render_steam_title("Fitur Utama Platform", "gear")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        f"""
        <div style="background: rgba(21, 34, 50, 0.8); border: 1px solid #2a475e; border-top: 3px solid #66c0f4; border-radius: 8px; padding: 18px 20px;">
            <h4 style="color: #ffffff; margin-top: 0;">{SVG_ICONS['chart']} 1. Dashboard Analytics</h4>
            <p style="color: #8ba2b5; font-size: 0.9rem;">Ringkasan statistik game, sebaran harga, genre terbanyak, serta distribusi atribut game.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="background: rgba(21, 34, 50, 0.8); border: 1px solid #2a475e; border-top: 3px solid #66c0f4; border-radius: 8px; padding: 18px 20px;">
            <h4 style="color: #ffffff; margin-top: 0;">{SVG_ICONS['gear']} 2. Simulasi Kriteria</h4>
            <p style="color: #8ba2b5; font-size: 0.9rem;">Atur bobot kriteria (Harga, Metacritic, Rating Positif, Playtime) secara interaktif sesuai keinginan.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div style="background: rgba(21, 34, 50, 0.8); border: 1px solid #2a475e; border-top: 3px solid #66c0f4; border-radius: 8px; padding: 18px 20px;">
            <h4 style="color: #ffffff; margin-top: 0;">{SVG_ICONS['trophy']} 3. Ranking & Detail Game</h4>
            <p style="color: #8ba2b5; font-size: 0.9rem;">Dapatkan rekomendasi ranking game teratas lengkap dengan kartu skor dan unduhan CSV.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
