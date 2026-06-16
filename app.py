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
# SESSION STATE
# =========================
if "result" not in st.session_state:
    st.session_state.result = ""

if "generated" not in st.session_state:
    st.session_state.generated = False

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
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🚀 ClientBoost AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Get more customers. Grow your business faster.</div>", unsafe_allow_html=True)

# =========================
# MENU
# =========================
menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Sales Message", "Marketing Content", "Follow-Up", "Pricing"]
)

# =========================
# HOME
# =========================
if menu == "Home":
    st.markdown("""
    <div class="box">
    <h3>Welcome 👋</h3>
    <p>Create sales messages, marketing content and follow-ups instantly.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# SALES MESSAGE
# =========================
elif menu == "Sales Message":

    st.subheader("💬 Sales Message Generator")

    business = st.text_input("Business Name")
    product = st.text_input("Product / Service")
    audience = st.text_input("Target Audience")

    if st.button("Generate"):

        st.session_state.result = f"""
Hello,

We are {business}.

We help {audience} with our {product}.

We can help you grow your business and increase your sales.

Best regards,
{business} team
"""
        st.session_state.generated = True

    if st.session_state.generated:
        st.success("Result generated")
        st.text_area("Output", st.session_state.result, height=200)

# =========================
# MARKETING CONTENT
# =========================
elif menu == "Marketing Content":

    st.subheader("📢 Marketing Content Generator")

    platform = st.selectbox("Platform", ["Facebook", "Instagram", "LinkedIn", "TikTok"])
    topic = st.text_input("Topic")

    if st.button("Generate"):

        st.session_state.result = f"""
🔥 {topic}

Discover how our solution helps your business grow faster on {platform}.

Start today and see results instantly.

#Business #Growth #Marketing
"""
        st.session_state.generated = True

    if st.session_state.generated:
        st.success("Result generated")
        st.text_area("Output", st.session_state.result, height=200)

# =========================
# FOLLOW-UP
# =========================
elif menu == "Follow-Up":

    st.subheader("🔄 Follow-Up Generator")

    name = st.text_input("Client Name")
    service = st.text_input("Service")

    if st.button("Generate"):

        st.session_state.result = f"""
Hello {name},

Just following up regarding our {service} discussion.

Let me know if you have any questions.

Looking forward to your reply.
"""
        st.session_state.generated = True

    if st.session_state.generated:
        st.success("Result generated")
        st.text_area("Output", st.session_state.result, height=200)

# =========================
# PRICING
# =========================
elif menu == "Pricing":

    st.subheader("💰 Pricing Plans")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Starter\n€5\n1 result")

    with col2:
        st.markdown("### ⭐ Pro\n€15\n5 results")

    with col3:
        st.markdown("### Business\n€29/month\nUnlimited")

st.markdown("---")
st.caption("Created by kēllønę 🔗💨")import streamlit as st

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
if "result" not in st.session_state:
    st.session_state.result = ""

if "generated" not in st.session_state:
    st.session_state.generated = False

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
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🚀 ClientBoost AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Get more customers. Grow your business faster.</div>", unsafe_allow_html=True)

# =========================
# MENU
# =========================
menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Sales Message", "Marketing Content", "Follow-Up", "Pricing"]
)

# =========================
# HOME
# =========================
if menu == "Home":
    st.markdown("""
    <div class="box">
    <h3>Welcome 👋</h3>
    <p>Create sales messages, marketing content and follow-ups instantly.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# SALES MESSAGE
# =========================
elif menu == "Sales Message":

    st.subheader("💬 Sales Message Generator")

    business = st.text_input("Business Name")
    product = st.text_input("Product / Service")
    audience = st.text_input("Target Audience")

    if st.button("Generate"):

        st.session_state.result = f"""
Hello,

We are {business}.

We help {audience} with our {product}.

We can help you grow your business and increase your sales.

Best regards,
{business} team
"""
        st.session_state.generated = True

    if st.session_state.generated:
        st.success("Result generated")
        st.text_area("Output", st.session_state.result, height=200)

# =========================
# MARKETING CONTENT
# =========================
elif menu == "Marketing Content":

    st.subheader("📢 Marketing Content Generator")

    platform = st.selectbox("Platform", ["Facebook", "Instagram", "LinkedIn", "TikTok"])
    topic = st.text_input("Topic")

    if st.button("Generate"):

        st.session_state.result = f"""
🔥 {topic}

Discover how our solution helps your business grow faster on {platform}.

Start today and see results instantly.

#Business #Growth #Marketing
"""
        st.session_state.generated = True

    if st.session_state.generated:
        st.success("Result generated")
        st.text_area("Output", st.session_state.result, height=200)

# =========================
# FOLLOW-UP
# =========================
elif menu == "Follow-Up":

    st.subheader("🔄 Follow-Up Generator")

    name = st.text_input("Client Name")
    service = st.text_input("Service")

    if st.button("Generate"):

        st.session_state.result = f"""
Hello {name},

Just following up regarding our {service} discussion.

Let me know if you have any questions.

Looking forward to your reply.
"""
        st.session_state.generated = True

    if st.session_state.generated:
        st.success("Result generated")
        st.text_area("Output", st.session_state.result, height=200)

# =========================
# PRICING
# =========================
elif menu == "Pricing":

    st.subheader("💰 Pricing Plans")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Starter\n€5\n1 result")

    with col2:
        st.markdown("### ⭐ Pro\n€15\n5 results")

    with col3:
        st.markdown("### Business\n€29/month\nUnlimited")

st.markdown("---")
st.caption("Created by kēllønę 🔗💨")
