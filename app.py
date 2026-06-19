import streamlit as st

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="ClientBoost AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DICTIONNAIRE DE TRADUCTION POUR L'INTERFACE ---
T = {
    "English": {
        "nav_home": "🏠 Home",
        "nav_gen": "🚀 Generator",
        "nav_sub": "💳 My Subscription",
        "nav_hist": "📜 History",
        "nav_set": "⚙️ Settings",
        "tagline": "The intelligent sales copy generator that converts prospects into loyal customers.",
        "description": "Stop wasting time writing generic messages. ClientBoost AI analyzes your prospect's pain points to create high-impact, personalized hooks that trigger immediate interest.",
        "motivation_title": "Daily Motivation",
        "motivation": "“Don't sell a product. Sell the solution to your customer's deepest pain.”",
        "cta": "🚀 Start Now",
        "lang_info": "Target language active",
        "secteur_lbl": "Your industry / Product :",
        "secteur_ph": "e.g., SEO Agency, Fitness Coach, HR SaaS...",
        "cible_lbl": "Who is your ideal customer (Persona)?",
        "cible_ph": "e.g., Marketing Directors, Busy parents...",
        "prob_lbl": "What is your customer's main pain point?",
        "prob_ph": "e.g., They lack online visibility, they don't have time to cook...",
        "gen_btn": "✨ Generate my sales copy",
        "gen_wait": "AI is drafting your copy in",
        "gen_success": "Your copy has been generated in",
        "gen_ready": "Your copy ready to copy-paste:",
        "gen_sample": "Example of persuasive copy written in",
        "gen_warn": "Please fill in all fields before launching the generation.",
        "sub_title": "💳 Pricing & Plans",
        "sub_sub": "Upgrade to unlock unlimited AI generations.",
        "sub_std": "🥉 Standard Plan",
        "sub_std_price": "$9 / month",
        "sub_pro": "🥈 Pro Plan (Popular)",
        "sub_pro_price": "$29 / month",
        "sub_agn": "🥇 Agency Plan",
        "sub_agn_price": "$79 / month"
    },
    "Français": {
        "nav_home": "🏠 Accueil",
        "nav_gen": "🚀 Générateur",
        "nav_sub": "💳 Mon Abonnement",
        "nav_hist": "📜 Historique",
        "nav_set": "⚙️ Paramètres",
        "tagline": "Le générateur de messages de vente intelligent qui convertit vos prospects en clients.",
        "description": "Arrêtez d'envoyer des messages génériques. ClientBoost AI cible la douleur majeure de votre prospect pour rédiger des accroches percutantes et adaptées qui déclenchent des ventes.",
        "motivation_title": "Motivation du jour",
        "motivation": "« Ne vendez pas un produit. Vendez la solution à la douleur la plus profonde de votre client. »",
        "cta": "🚀 Commencer maintenant",
        "lang_info": "Langue de génération active",
        "secteur_lbl": "Votre secteur d'activité / Produit :",
        "secteur_ph": "Ex : Agence SEO, Coach de fitness, SaaS RH...",
        "cible_lbl": "Qui est votre client idéal (Persona) ?",
        "cible_ph": "Ex : Directeurs Marketing, Particuliers débordés...",
        "prob_lbl": "Quel est le problème principal de votre client ?",
        "prob_ph": "Ex : Ils manquent de visibilité en ligne, ils n'ont pas le temps...",
        "gen_btn": "✨ Générer mon message de vente",
        "gen_wait": "L'IA rédige votre message en",
        "gen_success": "Votre message a été généré en",
        "gen_ready": "Votre texte prêt à copier :",
        "gen_sample": "Exemple de message persuasif rédigé en",
        "gen_warn": "Veuillez remplir tous les champs avant de lancer la génération.",
        "sub_title": "💳 Tarifs & Abonnement",
        "sub_sub": "Passez à la vitesse supérieure pour débloquer l'illimité.",
        "sub_std": "🥉 Plan Standard",
        "sub_std_price": "9€ / mois",
        "sub_pro": "🥈 Plan Pro (Populaire)",
        "sub_pro_price": "29€ / mois",
        "sub_agn": "🥇 Plan Agence",
        "sub_agn_price": "79€ / mois"
    }
}

