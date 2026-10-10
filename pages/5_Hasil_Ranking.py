import pandas as pd
import streamlit as st

from src.custom_dataset import render_dataset_source
from src.dataset import CRITERIA_LABELS, CRITERIA_TYPES, format_price
from src.saw import hitung_nilai_akhir, normalisasi
from src.ui import (
    SVG_ICONS,
    apply_steam_theme,
    render_steam_header,
    render_steam_table,
    render_steam_title,
    render_top_game_cards,
)

apply_steam_theme("Hasil Ranking - SPK Game PC")
data, dataset_name = render_dataset_source()

render_steam_header(
    "Hasil Ranking & Rekomendasi Game",
    f"Rekomendasi game Steam terbaik diurutkan berdasarkan skor preferensi SAW ({dataset_name}).",
    tag="RECOMMENDATION",
)

if data.empty:
    st.info("Pilih dataset Steam atau upload CSV melalui sidebar untuk melihat ranking.")
    st.stop()

with st.sidebar:
    st.header("Filter Game")
    genres = sorted(
        {
            genre.strip()
            for value in data["Genre"].dropna()
            for genre in str(value).split(";")
            if genre.strip()
        }
    )
    selected_genre = st.selectbox("Genre Game", ["Semua Genre", *genres])
    maximum_price = max(float(data["Harga"].max()), 1.0)
    max_price = st.slider(
        "Harga Maksimum ($)",
        min_value=0.0,
        max_value=maximum_price,
        value=maximum_price,
        step=0.5,
    )

    st.header("Penyesuaian Bobot")
    weight_columns = {}
    for name in CRITERIA_TYPES:
        weight_columns[name] = st.number_input(
            CRITERIA_LABELS[name],
            min_value=0,
            max_value=100,
            value=round(st.session_state.bobot[name] * 100),
            step=5,
            key=f"bobot_{name}",
        )

filtered = data[data["Harga"] <= max_price].copy()
if selected_genre != "Semua Genre":
    filtered = filtered[
        filtered["Genre"].fillna("").map(
            lambda value: selected_genre
            in [genre.strip() for genre in str(value).split(";")]
        )
    ]

total_weight = sum(weight_columns.values())
if total_weight != 100:
    st.error(f"Total bobot harus berjumlah 100% (saat ini {total_weight}%).")
    st.stop()

if filtered.empty:
    st.warning("Tidak ada game yang cocok dengan filter yang Anda pilih.")
    st.stop()

weights = {name: value / 100 for name, value in weight_columns.items()}
st.session_state.bobot = weights
normalized = normalisasi(filtered, CRITERIA_TYPES)
results = hitung_nilai_akhir(normalized, weights)
results.insert(0, "Rank", range(1, len(results) + 1))

ranking = results.merge(
    filtered[["Nama Game", "Harga", "Genre", "Developer"]],
    on="Nama Game",
    how="left",
)
ranking["Harga"] = ranking["Harga"].map(format_price)
ranking = ranking.rename(
    columns={
        "Nama Game": "Nama Game",
        "Rating_Positif": "Rating Positif",
        "Nilai Akhir": "Nilai SAW",
    }
)

render_steam_title("Top Game Rekomendasi SAW", "trophy")
render_top_game_cards(ranking, top_n=3)

st.markdown("<br>", unsafe_allow_html=True)
render_steam_title("Tabel Ranking Game Lengkap", "chart")
render_steam_table(ranking[["Rank", "Nama Game", "Genre", "Harga", "Nilai SAW"]].round(4))

if ranking.empty:
    st.warning("Tidak ada data game untuk ditampilkan.")
    st.stop()

st.markdown("<br>", unsafe_allow_html=True)
render_steam_title("Detail Inspeksi Game", "search")
selected_name = st.selectbox("Pilih game untuk melihat rincian:", ranking["Nama Game"].tolist())
result_row = results[results["Nama Game"] == selected_name].iloc[0]
game_row = filtered[filtered["Nama Game"] == selected_name].iloc[0]

detail_col, score_col = st.columns([3, 1])
with detail_col:
    st.markdown(
        f"""
        <div style="background: rgba(21, 34, 50, 0.85); border: 1px solid #2a475e; border-top: 3px solid #66c0f4; border-radius: 8px; padding: 20px 24px; margin-bottom: 16px;">
            <h3 style="color: #ffffff; margin-top: 0; display: flex; align-items: center;">{SVG_ICONS['game']} {selected_name}</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 14px; color: #c7d5e0; font-size: 0.95rem;">
                <div><b>Developer:</b> {game_row['Developer'] or 'Tidak tersedia'}</div>
                <div><b>Genre:</b> {game_row['Genre'] or 'Tidak tersedia'}</div>
                <div><b>Harga:</b> <span style="color: #a3e635; font-weight: 700;">{format_price(game_row['Harga'])}</span></div>
                <div><b>Metacritic / Rating Usia:</b> {game_row['Metacritic']}</div>
                <div><b>Rating Positif User:</b> {game_row['Rating_Positif']:,} ulasan</div>
                <div><b>Rata-rata Playtime:</b> {game_row['Playtime']:,} menit</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with score_col:
    st.metric("Peringkat Game", f"Rank #{int(result_row['Rank'])}")
    st.metric("Skor SAW", f"{result_row['Nilai Akhir']:.4f}")

st.markdown("<br>", unsafe_allow_html=True)
render_steam_title("Analisis Kontribusi Kriteria Penilaian", "chart")
contributions = pd.DataFrame(
    {
        "Kontribusi Skor": [
            result_row[f"Kontribusi {name}"] for name in CRITERIA_TYPES
        ]
    },
    index=[CRITERIA_LABELS[name] for name in CRITERIA_TYPES],
)
st.bar_chart(contributions, color="#66c0f4")

st.markdown("<br>", unsafe_allow_html=True)
csv_data = ranking.to_csv(index=False).encode("utf-8-sig")
st.download_button(
    "Download Hasil Ranking CSV",
    data=csv_data,
    file_name="ranking_game_steam_saw.csv",
    mime="text/csv",
    type="primary",
)
