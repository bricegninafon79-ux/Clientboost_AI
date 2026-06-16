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

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected" not in st.session_state:
    st.session_state.selected = ""

if "level" not in st.session_state:
    st.session_state.level = ""

if "paid" not in st.session_state:
    st.session_state.paid = False


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
    font-size: 52px;
    font-weight: 800;
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
    font-weight: bold;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🚀 ClientBoost AI</div>", unsafe_allow_html=True)

# =========================
# AI ENGINE (LEVEL BASED)
# =========================
def generate_solution(problem, business, product, audience, level):

    base = f"We are {business} helping {audience} with {product}."

    if level == "basic":
        return f"""
🔥 BASIC RESULT

{base}

👉 Simple message:
Buy {product} and improve your business.

"""

    if level == "premium":
        return f"""
🚀 PREMIUM RESULT

{base}

💡 Persuasive message:
{product} is designed to help {audience} achieve better results faster.

✔ Clear value
✔ Better engagement
✔ Higher conversion

"""

    if level == "ultra":
        return f"""
👑 ULTRA RESULT

{base}

🎯 Hook:
Stop struggling, start growing today.

💡 Value:
{product} helps {audience} save time, increase sales and scale faster.

🚀 Strategy:
- Strong positioning
- Emotional trigger
- Clear CTA

👉 Optimized for maximum conversion.

"""

    return base


# =========================
# HOME
# =========================
if st.session_state.page == "home":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write("""
## 🔥 Grow your business with AI

❌ You struggle to write content  
❌ You waste time on marketing  
❌ You don’t know how to sell  

---

💡 Everything becomes instant with AI
""")

    if st.button("🚀 Commencer maintenant"):
        st.session_state.page = "problems"

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# PROBLEMS
# =========================
elif st.session_state.page == "problems":

    st.subheader("💡 Choose your problem")

    problems = [
        "📩 Sales messages",
        "📢 Marketing content",
        "🔄 Client follow-up",
        "💰 Increase sales",
        "⚡ Save time",
        "🧠 Beginner help",
        "📈 Business growth"
    ]

    st.session_state.selected = st.radio("Select one:", problems)

    if st.button("Continue"):
        st.session_state.page = "levels"


# =========================
# LEVELS (BASIC / PREMIUM / ULTRA)
# =========================
elif st.session_state.page == "levels":

    st.subheader("💎 Choose your plan")

    st.write(f"### Problem: {st.session_state.selected}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🥉 BASIC
        💰 5€
        Simple content generation
        """)
        if st.button("Choose Basic"):
            st.session_state.level = "basic"
            st.session_state.page = "payment"

    with col2:
        st.markdown("""
        ### 🥈 PREMIUM ⭐
        💰 15€
        Better conversion content
        """)
        if st.button("Choose Premium"):
            st.session_state.level = "premium"
            st.session_state.page = "payment"

    with col3:
        st.markdown("""
        ### 🥇 ULTRA 👑
        💰 29€
        Full AI strategy + high conversion
        """)
        if st.button("Choose Ultra"):
            st.session_state.level = "ultra"
            st.session_state.page = "payment"


# =========================
# PAYMENT + RESULT
# =========================
elif st.session_state.page == "payment":

    st.subheader("💳 Payment")

    if not st.session_state.paid:
        st.warning("🔒 Unlock required")

        if st.button("💳 Pay (demo)"):
            st.session_state.paid = True
            st.success("Payment successful ✔")

    else:

        st.success("Access unlocked ✔")

        business = st.text_input("Business name")
        product = st.text_input("Product / Service")
        audience = st.text_input("Target audience")

        if st.button("Generate"):

            result = generate_solution(
                st.session_state.selected,
                business,
                product,
                audience,
                st.session_state.level
            )

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("🚀 Result")
            st.text_area("Output", result, height=300)
            st.markdown("</div>", unsafe_allow_html=True)


# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Created by kēllønę 🔗💨")
