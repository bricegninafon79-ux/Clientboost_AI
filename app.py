import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="ClientBoost Shopify", page_icon="🛍️", layout="wide")

# STATE
if "page" not in st.session_state: st.session_state.page = "home"
if "content_type" not in st.session_state: st.session_state.content_type = ""
if "tone" not in st.session_state: st.session_state.tone = "💥 Cash & Aggressive"
if "level" not in st.session_state: st.session_state.level = ""
if "paid" not in st.session_state: st.session_state.paid = False

# DYNAMIC INPUTS STATE
if "input_1" not in st.session_state: st.session_state.input_1 = ""
if "input_2" not in st.session_state: st.session_state.input_2 = ""
if "input_3" not in st.session_state: st.session_state.input_3 = ""

# DESIGN
st.markdown("""
<style>
.stApp {background-color: #0a0e1a; color: white;}
.title {text-align: center; font-size: 48px; font-weight: 800; background: linear-gradient(90deg, #F97316 0%, #FACC15 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
.card {background-color: #111827; padding: 25px; border-radius: 16px; margin-top: 15px; border: 1px solid #1f2937;}
.stButton > button {background: linear-gradient(90deg, #F97316 0%, #FB923C 100%); color: white; font-weight: bold; border-radius: 12px; width: 100%; padding: 16px; font-size: 16px; border: none;}
.trust {text-align: center; color: #9CA3AF; font-size: 14px;}
</style>
""", unsafe_allow_html=True)

# SMART COPYWRITING ENGINE USING DYNAMIC VARIABLES
def generate_shopify_content(content_type, i1, i2, i3, level, tone):
    if content_type == "📢 Instagram Bio":
        # i1 = Product/Brand, i2 = Niche/Audience, i3 = Promo Code
        if tone == "💥 Cash & Aggressive":
            return f"❌ Tired of cheap alternatives?\n🛍️ The original {i1} for {i2} has finally arrived.\n⚡ Limited: -20% off with code: {i3}\n👇 Claim yours before stock hits zero!"
        else:
            return f"🔬 Certified {i1} Hub\n💡 Engineered for high-performance results among {i2}.\n🌿 Code active: {i3}\n👇 Read our report here:"

    elif content_type == "📢 Shopify Product Description":
        # i1 = Product Name, i2 = Target Pain Point, i3 = Guarantee/Bonus
        return f"### 📑 Premium {i1} — Eradicate {i2} Permanently\n\nSpecifically engineered to tackle the main struggle of modern users, the {i1} redefines efficiency standard.\n\n#### 🔬 Why it changes everything:\nStop dealing with {i2} every day. This formula delivers noticeable improvements within 24 hours.\n\n#### 📊 What you lock in today:\n* **Risk-Free Trial:** {i3} covered on every purchase.\n* **Premium Build Quality:** Tested and certified structure.\n\n*Hit 'Add to Cart' to protect your routine.*"

    elif content_type in ["📢 1st TikTok Post", "📢 6s Video Script"]:
        # i1 = Main hook hook trend, i2 = Product, i3 = Main Action on screen
        return f"🎬 VIRAL CONVERSION VIDEO SCRIPT ({level.upper()})\n\n[0s - 2s: Pattern Interrupt]\n🎥 VISUAL: {i3}\n🗣️ VOICE-OVER: \"Stop scrolling if you are dealing with {i1} right now!\"\n\n[2s - 4s: Solution Showcased]\n🎥 VISUAL: Smooth cut showing how {i2} acts instantly.\n🗣️ VOICE-OVER: \"This {i2} is literally breaking the market.\"\n\n[4s - 6s: Quick CTA]\n🎥 VISUAL: Fast pointing gesture towards bio.\n🗣️ VOICE-OVER: \"Secure yours via our bio link right now!\""

    elif content_type == "📢 Cart Abandonment Email":
        # i1 = Product left behind, i2 = Scarcity time limit, i3 = Incentive/Free shipping
        return f"🛒 Subject: ⏳ Your {i1} cart expires in {i2}...\n\nHey there!\n\nWe noticed you left your custom {i1} behind. Demand is exceptionally high and your slot will expire in exactly {i2}.\n\nTo help you make up your mind, we unlocked this special perk just for you: {i3}.\n\n⚡ [Reclaim My Order & Applied Perk]"

    else:
        # Defaults / Ads
        return f"💥 ACQUISITION HOOK ({tone})\n\nFocus: {i1} | Solution: {i2}\n\n👉 Angle: \"Tired of {i1}? {i2} is the missing link your ecommerce store needed. Click learn more to claim our blueprint.\""

