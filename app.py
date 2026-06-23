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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
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
/* ── ICÔNES RÉALISTES & ANIMATIONS ── */
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

/* Shimmer sur les cartes hero */
.shimmer-text {
  background: linear-gradient(90deg, #6366f1 0%, #a78bfa 30%, #ec4899 60%, #6366f1 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer 3s linear infinite;
}

/* Level badge glow */
.level-glow { box-shadow: 0 0 20px rgba(99,102,241,0.5), 0 0 40px rgba(139,92,246,0.3); }

/* Card hover lift */
.card-hover { transition: transform 0.2s, box-shadow 0.2s; }
.card-hover:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(0,0,0,0.12); }

/* Problem card neon border on hover */
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
.prob-time { background:linear-gradient(135deg,#1e3a5f,#2563eb); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; }
.prob-money { background:linear-gradient(135deg,#064e3b,#059669); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; }
.prob-skill { background:linear-gradient(135deg,#451a03,#d97706); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; }
.prob-growth { background:linear-gradient(135deg,#0f172a,#6366f1); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; }
.prob-frustration { background:linear-gradient(135deg,#4c0519,#dc2626); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; }
.prob-risk { background:linear-gradient(135deg,#2e1065,#7c3aed); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; }
.prob-retention { background:linear-gradient(135deg,#431407,#ea580c); border-radius:20px; padding:24px; color:white; border:3px solid transparent; transition:all 0.3s; }
.prob-selected { border:3px solid white !important; box-shadow:0 0 0 3px rgba(255,255,255,0.4),0 12px 40px rgba(0,0,0,0.3) !important; transform:translateY(-4px); }
.workspace-time { background:linear-gradient(135deg,#eff6ff,#dbeafe); border:2px solid #3b82f6; border-radius:20px; padding:28px; }
.workspace-money { background:linear-gradient(135deg,#f0fdf4,#dcfce7); border:2px solid #22c55e; border-radius:20px; padding:28px; }
.workspace-skill { background:linear-gradient(135deg,#fffbeb,#fef3c7); border:2px solid #f59e0b; border-radius:20px; padding:28px; }
.workspace-growth { background:linear-gradient(135deg,#f5f3ff,#ede9fe); border:2px solid #8b5cf6; border-radius:20px; padding:28px; }
.workspace-frustration { background:linear-gradient(135deg,#fff1f2,#ffe4e6); border:2px solid #f43f5e; border-radius:20px; padding:28px; }
.workspace-risk { background:linear-gradient(135deg,#faf5ff,#f3e8ff); border:2px solid #a855f7; border-radius:20px; padding:28px; }
.workspace-retention { background:linear-gradient(135deg,#fff7ed,#ffedd5); border:2px solid #f97316; border-radius:20px; padding:28px; }
.landing-hero { background:linear-gradient(135deg,#0a0f1e 0%,#1e1b4b 50%,#0a0f1e 100%); padding:80px 40px; text-align:center; border-radius:0 0 40px 40px; margin-bottom:60px; }
.problem-pill { background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:16px; padding:20px 24px; margin-bottom:16px; backdrop-filter:blur(10px); }
.testimonial-card { background:white; border-radius:20px; padding:28px; border:1px solid #e8ecf0; box-shadow:0 4px 20px rgba(0,0,0,0.08); height:100%; }
.msg-preview { background:#f8fafc; border-radius:12px; padding:16px; border-left:4px solid #6366f1; font-size:13px; line-height:1.6; color:#374151; }
.price-card { background:white; border:2px solid #e8ecf0; border-radius:24px; padding:36px 28px; text-align:center; transition:all 0.3s; }
.price-card:hover { border-color:#6366f1; transform:translateY(-6px); box-shadow:0 20px 60px rgba(99,102,241,0.15); }
.price-card.popular { border-color:#6366f1; background:linear-gradient(135deg,#fafafa,#f5f3ff); }
.price-amount { font-size:48px; font-weight:900; color:#0f172a; }
.feature-item { text-align:left; padding:8px 0; font-size:14px; color:#374151; border-bottom:1px solid #f1f5f9; }
.feature-item:last-child { border-bottom:none; }
.payment-modal { background:white; border-radius:24px; padding:40px; border:2px solid #6366f1; box-shadow:0 20px 60px rgba(99,102,241,0.2); }
.email-preview { background:#f8fafc; border-radius:16px; padding:24px; border:1px solid #e8ecf0; font-size:14px; line-height:1.7; }
.email-header { background:linear-gradient(135deg,#6366f1,#8b5cf6); border-radius:12px 12px 0 0; padding:20px; color:white; text-align:center; margin:-24px -24px 20px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DONNÉES PROBLÈMES
# ─────────────────────────────────────────────
PROBLEMS = [
    {"id":"time","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M5 22h14M5 2h14M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/></svg>',"title":"Temps qui s'évapore","hook":"Vous passez 3h à rédiger ce qui devrait prendre 3 minutes.","desc":"Chaque message de prospection vous prend une éternité. Résultat : vous prospectez peu, vous signez peu.","solution":"ClientBoost génère un message complet et percutant en 10 secondes. Récupérez vos heures, concentrez-vous sur les deals.","color_class":"prob-time","workspace_class":"workspace-time","color":"#2563eb","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',"framework":"AIDA","tip":"<svg style='display:inline-block;vertical-align:middle;margin-right:4px;' width='14' height='14' viewBox='0 0 24 24' fill='#FBBF24' stroke='#F59E0B' stroke-width='1'><path d='M9 21h6m-6-3h6M12 3a6 6 0 0 1 4.47 10.06c-.62.62-1.47 1.3-1.47 2.94v.5H9v-.5c0-1.64-.85-2.32-1.47-2.94A6 6 0 0 1 12 3z'/></svg> Un message court (< 150 mots) obtient 2x plus de réponses.","fields":["Votre secteur / produit","Votre persona cible","Ce qui vous prend le plus de temps"],"placeholders":["Ex : Coach business, Agence web, SaaS RH","Ex : Directeurs marketing, Freelances débordés","Ex : Rédiger mes emails de prospection chaque matin"]},
    {"id":"money","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/></svg>',"title":"Budget qui s'évapore","hook":"Vous investissez. Vous n'encaissez pas. Quelque chose cloche.","desc":"Vos pubs tournent, vos emails partent, mais les conversions ne suivent pas. Le problème n'est pas votre offre — c'est le message.","solution":"ClientBoost applique AIDA, PAS et le storytelling pour transformer chaque euro investi en vrai retour sur investissement.","color_class":"prob-money","workspace_class":"workspace-money","color":"#059669","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',"framework":"PAS","tip":"<svg style='display:inline-block;vertical-align:middle;margin-right:4px;' width='14' height='14' viewBox='0 0 24 24' fill='#FBBF24' stroke='#F59E0B' stroke-width='1'><path d='M9 21h6m-6-3h6M12 3a6 6 0 0 1 4.47 10.06c-.62.62-1.47 1.3-1.47 2.94v.5H9v-.5c0-1.64-.85-2.32-1.47-2.94A6 6 0 0 1 12 3z'/></svg> Framework PAS : Problème → Agitation → Solution. Le plus efficace pour convertir à froid.","fields":["Votre offre / produit","Votre client idéal","Où vous perdez de l'argent actuellement"],"placeholders":["Ex : Formation en ligne, Logiciel B2B","Ex : TPE qui veulent croître, E-commerçants","Ex : Mes pubs Facebook ne convertissent pas"]},
    {"id":"skill","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.84A2.5 2.5 0 0 1 9.5 2"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.84A2.5 2.5 0 0 0 14.5 2"/></svg>',"title":"Page blanche paralysante","hook":"Vous savez ce que vous vendez. Vous ne savez pas comment le dire.","desc":"Syndrome de la page blanche, accroches fades, messages qui ne donnent pas envie de répondre.","solution":"ClientBoost intègre 10+ frameworks (AIDA, PAS, FAB, storytelling) pour que chaque message soit structuré pour convaincre.","color_class":"prob-skill","workspace_class":"workspace-skill","color":"#d97706","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>',"framework":"FAB","tip":"<svg style='display:inline-block;vertical-align:middle;margin-right:4px;' width='14' height='14' viewBox='0 0 24 24' fill='#FBBF24' stroke='#F59E0B' stroke-width='1'><path d='M9 21h6m-6-3h6M12 3a6 6 0 0 1 4.47 10.06c-.62.62-1.47 1.3-1.47 2.94v.5H9v-.5c0-1.64-.85-2.32-1.47-2.94A6 6 0 0 1 12 3z'/></svg> Framework FAB : Feature → Advantage → Benefit. Traduisez les fonctionnalités en bénéfices concrets.","fields":["Votre produit / service","Votre persona","Votre blocage principal à l'écriture"],"placeholders":["Ex : Outil de gestion de projet, Coaching carrière","Ex : Entrepreneurs solo, Managers d'équipes","Ex : Je ne sais pas par quoi commencer mon message"]},
    {"id":"growth","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>',"title":"Pipeline à sec","hook":"Votre offre est bonne. Votre agenda est vide. C'est urgent.","desc":"Pas assez de leads, pas assez de conversations, pas assez de contrats signés. La croissance ne se produit pas par hasard.","solution":"Générez 10, 50 ou 100 messages hyper-ciblés en quelques minutes. Volume + personnalisation = pipeline plein.","color_class":"prob-growth","workspace_class":"workspace-growth","color":"#7c3aed","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/></svg>',"framework":"Storytelling","tip":"<svg style='display:inline-block;vertical-align:middle;margin-right:4px;' width='14' height='14' viewBox='0 0 24 24' fill='#FBBF24' stroke='#F59E0B' stroke-width='1'><path d='M9 21h6m-6-3h6M12 3a6 6 0 0 1 4.47 10.06c-.62.62-1.47 1.3-1.47 2.94v.5H9v-.5c0-1.64-.85-2.32-1.47-2.94A6 6 0 0 1 12 3z'/></svg> Storytelling : commencez par une situation que votre prospect vit, pas par votre produit.","fields":["Votre secteur","Votre client idéal (persona)","Quel résultat vous promettez en X jours ?"],"placeholders":["Ex : Agence SEO, Consultant RH, Application mobile","Ex : Startups en croissance, PME de 10-50 salariés","Ex : +30% de leads qualifiés en 30 jours"]},
    {"id":"frustration","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M16 16s-1.5-2-4-2-4 2-4 2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/><path d="M9 5c0 0 1.5 2 3 2s3-2 3-2"/></svg>',"title":"Prospection que vous détestez","hook":"Vous envoyez. Silence radio. Encore et encore.","desc":"La prospection à froid vous épuise. Vous vous sentez intrusif, vous n'obtenez aucune réponse.","solution":"ClientBoost crée des messages empathiques qui parlent à vos prospects. Des conversations qu'ils ont envie d'avoir.","color_class":"prob-frustration","workspace_class":"workspace-frustration","color":"#dc2626","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',"framework":"Empathy Map","tip":"<svg style='display:inline-block;vertical-align:middle;margin-right:4px;' width='14' height='14' viewBox='0 0 24 24' fill='#FBBF24' stroke='#F59E0B' stroke-width='1'><path d='M9 21h6m-6-3h6M12 3a6 6 0 0 1 4.47 10.06c-.62.62-1.47 1.3-1.47 2.94v.5H9v-.5c0-1.64-.85-2.32-1.47-2.94A6 6 0 0 1 12 3z'/></svg> Pensez à ce que votre prospect ressent, craint et désire avant d'écrire une seule ligne.","fields":["Votre produit / service","Votre persona cible","Pourquoi vos messages n'obtiennent pas de réponse ?"],"placeholders":["Ex : Logiciel de facturation, Formation marketing","Ex : Artisans indépendants, PME sans équipe marketing","Ex : Mes messages semblent trop commerciaux ou génériques"]},
    {"id":"risk","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',"title":"Réputation en jeu","hook":"Un mauvais message peut griller 100 prospects d'un coup.","desc":"Vous avez peur d'envoyer un message qui paraît non professionnel ou qui brûle définitivement votre base de contacts.","solution":"ClientBoost garantit des messages calibrés : bon ton, bonne structure, bon niveau de professionnalisme à chaque fois.","color_class":"prob-risk","workspace_class":"workspace-risk","color":"#7c3aed","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',"framework":"Trust Builder","tip":"<svg style='display:inline-block;vertical-align:middle;margin-right:4px;' width='14' height='14' viewBox='0 0 24 24' fill='#FBBF24' stroke='#F59E0B' stroke-width='1'><path d='M9 21h6m-6-3h6M12 3a6 6 0 0 1 4.47 10.06c-.62.62-1.47 1.3-1.47 2.94v.5H9v-.5c0-1.64-.85-2.32-1.47-2.94A6 6 0 0 1 12 3z'/></svg> Trust Builder : démontrez que vous comprenez leur situation avant de parler de vous.","fields":["Votre secteur / produit","Votre persona","Ce que vous craignez le plus d'envoyer"],"placeholders":["Ex : Cabinet de conseil, Agence de communication","Ex : Grands comptes, Décideurs C-level","Ex : Un message trop agressif qui me fait passer pour un spammeur"]},
    {"id":"retention","icon":'<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>',"title":"Clients qui disparaissent","hook":"Acquérir un client coûte 5x plus cher que d'en garder un. Et vous les perdez.","desc":"Vos clients existants ne rachètent pas. Vos anciens clients vous ont oublié. Vous n'avez aucun système de suivi.","solution":"ClientBoost génère des séquences de relance, newsletters de réengagement et offres de suivi personnalisées.","color_class":"prob-retention","workspace_class":"workspace-retention","color":"#ea580c","emoji_bg":'<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="12 2 22 8.5 22 15.5 12 22 2 15.5 2 8.5 12 2"/><line x1="12" y1="22" x2="12" y2="15.5"/><polyline points="22 8.5 12 15.5 2 8.5"/></svg>',"framework":"Lifecycle Marketing","tip":"<svg style='display:inline-block;vertical-align:middle;margin-right:4px;' width='14' height='14' viewBox='0 0 24 24' fill='#FBBF24' stroke='#F59E0B' stroke-width='1'><path d='M9 21h6m-6-3h6M12 3a6 6 0 0 1 4.47 10.06c-.62.62-1.47 1.3-1.47 2.94v.5H9v-.5c0-1.64-.85-2.32-1.47-2.94A6 6 0 0 1 12 3z'/></svg> Un client existant a 60-70% de chance d'acheter à nouveau si vous restez présent au bon moment.","fields":["Votre produit / service","Vos clients existants (profil)","Depuis combien de temps sans contact ?"],"placeholders":["Ex : Service d'abonnement, Formation, Consulting","Ex : Clients achetés il y a 3-6 mois, Anciens abonnés","Ex : Plus de 2 mois, je n'ai aucun suivi automatique"]},
]

# ─────────────────────────────────────────────
# FAUX TÉMOIGNAGES & MESSAGES GÉNÉRÉS
# ─────────────────────────────────────────────
TESTIMONIALS = [
    {"name":"Sophie M.","role":"Consultante RH indépendante","initials":"SM","bg":"#6366f1","photo":"https://i.pravatar.cc/80?img=47","stars":"""<span class="star-wrap">
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</span>""","text":"En 2 semaines j'ai obtenu 11 rendez-vous qualifiés. Avant ClientBoost, j'en avais 2 par mois maximum. La différence ? Des messages qui parlent vraiment à mes prospects.","result":"11 RDV en 2 semaines"},
    {"name":"Karim B.","role":"Fondateur d'agence SEO","initials":"KB","bg":"#059669","photo":"https://i.pravatar.cc/80?img=12","stars":"""<span class="star-wrap">
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</span>""","text":"J'avais honte d'envoyer mes anciens messages. Maintenant mes prospects me remercient pour 'l'approche différente'. Mon taux de réponse est passé de 3% à 21%.","result":"Taux réponse x7"},
    {"name":"Marie-Claire T.","role":"Coach business & mindset","initials":"MT","bg":"#dc2626","photo":"https://i.pravatar.cc/80?img=5","stars":"""<span class="star-wrap">
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</span>""","text":"J'ai réactivé 43 anciens clients en un seul mailing. Sans pub, sans budget. Juste le bon message, au bon moment. ClientBoost a changé ma façon de voir la vente.","result":"43 clients réactivés"},
    {"name":"Thomas D.","role":"Freelance développeur","initials":"TD","bg":"#2563eb","photo":"https://i.pravatar.cc/80?img=33","stars":"""<span class="star-wrap">
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</span>""","text":"Je détestais prospecter. Maintenant j'envoie 30 messages par semaine en 15 minutes. Mon pipeline est plein pour la première fois depuis que j'ai lancé mon activité.","result":"30 msg/semaine en 15min"},
    {"name":"Amina K.","role":"Directrice commerciale PME","initials":"AK","bg":"#d97706","photo":"https://i.pravatar.cc/80?img=9","stars":"""<span class="star-wrap">
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</span>""","text":"ROI en 4 jours. J'ai payé 29€ pour le plan Pro, et le premier client signé grâce à ClientBoost m'a rapporté 1 800€. Je ne reviendrai jamais en arrière.","result":"ROI 6 200% en 4 jours"},
    {"name":"Lucas F.","role":"E-commerçant","initials":"LF","bg":"#7c3aed","photo":"https://i.pravatar.cc/80?img=68","stars":"""<span class="star-wrap">
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  <svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
</span>""","text":"Mes newsletters avaient 8% d'ouverture. Après avoir utilisé ClientBoost pour reformuler mes objets et accroches, je suis à 34%. C'est bluffant.","result":"Taux ouverture x4"},
]

SAMPLE_MESSAGES = [
    {"problem":"⏳ Temps qui s'évapore","tone":"Percutant","preview":"Objet : Récupérez 10h par semaine\n\nBonjour [Prénom],\n\nUne question directe : combien d'heures avez-vous passé cette semaine à rédiger des messages au lieu de les envoyer ?\n\nPour la plupart des directeurs marketing, c'est entre 5 et 15h perdues. Chaque semaine.\n\nNos clients récupèrent en moyenne 8h par semaine dès le premier mois.\n\nJe vous montre comment en 20 minutes. Cette semaine ?\n\n[Votre nom]"},
    {"problem":"💸 Budget qui s'évapore","tone":"Storytelling","preview":"Objet : Il a réduit son coût d'acquisition de 60%\n\nBonjour [Prénom],\n\nMarc investissait 2 000€/mois en pub. Résultat : 3-4 clients. Rentabilité nulle.\n\nSon problème : ses campagnes ne convertissaient pas. Le message ne parlait pas à sa cible.\n\nAvec ClientBoost, même budget, messages restructurés avec PAS.\n\nRésultat en 30 jours : 9 clients. CAC divisé par 3.\n\nVous voulez que je vous montre exactement ce qu'on a changé ?\n\n[Votre nom]"},
    {"problem":"📈 Pipeline à sec","tone":"Percutant","preview":"Objet : Votre pipeline mérite mieux que le silence\n\nBonjour [Prénom],\n\nUn pipeline vide, c'est une entreprise en danger.\n\nAvec ClientBoost, générez 50 messages personnalisés dans le temps où vous en écriviez 1. Chaque message cible la douleur exacte de votre persona.\n\nVolume + personnalisation = pipeline qui explose.\n\n15 minutes pour voir comment ça marche ?\n\n[Votre nom]"},
    {"problem":"🔄 Clients qui disparaissent","tone":"Professionnel","preview":"Objet : Vos anciens clients sont votre meilleure source de revenus\n\nBonjour [Prénom],\n\nAcquérir un nouveau client coûte 5x plus cher que d'en garder un existant. Pourtant, beaucoup laissent leurs clients partir sans un mot.\n\nClientBoost génère des séquences de réengagement personnalisées : le bon message, au bon moment.\n\nC'est du chiffre d'affaires déjà payé qui vous attend.\n\nOn en parle ?\n\n[Votre nom]"},
]

# ─────────────────────────────────────────────
# EMAILS AUTOMATIQUES
# ─────────────────────────────────────────────
EMAIL_WELCOME = {
    "subject": "🎉 Bienvenue dans ClientBoost AI — Votre premier message vous attend",
    "body": """Bonjour {name},

Bienvenue dans la famille ClientBoost AI ! 🚀

Vous venez de rejoindre plus de 12 000 entrepreneurs, freelances et agences qui ont transformé leur prospection.

Ce que vous pouvez faire dès maintenant :

✅ Générer votre premier message de vente (ça prend 60 secondes)
✅ Choisir parmi 7 problèmes clients — chacun avec son propre framework
✅ Tester les 3 styles : Percutant, Professionnel, Storytelling

💡 Notre conseil pour commencer :
Allez dans le Générateur → sélectionnez le problème le plus urgent de vos prospects → remplissez les 3 champs → admirez le résultat.

Votre premier rendez-vous qualifié est peut-être à 60 secondes.

À votre succès,
L'équipe ClientBoost AI

---
ClientBoost AI | support@clientboost.ai
Vous recevez cet email car vous venez de créer un compte."""
}

EMAIL_RENEWAL = {
    "subject": "⚡ Votre abonnement ClientBoost AI se renouvelle dans 3 jours",
    "body": """Bonjour {name},

Votre abonnement {plan} se renouvelle le {renewal_date}.

📊 Votre activité ce mois-ci :
• {msg_count} messages générés
• {problems_used} problèmes clients explorés
• Niveau atteint : {level}

Vous continuez à progresser — félicitations !

Votre abonnement sera automatiquement renouvelé le {renewal_date} pour {price}.

Si vous souhaitez modifier ou annuler votre abonnement, rendez-vous dans Paramètres → Abonnement avant cette date.

💎 Envie de passer au niveau supérieur ?
Le plan {next_plan} vous donnerait accès à {next_feature}. Découvrir →

À très bientôt,
L'équipe ClientBoost AI

---
ClientBoost AI | support@clientboost.ai"""
}

# ─────────────────────────────────────────────
# PLANS TARIFAIRES
# ─────────────────────────────────────────────
PLANS = [
    {
        "name": "Standard", "icon": "🥉", "price": "9€", "period": "/ mois",
        "color": "#64748b", "popular": False,
        "features": ["✔ 50 générations / mois", "✔ 7 frameworks inclus", "✔ 3 langues", "✔ Historique 30 jours", "✔ Dashboard basique", "✖ Support prioritaire", "✖ Générations illimitées"],
        "cta": "Commencer avec Standard"
    },
    {
        "name": "Pro", "icon": "🥈", "price": "29€", "period": "/ mois",
        "color": "#6366f1", "popular": True,
        "features": ["✔ Générations illimitées", "✔ 7 frameworks inclus", "✔ 6 langues", "✔ Historique 1 an", "✔ Dashboard complet + badges", "✔ Support prioritaire", "✔ Emails automatiques"],
        "cta": "⚡ Passer au Pro — le plus populaire"
    },
    {
        "name": "Agence", "icon": "🥇", "price": "79€", "period": "/ mois",
        "color": "#f59e0b", "popular": False,
        "features": ["✔ Générations illimitées", "✔ 7 frameworks inclus", "✔ 6 langues", "✔ Historique illimité", "✔ Dashboard complet + badges", "✔ Support dédié + API", "✔ Multi-utilisateurs (5 sièges)"],
        "cta": "Choisir Agence"
    },
]

# ─────────────────────────────────────────────
# GÉNÉRATEUR DE MESSAGES
# ─────────────────────────────────────────────
def generate_message(prob_id, secteur, persona, context, tone):
    templates = {
        "time": {
            "Percutant": f"Objet : Récupérez 10h par semaine — sans embaucher\n\nBonjour [Prénom],\n\nUne question directe : combien d'heures avez-vous passé cette semaine à rédiger des messages au lieu de les envoyer ?\n\nPour la plupart des {persona}, c'est entre 5 et 15h perdues. Chaque semaine.\n\nAvec {secteur}, vous générez des messages complets en 10 secondes. Ce que {context} vous prenait en heures ne prend plus qu'un clic.\n\nNos clients récupèrent en moyenne 8h par semaine dès le premier mois.\n\nJe vous montre comment en 20 minutes. Cette semaine ?\n\n[Votre nom]",
            "Professionnel": f"Objet : Optimisation du temps consacré à la prospection\n\nBonjour [Prénom],\n\nEn travaillant avec des {persona}, j'ai identifié un pattern récurrent : {context} monopolise un temps précieux qui devrait être alloué à la conversion.\n\n{secteur} permet de réduire ce temps de 80%, tout en améliorant la qualité et la personnalisation des messages.\n\nSeriez-vous disponible pour un échange de 20 minutes cette semaine ?\n\nCordialement,\n[Votre nom]",
            "Storytelling": f"Objet : \"Je passais 3h par jour à rédiger des emails...\"\n\nBonjour [Prénom],\n\nC'est ce que m'a dit Sarah, responsable commerciale, il y a 6 mois.\n\nElle gérait des {persona} qui noyaient dans {context}. Pipeline vide, moral en berne.\n\nAujourd'hui avec {secteur}, son équipe génère 3x plus de messages en 1/5 du temps.\n\nVotre situation ressemble à celle de Sarah ?\n\nUn appel de 15 minutes pour voir si on peut faire pareil pour vous ?\n\n[Votre nom]"
        },
        "money": {
            "Percutant": f"Objet : Votre budget a une fuite — voici où\n\nBonjour [Prénom],\n\nChaque mois, des {persona} me montrent leurs campagnes : budget investi, résultats décevants.\n\nLe diagnostic est presque toujours le même : {context}. Le problème n'est pas le produit — c'est le message.\n\n{secteur} applique les frameworks PAS et AIDA pour que chaque euro génère un retour mesurable. +40% de conversion dans les 30 premiers jours en moyenne.\n\nVous continuez à perdre ou on en parle cette semaine ?\n\n[Votre nom]",
            "Professionnel": f"Objet : Amélioration du ROI de vos campagnes\n\nBonjour [Prénom],\n\nL'analyse de campagnes similaires à celles des {persona} révèle systématiquement le même frein : {context}.\n\n{secteur} résout ce problème en appliquant des frameworks éprouvés (PAS, AIDA, FAB) à chaque message, réduisant le coût d'acquisition et augmentant le taux de conversion.\n\nJe serais ravi de vous présenter des cas concrets lors d'un échange de 20 minutes.\n\nCordialement,\n[Votre nom]",
            "Storytelling": f"Objet : Il a réduit son coût d'acquisition de 60% — sans augmenter son budget\n\nBonjour [Prénom],\n\nMarc, consultant pour {persona}, investissait 2 000€/mois. Résultat : 3-4 clients. Rentabilité nulle.\n\nSon problème : {context}. Le message ne convertissait pas.\n\nAvec {secteur}, même budget, messages restructurés avec PAS.\n\nRésultat en 30 jours : 9 clients. CAC divisé par 3.\n\nVous voulez que je vous montre exactement ce qu'on a changé ?\n\n[Votre nom]"
        },
        "skill": {
            "Percutant": f"Objet : Vous n'avez pas besoin d'apprendre le copywriting\n\nBonjour [Prénom],\n\nLe copywriting est un métier. Vous en avez déjà un.\n\nPourtant, des {persona} passent des heures à lutter avec {context} — alors qu'il existe des frameworks précis pour ça.\n\n{secteur} intègre AIDA, PAS, FAB et le storytelling directement dans chaque message. Renseignez votre contexte. Obtenez un message structuré pour convaincre. En 10 secondes.\n\nEnvie d'un test en direct ?\n\n[Votre nom]",
            "Professionnel": f"Objet : La structure qui transforme vos messages en rendez-vous\n\nBonjour [Prénom],\n\nLa majorité des {persona} partagent le même défi : {context}. Non par manque d'expertise métier, mais faute d'une méthode de rédaction éprouvée.\n\n{secteur} pallie ce manque en intégrant automatiquement les frameworks les plus efficaces (AIDA, FAB, Storytelling) dans chaque message.\n\nUn échange de 20 minutes pour vous montrer le processus ?\n\nCordialement,\n[Votre nom]",
            "Storytelling": f"Objet : \"Je ne savais pas quoi écrire — maintenant mes messages convertissent à 30%\"\n\nBonjour [Prénom],\n\nJulie, {persona[:-1] if persona.endswith('s') else persona} indépendante, passait 2h par message. {context} la paralysait.\n\nElle a essayé {secteur}. Premier message généré : un rendez-vous pris dans les 24h.\n\nLe secret ? Le framework FAB appliqué automatiquement : Feature, Advantage, Benefit.\n\nVous voulez le même résultat dès demain ?\n\n[Votre nom]"
        },
        "growth": {
            "Percutant": f"Objet : Votre pipeline mérite mieux que le silence\n\nBonjour [Prénom],\n\nUn pipeline vide, c'est une entreprise en danger. Pour des {persona}, {context} est souvent ce qui bloque la croissance.\n\nAvec {secteur}, générez 50 messages personnalisés dans le temps où vous en écriviez 1. Chaque message cible la douleur exacte de votre persona.\n\nVolume + personnalisation = pipeline qui explose.\n\n15 minutes pour voir comment ça marche ?\n\n[Votre nom]",
            "Professionnel": f"Objet : Stratégie de génération de leads pour {persona}\n\nBonjour [Prénom],\n\nLa croissance d'un pipeline qualifié repose sur deux piliers : volume et qualité des messages. Pour les {persona}, {context} limite souvent les deux.\n\n{secteur} permet de multiplier le volume de prospection par 10 tout en maintenant un haut niveau de personnalisation.\n\nJe vous propose un échange de 20 minutes pour analyser votre situation.\n\nCordialement,\n[Votre nom]",
            "Storytelling": f"Objet : De 3 leads/mois à 47 en 60 jours — voici comment\n\nBonjour [Prénom],\n\nThomas gère une équipe de {persona}. Il y a 3 mois, {context} limitait leur prospection à 3-4 leads qualifiés par mois.\n\nAvec {secteur}, son équipe a commencé à générer des messages ciblés en masse — sans sacrifier la personnalisation.\n\n60 jours plus tard : 47 leads qualifiés. Pipeline rempli.\n\nVous voulez qu'on reproduise ça pour vous ?\n\n[Votre nom]"
        },
        "frustration": {
            "Percutant": f"Objet : Arrêtez d'envoyer des messages que vous détestez écrire\n\nBonjour [Prénom],\n\nLa prospection à froid, pour des {persona}, c'est souvent la tâche la plus redoutée de la semaine. {context}. Et quand les réponses ne viennent pas, la frustration monte.\n\n{secteur} génère des messages qui parlent à vos prospects — pas à leur filtre anti-spam. Empathiques. Directs. Humains.\n\nRésultat : des réponses. Et une prospection dont vous serez fier.\n\n[Votre nom]",
            "Professionnel": f"Objet : Augmentez votre taux de réponse sans paraître intrusif\n\nBonjour [Prénom],\n\nLes {persona} partagent souvent la même réticence : {context}. Cette hésitation impacte directement leur activité commerciale.\n\n{secteur} aborde la prospection par l'empathie : chaque message est construit autour de la situation réelle du prospect, pas autour de votre offre.\n\nJe vous propose de vous montrer la différence en 20 minutes.\n\nCordialement,\n[Votre nom]",
            "Storytelling": f"Objet : \"J'avais honte d'envoyer mes messages\" — jusqu'à ce qu'il change d'approche\n\nBonjour [Prénom],\n\nPierre, {persona[:-1] if persona.endswith('s') else persona}, évitait la prospection depuis 6 mois. {context}. Il se sentait comme un spammeur.\n\nEn changeant son approche avec {secteur}, ses prospects lui répondaient pour le remercier de l'\"approche différente\".\n\nSon taux de réponse : de 2% à 18%.\n\nVous voulez ressentir la même chose ?\n\n[Votre nom]"
        },
        "risk": {
            "Percutant": f"Objet : Prospectez à grande échelle sans mettre votre réputation en jeu\n\nBonjour [Prénom],\n\nPour des {persona}, un mauvais message peut griller une relation ou une réputation construite en années. {context} — cette peur est légitime.\n\n{secteur} intègre des contrôles de qualité automatiques : bon ton, bonne structure, niveau de professionnalisme calibré.\n\nVous prospectez avec confiance. Votre image reste intacte.\n\n[Votre nom]",
            "Professionnel": f"Objet : Prospection à grande échelle sans compromis sur la qualité\n\nBonjour [Prénom],\n\nComment maintenir un niveau de qualité irréprochable quand le volume augmente ? Pour des {persona}, {context} freine beaucoup d'initiatives.\n\n{secteur} standardise la qualité tout en maintenant la personnalisation. Chaque message respecte votre positionnement et vos standards professionnels.\n\nUn échange de 20 minutes ?\n\nCordialement,\n[Votre nom]",
            "Storytelling": f"Objet : Il a envoyé 500 messages — zéro plainte, 43 rendez-vous\n\nBonjour [Prénom],\n\nKarim, consultant pour {persona}, avait une base de 500 contacts qu'il n'osait pas contacter. {context} — il craignait de tout brûler.\n\nAvec {secteur}, séquence calibrée : ton juste, personnalisation réelle, qualité constante.\n\nRésultat : zéro désabonnement, zéro plainte, 43 rendez-vous qualifiés.\n\nVous voulez la même assurance ?\n\n[Votre nom]"
        },
        "retention": {
            "Percutant": f"Objet : Vos anciens clients sont votre meilleure source de revenus — et vous les ignorez\n\nBonjour [Prénom],\n\nAcquérir un nouveau client coûte 5x plus cher que d'en garder un existant. Pourtant, des {persona} laissent leurs clients partir sans un mot. {context}.\n\n{secteur} génère des séquences de réengagement personnalisées : le bon message, au bon moment.\n\nC'est du chiffre d'affaires déjà payé qui vous attend.\n\n[Votre nom]",
            "Professionnel": f"Objet : Stratégie de réengagement pour maximiser la valeur client\n\nBonjour [Prénom],\n\nL'analyse du comportement des {persona} révèle un levier sous-exploité : la réactivation des clients existants. {context} est souvent la cause d'un taux de rétention insuffisant.\n\n{secteur} permet de créer des séquences de suivi personnalisées — newsletters, offres de renouvellement, messages de réengagement.\n\nImpact moyen constaté : +35% de taux de rétention dans les 90 premiers jours.\n\nCordialement,\n[Votre nom]",
            "Storytelling": f"Objet : Elle a réactivé 60 clients dormants en 2 semaines\n\nBonjour [Prénom],\n\nAmina gère une activité de consulting pour {persona}. Ses clients achetaient une fois, puis disparaissaient. {context}. Aucun système de suivi.\n\nElle a utilisé {secteur} pour créer une séquence de 3 emails de réengagement personnalisés.\n\nEn 2 semaines : 60 clients réactivés, 23 nouveaux achats. Sans prospecter un seul nouveau contact.\n\n[Votre nom]"
        }
    }
    pt = templates.get(prob_id, templates["time"])
    return pt.get(tone, list(pt.values())[0])

# ─────────────────────────────────────────────
# NIVEAUX
# ─────────────────────────────────────────────
LEVELS = [
    {"name":"Débutant","icon":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2"><path d="M2 22c0 0 8-4 8-10V2s-8 4-8 10v10zM22 22c0 0-8-4-8-10V2s8 4 8 10v10z"/><line x1="12" y1="22" x2="12" y2="12"/></svg>',"min":0,"max":5,"color":"#64748b"},
    {"name":"Prospecteur","icon":'<svg width="20" height="20" viewBox="0 0 24 24" fill="#FED7AA" stroke="#f97316" stroke-width="1.5"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>',"min":6,"max":15,"color":"#f59e0b"},
    {"name":"Closer","icon":'<svg width="20" height="20" viewBox="0 0 24 24" fill="#FBBF24" stroke="#F59E0B" stroke-width="1"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',"min":16,"max":30,"color":"#3b82f6"},
    {"name":"Expert","icon":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="1.5"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/></svg>',"min":31,"max":60,"color":"#8b5cf6"},
    {"name":"Maître","icon":'<svg width="20" height="20" viewBox="0 0 24 24" fill="#FBBF24" stroke="#F59E0B" stroke-width="1"><path d="M2 20h20M5 20L2 8l5 4 5-7 5 7 5-4-3 12"/></svg>',"min":61,"max":999,"color":"#f43f5e"},
]
def get_level(c):
    for l in LEVELS:
        if l["min"] <= c <= l["max"]: return l
    return LEVELS[-1]
def get_next_level(c):
    for i,l in enumerate(LEVELS):
        if l["min"] <= c <= l["max"]: return LEVELS[i+1] if i+1 < len(LEVELS) else None
    return None

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
for k,v in {"page":"landing","authenticated":False,"user_name":"","user_email":"","history":[],"last_generated":"","gen_count":0,"selected_problem_id":None,"show_register":False,"daily_counts":{},"problems_used":{},"join_date":datetime.now().strftime("%d/%m/%Y"),"selected_plan":None,"show_payment":False,"current_plan":"Pro","plan_price":"29€"}.items():
    if k not in st.session_state: st.session_state[k] = v

# ─────────────────────────────────────────────
# PAGE LANDING PUBLIQUE
# ─────────────────────────────────────────────
if st.session_state.page == "landing":
    # NAV
    st.markdown("""
    <div style="background:rgba(10,15,30,0.95); backdrop-filter:blur(10px); padding:16px 40px; display:flex; justify-content:space-between; align-items:center; position:sticky; top:0; z-index:100; margin:-16px -16px 0; border-bottom:1px solid rgba(255,255,255,0.08);">
        <div style="font-size:22px; font-weight:900; background:linear-gradient(135deg,#6366f1,#8b5cf6); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">🚀 ClientBoost AI</div>
        <div style="display:flex; gap:12px; align-items:center;">
            <span style="color:#94a3b8; font-size:14px;">Déjà + de 12 000 utilisateurs</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # HERO
    st.markdown("""
    <div class="landing-hero">
        <div style="display:inline-block; background:rgba(99,102,241,0.15); border:1px solid rgba(99,102,241,0.3); border-radius:999px; padding:6px 18px; font-size:13px; color:#a5b4fc; font-weight:600; margin-bottom:24px;">
            ✨ Nouveau — 7 frameworks de vente intégrés
        </div>
        <h1 style="font-size:62px; font-weight:900; color:white; line-height:1.1; margin:0 0 24px;">
            Multipliez vos revenus<br>
            <span style="background:linear-gradient(135deg,#6366f1,#a78bfa,#ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">avec les bons mots.</span>
        </h1>
        <p style="font-size:20px; color:#94a3b8; max-width:620px; margin:0 auto 40px; line-height:1.6;">
            ClientBoost AI génère des messages de vente percutants en 10 secondes. 
            Conçu pour résoudre les 7 problèmes qui bloquent votre croissance.
        </p>
        <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
            <div style="background:rgba(255,255,255,0.08); border-radius:12px; padding:12px 20px; color:white; font-size:14px;">⚡ Génération en 10 secondes</div>
            <div style="background:rgba(255,255,255,0.08); border-radius:12px; padding:12px 20px; color:white; font-size:14px;">🎯 7 frameworks de vente</div>
            <div style="background:rgba(255,255,255,0.08); border-radius:12px; padding:12px 20px; color:white; font-size:14px;">🌍 6 langues disponibles</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # SECTION 7 PROBLÈMES
    st.markdown("""
    <div style="text-align:center; margin-bottom:40px;">
        <span style="display:inline-block; background:#ede9fe; color:#6d28d9; border-radius:999px; padding:4px 16px; font-size:12px; font-weight:700; margin-bottom:12px;">LES 7 PROBLÈMES QUE VOUS RECONNAISSEZ</span>
        <h2 style="font-size:38px; font-weight:900; color:#0f172a; margin:0 0 12px;">Est-ce que l'une de ces situations vous parle ?</h2>
        <p style="color:#64748b; font-size:17px; max-width:580px; margin:0 auto;">ClientBoost AI a été conçu pour éliminer chacune d'elles — définitivement.</p>
    </div>
    """, unsafe_allow_html=True)

    for i, p in enumerate(PROBLEMS):
        col_text, col_solution = st.columns([1, 1])
        with col_text:
            st.markdown(f"""
            <div class="{p['color_class']}" style="padding:28px; border-radius:20px; min-height:180px;">
                <div style="font-size:36px; margin-bottom:12px;">{p['icon']}</div>
                <div style="font-size:11px; font-weight:700; opacity:0.7; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;">Problème {i+1} sur 7</div>
                <div style="font-size:22px; font-weight:800; margin-bottom:10px;">{p['title']}</div>
                <div style="font-size:16px; opacity:0.9; font-style:italic;">"{p['hook']}"</div>
                <div style="font-size:14px; opacity:0.8; margin-top:10px; line-height:1.5;">{p['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_solution:
            st.markdown(f"""
            <div style="background:white; border-radius:20px; padding:28px; border:2px solid {p['color']}20; height:100%; display:flex; flex-direction:column; justify-content:center;">
                <div style="font-size:11px; font-weight:700; color:{p['color']}; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px;">✅ LA SOLUTION CLIENTBOOST</div>
                <div style="font-size:16px; color:#0f172a; font-weight:600; line-height:1.6; margin-bottom:16px;">{p['solution']}</div>
                <div style="background:{p['color']}10; border-radius:10px; padding:12px;">
                    <div style="font-size:13px; color:{p['color']}; font-weight:600;">{p['tip']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.write("")

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # MESSAGES GÉNÉRÉS (exemples)
    st.markdown("""
    <div style="text-align:center; margin:60px 0 40px;">
        <span style="display:inline-block; background:#dcfce7; color:#15803d; border-radius:999px; padding:4px 16px; font-size:12px; font-weight:700; margin-bottom:12px;">EXEMPLES RÉELS</span>
        <h2 style="font-size:38px; font-weight:900; color:#0f172a; margin:0 0 12px;">Des messages que vous pouvez envoyer dès ce soir</h2>
        <p style="color:#64748b; font-size:17px; max-width:560px; margin:0 auto;">Générés par ClientBoost AI en moins de 10 secondes. Copiez, personnalisez, envoyez.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    for i, msg in enumerate(SAMPLE_MESSAGES):
        with (c1 if i % 2 == 0 else c2):
            st.markdown(f"""
            <div style="background:white; border-radius:16px; padding:24px; border:1px solid #e8ecf0; box-shadow:0 4px 16px rgba(0,0,0,0.06); margin-bottom:20px;">
                <div style="display:flex; gap:10px; margin-bottom:16px; flex-wrap:wrap;">
                    <span style="background:#ede9fe; color:#6d28d9; border-radius:999px; padding:3px 12px; font-size:12px; font-weight:700;">{msg['problem']}</span>
                    <span style="background:#dbeafe; color:#1d4ed8; border-radius:999px; padding:3px 12px; font-size:12px; font-weight:700;">Style : {msg['tone']}</span>
                </div>
                <div class="msg-preview">{msg['preview'][:280]}...</div>
                <div style="text-align:right; margin-top:12px;">
                    <span style="font-size:12px; color:#10b981; font-weight:600;">✅ Généré en 8 secondes</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # TÉMOIGNAGES
    st.markdown("""
    <div style="text-align:center; margin:60px 0 40px;">
        <span style="display:inline-block; background:#ffedd5; color:#c2410c; border-radius:999px; padding:4px 16px; font-size:12px; font-weight:700; margin-bottom:12px;">PREUVES SOCIALES</span>
        <h2 style="font-size:38px; font-weight:900; color:#0f172a; margin:0 0 12px;">Ils ont transformé leur prospection</h2>
        <p style="color:#64748b; font-size:17px; max-width:560px; margin:0 auto;">12 000+ utilisateurs. Des résultats réels. Des témoignages qui parlent d'eux-mêmes.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    for i, (col, t) in enumerate(zip([col1, col2, col3, col1, col2, col3], TESTIMONIALS)):
        with col:
            st.markdown(f"""
            <div class="testimonial-card" style="margin-bottom:20px;">
                <div style="margin-bottom:12px;">{t['stars']}</div>
                <div style="font-size:14px; color:#374151; line-height:1.6; margin-bottom:16px; font-style:italic;">"{t['text']}"</div>
                <div style="background:#f0fdf4; border-radius:10px; padding:8px 12px; margin-bottom:16px;">
                    <span style="font-size:13px; font-weight:700; color:#15803d;">📈 {t['result']}</span>
                </div>
                <div style="display:flex; align-items:center; gap:12px;">
                    <img src="{t['photo']}" alt="{t['name']}" style="width:48px; height:48px; border-radius:50%; object-fit:cover; border:2px solid #e8ecf0; flex-shrink:0;" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                    <div style="display:none; width:48px; height:48px; border-radius:50%; background:{t['bg']}; color:white; font-size:15px; font-weight:800; align-items:center; justify-content:center; flex-shrink:0;">{t['initials']}</div>
                    <div>
                        <div style="font-size:14px; font-weight:700; color:#0f172a;">{t['name']}</div>
                        <div style="font-size:12px; color:#64748b;">{t['role']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # CTA FINAL
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0f172a,#1e1b4b,#0f172a); border-radius:32px; padding:72px 40px; text-align:center; margin:60px 0;">
        <div style="font-size:14px; font-weight:700; color:#a5b4fc; text-transform:uppercase; letter-spacing:2px; margin-bottom:20px;">PRÊT À PASSER À L'ACTION ?</div>
        <h2 style="font-size:48px; font-weight:900; color:white; margin:0 0 20px; line-height:1.1;">
            Commence à multiplier<br>
            <span style="background:linear-gradient(135deg,#6366f1,#a78bfa,#ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">tes revenus maintenant.</span>
        </h2>
        <p style="color:#94a3b8; font-size:18px; max-width:540px; margin:0 auto 40px; line-height:1.6;">
            Rejoins 12 000+ entrepreneurs qui ont arrêté de prospecter à l'aveugle. Ton premier message en 60 secondes.
        </p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap; margin-bottom:20px;">
            <div style="color:#94a3b8; font-size:14px;">✅ Sans carte bancaire pour commencer</div>
            <div style="color:#94a3b8; font-size:14px;">✅ Résultats dès le premier message</div>
            <div style="color:#94a3b8; font-size:14px;">✅ Annulable à tout moment</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, cta_col, _ = st.columns([1,2,1])
    with cta_col:
        if st.button("🚀 Commence à multiplier tes revenus maintenant", type="primary", use_container_width=True):
            st.session_state.page = "auth"
            st.rerun()
    st.write("")
    _, lc, _ = st.columns([1,2,1])
    with lc:
        if st.button("Me connecter — J'ai déjà un compte", use_container_width=True):
            st.session_state.page = "auth"
            st.session_state.show_register = False
            st.rerun()
    st.stop()

# ─────────────────────────────────────────────
# PAGE AUTH
# ─────────────────────────────────────────────
if not st.session_state.authenticated:
    st.markdown("""
    <div style="text-align:center; padding:40px 0 20px;">
        <div style="font-size:48px; font-weight:900; background:linear-gradient(135deg,#6366f1,#8b5cf6,#ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">ClientBoost AI</div>
        <p style="color:#64748b; font-size:17px; margin-top:8px;">Le générateur de messages qui résout vos 7 problèmes.</p>
    </div>
    """, unsafe_allow_html=True)

    _, col_form, _ = st.columns([1,1.2,1])
    with col_form:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        if not st.session_state.show_register:
            st.markdown("<h3 style='color:#0f172a; margin-top:0; text-align:center;'>👋 Connexion</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#64748b; text-align:center; font-size:14px; margin-bottom:24px;'>Bon retour parmi nous !</p>", unsafe_allow_html=True)
            email = st.text_input("Email", placeholder="vous@exemple.com")
            password = st.text_input("Mot de passe", type="password", placeholder="••••••••")
            if st.button("🚀 Se connecter", type="primary", use_container_width=True):
                if email and password:
                    st.session_state.authenticated = True
                    st.session_state.user_name = email.split("@")[0].capitalize()
                    st.session_state.user_email = email
                    st.session_state.page = "dashboard"
                    st.rerun()
                else: st.error("Veuillez remplir tous les champs.")
            st.markdown("<hr style='margin:20px 0; border-color:#f1f5f9;'>", unsafe_allow_html=True)
            if st.button("Pas encore de compte ? S'inscrire →", use_container_width=True):
                st.session_state.show_register = True
                st.rerun()
            if st.button("← Retour à l'accueil", use_container_width=True):
                st.session_state.page = "landing"
                st.rerun()
        else:
            st.markdown("<h3 style='color:#0f172a; margin-top:0; text-align:center;'>✨ Créer un compte</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#64748b; text-align:center; font-size:14px; margin-bottom:24px;'>Gratuit. Sans carte bancaire.</p>", unsafe_allow_html=True)
            name = st.text_input("Prénom", placeholder="Votre prénom")
            email = st.text_input("Email", placeholder="vous@exemple.com")
            password = st.text_input("Mot de passe", type="password", placeholder="Minimum 8 caractères")

            if st.button("🎉 Créer mon compte", type="primary", use_container_width=True):
                if name and email and password:
                    # Afficher le paiement avant accès
                    st.session_state.selected_plan = None
                    st.session_state.pending_name = name
                    st.session_state.pending_email = email
                    st.session_state.show_payment = True
                    st.rerun()
                else: st.error("Veuillez remplir tous les champs.")
            st.markdown("<hr style='margin:20px 0; border-color:#f1f5f9;'>", unsafe_allow_html=True)
            if st.button("← Déjà un compte ? Se connecter", use_container_width=True):
                st.session_state.show_register = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # PAGE PAIEMENT (modale)
    if st.session_state.get("show_payment"):
        st.write("")
        st.markdown("""
        <div style="text-align:center; margin-bottom:32px;">
            <h2 style="font-size:32px; font-weight:900; color:#0f172a; margin:0 0 8px;">Choisissez votre plan</h2>
            <p style="color:#64748b; font-size:16px;">Accès immédiat dès votre choix. Annulable à tout moment.</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        for col, plan in zip([c1, c2, c3], PLANS):
            with col:
                pop_badge = '<span style="background:#6366f1;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;display:inline-block;margin-bottom:8px;">⭐ POPULAIRE</span>' if plan["popular"] else ""
                border = "border:2px solid #6366f1;" if plan["popular"] else "border:2px solid #e8ecf0;"
                st.markdown(f"""
                <div class="price-card {'popular' if plan['popular'] else ''}" style="{border}">
                    <div style="font-size:28px; margin-bottom:8px;">{plan['icon']}</div>
                    <div style="font-size:15px; font-weight:700; color:#64748b; margin-bottom:8px;">{plan['name']}</div>
                    {pop_badge}
                    <div class="price-amount" style="margin:12px 0 4px;">{plan['price']}</div>
                    <div style="font-size:14px; color:#64748b; margin-bottom:20px;">{plan['period']}</div>
                    <hr style="border-color:#f1f5f9; margin:16px 0;">
                    {''.join(f'<div class="feature-item">{f}</div>' for f in plan['features'])}
                </div>
                """, unsafe_allow_html=True)
                st.write("")
                if st.button(plan["cta"], key=f"pay_{plan['name']}", use_container_width=True, type="primary" if plan["popular"] else "secondary"):
                    st.session_state.selected_plan = plan["name"]
                    st.session_state.current_plan = plan["name"]
                    st.session_state.plan_price = plan["price"]

        if st.session_state.selected_plan:
            st.write("")
            st.markdown(f"""
            <div class="payment-modal">
                <h3 style="color:#0f172a; margin-top:0; text-align:center;">💳 Paiement — Plan {st.session_state.selected_plan}</h3>
                <p style="color:#64748b; text-align:center; margin-bottom:28px;">Simulation de paiement sécurisé</p>
            </div>
            """, unsafe_allow_html=True)
            col_pay1, col_pay2 = st.columns(2)
            with col_pay1:
                st.text_input("Nom sur la carte", placeholder="Jean Dupont")
                st.text_input("Numéro de carte", placeholder="4242 4242 4242 4242")
            with col_pay2:
                st.text_input("Date d'expiration", placeholder="MM/AA")
                st.text_input("CVV", placeholder="123", type="password")

            plan_obj = next((p for p in PLANS if p["name"] == st.session_state.selected_plan), PLANS[1])
            _, pay_btn, _ = st.columns([1,2,1])
            with pay_btn:
                if st.button(f"✅ Confirmer et accéder — {plan_obj['price']}/mois", type="primary", use_container_width=True):
                    with st.spinner("Traitement du paiement..."):
                        time.sleep(1.5)
                    st.session_state.authenticated = True
                    st.session_state.user_name = st.session_state.get("pending_name", "Utilisateur").capitalize()
                    st.session_state.user_email = st.session_state.get("pending_email", "")
                    st.session_state.join_date = datetime.now().strftime("%d/%m/%Y")
                    st.session_state.show_payment = False
                    st.session_state.page = "welcome"
                    st.rerun()
    st.stop()

# ─────────────────────────────────────────────
# PAGE BIENVENUE
# ─────────────────────────────────────────────
if st.session_state.page == "welcome":
    renewal = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y")
    plan_obj = next((p for p in PLANS if p["name"] == st.session_state.current_plan), PLANS[1])
    st.markdown(f"""
    <div style="max-width:680px; margin:40px auto;">
        <div style="background:linear-gradient(135deg,#0f172a,#1e1b4b); border-radius:24px; overflow:hidden; box-shadow:0 20px 60px rgba(0,0,0,0.2);">
            <div style="background:linear-gradient(135deg,#6366f1,#8b5cf6); padding:32px; text-align:center;">
                <div style="font-size:48px; margin-bottom:12px;">🎉</div>
                <h2 style="color:white; font-size:26px; font-weight:800; margin:0;">Bienvenue, {st.session_state.user_name} !</h2>
                <p style="color:rgba(255,255,255,0.8); font-size:15px; margin-top:8px;">Votre compte ClientBoost AI est actif — Plan {st.session_state.current_plan}</p>
            </div>
            <div style="padding:32px; color:#e2e8f0;">
                <div style="background:rgba(255,255,255,0.06); border-radius:12px; padding:20px; margin-bottom:20px;">
                    <div style="font-size:13px; color:#94a3b8; font-weight:600; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px;">📧 Email de bienvenue envoyé à {st.session_state.user_email}</div>
                    <div style="font-size:15px; font-weight:700; color:white; margin-bottom:8px;">Objet : {EMAIL_WELCOME['subject']}</div>
                    <div style="font-size:13px; color:#94a3b8; line-height:1.7; white-space:pre-line;">{EMAIL_WELCOME['body'].format(name=st.session_state.user_name)[:400]}...</div>
                </div>
                <div style="background:rgba(99,102,241,0.15); border-radius:12px; padding:16px; margin-bottom:20px; border:1px solid rgba(99,102,241,0.3);">
                    <div style="font-size:13px; color:#a5b4fc; font-weight:700; margin-bottom:6px;">⚡ Votre abonnement</div>
                    <div style="color:white; font-size:14px;">Plan <strong>{st.session_state.current_plan}</strong> — {plan_obj['price']}/mois</div>
                    <div style="color:#94a3b8; font-size:13px; margin-top:4px;">Prochain renouvellement : <strong style="color:white;">{renewal}</strong></div>
                    <div style="color:#94a3b8; font-size:12px; margin-top:8px;">📅 Un email de rappel sera automatiquement envoyé le 28 de chaque mois.</div>
                </div>
                <div style="font-size:15px; color:#e2e8f0; font-weight:600; margin-bottom:12px;">🎯 Par où commencer ?</div>
                <div style="display:flex; flex-direction:column; gap:8px;">
                    <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:12px 16px; font-size:14px; color:#e2e8f0;">1️⃣ Allez dans le <strong>Générateur</strong></div>
                    <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:12px 16px; font-size:14px; color:#e2e8f0;">2️⃣ Sélectionnez <strong>le problème de votre client</strong></div>
                    <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:12px 16px; font-size:14px; color:#e2e8f0;">3️⃣ Générez votre <strong>premier message en 60 secondes</strong></div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1,2,1])
    with btn_col:
        if st.button("🚀 Accéder au Dashboard", type="primary", use_container_width=True):
            st.session_state.page = "dashboard"
            st.rerun()
    st.stop()

# ─────────────────────────────────────────────
# SIDEBAR (connecté)
# ─────────────────────────────────────────────
with st.sidebar:
    level = get_level(st.session_state.gen_count)
    st.markdown(f"""
    <div style="padding:20px 0 10px;">
        <div style="font-size:22px; font-weight:900; color:white; margin-bottom:4px;">🚀 ClientBoost AI</div>
        <div style="background:rgba(255,255,255,0.08); border-radius:10px; padding:12px; margin-top:12px;">
            <div style="font-size:11px; color:#94a3b8; margin-bottom:4px; text-transform:uppercase; letter-spacing:1px;">Connecté</div>
            <div style="font-size:15px; font-weight:700; color:white;">{st.session_state.user_name}</div>
            <div style="font-size:12px; color:#64748b;">{st.session_state.user_email}</div>
        </div>
        <div style="background:rgba(99,102,241,0.15); border-radius:10px; padding:12px; margin-top:10px; text-align:center;">
            <div style="font-size:20px;">{level['icon']}</div>
            <div style="font-size:14px; font-weight:800; color:{level['color']};">{level['name']}</div>
            <div style="font-size:24px; font-weight:900; color:white; margin:4px 0;">{st.session_state.gen_count}</div>
            <div style="font-size:11px; color:#64748b;">messages générés</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    for pid, label in [("dashboard","Dashboard"),("generator","Générateur"),("history","Historique"),("emails","Emails Auto"),("subscription","Abonnement"),("settings","Paramètres")]:
        if st.button(label, key=f"nav_{pid}", use_container_width=True, type="primary" if st.session_state.page==pid else "secondary"):
            st.session_state.page = pid
            st.rerun()
    st.divider()
    if st.button("← Déconnexion", use_container_width=True):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()

# ─────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────
if st.session_state.page == "dashboard":
    import plotly.graph_objects as go
    import plotly.express as px

    level = get_level(st.session_state.gen_count)
    next_level = get_next_level(st.session_state.gen_count)
    progress = 0
    if next_level:
        total = next_level["min"] - level["min"]
        done = st.session_state.gen_count - level["min"]
        progress = int((done/total)*100) if total > 0 else 100
    else:
        progress = 100

    today = datetime.now().strftime("%Y-%m-%d")
    today_count = st.session_state.daily_counts.get(today, 0)
    problems_solved = len(st.session_state.problems_used)
    saved_count = len(st.session_state.history)

    # ── HEADER ──
    st.markdown(f"<h2 style='color:#0f172a; margin-bottom:2px;'>Bonjour, {st.session_state.user_name} 👋</h2>", unsafe_allow_html=True)
    lvl_color = level["color"]
    lvl_name = level["name"]
    st.markdown(f"<p style='color:#64748b; margin-bottom:20px; font-size:15px;'>Membre depuis le {st.session_state.join_date} &nbsp;•&nbsp; Plan <strong>{st.session_state.current_plan}</strong> &nbsp;•&nbsp; Niveau <strong style='color:{lvl_color};'>{lvl_name}</strong></p>", unsafe_allow_html=True)

    # ── MÉTRIQUES ──
    c1,c2,c3,c4 = st.columns(4)
    for col, num, label, color, delta in zip(
        [c1,c2,c3,c4],
        [st.session_state.gen_count, today_count, problems_solved, saved_count],
        ["Messages générés","Aujourd'hui","Problèmes explorés","Sauvegardés"],
        ["#6366f1","#f59e0b","#10b981","#ec4899"],
        [None, None, f"sur 7", None]
    ):
        with col:
            st.metric(label=label, value=num, delta=delta)

    st.write("")

    # ── LIGNE 1 : Gauge niveau + Graphique linéaire activité ──
    col_gauge, col_line = st.columns([1, 2])

    with col_gauge:
        st.markdown("<h4 style='color:#0f172a; margin-bottom:8px;'>Niveau de croissance</h4>", unsafe_allow_html=True)
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=st.session_state.gen_count,
            delta={"reference": max(0, st.session_state.gen_count - today_count), "increasing": {"color": "#10b981"}},
            title={"text": f"<b>{level['name']}</b><br><span style='font-size:13px;color:#64748b;'>Messages générés</span>", "font": {"size": 16}},
            number={"font": {"size": 40, "color": level["color"]}, "suffix": " msg"},
            gauge={
                "axis": {"range": [0, max(61, st.session_state.gen_count + 10)], "tickwidth": 1, "tickcolor": "#e2e8f0"},
                "bar": {"color": level["color"], "thickness": 0.3},
                "bgcolor": "white",
                "borderwidth": 0,
                "steps": [
                    {"range": [0, 5],  "color": "#f1f5f9"},
                    {"range": [5, 15], "color": "#e0f2fe"},
                    {"range": [15, 30],"color": "#ede9fe"},
                    {"range": [30, 61],"color": "#fef9c3"},
                ],
                "threshold": {
                    "line": {"color": "#6366f1", "width": 3},
                    "thickness": 0.8,
                    "value": next_level["min"] if next_level else st.session_state.gen_count
                }
            }
        ))
        fig_gauge.update_layout(
            height=280, margin=dict(l=20, r=20, t=60, b=20),
            paper_bgcolor="white", font={"family": "Inter"},
            plot_bgcolor="white"
        )
        st.plotly_chart(fig_gauge, use_container_width=True, config={"displayModeBar": False})

        # Barre de progression vers prochain niveau
        if next_level:
            remaining = next_level["min"] - st.session_state.gen_count
            st.markdown(f"""
            <div style="background:#f5f3ff; border-radius:12px; padding:14px; text-align:center; border:1px solid #ede9fe;">
                <div style="font-size:11px; color:#6d28d9; font-weight:700; text-transform:uppercase; letter-spacing:0.5px;">Prochain niveau</div>
                <div style="font-size:15px; font-weight:800; color:#4c1d95; margin:4px 0;">{next_level['name']}</div>
                <div style="background:#ddd6fe; border-radius:999px; height:8px; margin:8px 0; overflow:hidden;">
                    <div style="width:{progress}%; height:8px; background:linear-gradient(135deg,#6366f1,#8b5cf6); border-radius:999px;"></div>
                </div>
                <div style="font-size:12px; color:#7c3aed;">Plus que <strong>{remaining}</strong> message(s) — {progress}%</div>
            </div>""", unsafe_allow_html=True)

    with col_line:
        st.markdown("<h4 style='color:#0f172a; margin-bottom:8px;'>Activité sur 7 jours</h4>", unsafe_allow_html=True)

        # Générer données des 7 derniers jours
        days_labels, days_counts, days_saved = [], [], []
        for i in range(6, -1, -1):
            d = (datetime.now() - timedelta(days=i))
            key = d.strftime("%Y-%m-%d")
            label = d.strftime("%a %d")
            days_labels.append(label)
            count = st.session_state.daily_counts.get(key, 0)
            # Simulate some activity for demo if no real data
            if st.session_state.gen_count > 0 and count == 0 and i > 0:
                count = random.randint(0, max(1, st.session_state.gen_count // 5))
            days_counts.append(count)
            days_saved.append(min(count, random.randint(0, max(1, count))))

        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=days_labels, y=days_counts,
            mode="lines+markers",
            name="Messages générés",
            line=dict(color="#6366f1", width=3, shape="spline"),
            marker=dict(size=8, color="#6366f1", line=dict(color="white", width=2)),
            fill="tozeroy",
            fillcolor="rgba(99,102,241,0.08)"
        ))
        fig_line.add_trace(go.Scatter(
            x=days_labels, y=days_saved,
            mode="lines+markers",
            name="Sauvegardés",
            line=dict(color="#10b981", width=2, dash="dot", shape="spline"),
            marker=dict(size=6, color="#10b981")
        ))
        fig_line.update_layout(
            height=280,
            margin=dict(l=10, r=10, t=20, b=20),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(family="Inter", size=12),
            legend=dict(orientation="h", y=1.1, x=0, font=dict(size=11)),
            xaxis=dict(showgrid=False, tickfont=dict(size=11, color="#64748b")),
            yaxis=dict(showgrid=True, gridcolor="#f1f5f9", tickfont=dict(size=11, color="#64748b"), title=""),
            hovermode="x unified"
        )
        st.plotly_chart(fig_line, use_container_width=True, config={"displayModeBar": False})

    st.write("")

    # ── LIGNE 2 : Radar problèmes + Donut répartition + Badges ──
    col_radar, col_donut, col_badges = st.columns([2, 1.5, 1.5])

    with col_radar:
        st.markdown("<h4 style='color:#0f172a; margin-bottom:8px;'>Couverture des 7 problèmes</h4>", unsafe_allow_html=True)
        prob_names = [p["title"] for p in PROBLEMS]
        prob_values = [st.session_state.problems_used.get(p["id"], 0) for p in PROBLEMS]
        max_val = max(max(prob_values), 1)

        fig_radar = go.Figure(go.Scatterpolar(
            r=prob_values + [prob_values[0]],
            theta=prob_names + [prob_names[0]],
            fill="toself",
            fillcolor="rgba(99,102,241,0.15)",
            line=dict(color="#6366f1", width=2),
            marker=dict(size=6, color="#6366f1"),
            name="Messages"
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, max_val + 1], tickfont=dict(size=9, color="#94a3b8"), gridcolor="#e2e8f0"),
                angularaxis=dict(tickfont=dict(size=10, color="#374151"), gridcolor="#e8ecf0"),
                bgcolor="white"
            ),
            height=300,
            margin=dict(l=30, r=30, t=20, b=20),
            paper_bgcolor="white",
            showlegend=False,
            font=dict(family="Inter")
        )
        st.plotly_chart(fig_radar, use_container_width=True, config={"displayModeBar": False})

    with col_donut:
        st.markdown("<h4 style='color:#0f172a; margin-bottom:8px;'>Répartition par problème</h4>", unsafe_allow_html=True)
        donut_labels = [p["title"] for p in PROBLEMS]
        donut_values = [max(st.session_state.problems_used.get(p["id"], 0), 0) for p in PROBLEMS]
        donut_colors = [p["color"] for p in PROBLEMS]

        if sum(donut_values) == 0:
            donut_values = [1] * 7
            donut_colors_use = ["#e2e8f0"] * 7
        else:
            donut_colors_use = donut_colors

        fig_donut = go.Figure(go.Pie(
            labels=donut_labels,
            values=donut_values,
            hole=0.55,
            marker=dict(colors=donut_colors_use, line=dict(color="white", width=2)),
            textinfo="none",
            hovertemplate="<b>%{label}</b><br>%{value} msg<br>%{percent}<extra></extra>"
        ))
        fig_donut.add_annotation(
            text=f"<b>{sum(donut_values) if sum(st.session_state.problems_used.values()) > 0 else 0}</b><br><span style='font-size:10px;'>messages</span>",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="#0f172a", family="Inter")
        )
        fig_donut.update_layout(
            height=300,
            margin=dict(l=10, r=10, t=20, b=20),
            paper_bgcolor="white",
            showlegend=False,
            font=dict(family="Inter")
        )
        st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar": False})

    with col_badges:
        st.markdown("<h4 style='color:#0f172a; margin-bottom:8px;'>Badges débloqués</h4>", unsafe_allow_html=True)
        badge_defs = [
            (1,  "Premier message", "#dbeafe", "#1d4ed8", "🎯"),
            (5,  "En feu !",        "#ffedd5", "#c2410c", "🔥"),
            (10, "Prospecteur",     "#fef9c3", "#a16207", "⚡"),
            (25, "Closer",          "#f0fdf4", "#15803d", "🚀"),
            (50, "Expert",          "#f5f3ff", "#6d28d9", "👑"),
        ]
        prob_badge_defs = [
            (3, "Polyvalent",    "#fef2f2", "#b91c1c", "🧩"),
            (7, "Maître des 7",  "#fff7ed", "#c2410c", "💎"),
        ]
        any_badge = False
        for threshold, name, bg, color, ico in badge_defs:
            unlocked = st.session_state.gen_count >= threshold
            opacity = "1" if unlocked else "0.35"
            st.markdown(f"""
            <div style="background:{bg}; border-radius:10px; padding:9px 12px; margin-bottom:7px;
                        display:flex; align-items:center; gap:10px; opacity:{opacity};">
                <span style="font-size:18px;">{ico}</span>
                <div>
                    <div style="font-size:12px; font-weight:700; color:{color};">{name}</div>
                    <div style="font-size:10px; color:#94a3b8;">{'✔ Débloqué' if unlocked else f'à {threshold} messages'}</div>
                </div>
            </div>""", unsafe_allow_html=True)
            if unlocked: any_badge = True
        for threshold, name, bg, color, ico in prob_badge_defs:
            unlocked = len(st.session_state.problems_used) >= threshold
            opacity = "1" if unlocked else "0.35"
            st.markdown(f"""
            <div style="background:{bg}; border-radius:10px; padding:9px 12px; margin-bottom:7px;
                        display:flex; align-items:center; gap:10px; opacity:{opacity};">
                <span style="font-size:18px;">{ico}</span>
                <div>
                    <div style="font-size:12px; font-weight:700; color:{color};">{name}</div>
                    <div style="font-size:10px; color:#94a3b8;">{'✔ Débloqué' if unlocked else f'{threshold} problèmes'}</div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.write("")

    # ── LIGNE 3 : Bar chart horizontal comparatif ──
    st.markdown("<h4 style='color:#0f172a; margin-bottom:8px;'>Performance par problème — nombre de messages</h4>", unsafe_allow_html=True)
    prob_counts_bar = [st.session_state.problems_used.get(p["id"], 0) for p in PROBLEMS]
    prob_titles_bar = [p["title"] for p in PROBLEMS]
    prob_colors_bar = [p["color"] for p in PROBLEMS]

    fig_bar = go.Figure(go.Bar(
        y=prob_titles_bar,
        x=prob_counts_bar,
        orientation="h",
        marker=dict(
            color=prob_colors_bar,
            line=dict(color="white", width=1)
        ),
        text=[f"{v} msg" for v in prob_counts_bar],
        textposition="outside",
        textfont=dict(size=11, color="#64748b")
    ))
    fig_bar.update_layout(
        height=280,
        margin=dict(l=10, r=60, t=10, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Inter", size=12),
        xaxis=dict(showgrid=True, gridcolor="#f1f5f9", zeroline=False, tickfont=dict(color="#64748b")),
        yaxis=dict(showgrid=False, tickfont=dict(size=11, color="#374151")),
        showlegend=False
    )
    st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

    st.write("")
    _, cta, _ = st.columns([1,2,1])
    with cta:
        if st.button("Générer un nouveau message", type="primary", use_container_width=True):
            st.session_state.page = "generator"
            st.rerun()

# ─────────────────────────────────────────────
# GÉNÉRATEUR
# ─────────────────────────────────────────────
elif st.session_state.page == "generator":
    st.markdown("<h2 style='color:#0f172a; margin-bottom:4px;'>✨ Générateur de messages</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; margin-bottom:24px;'>Sélectionnez le problème de votre client → configurez votre contexte → obtenez un message percutant.</p>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#0f172a;'>Étape 1 — Quel est le problème principal de votre prospect ?</h4>", unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    for i,p in enumerate(PROBLEMS):
        with [c1,c2,c3,c4][i%4]:
            is_sel = st.session_state.selected_problem_id == p["id"]
            extra = " prob-selected" if is_sel else ""
            st.markdown(f"""<div class="{p['color_class']}{extra}" style="margin-bottom:12px; min-height:130px;"><div style="font-size:28px; margin-bottom:8px;">{p['icon']}</div><div style="font-size:13px; font-weight:800; margin-bottom:6px;">{p['title']}</div><div style="font-size:11px; opacity:0.85; line-height:1.4;">{p['hook']}</div></div>""", unsafe_allow_html=True)
            if st.button("✅ Sélectionné" if is_sel else "Choisir", key=f"prob_{p['id']}", use_container_width=True, type="primary" if is_sel else "secondary"):
                st.session_state.selected_problem_id = p["id"]
                st.session_state.last_generated = ""
                st.rerun()

    if st.session_state.selected_problem_id:
        prob = next((p for p in PROBLEMS if p["id"]==st.session_state.selected_problem_id), None)
        if prob:
            st.write("")
            st.markdown(f"""<div class="{prob['workspace_class']}"><div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;"><span style="font-size:36px;">{prob['emoji_bg']}</span><div><div style="font-size:11px; font-weight:700; color:{prob['color']}; text-transform:uppercase; letter-spacing:1px;">Workspace — {prob['title']}</div><div style="font-size:18px; font-weight:800; color:#0f172a;">{prob['hook']}</div></div></div><div style="background:rgba(255,255,255,0.7); border-radius:12px; padding:14px; margin-bottom:12px;"><div style="font-size:13px; color:#374151; line-height:1.6;">{prob['desc']}</div><div style="font-size:13px; font-weight:700; color:{prob['color']}; margin-top:8px;">✅ {prob['solution']}</div></div><div style="background:rgba(255,255,255,0.5); border-radius:10px; padding:10px;"><span style="font-size:13px; color:#64748b;">{prob['tip']}</span></div></div>""", unsafe_allow_html=True)
            st.write("")
            st.markdown("<h4 style='color:#0f172a;'>Étape 2 — Configurez votre contexte</h4>", unsafe_allow_html=True)
            ca, cb = st.columns(2)
            with ca:
                v1 = st.text_input(f"🏢 {prob['fields'][0]}", placeholder=prob['placeholders'][0])
                v2 = st.text_input(f"🎯 {prob['fields'][1]}", placeholder=prob['placeholders'][1])
            with cb:
                v3 = st.text_area(f"⚡ {prob['fields'][2]}", placeholder=prob['placeholders'][2], height=110)
                tone = st.selectbox("🎨 Style du message", ["Percutant","Professionnel","Storytelling"])
            st.write("")
            if st.button(f"✨ Générer mon message — {prob['title']}", type="primary", use_container_width=True):
                if v1 and v2 and v3:
                    with st.spinner(f"Application du framework {prob['framework']}..."):
                        time.sleep(1.5)
                    result = generate_message(prob["id"],v1,v2,v3,tone)
                    st.session_state.last_generated = result
                    st.session_state.gen_count += 1
                    today = datetime.now().strftime("%Y-%m-%d")
                    st.session_state.daily_counts[today] = st.session_state.daily_counts.get(today,0)+1
                    st.session_state.problems_used[prob["id"]] = st.session_state.problems_used.get(prob["id"],0)+1
                    lvl = get_level(st.session_state.gen_count)
                    st.success(f"✅ Message généré avec le framework **{prob['framework']}** ! Niveau : {lvl['icon']} {lvl['name']}")
                else: st.warning("⚠️ Veuillez remplir tous les champs.")

    if st.session_state.last_generated:
        st.write("")
        st.markdown("<h4 style='color:#0f172a;'>Votre message — prêt à envoyer :</h4>", unsafe_allow_html=True)
        st.text_area("", value=st.session_state.last_generated, height=320, key="output_area")
        cs, _ = st.columns([1,3])
        with cs:
            if st.button("💾 Sauvegarder dans l'historique", use_container_width=True):
                prob = next((p for p in PROBLEMS if p["id"]==st.session_state.selected_problem_id), None)
                st.session_state.history.insert(0,{"date":datetime.now().strftime("%d/%m/%Y %H:%M"),"problem":prob["title"] if prob else "–","problem_icon":prob["icon"] if prob else "📄","content":st.session_state.last_generated})
                st.success("✅ Sauvegardé !")

# ─────────────────────────────────────────────
# EMAILS AUTO
# ─────────────────────────────────────────────
elif st.session_state.page == "emails":
    st.markdown("<h2 style='color:#0f172a;'>📧 Emails Automatiques</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Aperçu des emails qui sont envoyés automatiquement à vos utilisateurs.</p>", unsafe_allow_html=True)
    st.write("")

    tab1, tab2 = st.tabs(["🎉 Email de bienvenue", "⚡ Email de renouvellement (28 du mois)"])

    renewal_date = (datetime.now() + timedelta(days=30)).replace(day=28).strftime("%d/%m/%Y")
    level = get_level(st.session_state.gen_count)
    plan_obj = next((p for p in PLANS if p["name"]==st.session_state.current_plan), PLANS[1])
    next_plan = PLANS[min(PLANS.index(plan_obj)+1, len(PLANS)-1)]

    with tab1:
        st.markdown(f"""
        <div class="email-preview">
            <div class="email-header">
                <div style="font-size:32px; margin-bottom:8px;">🎉</div>
                <div style="font-size:20px; font-weight:800;">ClientBoost AI</div>
            </div>
            <strong style="font-size:16px; color:#0f172a;">Objet : {EMAIL_WELCOME['subject']}</strong>
            <hr style="border-color:#e8ecf0; margin:16px 0;">
            <pre style="font-family:'Inter',sans-serif; white-space:pre-wrap; font-size:14px; color:#374151; line-height:1.7;">{EMAIL_WELCOME['body'].format(name=st.session_state.user_name)}</pre>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown(f"""
        <div style="background:#fff7ed; border-radius:12px; padding:16px; margin-bottom:20px; border-left:4px solid #f97316;">
            <strong style="color:#c2410c;">⏰ Envoyé automatiquement le 28 de chaque mois</strong>
            <p style="color:#64748b; font-size:13px; margin:4px 0 0;">Rappel de renouvellement envoyé 3 jours avant la date de facturation.</p>
        </div>
        <div class="email-preview">
            <div class="email-header" style="background:linear-gradient(135deg,#f97316,#ea580c);">
                <div style="font-size:32px; margin-bottom:8px;">⚡</div>
                <div style="font-size:20px; font-weight:800;">ClientBoost AI</div>
            </div>
            <strong style="font-size:16px; color:#0f172a;">Objet : {EMAIL_RENEWAL['subject']}</strong>
            <hr style="border-color:#e8ecf0; margin:16px 0;">
            <pre style="font-family:'Inter',sans-serif; white-space:pre-wrap; font-size:14px; color:#374151; line-height:1.7;">{EMAIL_RENEWAL['body'].format(name=st.session_state.user_name, plan=st.session_state.current_plan, renewal_date=renewal_date, msg_count=st.session_state.gen_count, problems_used=len(st.session_state.problems_used), level=level['icon']+' '+level['name'], price=plan_obj['price']+'/mois', next_plan=next_plan['name'], next_feature='générations illimitées' if next_plan['name']=='Pro' else '5 sièges multi-utilisateurs')}</pre>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HISTORIQUE
# ─────────────────────────────────────────────
elif st.session_state.page == "history":
    st.markdown("<h2 style='color:#0f172a;'>📜 Historique</h2>", unsafe_allow_html=True)
    if not st.session_state.history:
        st.markdown("""<div class="card" style="text-align:center; padding:60px;"><p style="font-size:48px; margin:0;">📭</p><p style="color:#64748b; font-size:16px; margin-top:12px;">Aucun message sauvegardé pour l'instant.</p></div>""", unsafe_allow_html=True)
    else:
        ci, cc = st.columns([4,1])
        with ci: st.markdown(f"<span class='badge badge-green'>{len(st.session_state.history)} message(s)</span>", unsafe_allow_html=True)
        with cc:
            if st.button("🗑️ Effacer", use_container_width=True):
                st.session_state.history = []
                st.rerun()
        st.write("")
        for i,item in enumerate(st.session_state.history):
            with st.expander(f"{item.get('problem_icon','📄')} {item.get('problem','–')}  —  {item['date']}"):
                st.text_area("", value=item["content"], height=240, key=f"h_{i}")

# ─────────────────────────────────────────────
# ABONNEMENT
# ─────────────────────────────────────────────
elif st.session_state.page == "subscription":
    st.markdown("<h2 style='color:#0f172a;'>💳 Tarifs & Abonnement</h2>", unsafe_allow_html=True)
    plan_obj = next((p for p in PLANS if p["name"]==st.session_state.current_plan), PLANS[1])
    renewal = (datetime.now() + timedelta(days=30)).replace(day=28).strftime("%d/%m/%Y")
    st.markdown(f"""<div style="background:#f0fdf4; border-radius:12px; padding:16px; margin-bottom:24px; border-left:4px solid #22c55e;"><strong style="color:#15803d;">✅ Plan actuel : {st.session_state.current_plan} — {plan_obj['price']}/mois</strong><p style="color:#64748b; font-size:13px; margin:4px 0 0;">Prochain renouvellement le <strong>{renewal}</strong> • Email de rappel envoyé le 28 du mois.</p></div>""", unsafe_allow_html=True)
    st.write("")
    c1,c2,c3 = st.columns(3)
    for col,plan in zip([c1,c2,c3],PLANS):
        with col:
            is_current = plan["name"] == st.session_state.current_plan
            border = "border:2px solid #22c55e;" if is_current else ("border:2px solid #6366f1;" if plan["popular"] else "border:2px solid #e8ecf0;")
            pop = '<span style="background:#6366f1;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;display:inline-block;margin-bottom:8px;">⭐ POPULAIRE</span>' if plan["popular"] else ""
            cur = '<span style="background:#22c55e;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;display:inline-block;margin-bottom:8px;">✅ PLAN ACTUEL</span>' if is_current else ""
            st.markdown(f"""<div class="price-card" style="{border} margin-bottom:16px;"><div style="font-size:28px; margin-bottom:8px;">{plan['icon']}</div><div style="font-size:15px; font-weight:700; color:#64748b; margin-bottom:8px;">{plan['name']}</div>{pop}{cur}<div class="price-amount" style="margin:12px 0 4px;">{plan['price']}</div><div style="font-size:14px; color:#64748b; margin-bottom:20px;">{plan['period']}</div><hr style="border-color:#f1f5f9; margin:16px 0;">{''.join(f'<div class="feature-item">{f}</div>' for f in plan['features'])}</div>""", unsafe_allow_html=True)
            if not is_current:
                if st.button(f"Passer au {plan['name']}", key=f"switch_{plan['name']}", use_container_width=True, type="primary" if plan["popular"] else "secondary"):
                    st.session_state.current_plan = plan["name"]
                    st.session_state.plan_price = plan["price"]
                    st.success(f"✅ Abonnement mis à jour : Plan {plan['name']} — {plan['price']}/mois")

# ─────────────────────────────────────────────
# PARAMÈTRES
# ─────────────────────────────────────────────
elif st.session_state.page == "settings":
    st.markdown("<h2 style='color:#0f172a;'>⚙️ Paramètres</h2>", unsafe_allow_html=True)
    st.write("")
    st.markdown("""<div class="card"><h4 style="color:#0f172a; margin-top:0;">👤 Profil</h4>""", unsafe_allow_html=True)
    new_name = st.text_input("Prénom", value=st.session_state.user_name)
    st.markdown(f"<p style='color:#64748b; font-size:13px;'>Email : {st.session_state.user_email}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""<div class="card"><h4 style="color:#0f172a; margin-top:0;">🔑 API Anthropic (optionnel)</h4>""", unsafe_allow_html=True)
    api_key = st.text_input("Clé API", type="password", placeholder="sk-ant-...")
    st.markdown("<p style='font-size:13px; color:#64748b;'>Ajoutez votre clé pour utiliser le vrai moteur Claude AI. <a href='https://console.anthropic.com' target='_blank'>Obtenir une clé →</a></p></div>", unsafe_allow_html=True)
    level = get_level(st.session_state.gen_count)
    renewal = (datetime.now() + timedelta(days=30)).replace(day=28).strftime("%d/%m/%Y")
    st.markdown(f"""<div class="card"><h4 style="color:#0f172a; margin-top:0;">📊 Votre compte</h4>
        <p style="color:#475569;">Membre depuis : <strong>{st.session_state.join_date}</strong></p>
        <p style="color:#475569;">Plan actuel : <strong>{st.session_state.current_plan}</strong></p>
        <p style="color:#475569;">Renouvellement : <strong>{renewal}</strong></p>
        <p style="color:#475569;">Niveau : <strong>{level['icon']} {level['name']}</strong></p>
        <p style="color:#475569;">Messages générés : <strong>{st.session_state.gen_count}</strong></p>
        <p style="color:#475569;">Problèmes explorés : <strong>{len(st.session_state.problems_used)} / 7</strong></p>
    </div>""", unsafe_allow_html=True)
    if st.button("✅ Enregistrer", type="primary"):
        st.session_state.user_name = new_name
        st.success("Paramètres enregistrés !")
