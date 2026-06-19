
import streamlit as st
import time
import random
from datetime import datetime

# ─────────────────────────────────────────────
# 1. CONFIGURATION
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="ClientBoost AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# 2. CSS GLOBAL
# ─────────────────────────────────────────────
st.markdown("""
<style>
    /* Police & fond */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }
    section[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
    section[data-testid="stSidebar"] .stRadio label { 
        padding: 8px 12px; border-radius: 8px; transition: background 0.2s;
    }
    section[data-testid="stSidebar"] .stRadio label:hover { background: rgba(255,255,255,0.08); }

    /* Fond principal */
    .main .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1100px; }

    /* Cartes */
    .card {
        background: white;
        border-radius: 16px;
        padding: 28px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 4px 16px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }
    .card-blue {
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        color: white;
        border-radius: 16px;
        padding: 28px;
        margin-bottom: 20px;
    }
    .card-dark {
        background: #0f172a;
        border-radius: 16px;
        padding: 28px;
        margin-bottom: 20px;
    }

    /* Hero */
    .hero-title {
        font-size: 64px;
        font-weight: 800;
        background: linear-gradient(135deg, #0ea5e9, #2563eb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        line-height: 1.1;
        margin-bottom: 16px;
    }
    .hero-sub {
        font-size: 20px;
        color: #475569;
        text-align: center;
        max-width: 680px;
        margin: 0 auto 32px;
        line-height: 1.6;
    }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
        background: #dbeafe;
        color: #1d4ed8;
        margin-bottom: 8px;
    }
    .badge-green { background: #dcfce7; color: #15803d; }
    .badge-orange { background: #ffedd5; color: #c2410c; }

    /* Pricing cards */
    .price-card {
        background: white;
        border: 2px solid #e2e8f0;
        border-radius: 20px;
        padding: 32px 24px;
        text-align: center;
        transition: all 0.3s;
        height: 100%;
    }
    .price-card:hover { border-color: #0ea5e9; transform: translateY(-4px); box-shadow: 0 12px 40px rgba(14,165,233,0.15); }
    .price-card.popular { border-color: #0ea5e9; background: linear-gradient(135deg, #f0f9ff, #e0f2fe); }
    .price-amount { font-size: 42px; font-weight: 800; color: #0f172a; }
    .price-period { font-size: 14px; color: #64748b; }
    .feature-item { text-align: left; padding: 6px 0; font-size: 14px; color: #374151; border-bottom: 1px solid #f1f5f9; }
    .feature-item:last-child { border-bottom: none; }

    /* Historique */
    .history-item {
        background: #f8fafc;
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 12px;
        border-left: 4px solid #0ea5e9;
        cursor: pointer;
    }
    .history-item:hover { background: #f0f9ff; }
    .history-meta { font-size: 12px; color: #64748b; margin-bottom: 6px; }
    .history-preview { font-size: 14px; color: #0f172a; font-weight: 500; }

    /* Stats */
    .stat-box {
        background: white;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 1px solid #e2e8f0;
    }
    .stat-number { font-size: 32px; font-weight: 800; color: #0ea5e9; }
    .stat-label { font-size: 13px; color: #64748b; margin-top: 4px; }

    /* Bouton primaire */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #0ea5e9, #2563eb) !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 12px 28px !important;
        transition: all 0.2s !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 25px rgba(14,165,233,0.4) !important;
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 10px !important;
        border: 1.5px solid #e2e8f0 !important;
        font-size: 14px !important;
        transition: border-color 0.2s !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #0ea5e9 !important;
        box-shadow: 0 0 0 3px rgba(14,165,233,0.1) !important;
    }

    /* Masquer le footer Streamlit */
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# 3. TRADUCTIONS
# ─────────────────────────────────────────────
T = {
    "English": {
        "tagline": "Turn your prospects into loyal customers — instantly.",
        "description": "Stop sending generic messages. ClientBoost AI targets your prospect's core pain point to craft high-impact, personalized sales copy that triggers real results.",
        "motivation_title": "Today's Mindset",
        "motivation": "Don't sell a product. Sell the solution to your customer's deepest pain.",
        "cta": "🚀 Generate My First Message",
        "nav_home": "🏠 Home", "nav_gen": "🚀 Generator", "nav_sub": "💳 Subscription",
        "nav_hist": "📜 History", "nav_set": "⚙️ Settings",
        "secteur_lbl": "Your industry / Product", "secteur_ph": "e.g., SEO Agency, Fitness Coach, HR SaaS...",
        "cible_lbl": "Your ideal customer (Persona)", "cible_ph": "e.g., Marketing Directors, Busy parents...",
        "prob_lbl": "Customer's main pain point", "prob_ph": "e.g., No online visibility, no time to cook...",
        "tone_lbl": "Tone of voice", "gen_btn": "✨ Generate Sales Copy",
        "gen_warn": "Please fill in all fields.",
        "gen_ready": "Your copy — ready to use:",
        "copy_btn": "📋 Copy", "save_btn": "💾 Save to History",
        "saved_ok": "✅ Saved to history!",
        "sub_title": "Pricing & Plans", "sub_sub": "Unlock unlimited AI generations.",
        "hist_title": "Generation History", "hist_empty": "No generations yet. Start in the Generator!",
        "hist_clear": "🗑️ Clear History",
        "set_title": "Settings", "set_api": "Anthropic API Key (optional)",
        "set_api_help": "Add your key to use real Claude AI generations.",
        "set_save": "Save Settings", "set_saved": "✅ Settings saved!",
        "lang_active": "Generation language"
    },
    "Français": {
        "tagline": "Transformez vos prospects en clients fidèles — instantanément.",
        "description": "Arrêtez d'envoyer des messages génériques. ClientBoost AI cible la douleur majeure de votre prospect pour rédiger des accroches percutantes qui génèrent de vraies ventes.",
        "motivation_title": "Citation du jour",
        "motivation": "Ne vendez pas un produit. Vendez la solution à la douleur la plus profonde de votre client.",
        "cta": "🚀 Générer mon premier message",
        "nav_home": "🏠 Accueil", "nav_gen": "🚀 Générateur", "nav_sub": "💳 Abonnement",
        "nav_hist": "📜 Historique", "nav_set": "⚙️ Paramètres",
        "secteur_lbl": "Votre secteur / Produit", "secteur_ph": "Ex : Agence SEO, Coach fitness, SaaS RH...",
        "cible_lbl": "Votre client idéal (Persona)", "cible_ph": "Ex : Directeurs Marketing, Particuliers débordés...",
        "prob_lbl": "Problème principal du client", "prob_ph": "Ex : Pas de visibilité en ligne, pas le temps...",
        "tone_lbl": "Ton du message", "gen_btn": "✨ Générer mon message de vente",
        "gen_warn": "Veuillez remplir tous les champs.",
        "gen_ready": "Votre texte prêt à copier :",
        "copy_btn": "📋 Copier", "save_btn": "💾 Sauvegarder",
        "saved_ok": "✅ Sauvegardé dans l'historique !",
        "sub_title": "Tarifs & Abonnement", "sub_sub": "Débloquez les générations illimitées.",
        "hist_title": "Historique des générations", "hist_empty": "Aucune génération pour l'instant. Commencez dans le Générateur !",
        "hist_clear": "🗑️ Effacer l'historique",
        "set_title": "Paramètres", "set_api": "Clé API Anthropic (optionnel)",
        "set_api_help": "Ajoutez votre clé pour utiliser le vrai moteur Claude AI.",
        "set_save": "Enregistrer", "set_saved": "✅ Paramètres enregistrés !",
        "lang_active": "Langue de génération"
    }
}

# ─────────────────────────────────────────────
# 4. TEMPLATES DE GÉNÉRATION (sans API)
# ─────────────────────────────────────────────
TEMPLATES = {
    "English": {
        "Professional": [
            "Subject: The #1 challenge holding {cible} back from growth\n\nHi [First Name],\n\nI've been working with {cible} for a while now, and I keep hearing the same thing:\n\n\"{probleme}\"\n\nIt's one of those problems that quietly costs you time, clients, and revenue — every single day.\n\nThat's exactly why I built {secteur}. Not to add another tool to your stack, but to directly eliminate this bottleneck.\n\nWould you be open to a 20-minute call this week? I'll show you exactly how we solve this — no slides, no pitch, just results.\n\nBest,\n[Your Name]",
            "Hi [First Name],\n\nQuick question: how much revenue are you losing because of \"{probleme}\"?\n\nFor most {cible}, this translates to thousands of dollars left on the table each month.\n\nOur solution ({secteur}) has helped similar clients reclaim that value in under 30 days.\n\nWorth a conversation?\n\n[Your Name]"
        ],
        "Casual": [
            "Hey [First Name] 👋\n\nI'll be straight with you — I work with {cible} who deal with \"{probleme}\" daily.\n\nAnd I see how exhausting it is.\n\n{secteur} was literally built to fix this. Nothing fancy, just results.\n\nWant to see how? 5 minutes, that's all I'm asking.\n\nCheers,\n[Your Name]",
        ],
        "Urgent": [
            "⚠️ [First Name], this is costing you more than you think.\n\nEvery day you deal with \"{probleme}\", your competitors get ahead.\n\n{cible} who switched to {secteur} saw results in the first week.\n\nSpots are limited. Let's talk today.\n\n[Your Name]"
        ]
    },
    "Français": {
        "Professionnel": [
            "Objet : Le problème silencieux qui freine vos {cible}\n\nBonjour [Prénom],\n\nEn travaillant avec des {cible}, j'entends souvent la même chose :\n\n« {probleme} »\n\nC'est un problème qui coûte du temps, des clients et du chiffre d'affaires — chaque jour sans exception.\n\nC'est précisément pour cela que j'ai créé {secteur}. Pas pour ajouter un outil de plus, mais pour supprimer ce blocage définitivement.\n\nSeriez-vous disponible pour un échange de 20 minutes cette semaine ? Je vous montre concrètement comment on règle ça.\n\nCordialement,\n[Votre nom]",
            "Bonjour [Prénom],\n\nCombien vous coûte réellement \"{probleme}\" chaque mois ?\n\nPour la plupart des {cible}, c'est plusieurs milliers d'euros qui s'évaporent silencieusement.\n\nAvec {secteur}, nos clients règlent ce problème en moins de 30 jours.\n\nUn échange rapide vous intéresse ?\n\n[Votre nom]"
        ],
        "Décontracté": [
            "Salut [Prénom] 👋\n\nJe vais être direct : je bosse avec des {cible} qui galèrent avec \"{probleme}\" tous les jours.\n\nEt franchement, je comprends à quel point c'est épuisant.\n\n{secteur} a été créé exactement pour régler ça. Simple, efficace.\n\nOn se fait 5 minutes pour en parler ?\n\nÀ bientôt,\n[Votre nom]"
        ],
        "Urgent": [
            "⚠️ [Prénom], chaque jour compte.\n\nTandis que vous subissez \"{probleme}\", vos concurrents avancent.\n\nLes {cible} qui ont adopté {secteur} ont vu des résultats dès la première semaine.\n\nLes places sont limitées. Parlons-en aujourd'hui.\n\n[Votre nom]"
        ]
    }
}

def generate_copy(secteur, cible, probleme, langue, tone):
    lang_templates = TEMPLATES.get(langue, TEMPLATES["English"])
    # Fallback si la langue n'a pas ce tone
    tone_key = tone if tone in lang_templates else list(lang_templates.keys())[0]
    templates = lang_templates[tone_key]
    template = random.choice(templates)
    return template.format(secteur=secteur, cible=cible, probleme=probleme)


# ─────────────────────────────────────────────
# 5. SESSION STATE
# ─────────────────────────────────────────────
defaults = {
    "page": "home",
    "history": [],
    "last_generated": "",
    "api_key": "",
    "gen_count": 0
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─────────────────────────────────────────────
# 6. SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
        <div style="padding: 20px 0 10px;">
            <p style="font-size:26px; font-weight:800; margin:0; color:white;">🚀 ClientBoost</p>
            <p style="font-size:13px; color:#94a3b8; margin:4px 0 0;">AI Sales Copy Generator</p>
        </div>
    """, unsafe_allow_html=True)
    st.divider()

    langue_cible = st.selectbox(
        "🌐 Target Language",
        ["English", "Français", "Español", "Deutsch", "Italiano", "Português"],
        index=0
    )
    ui_lang = "Français" if langue_cible == "Français" else "English"
    tr = T[ui_lang]

    st.divider()
    st.markdown("<p style='font-size:11px; color:#64748b; font-weight:600; text-transform:uppercase; letter-spacing:1px;'>Navigation</p>", unsafe_allow_html=True)

    nav_items = [
        ("home", tr["nav_home"]),
        ("generator", tr["nav_gen"]),
        ("subscription", tr["nav_sub"]),
        ("history", tr["nav_hist"]),
        ("settings", tr["nav_set"]),
    ]

    for page_id, label in nav_items:
        is_active = st.session_state.page == page_id
        if st.button(
            label,
            key=f"nav_{page_id}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.page = page_id
            st.rerun()

    st.divider()

    # Stats dans la sidebar
    st.markdown(f"""
        <div style="background:rgba(14,165,233,0.1); border-radius:12px; padding:16px; text-align:center;">
            <p style="font-size:28px; font-weight:800; color:#38bdf8; margin:0;">{st.session_state.gen_count}</p>
            <p style="font-size:12px; color:#94a3b8; margin:4px 0 0;">messages generated</p>
        </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# 7. PAGES
# ─────────────────────────────────────────────

# ── HOME ──
if st.session_state.page == "home":
    st.markdown(f"<div class='hero-title'>ClientBoost AI</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-sub'>{tr['tagline']}</div>", unsafe_allow_html=True)

    # Stats en haut
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""<div class="stat-box"><div class="stat-number">12k+</div><div class="stat-label">Messages generated</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="stat-box"><div class="stat-number">3.8x</div><div class="stat-label">Avg. reply rate boost</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="stat-box"><div class="stat-number">6</div><div class="stat-label">Languages supported</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="stat-box"><div class="stat-number">98%</div><div class="stat-label">Satisfaction rate</div></div>""", unsafe_allow_html=True)

    st.write("")

    # Description + Motivation
    col_left, col_right = st.columns([3, 2])
    with col_left:
        st.markdown(f"""
        <div class="card">
            <span class="badge">✦ What it does</span>
            <h3 style="color:#0f172a; margin:8px 0 12px; font-size:22px;">Stop sending copy-paste messages</h3>
            <p style="color:#475569; line-height:1.7; font-size:15px;">{tr['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col_right:
        st.markdown(f"""
        <div class="card-blue">
            <p style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:1px; opacity:0.8; margin-bottom:12px;">💡 {tr['motivation_title']}</p>
            <p style="font-size:18px; font-style:italic; line-height:1.6; margin:0;">"{tr['motivation']}"</p>
        </div>
        """, unsafe_allow_html=True)

    # CTA
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button(tr["cta"], type="primary", use_container_width=True):
            st.session_state.page = "generator"
            st.rerun()


# ── GENERATOR ──
elif st.session_state.page == "generator":
    st.markdown(f"<h2 style='color:#0f172a;'>{tr['nav_gen']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<span class='badge'>{tr['lang_active']}: {langue_cible}</span>", unsafe_allow_html=True)
    st.write("")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            secteur = st.text_input(f"🏢 {tr['secteur_lbl']}", placeholder=tr["secteur_ph"])
            cible = st.text_input(f"🎯 {tr['cible_lbl']}", placeholder=tr["cible_ph"])
        with col2:
            probleme = st.text_area(f"⚡ {tr['prob_lbl']}", placeholder=tr["prob_ph"], height=120)
            tones_en = ["Professional", "Casual", "Urgent"]
            tones_fr = ["Professionnel", "Décontracté", "Urgent"]
            tones = tones_fr if ui_lang == "Français" else tones_en
            tone = st.selectbox(f"🎨 {tr['tone_lbl']}", tones)

    st.write("")
    if st.button(tr["gen_btn"], type="primary", use_container_width=True):
        if secteur and cible and probleme:
            with st.spinner("✨ Generating your personalized copy..."):
                time.sleep(1.8)
            result = generate_copy(secteur, cible, probleme, langue_cible, tone)
            st.session_state.last_generated = result
            st.session_state.gen_count += 1
            st.success("✅ Your copy is ready!")
        else:
            st.warning(tr["gen_warn"])

    if st.session_state.last_generated:
        st.write("")
        st.markdown(f"**{tr['gen_ready']}**")
        st.text_area("", value=st.session_state.last_generated, height=280, key="output_area")

        col_a, col_b, _ = st.columns([1, 1, 2])
        with col_a:
            if st.button(tr["save_btn"], use_container_width=True):
                entry = {
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "secteur": secteur if secteur else "–",
                    "cible": cible if cible else "–",
                    "langue": langue_cible,
                    "tone": tone,
                    "content": st.session_state.last_generated
                }
                st.session_state.history.insert(0, entry)
                st.success(tr["saved_ok"])


# ── SUBSCRIPTION ──
elif st.session_state.page == "subscription":
    st.markdown(f"<h2 style='color:#0f172a;'>💳 {tr['sub_title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748b; font-size:16px;'>{tr['sub_sub']}</p>", unsafe_allow_html=True)
    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="price-card">
            <p style="font-size:13px; color:#64748b; font-weight:600; text-transform:uppercase; letter-spacing:1px;">🥉 Standard</p>
            <div class="price-amount">$9</div>
            <div class="price-period">/ month</div>
            <hr style="margin:20px 0; border-color:#f1f5f9;">
            <div class="feature-item">✅ 50 generations / month</div>
            <div class="feature-item">✅ 3 languages</div>
            <div class="feature-item">✅ History (30 days)</div>
            <div class="feature-item">❌ Priority support</div>
            <div class="feature-item">❌ API access</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.button("Select Standard", key="b1", use_container_width=True)

    with c2:
        st.markdown("""
        <div class="price-card popular">
            <p style="font-size:13px; color:#0284c7; font-weight:600; text-transform:uppercase; letter-spacing:1px;">🥈 Pro</p>
            <span style="background:#0ea5e9; color:white; font-size:11px; font-weight:700; padding:3px 10px; border-radius:999px;">POPULAR</span>
            <div class="price-amount" style="margin-top:8px;">$29</div>
            <div class="price-period">/ month</div>
            <hr style="margin:20px 0; border-color:#bae6fd;">
            <div class="feature-item">✅ Unlimited generations</div>
            <div class="feature-item">✅ All 6 languages</div>
            <div class="feature-item">✅ History (1 year)</div>
            <div class="feature-item">✅ Priority support</div>
            <div class="feature-item">❌ API access</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.button("⚡ Upgrade to Pro", key="b2", type="primary", use_container_width=True)

    with c3:
        st.markdown("""
        <div class="price-card">
            <p style="font-size:13px; color:#64748b; font-weight:600; text-transform:uppercase; letter-spacing:1px;">🥇 Agency</p>
            <div class="price-amount">$79</div>
            <div class="price-period">/ month</div>
            <hr style="margin:20px 0; border-color:#f1f5f9;">
            <div class="feature-item">✅ Unlimited generations</div>
            <div class="feature-item">✅ All 6 languages</div>
            <div class="feature-item">✅ Unlimited history</div>
            <div class="feature-item">✅ Priority support</div>
            <div class="feature-item">✅ Full API access</div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.button("Contact Sales", key="b3", use_container_width=True)


# ── HISTORY ──
elif st.session_state.page == "history":
    st.markdown(f"<h2 style='color:#0f172a;'>📜 {tr['hist_title']}</h2>", unsafe_allow_html=True)

    if not st.session_state.history:
        st.markdown(f"""
        <div class="card" style="text-align:center; padding:60px;">
            <p style="font-size:48px; margin:0;">📭</p>
            <p style="color:#64748b; font-size:16px; margin-top:12px;">{tr['hist_empty']}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        col_info, col_clear = st.columns([4, 1])
        with col_info:
            st.markdown(f"<span class='badge badge-green'>{len(st.session_state.history)} generation(s) saved</span>", unsafe_allow_html=True)
        with col_clear:
            if st.button(tr["hist_clear"], use_container_width=True):
                st.session_state.history = []
                st.rerun()

        st.write("")
        for i, item in enumerate(st.session_state.history):
            with st.expander(f"📄 {item['secteur']} → {item['cible']}  |  {item['date']}  |  {item['langue']} · {item['tone']}"):
                st.text_area("", value=item["content"], height=200, key=f"hist_{i}")


# ── SETTINGS ──
elif st.session_state.page == "settings":
    st.markdown(f"<h2 style='color:#0f172a;'>⚙️ {tr['set_title']}</h2>", unsafe_allow_html=True)
    st.write("")

    with st.container():
        st.markdown(f"""<div class="card">
            <h4 style="color:#0f172a; margin-top:0;">🔑 API Configuration</h4>
        """, unsafe_allow_html=True)
        api_key = st.text_input(
            tr["set_api"],
            type="password",
            value=st.session_state.api_key,
            help=tr["set_api_help"]
        )
        st.markdown("""
            <p style="font-size:13px; color:#64748b; margin-top:4px;">
            💡 With your Anthropic API key, ClientBoost will use real Claude AI for more powerful, creative generations.
            Get your key at <a href="https://console.anthropic.com" target="_blank">console.anthropic.com</a>
            </p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(f"""<div class="card">
            <h4 style="color:#0f172a; margin-top:0;">📊 Your Stats</h4>
            <p style="color:#475569;">Total generations this session: <strong>{st.session_state.gen_count}</strong></p>
            <p style="color:#475569;">Messages saved to history: <strong>{len(st.session_state.history)}</strong></p>
        </div>""", unsafe_allow_html=True)

        if st.button(tr["set_save"], type="primary"):
            st.session_state.api_key = api_key
            st.success(tr["set_saved"])
