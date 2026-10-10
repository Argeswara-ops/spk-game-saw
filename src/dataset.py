from pathlib import Path

import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "steam.csv"
CRITERIA_TYPES = {
    "Harga": "cost",
    "Metacritic": "benefit",
    "Rating_Positif": "benefit",
    "Playtime": "benefit",
}
CRITERIA_LABELS = {
    "Harga": "Harga",
    "Metacritic": "Metacritic",
    "Rating_Positif": "Rating Positif",
    "Playtime": "Playtime",
}


def format_price(value: float | int) -> str:
    amount = float(value)
    return "Gratis" if amount == 0 else f"${amount:,.2f}"


def map_game_dataset(source: pd.DataFrame, mapping: dict[str, str | None]) -> pd.DataFrame:
    mapped = pd.DataFrame(index=source.index)
    for target, source_column in mapping.items():
        if source_column and source_column in source.columns:
            mapped[target] = source[source_column]

    if "Nama Game" not in mapped:
        mapped["Nama Game"] = [f"Game {index + 1}" for index in range(len(source))]

    for column in CRITERIA_TYPES:
        if column not in mapped:
            mapped[column] = 0
        mapped[column] = pd.to_numeric(mapped[column], errors="coerce").fillna(0)

    for optional_column in ("Genre", "Developer"):
        if optional_column not in mapped:
            mapped[optional_column] = ""
        mapped[optional_column] = mapped[optional_column].fillna("").astype(str)

    mapped["Nama Game"] = mapped["Nama Game"].fillna("").astype(str).str.strip()
    mapped = mapped[mapped["Nama Game"] != ""]
    return mapped.reset_index(drop=True)


@st.cache_data
def load_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        st.error(f"File dataset tidak ditemukan: {DATA_PATH}")
        return pd.DataFrame(columns=["Nama Game", *CRITERIA_TYPES, "Genre", "Developer"])

    try:
        source = pd.read_csv(DATA_PATH)
    except (OSError, pd.errors.ParserError, UnicodeDecodeError) as exc:
        st.error(f"Dataset Steam gagal dibaca: {exc}")
        return pd.DataFrame(columns=["Nama Game", *CRITERIA_TYPES, "Genre", "Developer"])

    name_column = "name" if "name" in source.columns else None
    price_column = "price" if "price" in source.columns else None
    metacritic_column = "metacritic" if "metacritic" in source.columns else "required_age"
    positive_column = "positive_ratings" if "positive_ratings" in source.columns else None
    playtime_column = "average_playtime" if "average_playtime" in source.columns else None

    required_columns = {
        "name": name_column,
        "price": price_column,
        "rating": metacritic_column if metacritic_column in source.columns else None,
        "positive_ratings": positive_column,
        "average_playtime": playtime_column,
    }
    missing_columns = [name for name, column in required_columns.items() if column is None]
    if missing_columns:
        st.error(f"Dataset Steam tidak memiliki kolom yang diperlukan: {', '.join(missing_columns)}.")
        return pd.DataFrame(columns=["Nama Game", *CRITERIA_TYPES, "Genre", "Developer"])

    mapping = {
        "Nama Game": name_column,
        "Harga": price_column,
        "Metacritic": metacritic_column,
        "Rating_Positif": positive_column,
        "Playtime": playtime_column,
        "Genre": "genres" if "genres" in source.columns else None,
        "Developer": "developer" if "developer" in source.columns else None,
    }
    return map_game_dataset(source, mapping)
