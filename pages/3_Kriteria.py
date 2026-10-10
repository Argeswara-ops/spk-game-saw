import pandas as pd
import streamlit as st

from src.custom_dataset import render_dataset_source
from src.dataset import CRITERIA_LABELS, CRITERIA_TYPES
from src.ui import (
    SVG_ICONS,
    apply_steam_theme,
    render_steam_header,
    render_steam_table,
    render_steam_title,
)

apply_steam_theme("Kriteria - SPK Game PC")
_, dataset_name = render_dataset_source()

render_steam_header(
    "Kriteria & Pengaturan Bobot",
    f"Konfigurasi kriteria dan pembobotan metode SAW. Dataset aktif: {dataset_name}.",
    tag="CRITERIA SETUP",
)

default_weights = {
    "Harga": 20,
    "Metacritic": 30,
    "Rating_Positif": 30,
    "Playtime": 20,
}
criteria = pd.DataFrame(
    [
        {
            "Kode": f"C{index}",
            "Kriteria": CRITERIA_LABELS[name],
            "Atribut Dataset": name,
            "Sifat (Attribute)": criterion_type.upper(),
            "Bobot Default": f"{default_weights[name]}%",
        }
        for index, (name, criterion_type) in enumerate(CRITERIA_TYPES.items(), start=1)
    ]
)

render_steam_title("Daftar Kriteria SAW", "gear")
render_steam_table(criteria)

st.markdown("<br>", unsafe_allow_html=True)
render_steam_title("Simulasi Interactive Bobot (%)", "gear")
st.caption("Atur persentase bobot setiap kriteria sesuai prioritas Anda. Total bobot wajib bernilai **100%**.")

saved_weights = st.session_state.bobot
columns = st.columns(4)
weights = {}
for column, name in zip(columns, CRITERIA_TYPES):
    initial_value = round(saved_weights[name] * 100)
    weights[name] = column.number_input(
        f"{CRITERIA_LABELS[name]} (%)",
        min_value=0,
        max_value=100,
        value=initial_value,
        step=5,
        key=f"bobot_{name}",
    )

total = sum(weights.values())

m_col, status_col = st.columns([1, 3])
m_col.metric("Total Bobot", f"{total}%")

with status_col:
    if total == 100:
        st.success("Total bobot valid (100%). Siap digunakan pada kalkulasi SAW.")
    else:
        st.error(f"Total bobot harus berjumlah tepat 100% (saat ini {total}%). Sesuaikan kembali nilainya.")

if st.button("Simpan Konfigurasi Bobot", type="primary"):
    if total != 100:
        st.error("Bobot gagal disimpan! Pastikan total seluruh bobot bernilai 100%.")
    else:
        st.session_state.bobot = {
            name: value / total for name, value in weights.items()
        }
        st.success("Konfigurasi bobot kriteria berhasil disimpan!")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div style="background: rgba(21, 34, 50, 0.8); border: 1px solid #2a475e; border-left: 4px solid #66c0f4; border-radius: 8px; padding: 18px 24px;">
        <h4 style="color: #66c0f4; margin-top: 0; font-family: 'Rajdhani', sans-serif;">{SVG_ICONS['info']} Formula Normalisasi Metrik SAW</h4>
        <ul style="color: #8ba2b5; margin-bottom: 0; padding-left: 20px; line-height: 1.6;">
            <li><b>Cost (Harga):</b> R<sub>ij</sub> = Min(X<sub>ij</sub>) / X<sub>ij</sub>. Semakin murah harga game (bahkan gratis), semakin tinggi skor preferensinya.</li>
            <li><b>Benefit (Metacritic, Rating Positif, Playtime):</b> R<sub>ij</sub> = X<sub>ij</sub> / Max(X<sub>ij</sub>). Semakin tinggi nilainya, semakin baik skor preferensinya.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
