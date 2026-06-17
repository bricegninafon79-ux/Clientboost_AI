import streamlit as st
‎import streamlit.components.v1 as components
‎
‎st.set_page_config(page_title="ClientBoost Shopify", page_icon="🛍️", layout="wide")
‎
‎# STATE
‎if "page" not in st.session_state: st.session_state.page = "home"
‎if "content_type" not in st.session_state: st.session_state.content_type = ""
‎if "level" not in st.session_state: st.session_state.level = ""
‎if "paid" not in st.session_state: st.session_state.paid = False
‎
‎# DESIGN
‎st.markdown("""
‎<style>
‎.stApp {background-color: #0a0e1a; color: white;}
‎.title {text-align: center; font-size: 48px; font-weight: 800; background: linear-gradient(90deg, #F97316 0%, #FACC15 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
‎.card {background-color: #111827; padding: 25px; border-radius: 16px; margin-top: 15px; border: 1px solid #1f2937;}
‎.stButton > button {background: linear-gradient(90deg, #F97316 0%, #FB923C 100%); color: white; font-weight: bold; border-radius: 12px; width: 100%; padding: 16px; font-size: 16px; border: none;}
‎.trust {text-align: center; color: #9CA3AF; font-size: 14px;}
‎</style>
‎""", unsafe_allow_html=True)
‎
‎# MOTEUR COPY NICHE SHOPIFY
‎def generate_shopify_content(content_type, product, audience, level):
‎    hooks = {
‎        "basic": f"Struggling to sell {product}?",
‎        "premium": f"Stop posting content that gets 0 sales for {product}.",
‎        "ultra": f"Your competitors sell {product} daily. Your posts don't. Fix it now."
‎    }
‎
‎    templates = {
‎        "📢 1er post TikTok": {
‎            "basic": f"""🔥 HOOK: "POV: You found {product} and your life changed"
‎🎯 SCRIPT 6s: Show problem → Show {product} → Show result
‎📝 CTA: "Link in bio before stock runs out" """,
‎            "premium": f"""🚀 HOOK: "3 reasons {audience} are obsessed with {product}"
‎🎯 SCRIPT: Pain 2s + Product 2s + Result 2s + CTA 1s
‎💎 ANGLES: Before/After + Testimonial + Unboxing
‎[CTA] Post this + check sales in 24h""",
‎            "ultra": f"""👑 VIRAL FORMULA FOR {product}:
‎HOOK 0-2s: Pattern interrupt "Stop scrolling if you have "
‎BODY 2-4s: {product} solves it + quick demo
‎PROOF 4-5s: "500+ {audience} already switched"
‎CTA 5-6s: "Tap link - 50% off ends today"
‎PSYCHOLOGY: FOMO + Social proof + Scarcity"""
‎        },
‎        "📢 Description produit Shopify": {
‎            "basic": f"Transform your  with {product}. Loved by {audience}. Shop now.",
‎            "premium": f"Meet {product} - The #1 choice for {audience}. \n\n✅ Benefit 1: Saves you time\n✅ Benefit 2: Premium quality\n✅ Benefit 3: 30-day guarantee\nJoin 1000+ happy customers.",
‎            "ultra": f"WARNING: {product} is addictive.\n\n{audience} who try it NEVER go back.\n\n🧠 WHY IT WORKS:\n1. Solves  in 24h\n2. Designed for {audience}\n3. Risk-free: Money back guarantee\n\n⚡ LIMITED: Only 47 units left. Your competitor is buying now."
‎        },
‎        "📢 Bio Instagram": {
‎            "basic": f"Helping {audience} with {product} | DM for orders",
‎            "premium": f"🛍️ {product} for {audience}\n🚚 Fast shipping US\n⭐ 4.9/5 from 200+ reviews\n👇 Shop below",
‎            "ultra": f"Stop scrolling. Start earning.\n{product} = Your unfair advantage\nUsed by {audience} to make $$$\n⚡ 1st order -20% code: START\n👇 Link below or lose money"
‎        },
‎        "📢 Message DM client froid": {
‎            "basic": f"Hey! Saw you might like {product}. Want details?",
‎            "premium": f"Hey {audience}, quick question: Struggling with ? \n{product} fixed it for 200+ people. Want me to show how?",
‎            "ultra": f"3sec read: {product} = more sales for {audience}.\n\nI help stores like yours get 2.3x more DM sales.\n\nReply 'INFO' and I send the exact script I used."
‎        },
‎        "📢 Email abandon panier": {
‎            "basic": f"Forgot something? Your {product} is waiting. Complete order now.",
‎            "premium": f"Hey, your {product} is almost gone... \nCart reserved 2h only. {audience} love this item.\n[Complete order] + Free shipping if you act now.",
‎            "ultra": f"LAST WARNING: {product} selling fast.\n\n{audience} bought 12 units in last hour.\nYour cart expires in 47min.\n\n[CLAIM YOURS NOW] or competitor gets it."
‎        },
‎        "📢 Script vidéo 6s": {
‎            "basic": f"0-2s: Show pain\n2-4s: Show {product}\n4-6s: Show result + CTA",
‎            "premium": f"HOOK: 'Tired of ?'\nDEMO: {product} in action 2s\nPROOF: Before/After\nCTA: 'Link in bio'",
‎            "ultra": f"0-1s: TEXT 'POV: You found this'\n1-3s: {product} solving pain FAST\n3-5s: Happy customer + result\n5-6s: '50% OFF - Link below'"
‎        },
‎        "📢 Hook Facebook Ads": {
‎            "basic": f"Stop wasting money on ads that don't sell {product}.",
‎            "premium": f"{audience} are buying {product} like crazy. Here's why...",
‎            "ultra": f"Your competitor just made $10k with {product}. \nYou didn't. \nFix your ads with this 6s script →"
‎        }
‎    }
‎
‎    return f"🎯 {hooks[level]}\n\n{templates[content_type][level]}"
‎
‎def copy_button(text):
‎    components.html(f"""
‎    <button onclick="navigator.clipboard.writeText(`{text.replace('`','\\`')}`)"
‎    style="background:#F97316;color:white;border:none;padding:12px;border-radius:8px;cursor:pointer;font-weight:bold;width:100%;font-size:15px;">
‎    📋 Copier en 1 clic
‎    </button>
‎    """, height=55)
‎
‎# HEADER
‎st.markdown("<div class='title'>🛍️ ClientBoost Shopify</div>", unsafe_allow_html=True)
‎st.markdown("<div class='trust'>2,941 débutants Shopify • Contenu qui vend en 6s • No signup</div>", unsafe_allow_html=True)
‎
‎# HOME
‎if st.session_state.page == "home":
‎    st.markdown("<div class='card'>", unsafe_allow_html=True)
‎    st.write("## ❌ T'es débutant Shopify?")
‎    st.write("❌ Tes posts TikTok font 12 vues")
‎    st.write("❌ Ta description produit = 0 vente")
‎    st.write("❌ Tu sais pas quoi écrire pour vendre")
‎    st.write("---")
‎    st.write("💡 IA génère contenu qui vend pour {product} en 6 secondes")
‎    if st.button("🚀 Générer mon 1er contenu qui vend"):
‎        st.session_state.page = "content"
‎    st.markdown("</div>", unsafe_allow_html=True)
‎
‎# CONTENT TYPE - 7 SOLUTIONS POUR 1 PERSONA
‎elif st.session_state.page == "content":
‎    st.subheader("💡 Quel contenu tu veux créer AUJOURD'HUI?")
‎    content_types = [
‎        "📢 1er post TikTok",
‎        "📢 Description produit Shopify",
‎        "📢 Bio Instagram",
‎        "📢 Message DM client froid",
‎        "📢 Email abandon panier",
‎        "📢 Script vidéo 6s",
‎        "📢 Hook Facebook Ads"
‎    ]
‎    st.session_state.content_type = st.radio("Choisis 1:", content_types)
‎    if st.button("Continue →"):
‎        st.session_state.page = "levels"
‎
‎# LEVELS
‎elif st.session_state.page == "levels":
‎    st.subheader("💎 Choisis ton niveau")
‎    st.write(f"### Contenu: {st.session_state.content_type}")
‎
‎    col1, col2, col3 = st.columns(3)
‎    with col1:
‎        st.markdown("### 🥉 BASIC\n💰 $5\nSimple & rapide")
‎        if st.button("Basic"): st.session_state.level = "basic"; st.session_state.page = "payment"
‎    with col2:
‎        st.markdown("### 🥈 PRO ⭐\n💰 $15\n2.3x conversion")
‎        if st.button("Pro"): st.session_state.level = "premium"; st.session_state.page = "payment"
‎    with col3:
‎        st.markdown("### 🥇 ULTRA 👑\n💰 $29\nFormule virale complète")
‎        if st.button("Ultra"): st.session_state.level = "ultra"; st.session_state.page = "payment"
‎
‎# PAYMENT + RESULT
‎elif st.session_state.page == "payment":
‎    if not st.session_state.paid:
‎        st.warning("🔒 Débloque l'IA")
‎        st.info("💳 Lemon Squeezy - Test avec 4242 4242 4242 4242")
‎        if st.button("💳 Payer Demo $0"):
‎            st.session_state.paid = True; st.rerun()
‎    else:
‎        st.success("✔ Accès débloqué")
‎        product = st.text_input("Nom de ton produit Shopify")
‎        audience = st.text_input("Qui tu vends? Ex: femmes 18-25 ans")
‎
‎        if st.button("🚀 Générer mon contenu"):
‎            result = generate_shopify_content(st.session_state.content_type, product, audience, st.session_state.level)
‎            st.markdown("<div class='card'>", unsafe_allow_html=True)
‎            st.subheader("🚀 Ton contenu qui vend")
‎            st.text_area("Output", result, height=350, key="out")
‎            copy_button(result)
‎            st.download_button("⬇ Télécharger.txt", result, file_name="clientboost_shopify.txt")
‎            st.markdown("</div>", unsafe_allow_html=True)
‎
‎st.caption("Built by kēllønę 🔗💨 | ClientBoost Shopify v3")
