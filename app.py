import streamlit as st
import random

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="ClientBoost AI",
    page_icon="🚀",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "paid" not in st.session_state:
    st.session_state.paid = False

if "selected" not in st.session_state:
    st.session_state.selected = ""

# =========================
# DESIGN
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🚀 ClientBoost AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your AI business assistant for sales, marketing & growth</div>", unsafe_allow_html=True)

# =========================
# 🧠 GENERATORS (PSEUDO IA)
# =========================
def generate_sales_message(business, product, audience):

    hooks = ["🔥 Attention !", "🚀 Nouvelle opportunité", "💡 Imagine ceci"]
    openings = [
        f"Nous sommes {business} et nous aidons déjà des entreprises comme la vôtre.",
        f"Chez {business}, nous avons une solution simple et efficace.",
        f"Beaucoup de {audience} utilisent déjà notre solution."
    ]
    benefits = [
        f"augmenter vos ventes avec {product}",
        "attirer plus de clients",
        "booster votre visibilité",
        "gagner du temps automatiquement"
    ]
    closings = [
        "Contactez-nous dès maintenant.",
        "Ne ratez pas cette opportunité.",
        "Passez à l’action aujourd’hui."
    ]

    return f"""
{random.choice(hooks)}

{random.choice(openings)}

Nous vous aidons à {random.choice(benefits)}.

👉 Résultat : croissance rapide et durable.

{random.choice(closings)}

— {business}
"""

def generate_marketing(platform, topic):

    return f"""
🔥 {topic}

Découvrez comment améliorer vos résultats sur {platform}.

👉 Stratégie simple + efficace + rapide

Commencez maintenant et faites grandir votre business.
"""

def generate_followup(name, service):

    return f"""
Bonjour {name},

Je fais juste un suivi concernant {service}.

Avez-vous eu le temps de réfléchir ?

Je reste disponible si besoin.
"""

# =========================
# 🏠 HOME
# =========================
if st.session_state.page == "home":

    st.subheader("💡 Choose a problem to solve")

    choices = [
        "📩 Vendre plus facilement",
        "📢 Créer du contenu marketing",
        "🔄 Relancer des clients",
        "💰 Augmenter les ventes",
        "⚡ Gagner du temps",
        "🧠 Aide débutants"
    ]

    selected = st.radio("What do you want to improve?", choices)

    if st.button("Continue"):
        st.session_state.selected = selected
        st.session_state.page = "details"

# =========================
# 📄 DETAILS PAGE
# =========================
elif st.session_state.page == "details":

    st.subheader("📄 Solution")

    st.markdown(f"""
    ## {st.session_state.selected}

    ✔ Analyse du besoin  
    ✔ Génération automatique de contenu  
    ✔ Résultat optimisé pour business  

    👉 Cette solution est conçue pour t’aider rapidement.
    """)

    if st.button("Start generator"):
        st.session_state.page = "generator"

    if st.button("⬅ Back"):
        st.session_state.page = "home"

# =========================
# 🔐 GENERATOR + PAYWALL
# =========================
elif st.session_state.page == "generator":

    st.subheader("🔐 AI Generator")

    business = st.text_input("Business name")
    product = st.text_input("Product / Service")
    audience = st.text_input("Target audience")

    if st.button("Generate"):

        if not st.session_state.paid:

            st.error("🔒 Payment required to unlock results")

            if st.button("💳 Pay (demo)"):
                st.session_state.paid = True
                st.success("Payment successful ✔")

        else:

            if st.session_state.selected == "📩 Vendre plus facilement":
                result = generate_sales_message(business, product, audience)

            elif st.session_state.selected == "📢 Créer du contenu marketing":
                result = generate_marketing("social media", product)

            elif st.session_state.selected == "🔄 Relancer des clients":
                result = generate_followup(business, product)

            else:
                result = "Feature coming soon..."

            st.success("✅ Generated result")
            st.text_area("Output", result, height=300)

    if st.button("⬅ Back"):
        st.session_state.page = "details"
