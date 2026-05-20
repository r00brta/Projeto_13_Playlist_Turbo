import streamlit as st
import pandas as pd

# 🌸 Tema rosa soft + texto preto
st.markdown("""
<style>
.stApp {
    background-color: #fff5f9;
    color: #000000;
}

[data-testid="stSidebar"] {
    background-color: #ffeaf3;
}

html, body, [class*="css"] {
    color: #000000;
    font-family: Arial, sans-serif;
}

h1, h2, h3, h4, p, span, label {
    color: #000000 !important;
}

[data-testid="stMetricValue"] {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

### 📂 1. Dados
df = pd.read_parquet("Dados_Artistas.parquet")

### 🎧 2. Título centralizado
st.markdown(
    """
    <h1 style='text-align: center;'>🎧 Spotify da Mika</h1>
    """,
    unsafe_allow_html=True
)

# 🎀 Logo centralizada
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/174/174872.png",
        width=150
    )

# 💖 Subtítulo centralizado
st.markdown(
    """
    <h3 style='color:#ff4da6; text-align:center;'>
        🎀 Spotify Rosa 🎀
    </h3>
    """,
    unsafe_allow_html=True
)

### 🎶 3. Sidebar
with st.sidebar:
    st.title("🎧 Playlist da Mika")

    artistas = st.selectbox(
        "🎤 Selecione o artista",
        df['Artist'].unique()
    )

### 🎤 4. Filtrar dados
df_artista = df[df['Artist'] == artistas]

### 💿 5. Artista selecionado
st.subheader(f"🎤 Artista selecionado: {artistas}")

### 🎶 6. Músicas
st.write("🎧 Aqui estão as músicas mais tocadas:")

for index, row in df_artista.iterrows():

    with st.container():

        st.markdown(f"### 🎵 {row['Track']}")

        col1, col2 = st.columns(2)

        col1.metric(
            "🎵 Streams no Spotify",
            f"{row['Stream']:,.0f}"
        )

        col2.metric(
            "📺 Views no YouTube",
            f"{row['Views']:,.0f}"
        )

        st.video(row['Url_youtube'])

        st.markdown("---")

### 🎧 7. Botão Spotify
st.link_button(
    "🎧 Ouça no Spotify",
    url=row['Url_spotify'],
    type="primary"
)