# HEADER
st.markdown("<div class='title'>🛍️ ClientBoost Shopify</div>", unsafe_allow_html=True)
st.markdown("<div class='trust'>2,941 Shopify Beginners • Dynamic Generation Engine • No signup</div>", unsafe_allow_html=True)

# PAGE 1: HOME
if st.session_state.page == "home":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("## ❌ Are you a struggling Shopify Beginner?")
    st.write("❌ Your TikTok videos get stuck at 12 views")
    st.write("❌ Your current product description = 0 sales")
    st.write("---")
    st.write("💡 Our engine dynamically adapts its forms and outputs based on the exact problem you are solving.")
    if st.button("🚀 Choose My Copywriting Asset"):
        st.session_state.page = "content"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# PAGE 2: SELECT CONTENT TYPE
elif st.session_state.page == "content":
    st.subheader("💡 Select Your Asset Type")
    content_types = [
        "📢 1st TikTok Post",
        "📢 Shopify Product Description",
        "📢 Instagram Bio",
        "📢 Cart Abandonment Email",
        "📢 Facebook Ads Hook"
    ]
    st.session_state.content_type = st.radio("What are we building?", content_types)
    
    if st.button("Configure Dynamic Setup →"):
        st.session_state.page = "config"
        st.rerun()

# PAGE 3: FULLY DYNAMIC CONFIGURATION PAGE (Changes according to choice)
elif st.session_state.page == "config":
    st.subheader("⚙️ Contextual Data Setup")
    st.info(f"Customizing parameters specifically for: **{st.session_state.content_type}**")
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # CONDITION 1: INSTAGRAM BIO
    if st.session_state.content_type == "📢 Instagram Bio":
        st.session_state.input_1 = st.text_input("Brand or Product Name", value=st.session_state.input_1, placeholder="e.g., PosturePro")
        st.session_state.input_2 = st.text_input("Target Community / Audience niche", value=st.session_state.input_2, placeholder="e.g., Developers & Office Workers")
        st.session_state.input_3 = st.text_input("Bio Discount Code", value=st.session_state.input_3, placeholder="e.g., BIO20")
        
    # CONDITION 2: PRODUCT DESCRIPTION
    elif st.session_state.content_type == "📢 Shopify Product Description":
        st.session_state.input_1 = st.text_input("Main Product Name", value=st.session_state.input_1, placeholder="e.g., Orthopedic Pillow")
        st.session_state.input_2 = st.text_input("Biggest Pain Point / Frustration solved", value=st.session_state.input_2, placeholder="e.g., Chronic Neck Pain & Insomnia")
        st.session_state.input_3 = st.text_input("Guarantee policy or Free Bonus included", value=st.session_state.input_3, placeholder="e.g., 90-Day Money Back Guarantee")
        
    # CONDITION 3: TIKTOK / VIDEO SCRIPTS
    elif st.session_state.content_type in ["📢 1st TikTok Post", "📢 6s Video Script"]:
        st.session_state.input_1 = st.text_input("Relatable hook problem or TikTok trend", value=st.session_state.input_1, placeholder="e.g., Waking up completely crushed at 7 AM")
        st.session_state.input_2 = st.text_input("Product name being showcased", value=st.session_state.input_2, placeholder="e.g., DeepSleep Mask")
        st.session_state.input_3 = st.text_input("Visual action taking place in first 2 seconds", value=st.session_state.input_3, placeholder="e.g., Throwing a pillow face-camera out of pure exhaustion")

    # CONDITION 4: ABANDONED CART EMAIL
    elif st.session_state.content_type == "📢 Cart Abandonment Email":
        st.session_state.input_1 = st.text_input("Name of items left in shopping cart", value=st.session_state.input_1, placeholder="e.g., Wireless Massage Gun")
        st.session_state.input_2 = st.text_input("Urgency countdown / Time limit", value=st.session_state.input_2, placeholder="e.g., 47 minutes")
        st.session_state.input_3 = st.text_input("Extra customer checkout incentive", value=st.session_state.input_3, placeholder="e.g., Free Shipping + Extra 10% off automated coupon")

    # DEFAULT FALLBACK
    else:
        st.session_state.input_1 = st.text_input("Core Customer Frustration", value=st.session_state.input_1)
        st.session_state.input_2 = st.text_input("Core Unique Selling Proposition", value=st.session_state.input_2)
        st.session_state.input_3 = st.text_input("Call to Action text", value=st.session_state.input_3)

    st.session_state.tone = st.selectbox("Brand Voice Tone:", ["💥 Cash & Aggressive", "🧠 Scientific & Expert", "🎯 Humorous & Quirky"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    col_back, col_next = st.columns([1, 4])
    with col_back:
        if st.button("⬅ Change Format"):
            st.session_state.page = "content"
            st.rerun()
    with col_next:
        if st.button("Proceed to Strategy Level →"):
            if st.session_state.input_1 and st.session_state.input_2:
                st.session_state.page = "levels"
                st.rerun()
            else:
                st.error("⚠️ Please fill out the dynamic fields before matching your strategy!")

# PAGE 4: PRICING LEVELS
elif st.session_state.page == "levels":
    st.subheader("💎 Step 3: Select Copywriting Power")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='card' style='text-align:center;'><h3>🥉 BASIC</h3><h2 style='color:#9CA3AF;'>$5</h2></div>", unsafe_allow_html=True)
        if st.button("Choose Basic Plan"): 
            st.session_state.level = "basic"; st.session_state.page = "payment"; st.rerun()
    with col2:
        st.markdown("<div class='card' style='text-align:center; border: 1px solid #F97316;'><h3>🥈 PRO ⭐</h3><h2 style='color:#F97316;'>$15</h2></div>", unsafe_allow_html=True)
        if st.button("Choose Pro Plan"): 
            st.session_state.level = "premium"; st.session_state.page = "payment"; st.rerun()
    with col3:
        st.markdown("<div class='card' style='text-align:center; border: 1px solid #FACC15;'><h3>🥇 ULTRA 👑</h3><h2 style='color:#FACC15;'>$29</h2></div>", unsafe_allow_html=True)
        if st.button("Choose Ultra Plan"): 
            st.session_state.level = "ultra"; st.session_state.page = "payment"; st.rerun()

# PAGE 5: PAYMENT & RESULT DELIVERY
elif st.session_state.page == "payment":
    if not st.session_state.paid:
        st.warning("🔒 Unlock your custom dynamic asset")
        st.info("💳 Sandbox Gateway - Test card: 4242 4242 4242 4242")
        if st.button("💳 Validate Demo Payment ($0)"):
            st.session_state.paid = True
            st.rerun()
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e1b4b 0%, #111827 100%); padding: 25px; border-radius: 16px; border: 2px solid #F97316; margin-bottom: 25px;">
            <h3 style="color: #FACC15; margin-top: 0;">🎉 Generation Complete!</h3>
        </div>
        """, unsafe_allow_html=True)

        # ENGINE CONVERSION
        result_text = generate_shopify_content(
            st.session_state.content_type, 
            st.session_state.input_1, 
            st.session_state.input_2, 
            st.session_state.input_3, 
            st.session_state.level,
            st.session_state.tone
        )
        
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.text_area("Your Copywriting Output:", result_text, height=380, key="out")
        
        # Clipboard component
        escaped_result = result_text.replace('`', '\\`').replace('$', '\\$').replace('\n', '\\n')
        components.html(f"""
        <button onclick="navigator.clipboard.writeText(`{escaped_result}`)"
        style="background: linear-gradient(90deg, #F97316 0%, #FACC15 100%); color:white; border:none; padding:12px; border-radius:8px; cursor:pointer; font-weight:bold; width:100%; font-size:15px; height: 45px;">
        📋 1-Click Copy To Clipboard
        </button>
        """, height=55)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("🔄 Create Another Asset"):
            st.session_state.page = "home"
            st.session_state.paid = False
            st.rerun()

st.caption("Built by kēllønę | ClientBoost Shopify v3")
            