# --- GESTION DE L'ÉTAT (SESSION STATE) ---
if "page_actuelle" not in st.session_state:
    st.session_state.page_actuelle = "🏠 Home"

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    st.title("🚀 ClientBoost AI")
    st.write("Turn your prospects into buyers.")
    st.write("---")
    
    # Langue de génération (Anglais par défaut / index 0)
    langue_cible = st.selectbox(
        "Target Language (AI) :",
        ["English", "Français", "Español", "Deutsch", "Italiano", "Português"],
        index=0
    )
    
    # Choix de la langue de l'interface (Automatique selon langue_cible)
    ui_lang = "Français" if langue_cible == "Français" else "English"
    trans = T[ui_lang]
    
    st.write("---")
    
    # Navigation
    st.subheader("Navigation")
    nav_map = {
        trans["nav_home"]: "🏠 Home",
        trans["nav_gen"]: "🚀 Generator",
        trans["nav_sub"]: "💳 My Subscription",
        trans["nav_hist"]: "📜 History",
        trans["nav_set"]: "⚙️ Settings"
    }
    
    # Inversion pour retrouver l'index actuel
    current_nav_label = [k for k, v in nav_map.items() if v == st.session_state.page_actuelle][0]
    selection = st.radio("Menu", list(nav_map.keys()), index=list(nav_map.keys()).index(current_nav_label), label_visibility="collapsed")
    st.session_state.page_actuelle = nav_map[selection]


# --- CONTENU DES PAGES ---

# 🏠 PAGE D'ACCUEIL (LANDING PAGE)
if st.session_state.page_actuelle == "🏠 Home":
    st.write("")
    st.write("")
    st.markdown(f"<h1 style='text-align: center; font-size: 70px; color: #0ea5e9;'>ClientBoost AI</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: #334155; font-weight: 500;'>{trans['tagline']}</h3>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='text-align: center; max-width: 800px; margin: 20px auto; font-size: 19px; color: #475569;'>{trans['description']}</p>", unsafe_allow_html=True)
    
    # Bloc Motivation
    st.markdown(f"""
        <div style="background-color: #f0f9ff; border-left: 5px solid #0ea5e9; padding: 25px; border-radius: 10px; max-width: 800px; margin: 40px auto; text-align: center;">
            <p style="font-size: 14px; font-weight: bold; color: #0284c7; text-transform: uppercase; margin-bottom: 10px;">💡 {trans['motivation_title']}</p>
            <p style="font-size: 22px; font-style: italic; color: #0f172a;">{trans['motivation']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # CTA - Bouton d'appel à l'action
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button(trans["cta"], type="primary", use_container_width=True):
            st.session_state.page_actuelle = "🚀 Generator"
            st.rerun()

# 🚀 GÉNÉRATEUR
elif st.session_state.page_actuelle == "🚀 Generator":
    st.title(trans["nav_gen"])
    st.info(f"{trans['lang_info']}: **{langue_cible}**")
    
    col1, col2 = st.columns(2)
    with col1:
        secteur = st.text_input(trans["secteur_lbl"], placeholder=trans["secteur_ph"])
        cible = st.text_input(trans["cible_lbl"], placeholder=trans["cible_ph"])
    with col2:
        probleme = st.text_area(trans["prob_lbl"], placeholder=trans["prob_ph"])
        
    if st.button(trans["gen_btn"], type="primary", use_container_width=True):
        if secteur and cible and probleme:
            with st.spinner(f"{trans['gen_wait']} {langue_cible}..."):
                import time
                time.sleep(1.5)
                st.success(f"✅ {trans['gen_success']} {langue_cible}!")
                st.text_area(trans["gen_ready"], value=f"[{trans['gen_sample']} {langue_cible} : '{probleme}']", height=200)
        else:
            st.warning(trans["gen_warn"])

# 💳 ABONNEMENT
elif st.session_state.page_actuelle == "💳 My Subscription":
    st.title(trans["sub_title"])
    st.write(trans["sub_sub"])
    
    c1, c2, c3 = st.columns(3)
    with c1: st.subheader(trans["sub_std"]); st.write(trans["sub_std_price"]); st.button("Select", key="b1")
    with c2: st.subheader(trans["sub_pro"]); st.write(trans["sub_pro_price"]); st.button("Upgrade", type="primary", key="b2")
    with c3: st.subheader(trans["sub_agn"]); st.write(trans["sub_agn_price"]); st.button("Contact Sales", key="b3")

# 📜 HISTORIQUE & PARAMÈTRES
elif st.session_state.page_actuelle == "📜 History":
    st.title("History")
    st.write("Your past generations will appear here.")

elif st.session_state.page_actuelle == "⚙️ Settings":
    st.title("Settings")
    st.text_input("API Key", type="password")
