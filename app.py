import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="ClientBoost AI",
    page_icon="🚀",
    layout="wide"
)

# =========================
# STATE
# =========================
if "started" not in st.session_state:
    st.session_state.started = False

if "selected" not in st.session_state:
    st.session_state.selected = ""

if "paid" not in st.session_state:
    st.session_state.paid = False

# =========================
# SIDEBAR (NAV + LANGUAGE)
# =========================
st.sidebar.title("🚀 ClientBoost AI")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📄 Details", "🚀 Generator"]
)

lang = st.sidebar.selectbox(
    "🌍 Language",
    ["English", "Français", "Español"]
)

# =========================
# TEXT SYSTEM (MULTI LANGUAGE)
# =========================
texts = {
    "English": {
        "title": "Grow your business with AI",
        "subtitle": "Create sales, marketing & follow-ups in seconds",
        "start": "🚀 Start now",
        "problems_title": "Choose your problem",
        "problems": [
            "Sales messages",
            "Marketing content",
            "Client follow-up",
            "Increase sales",
            "Save time",
            "Beginner help"
        ],
        "desc": "This tool helps you create business content instantly.",
        "locked": "🔒 Unlock required",
        "unlock": "💳 Unlock (demo)",
        "output": "Generated result"
    },

    "Français": {
        "title": "Développe ton business avec l'IA",
        "subtitle": "Crée des ventes et contenus en quelques secondes",
        "start": "🚀 Commencer",
        "problems_title": "Choisis ton problème",
        "problems": [
            "Messages de vente",
            "Contenu marketing",
            "Relance client",
            "Augmenter les ventes",
            "Gagner du temps",
            "Aide débutant"
        ],
        "desc": "Cet outil crée du contenu business automatiquement.",
        "locked": "🔒 Déverrouillage requis",
        "unlock": "💳 Débloquer (demo)",
        "output": "Résultat généré"
    },

    "Español": {
        "title": "Haz crecer tu negocio con IA",
        "subtitle": "Crea ventas y contenido en segundos",
        "start": "🚀 Empezar",
        "problems_title": "Elige tu problema",
        "problems": [
            "Mensajes de venta",
            "Contenido marketing",
            "Seguimiento clientes",
            "Aumentar ventas",
            "Ahorrar tiempo",
            "Ayuda principiantes"
        ],
        "desc": "Esta herramienta crea contenido automáticamente.",
        "locked": "🔒 Desbloqueo requerido",
        "unlock": "💳 Desbloquear (demo)",
        "output": "Resultado generado"
    }
}

t = texts[lang]

# =========================
# DESIGN
# =========================
st.markdown("""
<style>
.stApp {
    background-color: #0b1220;
    color: white;
}
.title {
    text-align: center;
    font-size: 50px;
    font-weight: 800;
}
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}
.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    margin-top: 15px;
    border: 1px solid #1f2937;
}
.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(f"<div class='title'>🚀 ClientBoost AI</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>{t['subtitle']}</div>", unsafe_allow_html=True)

# =========================
# HOME
# =========================
if page == "🏠 Home":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(f"## {t['title']}")

    st.write("""
❌ You struggle to write content  
❌ You waste time creating messages  
❌ You don’t know how to sell  

---

💡 AI solves everything in seconds
""")

    if st.button(t["start"]):
        st.session_state.started = True

    st.markdown("</div>", unsafe_allow_html=True)

    # PROBLEMS AFTER START
    if st.session_state.started:

        st.markdown("---")
        st.subheader(t["problems_title"])

        st.session_state.selected = st.radio("Select:", t["problems"])

# =========================
# DETAILS
# =========================
elif page == "📄 Details":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📄 Description")

    st.write(st.session_state.selected)
    st.write(t["desc"])

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# GENERATOR
# =========================
elif page == "🚀 Generator":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🚀 Generator")

    business = st.text_input("Business")
    product = st.text_input("Product")
    audience = st.text_input("Audience")

    if st.button("Generate"):

        if not st.session_state.paid:
            st.error(t["locked"])

            if st.button(t["unlock"]):
                st.session_state.paid = True
                st.success("Unlocked ✔")

        else:
            result = f"""
🔥 {st.session_state.selected}

We are {business}.  
We help {audience} with {product}.  

👉 Fast AI-generated content.

— ClientBoost AI
"""

            st.success(t["output"])
            st.text_area("Output", result, height=250)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Created by kēllønę 🔗💨")
