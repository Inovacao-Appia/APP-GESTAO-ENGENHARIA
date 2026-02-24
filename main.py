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

    .stApp {{
        background-color: white;
        font-family: 'Roboto', sans-serif;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}

    /* Centralizar o conteúdo usando classes padrão do Streamlit */
    .block-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding-top: 2rem;
        max-width: 500px;
        margin: 0 auto;
    }}

    .logo-img {{
        display: block !important;
        margin: 0 auto 10px auto !important;
        width: 80% !important;
        max-width: 270px !important;
        height: auto !important;
    }}

    .subtitle {{
        color: {CINZA_APPIA};
        font-weight: 600;   
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 8rem;  
        margin-bottom: 40px;
        text-align: center;
    }}

    /* Força os contêineres e botões do Streamlit a terem 100% de largura */
    div.stButton, div[data-testid="stButton"], div[data-testid="stBaseButton-secondary"] {{
        width: 100% !important;
    }}

    /* Design principal compartilhado: Botões HTML <a> e Botões do Streamlit */
    .nav-button,
    div.stButton > button,
    div[data-testid="stButton"] > button,
    div[data-testid="stBaseButton-secondary"] > button {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        background-color: {VERDE_APPIA} !important;
        color: white !important;
        text-decoration: none !important;
        width: 100% !important;
        padding: 22px 16px !important;
        margin-bottom: 16px !important;
        margin-top: 5px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
        border: none !important;
    }}

    /* Ajuste da fonte do texto interno do botão Streamlit */
    div.stButton > button p,
    div[data-testid="stBaseButton-secondary"] > button p {{
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        margin: 0 !important;
    }}

    /* Ajuste para a fonte dos links HTML (Produção e Qualidade) */
    .nav-button {{
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }}

    .nav-button:hover,
    div.stButton > button:hover,
    div[data-testid="stBaseButton-secondary"] > button:hover {{
        background-color: {VERDE_HOVER} !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
        color: white !important;
    }}

    .nav-button:active,
    div.stButton > button:active,
    div[data-testid="stBaseButton-secondary"] > button:active {{
        transform: translateY(0) !important;
    }}

    .emoji {{
        margin-right: 12px;
        font-size: 1.3rem;
    }}

    /* Separação do botão voltar no final */
    .back-btn-spacing {{
        margin-top: 25px;
        width: 100%;
        border-top: 1px dotted #ccc;
        padding-top: 25px;
    }}

    .footer-text {{
        margin-top: 30px;
        color: {CINZA_APPIA};
        font-size: 0.8rem;
        text-align: center;
        border-top: 1px solid #eee;
        padding-top: 20px;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

# Lógica da Logo (Base64)
logo_path = r"Logos/Via Appia/PNG/Via Appia.png"
logo_data = get_base64_of_bin_file(logo_path)

# Controle simples de "páginas"
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# REMOVIDO o botão de voltar daqui
def render_header(titulo="Gestão de Engenharia", subtitulo=None):
    if logo_data:
        st.markdown(
            f'<img src="data:image/png;base64,{logo_data}" class="logo-img">', 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<h1 style='text-align: center; color: {VERDE_APPIA}; margin-bottom:0;'>via appia</h1>", 
            unsafe_allow_html=True
        )

    st.markdown(
        f'<h1 style="text-align: center; color: {CINZA_APPIA}; margin-bottom:20px;">{titulo}</h1>', 
        unsafe_allow_html=True
    )

    if subtitulo:
        st.markdown(
            f'<p style="text-align:center; color:{CINZA_APPIA}; margin-bottom:30px;">{subtitulo}</p>',
            unsafe_allow_html=True
        )


# INSERIDO o botão de voltar aqui!
def render_footer(show_back=False, back_target="home"):
    # Botão de voltar renderizado logo antes do texto de rodapé
    if show_back:
        st.markdown('<div class="back-btn-spacing"></div>', unsafe_allow_html=True)
        if st.button("⬅️ VOLTAR", key=f"btn_voltar_to_{back_target}", use_container_width=True):
            st.session_state["page"] = back_target
            st.rerun()

    st.markdown(f"""
        <div class="footer-text">
            VIA APPIA CONCESSÕES<br>
            <strong>Unindo Caminhos. Construindo Novos Futuros.</strong>
        </div>
        """, unsafe_allow_html=True)

# Página inicial
def show_home():
    render_header(titulo="Gestão de Engenharia")

    if st.button("🛡️ SEGURANÇA", key="btn_seguranca", use_container_width=True):
        st.session_state["page"] = "seguranca_menu"
        st.rerun()

    links = [
        {"label": "PRODUÇÃO", "emoji": "🏗️", "url": "https://forms.office.com/r/HYDzb1TDcB"},
        {"label": "QUALIDADE", "emoji": "🏆", "url": "https://forms.office.com/r/c2T5a0XPf4"}
    ]

    for item in links:
        btn_html = f'''
            <a href="{item['url']}" target="_blank" class="nav-button">
                <span class="emoji">{item['emoji']}</span> {item['label']}
            </a>
        '''
        st.markdown(btn_html, unsafe_allow_html=True)

    # Aqui a home não tem botão voltar
    render_footer(show_back=False)

# Menu de Segurança
def show_seguranca_menu():
    render_header(titulo="Segurança", subtitulo="Escolha o módulo desejado")

    if st.button("📋 Checklist de Segurança", key="btn_seg_checklist", use_container_width=True):
        st.session_state["page"] = "seguranca_checklist"
        st.rerun()

    if st.button("👷 Controle de Integração", key="btn_seg_integracao", use_container_width=True):
        st.session_state["page"] = "seguranca_integracao"
        st.rerun()

    emergencia_url = "https://forms.office.com/r/SEU_FORM_DE_EMERGENCIA"  
    emergencia_btn = f'''
        <a href="{emergencia_url}" target="_blank" class="nav-button">
            <span class="emoji">🚨</span> Emergência (Acidentes / Incidentes)
        </a>
    '''
    st.markdown(emergencia_btn, unsafe_allow_html=True)

    # Agora ativamos o voltar pelo footer
    render_footer(show_back=True, back_target="home")

# Página 1: Checklist de Segurança
def show_seguranca_checklist():
    render_header(
        titulo="Checklist de Segurança",
        subtitulo="Preenchimento e acompanhamento do checklist"
    )

    st.info("Aqui entra a tabela de checklist de segurança que vocês já estão desenvolvendo.")

    # Voltar pelo footer
    render_footer(show_back=True, back_target="seguranca_menu")

# Página 2: Controle de Integração
def show_seguranca_integracao():
    render_header(
        titulo="Controle de Integração",
        subtitulo="Consulta rápida de funcionários integrados"
    )

    st.info("Aqui será exibido o controle de integração, com busca de funcionários integrados e status.")

    # Voltar pelo footer
    render_footer(show_back=True, back_target="seguranca_menu")

# Roteador simples
page = st.session_state["page"]

if page == "home":
    show_home()
elif page == "seguranca_menu":
    show_seguranca_menu()
elif page == "seguranca_checklist":
    show_seguranca_checklist()
elif page == "seguranca_integracao":
    show_seguranca_integracao()
