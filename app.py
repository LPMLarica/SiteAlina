import streamlit as st
from PIL import Image
import os

if "page" not in st.session_state:
    st.session_state.page = "Projetos"

def set_page(page_name):
    st.session_state.page = page_name

# Config da página
st.set_page_config(
    page_title="Dra. Alina Cardoso",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Função para carregar CSS
def load_css():
    css_file = "style.css"

    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        # CSS como fallback
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

            * {
                font-family: 'Poppins', sans-serif;
            }

            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
            }

            .nav-container {
                background: linear-gradient(135deg, #f5f5f0 0%, #ffffff 100%);
                padding: 1.5rem 2rem;
                border-radius: 15px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.05);
                margin-bottom: 2rem;
            }

            .stButton > button {
                background: linear-gradient(135deg, #d4af37 0%, #f4d03f 100%);
                color: white;
                border: none;
                padding: 0.6rem 2rem;
                border-radius: 25px;
                font-weight: 500;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
            }

            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
            }

            h1 {
                color: #d4af37;
                font-weight: 600;
                margin-bottom: 1rem;
            }

            h2 {
                color: #c9a959;
                font-weight: 500;
                margin-top: 1.5rem;
            }

            h3 {
                color: #8b7355;
                font-weight: 500;
            }

            .project-card {
                background: white;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);
                margin-bottom: 2rem;
                border-left: 4px solid #d4af37;
                transition: all 0.3s ease;
            }

            .project-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 25px rgba(0,0,0,0.12);
            }

            .footer {
                background: linear-gradient(135deg, #f5f5f0 0%, #ffffff 100%);
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                margin-top: 3rem;
                box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
            }

            .social-button {
                display: inline-block;
                padding: 0.8rem 2rem;
                margin: 0.5rem;
                background: linear-gradient(135deg, #d4af37 0%, #f4d03f 100%);
                color: white;
                text-decoration: none;
                border-radius: 25px;
                font-weight: 500;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
            }

            .social-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
                color: white;
                text-decoration: none;
            }

            hr {
                border: none;
                height: 2px;
                background: linear-gradient(90deg, transparent, #d4af37, transparent);
                margin: 2rem 0;
            }

            .profile-section {
                background: white;
                padding: 2.5rem;
                border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            }

            .profile-name {
                color: #d4af37;
                font-size: 2.5rem;
                font-weight: 600;
                margin-bottom: 0.5rem;
            }

            .profile-title {
                color: #8b7355;
                font-size: 1.2rem;
                font-weight: 400;
                margin-bottom: 1.5rem;
            }

            .profile-text {
                color: #555;
                line-height: 1.8;
                text-align: justify;
            }
            </style>
        """, unsafe_allow_html=True)


# tratamento de erro
def load_image(image_path, placeholder_text):
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            return img
        except:
            st.info(f"💡 {placeholder_text}")
            return None
    else:
        st.info(f"💡 {placeholder_text}")
        return None


# header com navegação
def render_header_navigation():
    st.markdown('<div class="header-container">', unsafe_allow_html=True)

    col_logo, col_nav1, col_nav2, col_space = st.columns([1.5, 1, 1, 2])

    with col_logo:
        logo = load_image("assets/logo_alina.png", "")
        if logo:
            st.markdown('<div class="logo-container">', unsafe_allow_html=True)
            st.image(logo, width=180)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="logo-placeholder">💎 Dra. Alina Cardoso</div>', unsafe_allow_html=True)

    with col_nav1:
        st.button(
            "Projetos",
            key="nav_projetos",
            on_click=set_page,
            args=("Projetos",)
        )

    with col_nav2:
        st.button(
            "Sobre Quem Sou",
            key="nav_sobre",
            on_click=set_page,
            args=("Sobre",)
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # Estilo do botão ativo
    st.markdown(
        f"""
        <style>
        button[key="nav_projetos"] {{
            color: {"#d4af37" if st.session_state.page == "Projetos" else "#8b7355"};
            font-weight: {"600" if st.session_state.page == "Projetos" else "500"};
        }}

        button[key="nav_sobre"] {{
            color: {"#d4af37" if st.session_state.page == "Sobre" else "#8b7355"};
            font-weight: {"600" if st.session_state.page == "Sobre" else "500"};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)


# renderizar card projetos
def render_project_card(image_path, title, description):
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("#### 📸 Imagem do Projeto")
        img = load_image(image_path, f"Adicione a imagem do projeto aqui ({image_path})")
        if img:
            st.image(img, use_column_width=True, caption=title)

    with col2:
        st.markdown(f"### {title}")
        st.markdown(f"""
        <div class="profile-text">
        {description}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# Página de projetos
def render_projects_page():
    st.markdown("# Meus Projetos")
    st.markdown("### Conheça alguns dos trabalhos realizados com excelência")
    st.markdown("<br>", unsafe_allow_html=True)

    # Projeto 1
    projeto1_desc = """
    <p><strong>O que é:</strong> A harmonização orofacial é um conjunto de procedimentos estéticos 
    que visa equilibrar e embelezar os traços faciais, respeitando a naturalidade e individualidade 
    de cada paciente.</p>

    <p><strong>Importância:</strong> Este procedimento vai além da estética, proporcionando 
    autoestima, confiança e bem-estar aos pacientes. Com técnicas modernas e seguras, 
    alcançamos resultados naturais que realçam a beleza única de cada pessoa.</p>

    <p><strong>Resultados:</strong> Rejuvenescimento facial, equilíbrio das proporções, 
    suavização de linhas de expressão e valorização dos contornos naturais.</p>
    """
    render_project_card("assets/projeto1.jpg", "Harmonização Orofacial", projeto1_desc)

    # Projeto 2
    projeto2_desc = """
    <p><strong>O que é:</strong> As facetas em porcelana são lâminas ultrafinas de cerâmica 
    que são aplicadas sobre os dentes, transformando completamente o sorriso com naturalidade 
    e durabilidade excepcional.</p>

    <p><strong>Importância:</strong> Esse tratamento revolucionou a odontologia estética, 
    permitindo correções de cor, formato, tamanho e alinhamento dos dentes de forma minimamente 
    invasiva e com resultados surpreendentes.</p>

    <p><strong>Resultados:</strong> Sorriso harmônico, dentes alinhados, cor uniforme e 
    brilhante, aspecto natural e duradouro que transforma vidas.</p>
    """
    render_project_card("assets/projeto2.jpg", "Facetas em Porcelana", projeto2_desc)

    # Projeto 3
    projeto3_desc = """
    <p><strong>O que é:</strong> O clareamento dental é um procedimento estético que remove 
    manchas e escurecimentos dos dentes, devolvendo o branco natural e a luminosidade do sorriso 
    através de técnicas seguras e eficazes.</p>

    <p><strong>Importância:</strong> Um sorriso branco e brilhante é sinônimo de saúde, 
    juventude e cuidado pessoal. Este procedimento eleva a autoestima e proporciona confiança 
    em situações sociais e profissionais.</p>

    <p><strong>Resultados:</strong> Dentes mais brancos em até 8 tons, sorriso rejuvenescido, 
    procedimento seguro e resultados que duram anos com cuidados adequados.</p>
    """
    render_project_card("assets/projeto3.jpg", "Clareamento Dental", projeto3_desc)


# Página sobre
def render_about_page():
    st.markdown("# Sobre Quem Sou")
    st.markdown("### Conheça minha história e formação profissional")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="profile-section">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        foto = load_image("assets/foto_alina.png", "assets/foto_alina.png")
        if foto:
            st.image(foto, use_column_width=True)

    with col2:
        st.markdown('<p class="profile-name">Dra. Alina Cardoso</p>', unsafe_allow_html=True)
        st.markdown('<p class="profile-title">Cirurgiã-Dentista | Especialista em Harmonização Orofacial</p>',
                    unsafe_allow_html=True)

        st.markdown("""
        <div class="profile-text">
        <h3 style="color: #d4af37; margin-top: 1rem;">Minha História</h3>
        <p>Desde o início da minha carreira, sempre tive a paixão por transformar sorrisos e vidas. 
        Acredito que a odontologia vai muito além da técnica - é sobre criar conexões, entender 
        sonhos e proporcionar bem-estar através de um sorriso confiante e saudável.</p>

        <p>Com anos de experiência e dedicação constante ao aperfeiçoamento profissional, 
        especializei-me nas áreas de harmonização orofacial, facetas estéticas e clareamento dental, 
        sempre priorizando a naturalidade e individualidade de cada paciente.</p>

        <h3 style="color: #d4af37; margin-top: 1.5rem;">Formação Profissional</h3>
        <p><strong>🎓 Graduação:</strong> Odontologia pela [Nome da Universidade]</p>
        <p><strong>🎓 Especialização:</strong> Harmonização Orofacial</p>
        <p><strong>🎓 Especialização:</strong> Prótese Dentária e Facetas Estéticas</p>
        <p><strong>🎓 Cursos:</strong> Clareamento Dental Avançado, Toxina Botulínica e Preenchimentos</p>
        <p><strong>📚 Atualização Constante:</strong> Participação regular em congressos nacionais e 
        internacionais de odontologia estética</p>

        <h3 style="color: #d4af37; margin-top: 1.5rem;">Filosofia de Trabalho</h3>
        <p>Meu compromisso é oferecer tratamentos de excelência com tecnologia de ponta, 
        aliando técnica, arte e ciência para resultados que respeitam a harmonia facial e 
        proporcionam sorrisos naturalmente belos. Cada paciente é único, e cada tratamento 
        é personalizado para atender suas necessidades e expectativas.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# Função para renderizar rodapé
def render_footer():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.markdown("### 📱 Entre em Contato")
    st.markdown("##### Agende sua consulta e transforme seu sorriso!")

    # Configurações de redes sociais
    instagram_url = "https://www.instagram.com/seu_usuario"
    whatsapp_url = "https://wa.me/5534999999999"

    st.markdown(f"""
        <div style="margin-top: 1.5rem;">
            <a href="{instagram_url}" target="_blank" class="social-button">
                📷 Instagram
            </a>
            <a href="{whatsapp_url}" target="_blank" class="social-button">
                💬 WhatsApp
            </a>
        </div>
        <p style="margin-top: 2rem; color: #8b7355; font-size: 0.9rem;">
            © 2026 Dra. Alina Cardoso - Todos os direitos reservados
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# Aplicação

def main():
    load_css()

    render_header_navigation()

    if st.session_state.page == 'Projetos':
        render_projects_page()
    elif st.session_state.page == 'Sobre':
        render_about_page()

    render_footer()

if __name__ == "__main__":
    main()