from io import BytesIO
from typing import Iterable

import pandas as pd
import streamlit as st

from .dataset import CRITERIA_TYPES, load_data, map_game_dataset

COLUMN_ALIASES = {
    "Nama Game": ["name", "nama_game", "nama", "game", "game_name", "title"],
    "Harga": ["price", "harga", "cost"],
    "Metacritic": ["metacritic", "required_age", "age_rating", "usia"],
    "Rating_Positif": ["positive_ratings", "rating_positif", "positive", "likes"],
    "Playtime": ["average_playtime", "playtime", "waktu_main", "rata_rata_playtime"],
    "Genre": ["genres", "genre", "kategori"],
    "Developer": ["developer", "pengembang"],
}
EMPTY_GAME_DATA = pd.DataFrame(
    columns=["Nama Game", *CRITERIA_TYPES, "Genre", "Developer"]
)


def _normalize_name(value: object) -> str:
    return str(value).strip().lower().replace(" ", "_").replace("-", "_")


def _guess_column(columns: Iterable[str], target: str) -> str | None:
    normalized = {_normalize_name(column): column for column in columns}
    for alias in COLUMN_ALIASES[target]:
        key = _normalize_name(alias)
        if key in normalized:
            return normalized[key]
    for column in columns:
        key = _normalize_name(column)
        if any(_normalize_name(alias) in key for alias in COLUMN_ALIASES[target]):
            return column
    return None


def read_uploaded_csv(uploaded_file) -> pd.DataFrame:
    content = uploaded_file.getvalue()
    for encoding in ("utf-8", "utf-8-sig", "latin1"):
        try:
            return pd.read_csv(
                BytesIO(content), encoding=encoding, sep=None, engine="python"
            )
        except UnicodeDecodeError:
            continue
    return pd.read_csv(BytesIO(content), sep=None, engine="python")


def render_dataset_source() -> tuple[pd.DataFrame, str]:
    source_type = st.sidebar.radio(
        "Sumber dataset",
        ["Dataset Steam", "Upload CSV"],
        key="active_dataset_source",
    )
    if source_type == "Dataset Steam":
        return load_data(), "Dataset Steam"

    uploaded_file = st.sidebar.file_uploader(
        "Upload dataset game (CSV)",
        type=["csv"],
        key="active_dataset_upload",
    )
    if uploaded_file is None:
        st.sidebar.info("Upload CSV untuk menggunakan dataset sendiri.")
        return EMPTY_GAME_DATA.copy(), "Belum ada dataset"

    try:
        source = read_uploaded_csv(uploaded_file)
    except (OSError, UnicodeDecodeError, pd.errors.ParserError, ValueError) as exc:
        st.sidebar.error(f"CSV gagal dibaca: {exc}")
        return EMPTY_GAME_DATA.copy(), uploaded_file.name

    if source.empty:
        st.sidebar.error("CSV kosong. Pilih file yang memiliki data game.")
        return EMPTY_GAME_DATA.copy(), uploaded_file.name

    mapping: dict[str, str | None] = {}
    labels = {
        "Nama Game": "Nama game",
        "Harga": "Harga",
        "Metacritic": "Metacritic / usia minimum",
        "Rating_Positif": "Rating positif",
        "Playtime": "Rata-rata playtime",
        "Genre": "Genre (opsional)",
        "Developer": "Developer (opsional)",
    }
    required_fields = ["Nama Game", *CRITERIA_TYPES]
    options = [""] + list(source.columns)
    with st.sidebar.expander("Mapping kolom CSV", expanded=True):
        for target, label in labels.items():
            guessed = _guess_column(source.columns, target)
            default_index = options.index(guessed) if guessed in options else 0
            selected = st.selectbox(
                label,
                options,
                index=default_index,
                key=f"active_map_{target}",
            )
            mapping[target] = selected or None

    missing = [field for field in required_fields if not mapping.get(field)]
    if missing:
        st.sidebar.error(
            "Pilih kolom untuk: "
            + ", ".join(labels[field] for field in missing)
            + "."
        )
        return EMPTY_GAME_DATA.copy(), uploaded_file.name

    data = map_game_dataset(source, mapping)
    if data.empty:
        st.sidebar.error("CSV tidak memiliki baris game dengan nama yang valid.")
        return EMPTY_GAME_DATA.copy(), uploaded_file.name

    st.sidebar.success(f"Dataset upload aktif: {len(data)} game.")
    return data, uploaded_file.name
