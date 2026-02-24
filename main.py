import streamlit as st
import os
import base64

# Configurações da página
st.set_page_config(page_title="Via Appia - Gestão", page_icon="🛣️", layout="centered")

# Cores oficiais Via Appia
VERDE_APPIA = "#1A5D5C"
VERDE_HOVER = "#144847"
CINZA_APPIA = "#656766"
FUNDO_LEVE = "#F8F9FA"

def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Estilização CSS Avançada
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    /* Reset e Fundo */
    .stApp {{
        background-color: white;
        font-family: 'Roboto', sans-serif;
    }}

    /* Esconder elementos nativos desnecessários */
    #MainMenu, footer, header {{visibility: hidden;}}

    /* Container Principal */
    .main-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        max-width: 500px;
        margin: 0 auto;
    }}

    .logo-img {{
        width: 100%;
        max-width: 280px;
        margin-bottom: 10px;
    }}

    .subtitle {{
        color: {CINZA_APPIA};
        font-weight: 300;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 0.9rem;
        margin-bottom: 40px;
        text-align: center;
    }}

    /* Botões customizados como cards */
    .nav-button {{
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: {VERDE_APPIA};
        color: white !important;
        text-decoration: none !important;
        width: 100%;
        padding: 22px;
        margin-bottom: 16px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: none;
    }}

    .nav-button:hover {{
        background-color: {VERDE_HOVER};
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }}

    .nav-button:active {{
        transform: translateY(0);
    }}

    .emoji {{
        margin-right: 12px;
        font-size: 1.3rem;
    }}

    .footer-text {{
        margin-top: 50px;
        color: {CINZA_APPIA};
        font-size: 0.8rem;
        text-align: center;
        border-top: 1px solid #eee;
        padding-top: 20px;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

# Lógica da Logo (Base64 para evitar problemas de renderização no HTML customizado)
logo_path = r"Logos/Via Appia/PNG/Via Appia.png"
logo_data = get_base64_of_bin_file(logo_path)

# Renderização da Interface
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if logo_data:
    st.markdown(f'<img src="data:image/png;base64,{logo_data}" class="logo-img">', unsafe_allow_html=True)
else:
    st.markdown(f"<h1 style='text-align: center; color: {VERDE_APPIA}; margin-bottom:0;'>via appia</h1>", unsafe_allow_html=True)

st.markdown('<p class="subtitle">Gestão de Engenharia</p>', unsafe_allow_html=True)

# Definição dos Links
links = [
    {"label": "SEGURANÇA", "emoji": "🛡️", "url": "https://forms.office.com/r/jnhvaaTiaC"},
    {"label": "PRODUÇÃO", "emoji": "🏗️", "url": "https://forms.office.com/r/HYDzb1TDcB"},
    {"label": "QUALIDADE", "emoji": "🏆", "url": "https://forms.office.com/r/c2T5a0XPf4"}
]

# Renderização dos Botões via HTML (evita lag de clique do Streamlit)
for item in links:
    btn_html = f'''
        <a href="{item['url']}" target="_blank" class="nav-button">
            <span class="emoji">{item['emoji']}</span> {item['label']}
        </a>
    '''
    st.markdown(btn_html, unsafe_allow_html=True)

# Rodapé
st.markdown(f"""
    <div class="footer-text">
        VIA APPIA CONCESSÕES<br>
        <strong>Unindo Caminhos. Construindo Novos Futuros.</strong>
    </div>
    </div>
    """, unsafe_allow_html=True)