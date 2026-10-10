import pandas as pd
import streamlit as st

from src.custom_dataset import render_dataset_source
from src.dataset import CRITERIA_LABELS, CRITERIA_TYPES
from src.saw import hitung_nilai_akhir, normalisasi
from src.ui import (
    apply_steam_theme,
    render_steam_header,
    render_steam_table,
    render_steam_title,
)

apply_steam_theme("Perhitungan SAW - SPK Game PC")
data, dataset_name = render_dataset_source()

render_steam_header(
    "Detail Perhitungan SAW",
    f"Proses kalkulasi transparan dari matriks keputusan hingga ranking ({dataset_name}).",
    tag="CALCULATION PIPELINE",
)

if data.empty:
    st.info("Pilih dataset Steam atau upload CSV melalui sidebar untuk melakukan perhitungan.")
    st.stop()

with st.sidebar:
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

total_weight = sum(weight_columns.values())
if total_weight != 100:
    st.error(f"Total bobot kriteria harus berjumlah 100% (saat ini {total_weight}%).")
    st.stop()

weights = {name: value / 100 for name, value in weight_columns.items()}
st.session_state.bobot = weights
normalized = normalisasi(data, CRITERIA_TYPES)
results = hitung_nilai_akhir(normalized, weights)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "1. Matriks Keputusan (X)",
        "2. Normalisasi (R)",
        "3. Bobot Kriteria (W)",
        "4. Nilai Preferensi (V)",
        "5. Hasil Ranking",
    ]
)

with tab1:
    render_steam_title("1. Matriks Keputusan (X)", "calculator")
    st.caption("Matriks data mentah game yang digunakan sebagai alternatif penilaian.")
    decision_matrix = data[["Nama Game", *CRITERIA_TYPES]].rename(
        columns={"Rating_Positif": "Rating Positif"}
    )
    render_steam_table(decision_matrix)

with tab2:
    render_steam_title("2. Matriks Ter-normalisasi (R)", "calculator")
    st.caption("Hasil normalisasi metrik skala 0.00 hingga 1.00 sesuai atribut Cost & Benefit.")
    render_steam_table(normalized.round(4))

with tab3:
    render_steam_title("3. Vektor Bobot Kriteria (W)", "gear")
    st.caption("Vektor bobot yang digunakan untuk mengalikan matriks ter-normalisasi.")
    weight_table = pd.DataFrame(
        [
            {
                "Kriteria": CRITERIA_LABELS[name],
                "Jenis Atribut": CRITERIA_TYPES[name].upper(),
                "Bobot (%)": weight_columns[name],
                "Vektor Desimal (W)": weights[name],
            }
            for name in CRITERIA_TYPES
        ]
    )
    render_steam_table(weight_table)

with tab4:
    render_steam_title("4. Matriks Nilai Preferensi (V)", "calculator")
    st.caption("Penjumlahan hasil perkalian ter-normalisasi dengan bobot kriteria.")
    contribution_columns = [f"Kontribusi {name}" for name in CRITERIA_TYPES]
    preference = results[["Nama Game", *contribution_columns, "Nilai Akhir"]].copy()
    preference = preference.rename(
        columns={
            **{
                f"Kontribusi {name}": f"Kontribusi {CRITERIA_LABELS[name]}"
                for name in CRITERIA_TYPES
            },
            "Nilai Akhir": "Nilai Preferensi (V)",
        }
    )
    render_steam_table(preference.round(4))

with tab5:
    render_steam_title("5. Hasil Akhir Ranking SAW", "trophy")
    ranking = results[["Nama Game", "Nilai Akhir"]].copy()
    ranking.insert(0, "Rank", range(1, len(ranking) + 1))
    ranking = ranking.rename(columns={"Nilai Akhir": "Nilai SAW"})
    render_steam_table(ranking.round(4))
