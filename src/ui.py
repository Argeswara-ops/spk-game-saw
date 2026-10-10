import streamlit as st

SVG_ICONS = {
    "game": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M6 11h4M8 9v4M15 10a1 1 0 100-2 1 1 0 000 2zM18 13a1 1 0 100-2 1 1 0 000 2z"/><rect x="2" y="6" width="20" height="12" rx="4"/></svg>',
    "chart": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>',
    "database": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
    "gear": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-2 2 2 2 0 01-2-2v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83 0 2 2 0 010-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 01-2-2 2 2 0 012-2h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 010-2.83 2 2 0 012.83 0l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 012-2 2 2 0 012 2v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 0 2 2 0 010 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 012 2 2 2 0 01-2 2h-.09a1.65 1.65 0 00-1.51 1z"/></svg>',
    "calculator": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"/></svg>',
    "trophy": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#f39c12" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M6 9H4.5a2.5 2.5 0 010-5H6M18 9h1.5a2.5 2.5 0 000-5H18M4 22h16M10 14.66V17c0 .55-.45 1-1 1H7M14 14.66V17c0 .55.45 1 1 1h2M18 4H6v7a6 6 0 0012 0V4z"/></svg>',
    "search": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    "tag": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>',
    "dollar": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#75b022" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>',
    "download": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
    "filter": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>',
    "star": '<svg width="16" height="16" viewBox="0 0 24 24" fill="#66c0f4" stroke="#66c0f4" stroke-width="1" style="vertical-align: middle; margin-right: 4px;"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    "clock": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#aebdca" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    "info": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#66c0f4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>',
}


