# SPK Game SAW

A Streamlit‑based Decision Support System (DSS) for selecting Steam PC games using the Simple Additive Weighting (SAW) method.

## Overview
- **Tech stack**: Python, Streamlit, Pandas, NumPy.
- **Features**:
  - Load the default Steam dataset (`data/raw/steam.csv`).
  - Upload your own CSV with the same columns.
  - Adjust criteria weights (price, Metacritic, positive ratings, playtime).
  - View a dashboard, ranking cards, and the raw data preview.
  - All UI follows a dark/steam‑themed design.

## Prerequisites
- Windows 10/11 (PowerShell or CMD)
- Python 3.10+ (already installed on your system)
- Git (for cloning / pushing)

## Quick start (local clone)
```powershell
# 1️⃣ Clone the repo
git clone https://github.com/Argeswara-ops/spk-game-saw.git
cd spk-game-saw

# 2️⃣ Create a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell (or .\.venv\Scripts\activate.bat for CMD)

# 3️⃣ Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4️⃣ Run the app
streamlit run app.py
```
The app will start on `http://localhost:8501` (or `8502` if the default port is taken). Open the URL in a browser.

## Dataset
- The default dataset is located at `data/raw/steam.csv` (≈5 MB).
- If you want to use a custom CSV, select **“Upload CSV”** from the sidebar and map the columns accordingly.
- Required columns for the SAW calculation are:
  - `Nama Game` (or any column mapped to it)
  - `Harga`
  - `Metacritic`
  - `Rating_Positif`
  - `Playtime`

## Project structure
```
spk-game-saw/
│   app.py                # Streamlit entry‑point
│   requirements.txt
│   README.md             # ← this file
│
├─ data/
│   ├─ raw/               # Default CSV files
│   └─ processed/         # (optional) processed outputs
│
├─ pages/                 # Streamlit pages (Dashboard, Dataset, Kriteria, Ranking)
├─ src/                    # Core logic (UI helpers, dataset handling)
│   ├─ ui.py               # UI components & theming
│   └─ dataset.py          # Data loading & preprocessing
└─ .gitignore
```

## Development notes
- UI components are defined in `src/ui.py` – feel free to tweak colors or layout.
- The SAW calculation lives in `pages/4_Perhitungan_SAW.py`.
- To add new pages, create a new `.py` file inside `pages/` and add a navigation entry in `app.py`.

## Updating the repo
```powershell
# After making changes
git add -A
git commit -m "Your descriptive message"
git push origin main
```
---
*Enjoy exploring game recommendations!*
