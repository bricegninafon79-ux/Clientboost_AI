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
st.markdown("<div class='subtitle'>AI tool for sales, marketing & business growth</div>", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🚀 Navigation")

page = st.sidebar.radio(
    "Menu",
    ["🏠 Home", "📄 Details", "🔐 Generator"]
)

# =========================
# PSEUDO IA FUNCTIONS
# =========================
def generate_sales_message(business, product, audience):

    hooks = ["🔥 Attention !", "🚀 Opportunity", "💡 Imagine this"]
    openings = [
        f"We are {business}, helping businesses grow fast.",
        f"At {business}, we provide powerful solutions.",
        f"Many {audience} already trust our system."
    ]
    benefits = [
        f"increase sales with {product}",
        "attract more customers",
        "boost visibility quickly",
        "save time and automate growth"
    ]
    closings = [
        "Contact us today.",
        "Start now.",
        "Don’t miss this opportunity."
    ]

    return f"""
{random.choice(hooks)}

{random.choice(openings)}

We help you {random.choice(benefits)}.

👉 Result: fast and consistent growth.

{random.choice(closings)}

— {business}
"""

def generate_marketing(product, platform):

    return f"""
🔥 {product}

Learn how to grow your business on {platform}.

👉 Simple strategy. Fast results.

Start today and scale your business.
"""

def generate_followup(name, service):

    return f"""
Hello {name},

Just following up about {service}.

Let me know if you're interested.

Best regards.
"""

# =========================
# 🏠 HOME
# =========================
if page == "🏠 Home":

    st.subheader("💡 Choose a problem to solve")

    choices = [
        "📩 Vendre plus facilement",
        "📢 Créer du contenu marketing",
        "🔄 Relancer des clients",
        "💰 Augmenter les ventes",
        "⚡ Gagner du temps",
        "🧠 Aide débutants"
    ]

    st.session_state.selected = st.radio("What do you want to improve?", choices)

    st.info("👉 Select a problem then go to DETAILS")

# =========================
# 📄 DETAILS
# =========================
elif page == "📄 Details":

    st.subheader("📄 Solution overview")

    st.markdown(f"""
    ## {st.session_state.selected}

    ✔ Understand your problem  
    ✔ Provide structured solution  
    ✔ Prepare AI generation  
    ✔ Business-focused output  
    """)

    st.info("👉 Go to GENERATOR to create results")

# =========================
# 🔐 GENERATOR + PAYWALL
# =========================
elif page == "🔐 Generator":

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
                result = generate_marketing(product, "social media")

            elif st.session_state.selected == "🔄 Relancer des clients":
                result = generate_followup(business, product)

            else:
                result = "Feature coming soon..."

            st.success("✅ Generated result")
            st.text_area("Output", result, height=300)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Created by kēllønę 🔗💨")