def apply_steam_theme(page_title: str) -> None:
    st.set_page_config(
        page_title=page_title,
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    if "bobot" not in st.session_state:
        st.session_state.bobot = {
            "Harga": 0.2,
            "Metacritic": 0.3,
            "Rating_Positif": 0.3,
            "Playtime": 0.2,
        }

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Rajdhani:wght@600;700;800&display=swap');

        :root {
            --steam-bg-dark: #080c14;
            --steam-bg-mid: #0e1520;
            --steam-bg-card: #152232;
            --steam-bg-card-hover: #1c2d42;
            --steam-blue-light: #66c0f4;
            --steam-blue-vivid: #199fff;
            --steam-blue-glow: rgba(102, 192, 244, 0.4);
            --steam-border: #2a475e;
            --steam-border-bright: #3d6f99;
            --steam-text-muted: #8ba2b5;
            --steam-text-bright: #f5f7fa;
            --steam-green: #75b022;
            --steam-green-hover: #8ed629;
            --steam-gold: #f39c12;
            --steam-silver: #bdc3c7;
            --steam-bronze: #e67e22;
        }

        /* Reset & Base Fonts */
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        }

        .stApp {
            background: 
                radial-gradient(circle at 50% -10%, rgba(102, 192, 244, 0.15) 0%, transparent 60%),
                radial-gradient(circle at 85% 30%, rgba(25, 159, 255, 0.08) 0%, transparent 50%),
                linear-gradient(180deg, #070a10 0%, #0d141e 40%, #121a26 100%) !important;
            background-attachment: fixed !important;
            color: var(--steam-text-bright);
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #070a10;
        }
        ::-webkit-scrollbar-thumb {
            background: #2a475e;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #66c0f4;
        }

        /* Header Navigation */
        [data-testid="stHeader"] {
            background: rgba(7, 10, 16, 0.88) !important;
            backdrop-filter: blur(14px) !important;
            border-bottom: 1px solid rgba(42, 71, 94, 0.6);
        }

        /* Sidebar Container */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0b111a 0%, #101722 100%) !important;
            border-right: 1px solid var(--steam-border) !important;
            box-shadow: 6px 0 25px rgba(0, 0, 0, 0.6);
        }

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
            color: var(--steam-blue-light) !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 1.2px !important;
            border-bottom: 1px solid var(--steam-border);
            padding-bottom: 6px;
            margin-top: 1.2rem;
        }

        /* Sidebar Labels */
        [data-testid="stSidebar"] label,
        [data-testid="stWidgetLabel"] p {
            color: var(--steam-blue-light) !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.8px !important;
            text-transform: uppercase !important;
        }

        /* Navigation Links in Sidebar */
        [data-testid="stSidebarNav"] {
            padding-top: 0.5rem;
        }
        [data-testid="stSidebarNav"] li a {
            border-radius: 6px !important;
            margin: 3px 0 !important;
            padding: 9px 14px !important;
            transition: all 0.2s ease !important;
            color: #b0c3d4 !important;
            background: rgba(14, 21, 30, 0.5) !important;
            border: 1px solid transparent !important;
        }
        [data-testid="stSidebarNav"] li a span {
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1.05rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.5px !important;
        }
        [data-testid="stSidebarNav"] li a:hover {
            background: rgba(102, 192, 244, 0.14) !important;
            color: var(--steam-blue-light) !important;
            border-color: rgba(102, 192, 244, 0.3) !important;
        }
        [data-testid="stSidebarNav"] li a[aria-current="page"] {
            background: linear-gradient(90deg, rgba(102, 192, 244, 0.25) 0%, rgba(25, 159, 255, 0.08) 100%) !important;
            border-left: 4px solid var(--steam-blue-light) !important;
            border-color: rgba(102, 192, 244, 0.4) !important;
            font-weight: 800 !important;
            color: #ffffff !important;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3) !important;
        }

        /* Block Layout */
        .block-container {
            max-width: 1380px;
            padding-top: 1.2rem;
            padding-bottom: 4rem;
        }

        /* Headings */
        h1, h2, h3, h4 {
            color: #ffffff !important;
            font-family: 'Rajdhani', 'Inter', sans-serif !important;
            letter-spacing: 0.5px !important;
        }
        h1 {
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            text-shadow: 0 0 15px rgba(102, 192, 244, 0.3);
        }
        h2 {
            font-size: 1.6rem !important;
            font-weight: 700 !important;
            margin-top: 1.2rem !important;
            margin-bottom: 0.8rem !important;
        }
        h3 {
            font-size: 1.3rem !important;
            font-weight: 700 !important;
        }

        [data-testid="stMarkdownContainer"] p,
        [data-testid="stCaptionContainer"] {
            color: var(--steam-text-muted) !important;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        /* Streamlit Native Metric Cards */
        [data-testid="stMetric"] {
            background: linear-gradient(135deg, rgba(21, 34, 50, 0.9) 0%, rgba(13, 20, 30, 0.95) 100%) !important;
            border: 1px solid var(--steam-border) !important;
            border-top: 3px solid var(--steam-blue-light) !important;
            border-radius: 8px !important;
            padding: 16px 20px !important;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.4) !important;
            transition: all 0.25s ease-in-out !important;
        }
        [data-testid="stMetric"]:hover {
            border-color: var(--steam-blue-light) !important;
            box-shadow: 0 0 20px var(--steam-blue-glow) !important;
            transform: translateY(-2px) !important;
        }
        [data-testid="stMetricLabel"] {
            color: var(--steam-text-muted) !important;
            font-size: 0.85rem !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
        }
        [data-testid="stMetricValue"] {
            color: var(--steam-blue-light) !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 2rem !important;
            font-weight: 800 !important;
            text-shadow: 0 0 10px rgba(102, 192, 244, 0.4) !important;
        }

        /* Buttons & Download Buttons (Steam Green/Blue Premium) */
        [data-testid="stButton"] button,
        [data-testid="stDownloadButton"] button {
            background: linear-gradient(90deg, #75b022 0%, #588a1b 100%) !important;
            color: #ffffff !important;
            border: 1px solid #75b022 !important;
            border-radius: 4px !important;
            padding: 0.6rem 1.5rem !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1.05rem !important;
            font-weight: 800 !important;
            letter-spacing: 1px !important;
            text-transform: uppercase !important;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6) !important;
            box-shadow: 0 4px 15px rgba(117, 176, 34, 0.4) !important;
            transition: all 0.25s ease-in-out !important;
        }
        [data-testid="stButton"] button:hover,
        [data-testid="stDownloadButton"] button:hover {
            background: linear-gradient(90deg, #8ed629 0%, #689e22 100%) !important;
            box-shadow: 0 0 25px rgba(142, 214, 41, 0.6) !important;
            transform: translateY(-2px) !important;
            color: #ffffff !important;
        }

        /* BaseWeb Select Box Base & Inner Containers (Eliminate White Backgrounds) */
        [data-testid="stSelectbox"] div[data-baseweb="select"],
        div[data-baseweb="select"],
        div[data-baseweb="select"] > div,
        div[data-baseweb="select"] > div > div,
        [data-testid="stSelectbox"] div[role="combobox"] {
            background-color: #0b1118 !important;
            border-color: var(--steam-border) !important;
            color: #ffffff !important;
            border-radius: 6px !important;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.4) !important;
            transition: all 0.2s ease !important;
        }
        div[data-baseweb="select"] span,
        div[data-baseweb="select"] div {
            color: #ffffff !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 0.95rem !important;
        }
        div[data-baseweb="select"] svg {
            fill: var(--steam-blue-light) !important;
            color: var(--steam-blue-light) !important;
        }
        div[data-baseweb="select"]:hover > div {
            border-color: var(--steam-blue-light) !important;
            box-shadow: 0 0 10px var(--steam-blue-glow) !important;
        }

        /* Select Popover / Dropdown Menu Items */
        [data-baseweb="popover"] ul,
        [data-baseweb="menu"] {
            background-color: #0e1622 !important;
            border: 1px solid var(--steam-border) !important;
            border-radius: 6px !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6) !important;
        }
        [data-baseweb="popover"] li,
        [data-baseweb="menu"] [role="option"] {
            background-color: #0e1622 !important;
            color: #c7d5e0 !important;
            font-family: 'Inter', sans-serif !important;
        }
        [data-baseweb="popover"] li:hover,
        [data-baseweb="menu"] [role="option"]:hover,
        [data-baseweb="popover"] li[aria-selected="true"] {
            background: linear-gradient(90deg, rgba(102, 192, 244, 0.25) 0%, rgba(25, 159, 255, 0.1) 100%) !important;
            color: var(--steam-blue-light) !important;
            font-weight: 600 !important;
        }

        /* Radio Buttons (Steam Mode Selector) */
        [data-testid="stRadio"] [role="radiogroup"] label {
            background: #0d1520 !important;
            border: 1px solid var(--steam-border) !important;
            border-radius: 6px !important;
            padding: 8px 14px !important;
            margin: 4px 0 !important;
            transition: all 0.2s ease !important;
            color: #c7d5e0 !important;
            cursor: pointer !important;
        }
        [data-testid="stRadio"] [role="radiogroup"] label:hover {
            border-color: var(--steam-blue-light) !important;
            color: #ffffff !important;
            background: rgba(102, 192, 244, 0.1) !important;
        }
        [data-testid="stRadio"] [role="radiogroup"] label p {
            color: #c7d5e0 !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 0.95rem !important;
        }
        [data-testid="stRadio"] div[data-aria-checked="true"] {
            background-color: var(--steam-blue-light) !important;
            border-color: var(--steam-blue-light) !important;
        }

        /* Sliders Override */
        [data-baseweb="slider"] div[role="slider"] {
            background-color: var(--steam-blue-light) !important;
            border: 2px solid #ffffff !important;
            box-shadow: 0 0 12px rgba(102, 192, 244, 0.9) !important;
        }
        [data-baseweb="slider"] div[data-testid="stSliderTrack"] > div {
            background: linear-gradient(90deg, #199fff 0%, #66c0f4 100%) !important;
        }

        /* Number Inputs Override */
        [data-testid="stNumberInput"] input {
            background-color: #0b1118 !important;
            border: 1px solid var(--steam-border) !important;
            color: var(--steam-blue-light) !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
        }
        [data-testid="stNumberInput"] button {
            background-color: #14202d !important;
            color: var(--steam-blue-light) !important;
            border-color: var(--steam-border) !important;
        }
        [data-testid="stNumberInput"] button:hover {
            background-color: #1d2f42 !important;
            color: #ffffff !important;
        }

        /* Text Input Override */
        [data-testid="stTextInput"] input {
            background-color: #0b1118 !important;
            border: 1px solid var(--steam-border) !important;
            border-radius: 6px !important;
            color: #ffffff !important;
            padding-left: 12px !important;
        }
        [data-testid="stTextInput"] input:focus {
            border-color: var(--steam-blue-light) !important;
            box-shadow: 0 0 12px var(--steam-blue-glow) !important;
        }

        /* Charts Background Overrides (Remove White Canvas) */
        [data-testid="stVegaLiteChart"],
        [data-testid="stVegaLiteChart"] > div,
        .vega-embed,
        .vega-embed canvas,
        .vega-embed svg {
            background-color: transparent !important;
            background: transparent !important;
            border-radius: 8px !important;
        }
        .vega-embed svg text {
            fill: #8ba2b5 !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 11px !important;
        }
        .vega-embed svg line, .vega-embed svg path.domain {
            stroke: #2a475e !important;
        }

        /* Tabs Override */
        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            background: rgba(11, 17, 26, 0.8);
            border-bottom: 2px solid var(--steam-border);
            gap: 8px;
            padding: 6px 6px 0 6px;
            border-radius: 8px 8px 0 0;
        }
        [data-testid="stTabs"] [data-baseweb="tab"] {
            background: transparent;
            color: var(--steam-text-muted);
            font-family: 'Rajdhani', sans-serif;
            font-weight: 700;
            font-size: 1rem;
            border-radius: 6px 6px 0 0;
            padding: 10px 18px;
            border: 1px solid transparent;
            transition: all 0.2s ease;
        }
        [data-testid="stTabs"] [data-baseweb="tab"]:hover {
            color: #ffffff;
            background: rgba(102, 192, 244, 0.1);
        }
        [data-testid="stTabs"] [aria-selected="true"] {
            background: linear-gradient(180deg, #152334 0%, #0f1926 100%) !important;
            color: var(--steam-blue-light) !important;
            border: 1px solid var(--steam-border) !important;
            border-bottom: 2px solid var(--steam-blue-light) !important;
            box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.3) !important;
        }

        /* Streamlit Native DataFrame Override */
        [data-testid="stDataFrame"], [data-testid="stTable"] {
            background-color: rgba(14, 21, 30, 0.8) !important;
            border: 1px solid var(--steam-border) !important;
            border-radius: 8px !important;
            overflow: hidden !important;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.4) !important;
        }

        /* Alerts Override */
        [data-testid="stAlert"] {
            background-color: rgba(21, 34, 50, 0.95) !important;
            border: 1px solid var(--steam-border) !important;
            border-left: 4px solid var(--steam-blue-light) !important;
            color: var(--steam-text-bright) !important;
            border-radius: 8px !important;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3) !important;
        }

        /* Steam HTML Table */
        .steam-table-container {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 16px 0;
            border: 1px solid var(--steam-border);
            border-radius: 8px;
            overflow: hidden;
            background: rgba(11, 17, 26, 0.9);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.45);
        }

        .steam-table-wrapper {
            overflow-x: auto;
            width: 100%;
        }
        .steam-table-container th {
            background: linear-gradient(180deg, #182636 0%, #121c29 100%);
            color: var(--steam-blue-light);
            font-family: 'Rajdhani', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 12px 16px;
            border-bottom: 2px solid var(--steam-border);
            text-align: left;
        }
        .steam-table-container td {
            padding: 11px 16px;
            color: #c7d5e0;
            font-size: 0.9rem;
            border-bottom: 1px solid rgba(42, 71, 94, 0.4);
            transition: background 0.15s ease;
        }
        .steam-table-container tr:nth-child(even) td {
            background: rgba(17, 27, 39, 0.5);
        }
        .steam-table-container tr:hover td {
            background: rgba(102, 192, 244, 0.08);
            color: #ffffff;
        }
        .steam-rank-pill {
            display: inline-block;
            background: rgba(102, 192, 244, 0.15);
            border: 1px solid var(--steam-blue-light);
            color: var(--steam-blue-light);
            padding: 2px 8px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 0.8rem;
        }

        /* Custom Steam Hero Header */
        .steam-hero {
            background: linear-gradient(135deg, rgba(21, 34, 50, 0.95) 0%, rgba(10, 16, 24, 0.95) 100%),
                        radial-gradient(circle at 80% 20%, rgba(102, 192, 244, 0.2), transparent 50%);
            border: 1px solid var(--steam-border);
            border-top: 3px solid var(--steam-blue-light);
            border-radius: 12px;
            padding: 24px 30px;
            margin-bottom: 28px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.45);
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        .steam-hero-title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            color: #ffffff;
            margin: 0;
            display: flex;
            align-items: center;
            text-shadow: 0 0 12px rgba(102, 192, 244, 0.4);
        }
        .steam-hero-subtitle {
            color: var(--steam-text-muted);
            margin-top: 6px;
            font-size: 0.95rem;
        }
        .steam-tag {
            background: rgba(102, 192, 244, 0.15);
            border: 1px solid var(--steam-blue-light);
            color: var(--steam-blue-light);
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            box-shadow: 0 0 10px rgba(102, 192, 244, 0.2);
        }

        /* Steam Top 3 Cards */
        .steam-top-grid {
            display: flex;
            gap: 18px;
            margin: 20px 0 30px 0;
            flex-wrap: wrap;
        }
        .steam-top-card {
            flex: 1 1 270px;
            background: linear-gradient(145deg, rgba(21, 34, 50, 0.95) 0%, rgba(10, 16, 24, 0.98) 100%);
            border: 1px solid var(--steam-border);
            border-radius: 10px;
            padding: 22px;
            position: relative;
            box-shadow: 0 6px 22px rgba(0,0,0,0.4);
            transition: all 0.3s ease;
            min-width: 260px;
        }
        .steam-top-card:hover {
            transform: translateY(-3px);
            border-color: var(--steam-blue-light);
            box-shadow: 0 10px 30px rgba(102, 192, 244, 0.25);
        }
        .steam-rank-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            font-weight: 800;
            font-size: 0.95rem;
            margin-bottom: 12px;
        }
        .rank-1 { background: rgba(243, 156, 18, 0.2); color: #f39c12; border: 2px solid #f39c12; box-shadow: 0 0 12px rgba(243, 156, 18, 0.5); }
        .rank-2 { background: rgba(189, 195, 199, 0.2); color: #bdc3c7; border: 2px solid #bdc3c7; box-shadow: 0 0 12px rgba(189, 195, 199, 0.5); }
        .rank-3 { background: rgba(230, 126, 34, 0.2); color: #e67e22; border: 2px solid #e67e22; box-shadow: 0 0 12px rgba(230, 126, 34, 0.5); }

        .steam-top-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 6px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .steam-top-score {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--steam-blue-light);
        }
        .steam-top-meta {
            font-size: 0.85rem;
            color: var(--steam-text-muted);
            margin-top: 12px;
            display: flex;
            justify-content: space-between;
            border-top: 1px solid rgba(42, 71, 94, 0.4);
            padding-top: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_icon(icon_key: str) -> str:
    return SVG_ICONS.get(icon_key, "")


def render_steam_title(title: str, icon_key: str = "game") -> None:
    icon_svg = get_icon(icon_key)
    st.markdown(
        f"""<h2 style="display: flex; align-items: center; margin-top: 1.2rem;">{icon_svg}{title}</h2>""",
        unsafe_allow_html=True,
    )


def render_steam_header(title: str, subtitle: str, tag: str = "STEAM SAW ENGINE") -> None:
    icon_svg = get_icon("game")
    st.markdown(
        f"""<div class="steam-hero"><div><div class="steam-hero-title">{icon_svg}{title}</div><div class="steam-hero-subtitle">{subtitle}</div></div><div><span class="steam-tag">{tag}</span></div></div>""",

.")


def render_top_game_cards(results_df, top_n: int = 3) -> None:
    """Renders sleek Steam achievement cards for the top ranked games."""
    if results_df.empty:
        return

    top_games = results_df.head(top_n)
    cards_html = ['<div class="steam-top-grid">']

    for idx, (_, row) in enumerate(top_games.iterrows(), start=1):
        rank_class = f"rank-{idx}" if idx <= 3 else ""
        badge_text = f"#{idx}"
        game_name = str(row.get("Nama Game", "Unknown Game"))
        score = row.get("Nilai SAW", row.get("Nilai Akhir", 0.0))
        harga = str(row.get("Harga", "-"))
        genre = str(row.get("Genre", "Steam PC"))

        tag_icon = get_icon("tag")
        dollar_icon = get_icon("dollar")

        cards_html.append(
            f'<div class="steam-top-card">'
            f'<div class="steam-rank-badge {rank_class}">{badge_text}</div>'
            f'<div class="steam-top-title" title="{game_name}">{game_name}</div>'
            f'<div class="steam-top-score">SAW Score: {score:.4f}</div>'
            f'<div class="steam-top-meta"><span>{tag_icon}{genre}</span><span>{dollar_icon}{harga}</span></div>'
            f'</div>'
        )

    cards_html.append("</div>")
    st.markdown("".join(cards_html), unsafe_allow_html=True)

def render_steam_table(df, max_rows: int = 500) -> None:
    """Render a DataFrame as a styled Steam-themed HTML table with a responsive wrapper.
    Truncates to max_rows for performance.
    """
    import streamlit as st
    if df.empty:
        st.info("Tidak ada data untuk ditampilkan.")
        return
    if len(df) > max_rows:
        st.warning(f"Menampilkan {max_rows} baris pertama dari {len(df)} total baris.")
        df = df.head(max_rows)
    html_table = df.to_html(index=False, escape=False, classes="steam-table-container")
    wrapped = f"<div class='steam-table-wrapper'>{html_table}</div>"
    st.markdown(wrapped, unsafe_allow_html=True)
