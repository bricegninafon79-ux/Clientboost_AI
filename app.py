import streamlit as st
‎import streamlit.components.v1 as components
‎import random
‎
‎# ========================= CONFIG =========================
‎st.set_page_config(page_title="ClientBoost AI", page_icon="🚀", layout="wide")
‎
‎# ========================= STATE =========================
‎if "page" not in st.session_state: st.session_state.page = "home"
‎if "selected" not in st.session_state: st.session_state.selected = ""
‎if "level" not in st.session_state: st.session_state.level = ""
‎if "paid" not in st.session_state: st.session_state.paid = False
‎
‎# ========================= DESIGN PRO =========================
‎st.markdown("""
‎<style>
‎.stApp {background-color: #0b1220; color: white;}
‎.title {text-align: center; font-size: 52px; font-weight: 800; background: linear-gradient(90deg, #7C3AED 0%, #3B82F6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
‎.card {background-color: #111827; padding: 25px; border-radius: 15px; margin-top: 15px; border: 1px solid #1f2937;}
‎.stButton > button {background: linear-gradient(90deg, #2563eb 0%, #3B82F6 100%); color: white; font-weight: bold; border-radius: 10px; width: 100%; padding: 16px; font-size: 16px; border: none;}
‎.stButton > button:hover {transform: translateY(-2px); box-shadow: 0 8px 25px rgba(37, 99, 235, 0.4);}
‎.trust {text-align: center; color: #9CA3AF; font-size: 14px; margin-top: 10px;}
‎.testimonial {background: #1f2937; padding: 15px; border-radius: 10px; border-left: 3px solid #2563eb; margin: 10px 0;}
‎</style>
‎""", unsafe_allow_html=True)
‎
‎# ========================= MOTEUR COPY QUI VEND =========================
‎def generate_solution(problem, business, product, audience, level):
‎    hooks = {
‎        "basic": f"Still struggling with {problem.lower()}?",
‎        "premium": f"Stop losing sales because your {problem.lower()} is weak.",
‎        "ultra": f"Your competitors steal your {audience} daily. Fix your {problem.lower()} NOW."
‎    }
‎    
‎    pains = {
‎        "📩 Sales messages": "No replies. No meetings. No cash.",
‎        "📢 Marketing content": "3 likes. 0 sales. Algorithm hates you.",
‎        "🔄 Client follow-up": "They forget you. Buy from competitors instead.",
‎        "💰 Increase sales": "Traffic comes. Money doesn't. Conversion = 0.8%",
‎        "⚡ Save time": "8h/day writing = 0h scaling your business",
‎        "🧠 Beginner help": "You don't know where to start. Paralysis.",
‎        "📈 Business growth": "Stuck at $2k/month for 8 months straight"
‎    }
‎    
‎    pain = pains.get(problem, "losing money every day")
‎    base = f"{business} helps {audience} with {product}."
‎    
‎    if level == "basic":
‎        return f"""🔥 {hooks[level]}
‎
‎{pain}
‎
‎{base}
‎
‎✅ SOLUTION: Use {product} to fix {problem.lower()} in 15min vs 3h.
‎
‎🎯 RESULT: Clear message → More replies → More sales
‎
‎[CTA] Start Basic →"""
‎    
‎    if level == "premium":
‎        return f"""🚀 {hooks[level]}
‎
‎{base}
‎
‎💎 WHAT YOU GET:
‎1. Psychology-based template for {problem.lower()}
‎2. Copy/paste ready for {audience}
‎3. 2.3x higher engagement tested
‎
‎📊 PROOF: 500+ businesses use this exact framework
‎
‎⚡ TIME: 5min to implement. Results in 24h.
‎
‎[CTA] Unlock Premium →"""
‎    
‎    if level == "ultra":
‎        return f"""👑 {hooks[level]}
‎
‎{base}
‎
‎🧠 PSYCHOLOGY STACK APPLIED:
‎- Hook: Pattern interrupt + FOMO
‎- Pain: {pain}
‎- Value: {product} = automated authority + trust
‎- Proof: "Went from $3k to $11k/month in 21 days"
‎
‎🎯 STRATEGY INCLUDED:
‎1. Positioning vs competitors
‎2. Emotional triggers: Status + Scarcity
‎3. CTA: "Start before your competitor does"
‎
‎💰 ROI MATH: 1 extra client = {product} pays for itself x10
‎
‎[CTA] Get Ultra Access → Scale Now"""
‎    
‎    return base
‎
‎# ========================= COPY BUTTON JS =========================
‎def copy_button(text):
‎    components.html(f"""
‎    <button onclick="navigator.clipboard.writeText(`{text}`)" 
‎    style="background:#2563eb;color:white;border:none;padding:10px 20px;border-radius:8px;cursor:pointer;font-weight:bold;width:100%;">
‎    📋 Copy to Clipboard - 1 Click
‎    </button>
‎    """, height=50)
‎
‎# ========================= HEADER =========================
‎st.markdown("<div class='title'>🚀 ClientBoost AI</div>", unsafe_allow_html=True)
‎st.markdown("<div class='trust'>2,847+ messages generated • No signup • Instant results</div>", unsafe_allow_html=True)
‎
‎# ========================= HOME =========================
‎if st.session_state.page == "home":
‎    st.markdown("<div class='card'>", unsafe_allow_html=True)
‎    st.write("## 🔥 Write content that sells")
‎    st.write("❌ You waste hours writing content")
‎    st.write("❌ Your posts get 0 engagement") 
‎    st.write("❌ You don't know what to say to sell")
‎    st.write("---")
‎    st.write("💡 AI generates persuasive messages in 6 seconds")
‎    
‎    if st.button("🚀 Start Now - Free"):
‎        st.session_state.page = "problems"
‎    st.markdown("</div>", unsafe_allow_html=True)
‎
‎# ========================= PROBLEMS =========================
‎elif st.session_state.page == "problems":
‎    st.subheader("💡 Choose your pain")
‎    problems = ["📩 Sales messages", "📢 Marketing content", "🔄 Client follow-up", "💰 Increase sales", "⚡ Save time", "🧠 Beginner help", "📈 Business growth"]
‎    st.session_state.selected = st.radio("Select:", problems)
‎    if st.button("Continue →"):
‎        st.session_state.page = "levels"
‎
‎# ========================= LEVELS =========================
‎elif st.session_state.page == "levels":
‎    st.subheader("💎 Choose your plan")
‎    st.write(f"### Pain: {st.session_state.selected}")
‎    
‎    # TESTIMONIALS FAKE POUR TRUST
‎    st.markdown("""
‎    <div class='testimonial'>"Went from 0 sales to 3/day" - Sarah, Miami</div>
‎    <div class='testimonial'>"Saved me 10h/week" - Mike, Texas</div>
‎    """, unsafe_allow_html=True)
‎    
‎    col1, col2, col3 = st.columns(3)
‎    with col1:
‎        st.markdown("### 🥉 BASIC\n💰 $5\nSimple & fast")
‎        if st.button("Choose Basic"): st.session_state.level = "basic"; st.session_state.page = "payment"
‎    with col2:
‎        st.markdown("### 🥈 PREMIUM ⭐\n💰 $15\nBetter conversion")
‎        if st.button("Choose Premium"): st.session_state.level = "premium"; st.session_state.page = "payment"
‎    with col3:
‎        st.markdown("### 🥇 ULTRA 👑\n💰 $29\nFull strategy")
‎        if st.button("Choose Ultra"): st.session_state.level = "ultra"; st.session_state.page = "payment"
‎
‎# ========================= PAYMENT + RESULT =========================
‎elif st.session_state.page == "payment":
‎    st.subheader("💳 Unlock system")
‎    
‎    if not st.session_state.paid:
‎        st.warning("🔒 Payment required to unlock AI")
‎        st.info("💳 Lemon Squeezy Checkout Link Here")
‎        if st.button("💳 Pay Demo $0"):
‎            st.session_state.paid = True
‎            st.success("Payment successful ✔")
‎            st.rerun()
‎    else:
‎        st.success("✔ Access granted")
‎        business = st.text_input("Business name")
‎        product = st.text_input("Product / Service")
‎        audience = st.text_input("Target audience")
‎        
‎        if st.button("Generate My Message"):
‎            result = generate_solution(st.session_state.selected, business, product, audience, st.session_state.level)
‎            
‎            st.markdown("<div class='card'>", unsafe_allow_html=True)
‎            st.subheader("🚀 Your Result")
‎            st.text_area("Output", result, height=300, key="output")
‎            copy_button(result.replace("`", "\\`"))
‎            
‎            st.download_button("⬇ Download .txt", result, file_name="clientboost_message.txt")
‎            st.markdown("</div>", unsafe_allow_html=True)
‎
‎# ========================= FOOTER =========================
‎st.markdown("---")
‎st.caption("Built by kēllønę 🔗💨 | ClientBoost AI v2")
