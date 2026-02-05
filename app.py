import streamlit as st
from PIL import Image
from textwrap import dedent
import os

if "page" not in st.session_state:
    st.session_state.page = "Projetos"


def set_page(page_name):
    st.session_state.page = page_name


# Config da página
st.set_page_config(
    page_title="Start Centro Clinico",
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

# tratamento de erro
def load_image(image_path, placeholder_text):
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            return img
        except:
            return None
    else:
        return None


# header com navegação
def render_header_navigation():
    st.markdown('<div class="header-container">', unsafe_allow_html=True)

    col_logo, col_nav1, col_nav2, col_space = st.columns([1.5, 1.5, 1, 1])

    with col_logo:
        logo = load_image("assets/logo_alina.png", "")
        if logo:
            st.image(logo, width=150)
        else:
            st.markdown("💎 **Start Centro Clínico**")

    with col_nav1:
        st.button("Projetos", key="nav_projetos", on_click=set_page, args=("Projetos",))

    with col_nav2:
        st.button("Sobre Quem Sou", key="nav_sobre", on_click=set_page, args=("Sobre",))

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div style="
            height:0.5px;
            background: linear-gradient(60deg, transparent, #d4af37, transparent);
            margin: 1.5rem 0 2rem 0;
        "></div>
    """, unsafe_allow_html=True)


# renderizar card projetos
def render_project_card(image_path, title, description):
    col1, col2 = st.columns([1.5, 1.5])

    with col1:
        img = load_image(image_path, title)
        if img:
            st.image(img, use_container_width=True)

    with col2:
        st.markdown(f"""
        <div class="project-card">
            <h2>{title}</h2>
            <div class="profile-text">
                {description}
        """, unsafe_allow_html=True)



# Página de projetos
def render_projects_page():
    st.markdown("# Meus Projetos")
    st.markdown("### Conheça alguns dos trabalhos realizados com excelência")

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
    render_project_card(
        "assets/harmonizacao.png",
        "Harmonização Orofacial",
        projeto1_desc
    )

    # Projeto 2
    projeto2_desc = """
<p><strong>O que é:</strong> As facetas em porcelana são lâminas ultrafinas de cerâmica 
aplicadas sobre os dentes, transformando completamente o sorriso com naturalidade 
e durabilidade excepcional.</p>

<p><strong>Importância:</strong> Esse tratamento revolucionou a odontologia estética, 
permitindo correções de cor, formato, tamanho e alinhamento dos dentes de forma 
minimamente invasiva e com resultados surpreendentes.</p>

<p><strong>Resultados:</strong> Sorriso harmônico, dentes alinhados, cor uniforme e 
brilhante, aspecto natural e duradouro que transforma vidas.</p>
"""
    render_project_card(
        "assets/facetas.png",
        "Facetas em Porcelana",
        projeto2_desc
    )

    # Projeto 3
    projeto3_desc = """
<p><strong>O que é:</strong> O clareamento dental é um procedimento estético que remove 
manchas e escurecimentos dos dentes, devolvendo o branco natural e a luminosidade do sorriso 
por meio de técnicas seguras e eficazes.</p>

<p><strong>Importância:</strong> Um sorriso branco e brilhante é sinônimo de saúde, 
juventude e cuidado pessoal, elevando a autoestima e a confiança em ambientes sociais 
e profissionais.</p>

<p><strong>Resultados:</strong> Dentes mais brancos em até 8 tons, sorriso rejuvenescido, 
procedimento seguro e resultados duradouros com cuidados adequados.</p>
"""
    render_project_card(
        "assets/clareamento.png",
        "Clareamento Dental",
        projeto3_desc
    )



# Página sobre
def render_about_page():
    st.markdown("# Sobre Quem Sou")
    st.markdown("### Conheça minha história e formação profissional")
    st.markdown("<div style='height: 1.5rem'></div>", unsafe_allow_html=True)


    col1, col2 = st.columns([1, 2])

    with col1:
        foto = load_image("assets/foto_alina.png", "")
        if foto:
            st.image(foto, use_container_width=True)

    with col2:
        st.markdown('<p class="profile-name">Dra. Alina Cardoso</p>', unsafe_allow_html=True)
        st.markdown('<p class="profile-title">Cirurgiã-Dentista | Especialista em Harmonização Orofacial</p>', unsafe_allow_html=True)

        st.markdown("""
        <h3 style="color: #d4af37; margin-top: 1rem;">Minha História</h3>
        <p>Desde o início da minha carreira, sempre tive a paixão por transformar sorrisos e vidas. 
        Acredito que a odontologia vai muito além da técnica - é sobre criar conexões, entender 
        sonhos e proporcionar bem-estar através de um sorriso confiante e saudável.</p>

        <p>Com anos de experiência e dedicação constante ao aperfeiçoamento profissional, 
        especializei-me nas áreas de harmonização orofacial, facetas estéticas e clareamento dental, 
        sempre priorizando a naturalidade e individualidade de cada paciente.</p>

        <h3 style="color: #d4af37; margin-top: 1.5rem;">Formação Profissional</h3>
        <p><strong>🎓 Graduação:</strong> Odontologia pela Universidade Federal de Uberlândia</p>
        <p><strong>🎓 Especialização:</strong> Harmonização Orofacial</p>
        <p><strong>🎓 Especialização:</strong> Prótese Dentária e Facetas Estéticas</p>
        <p><strong>🎓 CRO:</strong> MG-16389</p>
        <p><strong>📚 Atualização Constante:</strong> Participação regular em congressos nacionais e 
        internacionais de odontologia estética</p>

        <h3 style="color: #d4af37; margin-top: 1.5rem;">Filosofia de Trabalho</h3>
        <p>Meu compromisso é oferecer tratamentos de excelência com tecnologia de ponta, 
        aliando técnica, arte e ciência para resultados que respeitam a harmonia facial e 
        proporcionam sorrisos naturalmente belos. Cada paciente é único, e cada tratamento 
        é personalizado para atender suas necessidades e expectativas.</p>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 1.5rem'></div>", unsafe_allow_html=True)


# Função para renderizar rodapé
def render_footer():
    st.markdown("<div style='height: 1.5rem'; color= '#F5F5DC';></div>", unsafe_allow_html=True)
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
    st.markdown("<div style='height: 1.5rem'></div>", unsafe_allow_html=True)


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