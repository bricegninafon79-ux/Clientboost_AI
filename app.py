import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(
    page_title="ClientBoost AI",
    page_icon="🚀",
    layout="centered"
)

# --- INITIALIZE SESSION STATE ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "landing"
if "selected_problem" not in st.session_state:
    st.session_state.selected_problem = None

# --- THE 7 EXACT PROBLEMS ---
PROBLEMS = {
    "Time": "Time slipping away — Hours wasted drafting manual outreach",
    "Money": "Money burning — High customer acquisition costs with low ROI",
    "Skill": "Blank page syndrome — Struggling to find the right words to convert",
    "Growth": "Empty pipeline — Not enough qualified leads and sales meetings",
    "Frustration": "Outreach burnout — Hating the tedious process of cold prospecting",
    "Risk": "Brand reputation — Sending poorly optimized messages that burn leads",
    "Retention": "Leaking bucket — Losing potential clients due to lack of follow-up"
}

# --- ISOLATED CONFIGURATION PANEL ---
# Placed in the sidebar to keep the main landing page perfectly clean and focused on conversion
with st.sidebar:
    st.title("⚙️ SaaS Configuration")
    st.write("Manage backend settings without disrupting the user funnel.")
    
    # Configuration fields
    api_key = st.text_input("OpenAI API Key", type="password", value="sk-mock-key-xxxxxx")
    app_mode = st.selectbox("Environment Mode", ["Production", "Development", "Staging"])
    target_currency = st.selectbox("Pricing Currency", ["USD ($)", "EUR (€)"])
    
    st.divider()
    st.info("ClientBoost AI v2.0 — Settings Active")

# --- CONVERSION FUNNEL FLOW ---

# 1. LANDING PAGE
if st.session_state.current_page == "landing":
    st.title("🚀 ClientBoost AI")
    st.subheader("Transform your cold outreach into an automated client acquisition machine.")
    st.write(
        "Stop wasting hours writing copy that gets ignored. "
        "Generate high-converting, hyper-personalized B2B messages tailored to your market in seconds."
    )
    
    if st.button("Get Started Now", use_container_width=True):
        st.session_state.current_page = "problem_selection"
        st.rerun()

# 2. PROBLEM SELECTION PAGE
elif st.session_state.current_page == "problem_selection":
    st.subheader("Identify Your Main Roadblock")
    st.write("Select the core challenge holding your business growth back right now:")
    
    # Displaying the 7 exact problems
    chosen_problem = st.radio(
        "Select your primary obstacle:",
        options=list(PROBLEMS.keys()),
        format_func=lambda x: f"**{x}**: {PROBLEMS[x]}"
    )
    
    if st.button("Continue to Solution", use_container_width=True):
        st.session_state.selected_problem = chosen_problem
        st.session_state.current_page = "payment"
        st.rerun()

# 3. PAYMENT PAGE (Comes strictly before generation)
elif st.session_state.current_page == "payment":
    st.subheader("Unlock Your Tailored Copywriting Solution")
    st.write(f"You selected **{st.session_state.selected_problem}**. Our AI engine is ready to solve this roadblock.")
    
    # Payment Box UI
    st.info("💳 Secure Checkout — Lifetime Access Plan")
    st.metric(label="Special Launch Offer", value="$49", delta="One-time payment, no subscription")
    
    st.write("✓ Full access to specialized B2B copywriting angles")
    st.write("✓ Unlimited high-converting variations")
    
    if st.button("Complete Payment & Access Generator", use_container_width=True):
        st.success("Payment successful! Redirecting to your dashboard...")
        st.session_state.current_page = "generation"
        st.rerun()

# 4. GENERATION DASHBOARD
elif st.session_state.current_page == "generation":
    st.subheader("🤖 ClientBoost AI Generation Dashboard")
    st.caption(f"Optimized for solving: {st.session_state.selected_problem}")
    
    # Inputs
    company_name = st.text_input("Your Company or Product Name", placeholder="e.g., SaaSFlow")
    target_audience = st.text_input("Target Audience / Ideal Customer Profile", placeholder="e.g., Marketing Directors, Tech Founders")
    
    if st.button("Generate Copywriting Angles", type="primary", use_container_width=True):
        with st.spinner("Analyzing problem matrix and generating templates..."):
            st.subheader("🔥 Your High-Converting Angles")
            
            # Simulated tailored output based on selected problem
            st.markdown(f"### 🎯 Angle Focus: Overcoming {st.session_state.selected_problem}")
            st.info(
                f"Hey [First Name],\n\n"
                f"I noticed you're dealing with {st.session_state.selected_problem.lower()} challenges over at [Company]. "
                f"At {company_name or 'our company'}, we built a framework specifically designed for {target_audience or 'your niche'} "
                f"to completely automate this workflow.\n\n"
                f"Worth a quick 2-minute look? Let me know."
            )
            
    st.divider()
    if st.button("Restart Demo Funnel", type="secondary"):
        st.session_state.current_page = "landing"
        st.session_state.selected_problem = None
        st.rerun()

# --- MANDATORY FOOTER SIGNATURE ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888888; font-size: 0.85em; font-family: monospace;'>"
    "kēllønę🔗💨"
    "</div>", 
    unsafe_allow_html=True
)
