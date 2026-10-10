import pandas as pd


def normalisasi(df, kriteria_sifat):
    df_norm = pd.DataFrame()
    if "Nama Game" in df.columns:
        df_norm["Nama Game"] = df["Nama Game"]
    
    for kolom, sifat in kriteria_sifat.items():
        if kolom not in df.columns:
            continue
        values = pd.to_numeric(df[kolom], errors="coerce").fillna(0)
        if sifat == 'cost':
            positive_values = values[values > 0]
            if positive_values.empty:
                df_norm[kolom] = 1.0
            else:
                minimum = positive_values.min()
                df_norm[kolom] = (minimum / values.where(values > 0)).fillna(1.0)
        elif sifat == 'benefit':
            maximum = values.max()
            df_norm[kolom] = values / maximum if maximum > 0 else 1.0
            
    return df_norm

def hitung_nilai_akhir(df_norm, bobot):
    df_hasil = pd.DataFrame()
    if "Nama Game" in df_norm.columns:
        df_hasil["Nama Game"] = df_norm["Nama Game"]

    nilai_akhir = pd.Series(0.0, index=df_norm.index)
    for kolom, nilai_bobot in bobot.items():
        if kolom not in df_norm.columns:
            continue
        contribution = df_norm[kolom] * nilai_bobot
        df_hasil[f"Kontribusi {kolom}"] = contribution
        nilai_akhir += contribution
        
    df_hasil['Nilai Akhir'] = nilai_akhir
    df_hasil = df_hasil.sort_values(
        by='Nilai Akhir', ascending=False, kind="stable"
    ).reset_index(drop=True)
    df_hasil.index = df_hasil.index + 1
    
    return df_hasil