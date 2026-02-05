"""
Arquivo de configuração do site Dra. Alina Cardoso
Centralize todas as configurações, textos e links aqui
"""

# INFORMAÇÕES PESSOAIS

NOME_PROFISSIONAL = "Dra. Alina Cardoso"
TITULO_PROFISSIONAL = "Cirurgiã-Dentista | Especialista em Harmonização Orofacial"
SUBTITULO = "Harmonização • Facetas • Clareamento"

# REDES SOCIAIS E CONTATO

INSTAGRAM_URL = "https://www.instagram.com/seu_usuario"
INSTAGRAM_USUARIO = "@seu_usuario"

WHATSAPP_NUMERO = "5534999999999"  # Formato: Código do país + DDD + Número
WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMERO}"
WHATSAPP_MENSAGEM = "Olá! Gostaria de agendar uma consulta."
WHATSAPP_URL_COM_MENSAGEM = f"https://wa.me/{WHATSAPP_NUMERO}?text={WHATSAPP_MENSAGEM}"

# CAMINHOS DAS IMAGENS

CAMINHO_LOGO = "assets/logo_alina.png"
CAMINHO_FOTO_PERFIL = "assets/foto_alina.png"

# Projetos
CAMINHO_PROJETO_1 = "assets/harmonizacao.png"
CAMINHO_PROJETO_2 = "assets/facetas.png"
CAMINHO_PROJETO_3 = "assets/clareamento.png"

# PROJETOS - CONTEÚDO
PROJETOS = [
    {
        "titulo": "Harmonização Orofacial",
        "imagem": CAMINHO_PROJETO_1,
"descricao": """
<p><strong>O que é:</strong> A harmonização orofacial é um conjunto de procedimentos estéticos 
que visa equilibrar e embelezar os traços faciais, respeitando a naturalidade e individualidade 
de cada paciente.</p>

<p><strong>Importância:</strong> Este procedimento vai além da estética, proporcionando 
autoestima, confiança e bem-estar aos pacientes. Com técnicas modernas e seguras, 
alcançamos resultados naturais que realçam a beleza única de cada pessoa.</p>

<p><strong>Resultados:</strong> Rejuvenescimento facial, equilíbrio das proporções, 
suavização de linhas de expressão e valorização dos contornos naturais.</p>
"""
    },
    {
        "titulo": "Facetas em Porcelana",
        "imagem": CAMINHO_PROJETO_2,
        "descricao": """
<p><strong>O que é:</strong> As facetas em porcelana são lâminas ultrafinas de cerâmica 
que são aplicadas sobre os dentes, transformando completamente o sorriso com naturalidade 
e durabilidade excepcional.</p>

<p><strong>Importância:</strong> Esse tratamento revolucionou a odontologia estética, 
permitindo correções de cor, formato, tamanho e alinhamento dos dentes de forma minimamente 
invasiva e com resultados surpreendentes.</p>

<p><strong>Resultados:</strong> Sorriso harmônico, dentes alinhados, cor uniforme e 
brilhante, aspecto natural e duradouro que transforma vidas.</p>
"""
    },
    {
        "titulo": "Clareamento Dental",
        "imagem": CAMINHO_PROJETO_3,
        "descricao": """
<p><strong>O que é:</strong> O clareamento dental é um procedimento estético que remove 
manchas e escurecimentos dos dentes, devolvendo o branco natural e a luminosidade do sorriso 
através de técnicas seguras e eficazes.</p>

<p><strong>Importância:</strong> Um sorriso branco e brilhante é sinônimo de saúde, 
juventude e cuidado pessoal. Este procedimento eleva a autoestima e proporciona confiança 
em situações sociais e profissionais.</p>

<p><strong>Resultados:</strong> Dentes mais brancos em até 8 tons, sorriso rejuvenescido, 
procedimento seguro e resultados que duram anos com cuidados adequados.</p>
"""
    }
]

# PÁGINA SOBRE - CONTEÚDO
SOBRE_HISTORIA = """
<h3 style="color: #d4af37; margin-top: 1rem;">Minha História</h3>
<p>Desde o início da minha carreira, sempre tive a paixão por transformar sorrisos e vidas. 
Acredito que a odontologia vai muito além da técnica - é sobre criar conexões, entender 
sonhos e proporcionar bem-estar através de um sorriso confiante e saudável.</p>

<p>Com anos de experiência e dedicação constante ao aperfeiçoamento profissional, 
especializei-me nas áreas de harmonização orofacial, facetas estéticas e clareamento dental, 
sempre priorizando a naturalidade e individualidade de cada paciente.</p>
"""

SOBRE_FORMACAO = """
<h3 style="color: #d4af37; margin-top: 1.5rem;">Formação Profissional</h3>
<p><strong>🎓 Graduação:</strong> Odontologia pela [Nome da Universidade]</p>
<p><strong>🎓 Especialização:</strong> Harmonização Orofacial</p>
<p><strong>🎓 Especialização:</strong> Prótese Dentária e Facetas Estéticas</p>
<p><strong>🎓 Cursos:</strong> Clareamento Dental Avançado, Toxina Botulínica e Preenchimentos</p>
<p><strong>📚 Atualização Constante:</strong> Participação regular em congressos nacionais e 
internacionais de odontologia estética</p>
"""

SOBRE_FILOSOFIA = """
<h3 style="color: #d4af37; margin-top: 1.5rem;">Filosofia de Trabalho</h3>
<p>Meu compromisso é oferecer tratamentos de excelência com tecnologia de ponta, 
aliando técnica, arte e ciência para resultados que respeitam a harmonia facial e 
proporcionam sorrisos naturalmente belos. Cada paciente é único, e cada tratamento 
é personalizado para atender suas necessidades e expectativas.</p>
"""

# TEXTOS DA INTERFACE

TEXTO_RODAPE_TITULO = "📱 Entre em Contato"
TEXTO_RODAPE_SUBTITULO = "Agende sua consulta e transforme seu sorriso!"
TEXTO_COPYRIGHT = "© 2026 Dra. Alina Cardoso - Todos os direitos reservados"

# Textos dos botões
BOTAO_INSTAGRAM = "📷 Instagram"
BOTAO_WHATSAPP = "💬 WhatsApp"
BOTAO_PROJETOS = "Projetos"
BOTAO_SOBRE = "Sobre Quem Sou"

# Títulos das páginas
TITULO_PROJETOS = "# Meus Projetos"
SUBTITULO_PROJETOS = "### Conheça alguns dos trabalhos realizados com excelência"

TITULO_SOBRE = "# Sobre Quem Sou"
SUBTITULO_SOBRE = "### Conheça minha história e formação profissional"

PAGE_CONFIG = {
    "page_title": "Start Centro Clinico",
    "page_icon": "💎",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}


PLACEHOLDER_LOGO = "assets/logo_alina.png"
PLACEHOLDER_FOTO_PERFIL = "assets/foto_alina.png"