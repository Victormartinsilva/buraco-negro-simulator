import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Buraco Negro · Victor",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.block-container { padding-top: 1rem; padding-bottom: 1rem; }
.sim-title { text-align: center; color: #00d4ff; margin-bottom: 0.25rem; }
.sim-desc { text-align: center; color: #888; font-size: 0.9rem; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="sim-title">Simulador de Buraco Negro e Espaço-Tempo</p>', unsafe_allow_html=True)
st.markdown('<p class="sim-desc">Projeto pessoal — arraste o cursor no canvas para ver a lente gravitacional.</p>', unsafe_allow_html=True)

html_path = Path(__file__).parent / "buraco-negro.html"
if html_path.exists():
    st.components.v1.html(html_path.read_text(encoding="utf-8"), height=820, scrolling=True)
else:
    st.error("Arquivo buraco-negro.html não encontrado nesta pasta.")
