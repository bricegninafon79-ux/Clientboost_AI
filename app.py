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

if "problem" not in st.session_state:
    st.session_state.problem = ""

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
    font-size: 45px;
    font-weight: bold;
}
.box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🚀 ClientBoost AI</div>", unsafe_allow_html=True)

# =========================
# SIDEBAR = PROBLEMES
# =========================
problem = st.sidebar.radio(
    "Choose a problem",
    [
        "📩 Sales messages",
        "📢 Marketing content",
        "🔄 Client follow-up",
        "💰 Increase sales",
        "⚡ Save time",
        "🧠 Beginner help"
    ]
)

st.session_state.problem = problem

# =========================
# 1. DESCRIPTION PAGE
# =========================
st.subheader("📄 Problem description")

if problem == "📩 Sales messages":
    st.write("Create powerful messages to sell your product or service easily.")

elif problem == "📢 Marketing content":
    st.write("Generate posts for social media like Instagram, Facebook, TikTok.")

elif problem == "🔄 Client follow-up":
    st.write("Send professional follow-up messages to clients.")

elif problem == "💰 Increase sales":
    st.write("Improve your conversion rate and sell more.")

elif problem == "⚡ Save time":
    st.write("Automate writing tasks and save hours every day.")

elif problem == "🧠 Beginner help":
    st.write("Perfect for beginners who don’t know how to write marketing content.")

# =========================
# 2. PAYMENT STEP
# =========================
st.markdown("---")
st.subheader("💳 Unlock solution")

if not st.session_state.paid:

    st.warning("This solution is locked. Pay to unlock.")

    if st.button("💳 Pay now (demo)"):

        st.session_state.paid = True
        st.success("Payment successful ✔ You can now see the solution")

else:
    st.success("Access granted ✔")

# =========================
# 3. SOLUTION GENERATION
# =========================
if st.session_state.paid:

    st.markdown("---")
    st.subheader("🚀 Generated Solution")

    if problem == "📩 Sales messages":
        result = "🔥 We help you sell faster with high-converting messages."

    elif problem == "📢 Marketing content":
        result = "🚀 Create viral social media posts in seconds."

    elif problem == "🔄 Client follow-up":
        result = "📩 Send perfect follow-ups that bring clients back."

    elif problem == "💰 Increase sales":
        result = "📈 Improve conversions and grow your revenue."

    elif problem == "⚡ Save time":
        result = "⏱ Automate content creation and save hours daily."

    elif problem == "🧠 Beginner help":
        result = "🧠 Easy AI guidance for beginners in business."

    st.text_area("Output", result, height=200)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("Created by kēllønę 🔗💨")
