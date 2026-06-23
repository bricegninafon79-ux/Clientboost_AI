import streamlit as st
import time
import random
from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(page_title="ClientBoost AI", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

# ─────────────────────────────────────────────
# CSS GLOBAL
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;500;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.main .block-container { padding-top: 0rem; padding-bottom: 3rem; max-width: 1150px; }

section[data-testid="stSidebar"] { background: linear-gradient(180deg,#0a0f1e,#0f172a,#1a1f35) !important; border-right:1px solid rgba(255,255,255,0.06); }
section[data-testid="stSidebar"] * { color:#e2e8f0 !important; }

.stButton > button[kind="primary"] { background:linear-gradient(135deg,#6366f1,#8b5cf6) !important; border:none !important; border-radius:10px !important; font-weight:700 !important; color:white !important; transition:all 0.2s !important; }
.stButton > button[kind="primary"]:hover { transform:translateY(-2px) !important; box-shadow:0 8px 25px rgba(99,102,241,0.4) !important; }
.stTextInput > div > div > input, .stTextArea > div > div > textarea { border-radius:10px !important; border:1.5px solid #e2e8f0 !important; font-size:14px !important; }
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus { border-color:#6366f1 !important; box-shadow:0 0 0 3px rgba(99,102,241,0.1) !important; }
.stSelectbox > div > div { border-radius:10px !important; border:1.5px solid #e2e8f0 !important; }
footer { visibility:hidden; } #MainMenu { visibility:hidden; }

@keyframes pulse { 0%,100%{transform:scale(1)} 50%{transform:scale(1.08)} }
@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }
@keyframes spin { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
@keyframes glow { 0%,100%{filter:drop-shadow(0 0 4px #fbbf24)} 50%{filter:drop-shadow(0 0 12px #f59e0b)} }
@keyframes bounce-in { 0%{transform:scale(0.7);opacity:0} 60%{transform:scale(1.1)} 100%{transform:scale(1);opacity:1} }
@keyframes shimmer { 0%{background-position:-200% center} 100%{background-position:200% center} }

.icon-animated { display:inline-flex; align-items:center; justify-content:center; }
.icon-pulse { animation: pulse 2s ease-in-out infinite; }
.icon-float { animation: float 3s ease-in-out infinite; }
.icon-glow { animation: glow 2s ease-in-out infinite; }
.icon-bounce { animation: bounce-in 0.5s ease forwards; }

.star-gold { filter: drop-shadow(0 1px 3px rgba(251,191,36,0.6)); }
.star-wrap { display:inline-flex; gap:3px; align-items:center; }

.shimmer-text {
  background: linear-gradient(90deg, #6366f1 0%, #a78bfa 30%, #ec4899 60%, #6366f1 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer 3s linear infinite;
}

.level-glow { box-shadow: 0 0 20px rgba(99,102,241,0.5), 0 0 40px rgba(139,92,246,0.3); }
.card-hover { transition: transform 0.2s, box-shadow 0.2s; }
.card-hover:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(0,0,0,0.12); }

.prob-time:hover, .prob-money:hover, .prob-skill:hover,
.prob-growth:hover, .prob-frustration:hover, .prob-risk:hover,
.prob-retention:hover {
  filter: brightness(1.08);
  box-shadow: 0 12px 40px rgba(0,0,0,0.3);
  transform: translateY(-4px);
}

.card { background:white; border-radius:20px; padding:28px; border:1px solid #e8ecf0; box-shadow:0 2px 8px rgba(0,0,0,0.06); margin-bottom:20px; }
.badge { display:inline-block; padding:4px 14px; border-radius:999px; font-size:12px; font-weight:700; background:#ede9fe; color:#6d28d9; margin-bottom:8px; }
.badge-green { background:#dcfce7; color:#15803d; }
.metric-box { background:white; border-radius:16px; padding:22px; text-align:center; border:1px solid #e8ecf0; box-shadow:0 2px 8px rgba(0,0,0,0.05); transition:all 0.2s; }
.metric-box:hover { transform:translateY(-3px); box-shadow:0 8px 24px rgba(0,0,0,0.1); }
.metric-num { font-size:36px; font-weight:900; }
.metric-label { font-size:12px; color:#64748b; margin-top:4px; font-weight:600; text-transform:uppercase; letter-spacing:0.5px; }
.prog-wrap { background:#f1f5f9; border-radius:999px; height:10px; margin:8px 0; overflow:hidden; }
.prog-fill { height:10px; border-radius:999px; }
.auth-container { max-width:460px; margin:0 auto; background:white; border-radius:24px; padding:40px; border:1px solid #e8ecf0; box-shadow:0 8px 40px rgba(0,0,0,0.08); }
.prob-time { background:linear-gradient(135deg,#1e3a5f,#2563eb); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; height: 100%; }
.prob-money { background:linear-gradient(135deg,#064e3b,#059669); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; height: 100%; }
.prob-skill { background:linear-gradient(135deg,#451a03,#d97706); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; height: 100%; }
.prob-growth { background:linear-gradient(135deg,#0f172a,#6366f1); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; height: 100%; }
.prob-frustration { background:linear-gradient(135deg,#4c0519,#dc2626); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; height: 100%; }
.prob-risk { background:linear-gradient(135deg,#2e1065,#7c3aed); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; height: 100%; }
.prob-retention { background:linear-gradient(135deg,#431407,#ea580c); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; height: 100%; }
.prob-selected { border:3px solid white !important; box-shadow:0 0 0 3px rgba(255,255,255,0.4),0 12px 40px rgba(0,0,0,0.3) !important; transform:translateY(-4px); }
.workspace-time { background:linear-gradient(135deg,#eff6ff,#dbeafe); border:2px solid #3b82f6; border-radius:20px; padding:28px; }
.workspace-money { background:linear-gradient(135deg,#f0fdf4,#dcfce7); border:2px solid #22c55e; border-radius:20px; padding:28px; }
.workspace-skill { background:linear-gradient(135deg,#fffbeb,#fef3c7); border:2px solid #f59e0b; border-radius:20px; padding:28px; }
.workspace-growth { background:linear-gradient(135deg,#f5f3ff,#ede9fe); border:2px solid #8b5cf6; border-radius:20px; padding:28px; }
.workspace-frustration { background:linear-gradient(135deg,#fff1f2,#ffe4e6); border:2px solid #f43f5e; border-radius:20px; padding:28px; }
.workspace-risk { background:linear-gradient(135deg,#faf5ff,#f3e8ff); border:2px solid #a855f7; border-radius:20px; padding:28px; }
.workspace-retention { background:linear-gradient(135deg,#fff7ed,#ffedd5); border:2px solid #f97316; border-radius:20px; padding:28px; }
.landing-hero { background:linear-gradient(135deg,#0a0f1e 0%,#1e1b4b 50%,#0a0f1e 100%); padding:80px 40px; text-align:center; border-radius:0 0 40px 40px; margin-bottom:60px; color: white; }
.problem-pill { background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:16px; padding:20px 24px; margin-bottom:16px; backdrop-filter:blur(10px); }
.testimonial-card { background:white; border-radius:20px; padding:28px; border:1px solid #e8ecf0; box-shadow:0 4px 20px rgba(0,0,0,0.08); height:100%; }
.msg-preview { background:#f8fafc; border-radius:12px; padding:16px; border-left:4px solid #6366f1; font-size:13px; line-height:1.6; color:#374151; }
.price-card { background:white; border:2px solid #e8ecf0; border-radius:24px; padding:36px 28px; text-align:center; transition:all 0.3s; height: 100%; }
.price-card:hover { border-color:#6366f1; transform:translateY(-6px); box-shadow:0 20px 60px rgba(99,102,241,0.15); }
.price-card.popular { border-color:#6366f1; background:linear-gradient(135deg,#fafafa,#f5f3ff); }
.price-amount { font-size:48px; font-weight:900; color:#0f172a; }
.feature-item { text-align:left; padding:8px 0; font-size:14px; color:#374151; border-bottom:1px solid #f1f5f9; }
.feature-item:last-child { border-bottom:none; }
.payment-modal { background:white; border-radius:24px; padding:40px; border:2px solid #6366f1; box-shadow:0 20px 60px rgba(99,102,241,0.2); }
.email-preview { background:#f8fafc; border-radius:16px; padding:24px; border:1px solid #e8ecf0; font-size:14px; line-height:1.7; color:#374151; }
.email-header { background:linear-gradient(135deg,#6366f1,#8b5cf6); border-radius:12px 12px 0 0; padding:20px; color:white; text-align:center; margin:-24px -24px 20px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DONNÉES PROBLÈMES
# ─────────────────────────────────────────────
PROBLEMS = [
    {"id":"time","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M5 22h14M5 2h14M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/></svg>',"title":"Temps qui s'évapore","hook":"Vous passez 3h à rédiger ce qui devrait prendre 3 minutes.","desc":"Chaque message de prospection vous prend une éternité. Résultat : vous prospectez peu, vous signez peu.","solution":"ClientBoost génère un message complet et percutant en 10 secondes. Récupérez vos heures, concentrez-vous sur les deals.","color_class":"prob-time","workspace_class":"workspace-time","color":"#2563eb","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',"framework":"AIDA","tip":"Un message court (< 150 mots) obtient 2x plus de réponses.","fields":["Votre secteur / produit","Votre persona cible","Ce qui vous prend le plus de temps"],"placeholders":["Ex : Coach business, Agence web, SaaS RH","Ex : Directeurs marketing, Freelances débordés","Ex : Rédiger mes emails de prospection chaque matin"]},
    {"id":"money","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/></svg>',"title":"Budget qui s'évapore","hook":"Vous investissez. Vous n'encaissez pas. Quelque chose cloche.","desc":"Vos pubs tournent, vos emails partent, mais les conversions ne suivent pas. Le problème n'est pas votre offre — c'est le message.","solution":"ClientBoost applique AIDA, PAS et le storytelling pour transformer chaque euro investi en vrai retour sur investissement.","color_class":"prob-money","workspace_class":"workspace-money","color":"#059669","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',"framework":"PAS","tip":"Framework PAS : Problème → Agitation → Solution. Le plus efficace pour convertir à froid.","fields":["Votre offre / produit","Votre client idéal","Où vous perdez de l'argent actuellement"],"placeholders":["Ex : Formation en ligne, Logiciel B2B","Ex : TPE qui veulent croître, E-commerçants","Ex : Mes pubs Facebook ne convertissent pas"]},
    {"id":"skill","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.84A2.5 2.5 0 0 1 9.5 2"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.84A2.5 2.5 0 0 0 14.5 2"/></svg>',"title":"Page blanche paralysante","hook":"Vous savez ce que vous vendez. Vous ne savez pas comment le dire.","desc":"Syndrome de la page blanche, accroches fades, messages qui ne donnent pas envie de répondre.","solution":"ClientBoost intègre 10+ frameworks (AIDA, PAS, FAB, storytelling) pour que chaque message soit structuré pour convaincre.","color_class":"prob-skill","workspace_class":"workspace-skill","color":"#d97706","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>',"framework":"FAB","tip":"Framework FAB : Feature → Advantage → Benefit. Traduisez les fonctionnalités en bénéfices concrets.","fields":["Votre produit / service","Votre persona","Votre blocage principal à l'écriture"],"placeholders":["Ex : Outil de gestion de projet, Coaching carrière","Ex : Entrepreneurs solo, Managers d'équipes","Ex : Je ne sais pas par quoi commencer mon message"]},
    {"id":"growth","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>',"title":"Pipeline à sec","hook":"Votre offre est bonne. Votre agenda est vide. C'est urgent.","desc":"Pas assez de leads, pas assez de conversations, pas assez de contrats signés. La croissance ne se produit pas par hasard.","solution":"Générez 10, 50 ou 100 messages hyper-ciblés en quelques minutes. Volume + personnalisation = pipeline plein.","color_class":"prob-growth","workspace_class":"workspace-growth","color":"#7c3aed","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/></svg>',"framework":"Storytelling","tip":"Storytelling : commencez par une situation que votre prospect vit, pas par votre produit.","fields":["Votre secteur","Votre client idéal (persona)","Quel résultat vous promettez en X jours ?"],"placeholders":["Ex : Agence SEO, Consultant RH, Application mobile","Ex : Startups en croissance, PME de 10-50 salariés","Ex : +30% de leads qualifiés en 30 jours"]},
]

SAMPLE_MESSAGES = [
    {"problem":"time","tone":"Percutant","preview":"Objet : Récupérez 10h par semaine\n\nBonjour [Prénom],\n\nUne question directe : combien d'heures avez-vous passé cette semaine à rédiger des messages au lieu de les envoyer ?\n\nPour la plupart des directeurs marketing, c'est entre 5 et 15h perdues. Chaque semaine.\n\nNos clients récupèrent en moyenne 8h par semaine dès le premier mois.\n\nJe vous montre comment en 20 minutes. Cette semaine ?\n\n[Votre nom]"},
    {"problem":"money","tone":"Storytelling","preview":"Objet : Il a réduit son coût d'acquisition de 60%\n\nBonjour [Prénom],\n\nMarc investissait 2 000€/mois en pub. Résultat : 3-4 clients. Rentabilité nulle.\n\nSon problème : ses campagnes ne convertissaient pas. Le message ne parlait pas à sa cible.\n\nAvec ClientBoost, même budget, messages restructurés avec PAS.\n\nRésultat en 30 jours : 9 clients. CAC divisé par 3.\n\nVous voulez que je vous montre exactement ce qu'on a changé ?\n\n[Votre nom]"},
]

# ─────────────────────────────────────────────
# INITIALISATION DES ÉTATS (ROUTER)
# ─────────────────────────────────────────────
if "step" not in st.session_state:
    st.session_state.step = "landing"
if "selected_problem" not in st.session_state:
    st.session_state.selected_problem = None
if "form_data" not in st.session_state:
    st.session_state.form_data = {}
if "selected_tone" not in st.session_state:
    st.session_state.selected_tone = "Percutant"
if "generated_text" not in st.session_state:
    st.session_state.generated_text = None

# ─────────────────────────────────────────────
# ÉTAPE 1 : LANDING & SÉLECTION DU PROBLÈME
# ─────────────────────────────────────────────
if st.session_state.step == "landing":
    st.markdown(f"""
    <div class="landing-hero">
        <h1 style='font-size:46px; font-weight:900; margin-bottom:12px;'>Multipliez vos réponses de prospection par <span class="shimmer-text">7x</span></h1>
        <p style='font-size:18px; opacity:0.85; max-width:700px; margin:0 auto 30px;'>Générez des messages de vente chirurgicaux basés sur les frameworks psychologiques les plus puissants du copywriting.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; margin-bottom:35px;'>Quel est votre plus grand obstacle actuel ?</h2>", unsafe_allow_html=True)

    cols_prob = st.columns(len(PROBLEMS))
    for idx, prob in enumerate(PROBLEMS):
        with cols_prob[idx]:
            st.markdown(f"""
            <div class="{prob['color_class']}">
                <div style="margin-bottom:15px;">{prob['icon']}</div>
                <h3 style="font-size:18px; font-weight:700; margin-bottom:8px;">{prob['title']}</h3>
                <p style="font-size:13px; opacity:0.9; line-height:1.4;">{prob['hook']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            if st.button("Sélectionner", key=f"btn_{prob['id']}", type="secondary", use_container_width=True):
                st.session_state.selected_problem = prob["id"]
                st.session_state.step = "description"
                st.rerun()

# ─────────────────────────────────────────────
# ÉTAPE 2 : DESCRIPTION DU PROBLÈME / INPUTS (ISOLÉE)
# ─────────────────────────────────────────────
elif st.session_state.step == "description":
    current_prob = next(p for p in PROBLEMS if p["id"] == st.session_state.selected_problem)
    
    if st.button("← Retour aux problèmes", type="secondary"):
        st.session_state.step = "landing"
        st.rerun()
        
    st.markdown(f"""
    <div class="{current_prob['workspace_class']}">
        <span class="badge badge-green">Framework {current_prob['framework']} activé</span>
        <h2 style="color:#0f172a; font-weight:800; margin-top:5px;">Atelier de configuration : {current_prob['title']}</h2>
        <p style="color:#475569; font-size:14px; margin-bottom:20px;">{current_prob['desc']}</p>
        <div style="background:rgba(255,255,255,0.6); padding:12px 18px; border-radius:10px; font-size:13px; color:#1e1b4b; margin-bottom:25px; font-weight:500;">
            💡 {current_prob['tip']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    with st.form("generation_form"):
        temp_inputs = []
        col_inputs = st.columns(3)
        for idx, field in enumerate(current_prob["fields"]):
            with col_inputs[idx]:
                val = st.text_input(field, placeholder=current_prob["placeholders"][idx], key=f"input_{idx}")
                temp_inputs.append(val)
                
        chosen_tone = st.selectbox("Ton du message", ["Percutant", "Storytelling", "Direct", "Institutionnel"])
        submit_inputs = st.form_submit_with_button_label("🔓 Verrouiller et passer au plan d'accès", kind="primary")
        
        if submit_inputs:
            if not all(temp_inputs):
                st.warning("Veuillez remplir tous les champs requis pour calibrer l'IA.")
            else:
                st.session_state.form_data = temp_inputs
                st.session_state.selected_tone = chosen_tone
                # Étape suivante obligatoire : Le Paiement
                st.session_state.step = "payment"
                st.rerun()

# ─────────────────────────────────────────────
# ÉTAPE 3 : PAIEMENT & ABONNEMENT OBLIGATOIRE (PAYWALL)
# ─────────────────────────────────────────────
elif st.session_state.step == "payment":
    current_prob = next(p for p in PROBLEMS if p["id"] == st.session_state.selected_problem)
    
    if st.button("← Modifier les informations", type="secondary"):
        st.session_state.step = "description"
        st.rerun()
        
    st.markdown("""
    <div style="text-align:center; margin-bottom:40px; background:#fff1f2; border:1px solid #fecdd3; padding:20px; border-radius:15px;">
        <span style="font-size:24px;">🔒</span>
        <h2 style="color:#9f1239; font-weight:800; margin-top:5px; margin-bottom:5px;">Une dernière étape pour débloquer votre message unique</h2>
        <p style="color:#4c0519; font-size:14px; margin:0;">Votre stratégie est configurée et prête à être injectée. Choisissez votre abonnement pour lancer l'IA.</p>
    </div>
    """, unsafe_allow_html=True)

    cols_price = st.columns(3)
    
    with cols_price[0]:
        st.markdown("""
        <div class="price-card">
            <div class="badge">Starter</div>
            <div class="price-amount">9€<span style="font-size:16px; font-weight:500; color:#64748b;">/mois</span></div>
            <p style="color:#64748b; font-size:13px; margin-bottom:20px;">Idéal pour tester</p>
            <div class="feature-item">✓ 5 générations de messages / mois</div>
            <div class="feature-item">✓ Accès au framework AIDA</div>
            <div class="feature-item">✗ Historique Cloud</div>
            <br>
        </div>
        """, unsafe_allow_html=True)
        if st.button("M'abonner au plan Starter", key="pay_1", use_container_width=True):
            with st.spinner("Validation de la souscription sécurisée..."):
                time.sleep(1.5)
            st.session_state.step = "result"
            st.rerun()

    with cols_price[1]:
        st.markdown("""
        <div class="price-card popular">
            <div class="badge badge-green" style="background:#6366f1; color:white;">🔥 PLUS POPULAIRE</div>
            <div class="price-amount">29€<span style="font-size:16px; font-weight:500; color:#64748b;">/mois</span></div>
            <p style="color:#64748b; font-size:13px; margin-bottom:20px;">Pour les agences & indépendants</p>
            <div class="feature-item"><strong>✓ Messages illimités sans restriction</strong></div>
            <div class="feature-item">✓ Accès complet aux 10+ Frameworks</div>
            <div class="feature-item">✓ Support ultra-prioritaire</div>
            <div class="feature-item">✓ Module IA d'optimisation d'accroches</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Débloquer le Plan PRO immédiatement", key="pay_2", type="primary", use_container_width=True):
            with st.spinner("Traitement du paiement en cours..."):
                time.sleep(1.5)
            st.session_state.step = "result"
            st.rerun()

    with cols_price[2]:
        st.markdown("""
        <div class="price-card">
            <div class="badge">Enterprise</div>
            <div class="price-amount">99€<span style="font-size:16px; font-weight:500; color:#64748b;">/mois</span></div>
            <p style="color:#64748b; font-size:13px; margin-bottom:20px;">Pour les équipes de vente</p>
            <div class="feature-item">✓ Équipe jusqu'à 5 commerciaux</div>
            <div class="feature-item">✓ IA entraînée sur vos offres</div>
            <div class="feature-item">✓ Intégration API Hubspot</div>
            <br>
        </div>
        """, unsafe_allow_html=True)
        if st.button("M'abonner au plan Enterprise", key="pay_3", use_container_width=True):
            with st.spinner("Validation de la licence d'équipe..."):
                time.sleep(1.5)
            st.session_state.step = "result"
            st.rerun()

# ─────────────────────────────────────────────
# ÉTAPE 4 : PAGE DE RÉSULTAT UNIQUE (SATISFACTION)
# ─────────────────────────────────────────────
elif st.session_state.step == "result":
    current_prob = next(p for p in PROBLEMS if p["id"] == st.session_state.selected_problem)
    
    st.balloons()
    st.success("💳 Abonnement actif ! Votre accès complet est déverrouillé.")
    
    st.markdown("<h2 style='margin-bottom:20px;'>Votre arme de prospection massive est prête</h2>", unsafe_allow_html=True)
    
    # Simulation de génération IA basée sur les entrées mémorisées
    with st.spinner("Génération finale en cours d'écriture..."):
        match = next((m for m in SAMPLE_MESSAGES if m["problem"] == current_prob["id"] and m["tone"] == st.session_state.selected_tone), None)
        if match:
            final_text = match["preview"]
        else:
            final_text = f"Objet : Amélioration stratégique pour votre activité\n\nBonjour,\n\nEn analysant les profils comme le vôtre, j'ai remarqué que la gestion de la douleur suivante est critique : {st.session_state.form_data[2]}.\n\nC'est pourquoi nous avons conçu une approche spécifique pour votre cible ({st.session_state.form_data[1]}).\n\nPrenons 10 minutes pour en parler de vive voix.\n\nCordialement."

    st.markdown(f"""
    <div class="email-preview">
        <div class="email-header">
            <strong>Format de Sortie • Framework {current_prob['framework']} • Ton {st.session_state.selected_tone}</strong>
        </div>
        <div style="white-space: pre-wrap; font-family: monospace; font-size: 14px;">{final_text}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🚀 Créer un nouveau message (Retour à l'accueil)", type="primary"):
        st.session_state.step = "landing"
        st.session_state.selected_problem = None
        st.session_state.generated_text = None
        st.rerun()

# ─────────────────────────────────────────────
# SIGNATURE DU CRÉATEUR
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:80px; font-size:12px; color:#94a3b8; font-weight:500; letter-spacing:0.5px;">
    SaaS développé par <span style="color:#6366f1; font-weight:700;">kēllønę🔗💨</span>
</div>
""", unsafe_allow_html=True)
