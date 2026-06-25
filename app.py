import streamlit as st
import time
import random
from datetime import datetime, timedelta

try:
    import plotly.graph_objects as go
    PLOTLY_OK = True
except ImportError:
    PLOTLY_OK = False

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(page_title="ClientBoost AI", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;}
.main .block-container{padding-top:0;padding-bottom:3rem;max-width:1150px;}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#0a0f1e,#0f172a,#1a1f35)!important;border-right:1px solid rgba(255,255,255,0.06);}
section[data-testid="stSidebar"] *{color:#e2e8f0!important;}
.stButton>button[kind="primary"]{background:linear-gradient(135deg,#6366f1,#8b5cf6)!important;border:none!important;border-radius:10px!important;font-weight:700!important;color:white!important;transition:all 0.2s!important;}
.stButton>button[kind="primary"]:hover{transform:translateY(-2px)!important;box-shadow:0 8px 25px rgba(99,102,241,0.4)!important;}
.stTextInput>div>div>input,.stTextArea>div>div>textarea{border-radius:10px!important;border:1.5px solid #e2e8f0!important;font-size:14px!important;}
footer{visibility:hidden;}#MainMenu{visibility:hidden;}

@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.04)}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes shimmer{0%{background-position:-200% center}100%{background-position:200% center}}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@keyframes glow{0%,100%{box-shadow:0 0 10px rgba(99,102,241,0.3)}50%{box-shadow:0 0 30px rgba(99,102,241,0.7)}}

.fade-up{animation:fadeUp 0.5s ease forwards;}
.card{background:white;border-radius:20px;padding:28px;border:1px solid #e8ecf0;box-shadow:0 2px 8px rgba(0,0,0,0.06);margin-bottom:20px;}
.prob-time{background:linear-gradient(135deg,#1e3a5f,#2563eb);border-radius:20px;padding:24px;color:white;border:3px solid transparent;transition:all 0.3s;cursor:pointer;}
.prob-money{background:linear-gradient(135deg,#064e3b,#059669);border-radius:20px;padding:24px;color:white;border:3px solid transparent;transition:all 0.3s;cursor:pointer;}
.prob-skill{background:linear-gradient(135deg,#451a03,#d97706);border-radius:20px;padding:24px;color:white;border:3px solid transparent;transition:all 0.3s;cursor:pointer;}
.prob-growth{background:linear-gradient(135deg,#0f172a,#6366f1);border-radius:20px;padding:24px;color:white;border:3px solid transparent;transition:all 0.3s;cursor:pointer;}
.prob-frustration{background:linear-gradient(135deg,#4c0519,#dc2626);border-radius:20px;padding:24px;color:white;border:3px solid transparent;transition:all 0.3s;cursor:pointer;}
.prob-risk{background:linear-gradient(135deg,#2e1065,#7c3aed);border-radius:20px;padding:24px;color:white;border:3px solid transparent;transition:all 0.3s;cursor:pointer;}
.prob-retention{background:linear-gradient(135deg,#431407,#ea580c);border-radius:20px;padding:24px;color:white;border:3px solid transparent;transition:all 0.3s;cursor:pointer;}
.prob-time:hover,.prob-money:hover,.prob-skill:hover,.prob-growth:hover,.prob-frustration:hover,.prob-risk:hover,.prob-retention:hover{filter:brightness(1.1);transform:translateY(-6px);box-shadow:0 20px 50px rgba(0,0,0,0.3);}
.workspace-time{background:linear-gradient(135deg,#eff6ff,#dbeafe);border:2px solid #3b82f6;border-radius:20px;padding:28px;}
.workspace-money{background:linear-gradient(135deg,#f0fdf4,#dcfce7);border:2px solid #22c55e;border-radius:20px;padding:28px;}
.workspace-skill{background:linear-gradient(135deg,#fffbeb,#fef3c7);border:2px solid #f59e0b;border-radius:20px;padding:28px;}
.workspace-growth{background:linear-gradient(135deg,#f5f3ff,#ede9fe);border:2px solid #8b5cf6;border-radius:20px;padding:28px;}
.workspace-frustration{background:linear-gradient(135deg,#fff1f2,#ffe4e6);border:2px solid #f43f5e;border-radius:20px;padding:28px;}
.workspace-risk{background:linear-gradient(135deg,#faf5ff,#f3e8ff);border:2px solid #a855f7;border-radius:20px;padding:28px;}
.workspace-retention{background:linear-gradient(135deg,#fff7ed,#ffedd5);border:2px solid #f97316;border-radius:20px;padding:28px;}
.price-card{background:white;border:2px solid #e8ecf0;border-radius:24px;padding:36px 28px;text-align:center;transition:all 0.3s;}
.price-card:hover{border-color:#6366f1;transform:translateY(-6px);box-shadow:0 20px 60px rgba(99,102,241,0.15);}
.price-card.popular{border-color:#6366f1;background:linear-gradient(135deg,#fafafa,#f5f3ff);}
.price-amount{font-size:48px;font-weight:900;color:#0f172a;}
.feature-item{text-align:left;padding:8px 0;font-size:14px;color:#374151;border-bottom:1px solid #f1f5f9;}
.feature-item:last-child{border-bottom:none;}
.result-card{background:linear-gradient(135deg,#0f172a,#1e1b4b);border-radius:24px;padding:32px;color:white;margin-bottom:20px;}
.star-wrap{display:inline-flex;gap:3px;align-items:center;}
.star-gold{filter:drop-shadow(0 1px 3px rgba(251,191,36,0.6));}
.auth-container{max-width:460px;margin:0 auto;background:white;border-radius:24px;padding:40px;border:1px solid #e8ecf0;box-shadow:0 8px 40px rgba(0,0,0,0.08);}
.testimonial-card{background:white;border-radius:20px;padding:28px;border:1px solid #e8ecf0;box-shadow:0 4px 20px rgba(0,0,0,0.08);}
.msg-preview{background:#f8fafc;border-radius:12px;padding:16px;border-left:4px solid #6366f1;font-size:13px;line-height:1.6;color:#374151;}
.email-preview{background:#f8fafc;border-radius:16px;padding:24px;border:1px solid #e8ecf0;font-size:14px;line-height:1.7;}
.email-header{background:linear-gradient(135deg,#6366f1,#8b5cf6);border-radius:12px 12px 0 0;padding:20px;color:white;text-align:center;margin:-24px -24px 20px;}
.prog-wrap{background:#f1f5f9;border-radius:999px;height:10px;margin:8px 0;overflow:hidden;}
.prog-fill{height:10px;border-radius:999px;}
.metric-box{background:white;border-radius:16px;padding:22px;text-align:center;border:1px solid #e8ecf0;box-shadow:0 2px 8px rgba(0,0,0,0.05);}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DONNÉES
# ─────────────────────────────────────────────
STAR_SVG = '<span class="star-wrap">' + ''.join([
    '<svg class="star-gold" width="16" height="16" viewBox="0 0 24 24"><path fill="#FBBF24" stroke="#F59E0B" stroke-width="0.5" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'
]*5) + '</span>'

PROBLEMS = [
    {"id":"time","css":"prob-time","ws":"workspace-time","color":"#2563eb","framework":"AIDA",
     "title":"Temps qui s'évapore","hook":"Vous passez 3h à rédiger ce qui devrait prendre 3 minutes.",
     "desc":"Chaque message de prospection vous prend une éternité. Résultat : vous prospectez peu, vous signez peu. Votre temps vaut trop cher pour être gaspillé sur du copier-coller.",
     "solution":"ClientBoost génère un message complet, personnalisé et percutant en 10 secondes chrono. Récupérez vos heures. Concentrez-vous sur les deals.",
     "stats":[("8h","récupérées/semaine en moyenne"),("10s","pour générer un message complet"),("80%","de réduction du temps de prospection")],
     "tip":"Un message court (< 150 mots) obtient 2x plus de réponses qu'un long discours.",
     "icon_svg":'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M5 22h14M5 2h14M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/></svg>',
     "fields":["Votre secteur / produit","Votre persona cible","Ce qui vous prend le plus de temps"],
     "placeholders":["Ex : Coach business, Agence web, SaaS RH","Ex : Directeurs marketing, Freelances débordés","Ex : Rédiger mes emails de prospection chaque matin"]},
    {"id":"money","css":"prob-money","ws":"workspace-money","color":"#059669","framework":"PAS",
     "title":"Budget qui s'évapore","hook":"Vous investissez. Vous n'encaissez pas. Quelque chose cloche.",
     "desc":"Vos pubs tournent, vos emails partent, mais les conversions ne suivent pas. Vous payez une agence qui pond des messages génériques. Stop. Le problème n'est pas votre offre — c'est le message.",
     "solution":"ClientBoost applique AIDA, PAS et le storytelling pour transformer chaque euro investi en vrai retour sur investissement. Fini les dépenses à perte.",
     "stats":[("40%","d'augmentation du taux de conversion"),("3x","de retour sur investissement moyen"),("30j","pour voir les premiers résultats")],
     "tip":"Framework PAS : Problème → Agitation → Solution. Le plus efficace pour convertir à froid.",
     "icon_svg":'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/></svg>',
     "fields":["Votre offre / produit","Votre client idéal","Où vous perdez de l'argent actuellement"],
     "placeholders":["Ex : Formation en ligne, Logiciel B2B","Ex : TPE qui veulent croître, E-commerçants","Ex : Mes pubs Facebook ne convertissent pas"]},
    {"id":"skill","css":"prob-skill","ws":"workspace-skill","color":"#d97706","framework":"FAB",
     "title":"Page blanche paralysante","hook":"Vous savez ce que vous vendez. Vous ne savez pas comment le dire.",
     "desc":"Syndrome de la page blanche, accroches fades, messages qui ne donnent pas envie de répondre. Écrire pour vendre est un métier. Vous n'êtes pas obligé de le maîtriser — juste d'avoir le bon outil.",
     "solution":"ClientBoost intègre 10+ frameworks de copywriting (AIDA, PAS, FAB, storytelling) pour que chaque message soit structuré pour convaincre. Même si vous n'avez jamais écrit une ligne de vente.",
     "stats":[("10+","frameworks de vente intégrés"),("60s","de la page blanche au message prêt"),("30%","de taux de conversion moyen")],
     "tip":"Framework FAB : Feature → Advantage → Benefit. Traduisez les fonctionnalités en bénéfices concrets.",
     "icon_svg":'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.84A2.5 2.5 0 0 1 9.5 2"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.84A2.5 2.5 0 0 0 14.5 2"/></svg>',
     "fields":["Votre produit / service","Votre persona","Votre blocage principal à l'écriture"],
     "placeholders":["Ex : Outil de gestion de projet, Coaching carrière","Ex : Entrepreneurs solo, Managers d'équipes","Ex : Je ne sais pas par quoi commencer mon message"]},
    {"id":"growth","css":"prob-growth","ws":"workspace-growth","color":"#7c3aed","framework":"Storytelling",
     "title":"Pipeline à sec","hook":"Votre offre est bonne. Votre agenda est vide. C'est urgent.",
     "desc":"Pas assez de leads, pas assez de conversations, pas assez de contrats signés. Votre tunnel de vente ressemble à un désert. La croissance ne se produit pas par hasard — elle se fabrique.",
     "solution":"Générez 10, 50 ou 100 messages de prospection hyper-ciblés en quelques minutes. Chaque message est adapté à la douleur exacte de votre persona. Volume + personnalisation = pipeline plein.",
     "stats":[("50x","plus de messages en même temps"),("47","leads qualifiés en 60 jours en moyenne"),("10x","le volume de prospection")],
     "tip":"Storytelling : commencez par une situation que votre prospect vit, pas par votre produit.",
     "icon_svg":'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>',
     "fields":["Votre secteur","Votre client idéal (persona)","Quel résultat vous promettez en X jours ?"],
     "placeholders":["Ex : Agence SEO, Consultant RH, Application mobile","Ex : Startups en croissance, PME de 10-50 salariés","Ex : +30% de leads qualifiés en 30 jours"]},
    {"id":"frustration","css":"prob-frustration","ws":"workspace-frustration","color":"#dc2626","framework":"Empathy Map",
     "title":"Prospection que vous détestez","hook":"Vous envoyez. Silence radio. Encore et encore.",
     "desc":"La prospection à froid vous épuise. Vous vous sentez intrusif, vous n'obtenez aucune réponse, et chaque relance ressemble à une humiliation. Ce n'est pas vous le problème. C'est la façon dont vous abordez vos prospects.",
     "solution":"ClientBoost crée des messages empathiques qui parlent à vos prospects — pas à leur boîte mail. Des messages qu'ils ont envie de lire. Une prospection dont vous serez fier.",
     "stats":[("18%","de taux de réponse moyen (vs 2%)"),("7x","d'amélioration du taux de réponse"),("0","message dont vous aurez honte")],
     "tip":"Pensez à ce que votre prospect ressent, craint et désire avant d'écrire une seule ligne.",
     "icon_svg":'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M16 16s-1.5-2-4-2-4 2-4 2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/><path d="M9 5c0 0 1.5 2 3 2s3-2 3-2"/></svg>',
     "fields":["Votre produit / service","Votre persona cible","Pourquoi vos messages n'obtiennent pas de réponse ?"],
     "placeholders":["Ex : Logiciel de facturation, Formation marketing","Ex : Artisans indépendants, PME sans équipe marketing","Ex : Mes messages semblent trop commerciaux ou génériques"]},
    {"id":"risk","css":"prob-risk","ws":"workspace-risk","color":"#7c3aed","framework":"Trust Builder",
     "title":"Réputation en jeu","hook":"Un mauvais message peut griller 100 prospects d'un coup.",
     "desc":"Vous avez peur d'envoyer un message qui fait fuir, qui paraît non professionnel, ou qui brûle définitivement votre base de contacts. Cette peur vous paralyse. Et pendant ce temps, vos concurrents prospectent.",
     "solution":"ClientBoost garantit des messages calibrés : bon ton, bonne structure, bon niveau de professionnalisme. Prospectez à grande échelle avec la certitude de ne jamais envoyer quelque chose dont vous auriez honte.",
     "stats":[("0","plainte sur 500 messages envoyés"),("43","RDV qualifiés en une seule campagne"),("100%","de messages professionnels garantis")],
     "tip":"Trust Builder : démontrez que vous comprenez leur situation avant de parler de vous.",
     "icon_svg":'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
     "fields":["Votre secteur / produit","Votre persona","Ce que vous craignez le plus d'envoyer"],
     "placeholders":["Ex : Cabinet de conseil, Agence de communication","Ex : Grands comptes, Décideurs C-level","Ex : Un message trop agressif qui me fait passer pour un spammeur"]},
    {"id":"retention","css":"prob-retention","ws":"workspace-retention","color":"#ea580c","framework":"Lifecycle",
     "title":"Clients qui disparaissent","hook":"Acquérir un client coûte 5x plus cher que d'en garder un. Et vous les perdez.",
     "desc":"Vos clients existants ne rachètent pas. Vos anciens clients vous ont oublié. Vous n'avez aucun système de suivi. Chaque client perdu, c'est du chiffre d'affaires qui s'évapore silencieusement.",
     "solution":"ClientBoost génère des séquences de relance, newsletters de réengagement et offres de suivi personnalisées. Transformez vos clients silencieux en ambassadeurs et acheteurs réguliers.",
     "stats":[("60","clients réactivés en 2 semaines"),("35%","d'augmentation du taux de rétention"),("5x","moins cher que d'acquérir un nouveau client")],
     "tip":"Un client existant a 60-70% de chance d'acheter à nouveau si vous restez présent au bon moment.",
     "icon_svg":'<svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>',
     "fields":["Votre produit / service","Vos clients existants (profil)","Depuis combien de temps sans contact ?"],
     "placeholders":["Ex : Service d'abonnement, Formation, Consulting","Ex : Clients achetés il y a 3-6 mois, Anciens abonnés","Ex : Plus de 2 mois, je n'ai aucun suivi automatique"]},
]

PLANS = [
    {"name":"Standard","price":"9€","period":"/mois","popular":False,"color":"#64748b",
     "features":["✔ 50 générations/mois","✔ 7 frameworks inclus","✔ 3 langues","✔ Historique 30 jours","✔ Dashboard basique","✖ Support prioritaire","✖ Illimité"],
     "cta":"Choisir Standard"},
    {"name":"Pro","price":"29€","period":"/mois","popular":True,"color":"#6366f1",
     "features":["✔ Générations illimitées","✔ 7 frameworks inclus","✔ 6 langues","✔ Historique 1 an","✔ Dashboard + badges","✔ Support prioritaire","✔ Emails automatiques"],
     "cta":"Choisir Pro — Populaire"},
    {"name":"Agence","price":"79€","period":"/mois","popular":False,"color":"#f59e0b",
     "features":["✔ Générations illimitées","✔ 7 frameworks inclus","✔ 6 langues","✔ Historique illimité","✔ Dashboard + badges","✔ Support dédié + API","✔ 5 sièges multi-users"],
     "cta":"Choisir Agence"},
]

TESTIMONIALS = [
    {"name":"Sophie M.","role":"Consultante RH","photo":"https://i.pravatar.cc/80?img=47","initials":"SM","bg":"#6366f1","text":"En 2 semaines j'ai obtenu 11 rendez-vous qualifiés. La différence ? Des messages qui parlent vraiment à mes prospects.","result":"11 RDV en 2 semaines"},
    {"name":"Karim B.","role":"Fondateur agence SEO","photo":"https://i.pravatar.cc/80?img=12","initials":"KB","bg":"#059669","text":"Mon taux de réponse est passé de 3% à 21%. Mes prospects me remercient pour l'approche différente.","result":"Taux réponse x7"},
    {"name":"Marie-Claire T.","role":"Coach business","photo":"https://i.pravatar.cc/80?img=5","initials":"MT","bg":"#dc2626","text":"J'ai réactivé 43 anciens clients en un seul mailing. Sans pub, sans budget.","result":"43 clients réactivés"},
    {"name":"Thomas D.","role":"Freelance dev","photo":"https://i.pravatar.cc/80?img=33","initials":"TD","bg":"#2563eb","text":"Je détestais prospecter. Maintenant j'envoie 30 messages/semaine en 15 minutes.","result":"30 msg/semaine"},
    {"name":"Amina K.","role":"Directrice commerciale","photo":"https://i.pravatar.cc/80?img=9","initials":"AK","bg":"#d97706","text":"J'ai payé 29€ Pro, le premier client signé m'a rapporté 1 800€. ROI immédiat.","result":"ROI 6 200%"},
    {"name":"Lucas F.","role":"E-commerçant","photo":"https://i.pravatar.cc/80?img=68","initials":"LF","bg":"#7c3aed","text":"Taux d'ouverture de mes newsletters : 8% → 34%. C'est bluffant.","result":"Ouverture x4"},
]

EMAIL_WELCOME = {"subject":"Bienvenue dans ClientBoost AI — Votre premier message vous attend",
"body":"""Bonjour {name},

Bienvenue dans la famille ClientBoost AI !

Vous venez de rejoindre plus de 12 000 entrepreneurs qui ont transformé leur prospection.

Ce que vous pouvez faire dès maintenant :
- Générer votre premier message de vente (60 secondes)
- Choisir parmi 7 problèmes clients avec frameworks dédiés
- Tester les 3 styles : Percutant, Professionnel, Storytelling

Notre conseil : allez dans le Générateur, sélectionnez votre problème, remplissez les 3 champs.

À votre succès,
L'équipe ClientBoost AI"""}

EMAIL_RENEWAL = {"subject":"Votre abonnement ClientBoost AI se renouvelle dans 3 jours",
"body":"""Bonjour {name},

Votre abonnement {plan} se renouvelle le {renewal_date}.

Votre activité ce mois-ci :
- {msg_count} messages générés
- {problems_used} problèmes clients explorés
- Niveau atteint : {level}

Votre abonnement sera renouvelé le {renewal_date} pour {price}.

Pour modifier ou annuler : Paramètres > Abonnement.

Envie de passer au niveau supérieur ? Le plan {next_plan} vous donnerait {next_feature}.

L'équipe ClientBoost AI"""}

LEVELS = [
    {"name":"Débutant","min":0,"max":5,"color":"#64748b"},
    {"name":"Prospecteur","min":6,"max":15,"color":"#f59e0b"},
    {"name":"Closer","min":16,"max":30,"color":"#3b82f6"},
    {"name":"Expert","min":31,"max":60,"color":"#8b5cf6"},
    {"name":"Maitre","min":61,"max":999,"color":"#f43f5e"},
]
def get_level(c):
    for l in LEVELS:
        if l["min"] <= c <= l["max"]: return l
    return LEVELS[-1]
def get_next_level(c):
    for i,l in enumerate(LEVELS):
        if l["min"] <= c <= l["max"]: return LEVELS[i+1] if i+1<len(LEVELS) else None
    return None

# ─────────────────────────────────────────────
# GÉNÉRATEUR
# ─────────────────────────────────────────────
def generate_message(prob_id, secteur, persona, context, tone):
    tpls = {
        "time":{
            "Percutant":f"Objet : Récupérez 10h par semaine — sans embaucher\n\nBonjour [Prénom],\n\nUne question directe : combien d'heures avez-vous passé cette semaine à rédiger des messages au lieu de les envoyer ?\n\nPour la plupart des {persona}, c'est entre 5 et 15h perdues. Chaque semaine.\n\nAvec {secteur}, {context} ne vous prend plus qu'un clic. Nos clients récupèrent en moyenne 8h par semaine dès le premier mois.\n\nJe vous montre comment en 20 minutes. Cette semaine ?\n\n[Votre nom]",
            "Professionnel":f"Objet : Optimisation du temps de prospection\n\nBonjour [Prénom],\n\nEn travaillant avec des {persona}, j'ai constaté que {context} monopolise un temps précieux qui devrait être consacré à la conversion.\n\n{secteur} permet de réduire ce temps de 80% tout en améliorant la personnalisation.\n\nUn échange de 20 minutes cette semaine ?\n\nCordialement,\n[Votre nom]",
            "Storytelling":f"Objet : \"Je passais 3h par jour à rédiger...\"\n\nBonjour [Prénom],\n\nC'est ce que m'a dit Sarah, il y a 6 mois. Elle gérait des {persona} qui noyaient dans {context}.\n\nAujourd'hui avec {secteur}, son équipe génère 3x plus de messages en 1/5 du temps.\n\nVotre situation ressemble à celle de Sarah ?\n\n[Votre nom]"
        },
        "money":{
            "Percutant":f"Objet : Votre budget a une fuite — voici où\n\nBonjour [Prénom],\n\nChaque mois, des {persona} me montrent leurs campagnes : budget investi, résultats décevants.\n\nLe diagnostic : {context}. Le problème n'est pas le produit — c'est le message.\n\n{secteur} applique PAS et AIDA pour que chaque euro génère un retour mesurable. +40% de conversion en 30 jours en moyenne.\n\nOn en parle cette semaine ?\n\n[Votre nom]",
            "Professionnel":f"Objet : Amélioration du ROI de vos campagnes\n\nBonjour [Prénom],\n\nL'analyse de campagnes similaires aux vôtres révèle le même frein : {context}.\n\n{secteur} résout ce problème en appliquant des frameworks éprouvés (PAS, AIDA, FAB) à chaque message, réduisant le CAC et augmentant le taux de conversion.\n\nUn échange de 20 minutes ?\n\nCordialement,\n[Votre nom]",
            "Storytelling":f"Objet : Il a réduit son CAC de 60% sans augmenter son budget\n\nBonjour [Prénom],\n\nMarc, consultant pour {persona}, investissait 2 000€/mois. Résultat : 3-4 clients. Rentabilité nulle.\n\nSon problème : {context}. Le message ne convertissait pas.\n\nAvec {secteur} et le framework PAS : même budget, 9 clients en 30 jours. CAC divisé par 3.\n\nJe vous montre ce qu'on a changé ?\n\n[Votre nom]"
        },
        "skill":{
            "Percutant":f"Objet : Vous n'avez pas besoin d'apprendre le copywriting\n\nBonjour [Prénom],\n\nLe copywriting est un métier. Vous en avez déjà un.\n\nPourtant, des {persona} passent des heures sur {context}. {secteur} intègre AIDA, PAS, FAB et le storytelling directement. Renseignez votre contexte. Obtenez un message structuré. En 10 secondes.\n\nTest en direct ?\n\n[Votre nom]",
            "Professionnel":f"Objet : La structure qui transforme vos messages en RDV\n\nBonjour [Prénom],\n\nLa majorité des {persona} partagent le même défi : {context}. Non par manque d'expertise, mais faute d'une méthode de rédaction éprouvée.\n\n{secteur} pallie ce manque en intégrant automatiquement les frameworks les plus efficaces (AIDA, FAB, Storytelling).\n\nUn échange de 20 minutes ?\n\nCordialement,\n[Votre nom]",
            "Storytelling":f"Objet : \"Je ne savais pas quoi écrire — maintenant je convertis à 30%\"\n\nBonjour [Prénom],\n\nJulie, {persona[:-1] if persona.endswith('s') else persona} indépendante, passait 2h par message. {context} la paralysait.\n\nElle a essayé {secteur}. Premier message généré : un RDV pris en 24h.\n\nLe secret ? Le framework FAB : Feature, Advantage, Benefit.\n\nMême résultat dès demain ?\n\n[Votre nom]"
        },
        "growth":{
            "Percutant":f"Objet : Votre pipeline mérite mieux que le silence\n\nBonjour [Prénom],\n\nUn pipeline vide, c'est une entreprise en danger. Pour des {persona}, {context} bloque souvent la croissance.\n\nAvec {secteur}, générez 50 messages personnalisés dans le temps où vous en écriviez 1.\n\nVolume + personnalisation = pipeline qui explose.\n\n15 minutes pour voir ?\n\n[Votre nom]",
            "Professionnel":f"Objet : Stratégie de génération de leads\n\nBonjour [Prénom],\n\nLa croissance repose sur deux piliers : volume et qualité. Pour les {persona}, {context} limite souvent les deux.\n\n{secteur} multiplie le volume par 10 tout en maintenant un haut niveau de personnalisation.\n\nUn échange de 20 minutes ?\n\nCordialement,\n[Votre nom]",
            "Storytelling":f"Objet : De 3 leads/mois à 47 en 60 jours\n\nBonjour [Prénom],\n\nThomas gère une équipe de {persona}. Il y a 3 mois, {context} limitait leur prospection à 3-4 leads/mois.\n\nAvec {secteur} : 47 leads qualifiés en 60 jours. Pipeline rempli.\n\nOn reproduit ça pour vous ?\n\n[Votre nom]"
        },
        "frustration":{
            "Percutant":f"Objet : Arrêtez d'envoyer des messages que vous détestez écrire\n\nBonjour [Prénom],\n\nPour des {persona}, la prospection c'est souvent la tâche la plus redoutée. {context}. Et quand les réponses ne viennent pas, la frustration monte.\n\n{secteur} génère des messages empathiques, directs, humains.\n\nRésultat : des réponses. Et une prospection dont vous serez fier.\n\n[Votre nom]",
            "Professionnel":f"Objet : Augmentez votre taux de réponse sans paraître intrusif\n\nBonjour [Prénom],\n\nLes {persona} partagent souvent la même réticence : {context}.\n\n{secteur} aborde la prospection par l'empathie : chaque message est construit autour de la situation réelle du prospect, pas autour de votre offre.\n\nUn échange de 20 minutes ?\n\nCordialement,\n[Votre nom]",
            "Storytelling":f"Objet : \"J'avais honte d'envoyer mes messages\"\n\nBonjour [Prénom],\n\nPierre, {persona[:-1] if persona.endswith('s') else persona}, évitait la prospection depuis 6 mois. {context}. Il se sentait comme un spammeur.\n\nAvec {secteur}, ses prospects le remercient pour l'approche différente. Taux de réponse : 2% → 18%.\n\nMême résultat ?\n\n[Votre nom]"
        },
        "risk":{
            "Percutant":f"Objet : Prospectez à grande échelle sans risquer votre réputation\n\nBonjour [Prénom],\n\nPour des {persona}, un mauvais message peut griller une réputation construite en années. {context}.\n\n{secteur} intègre des contrôles qualité automatiques : bon ton, bonne structure, bon professionnalisme.\n\nVous prospectez avec confiance.\n\n[Votre nom]",
            "Professionnel":f"Objet : Qualité irréprochable à grande échelle\n\nBonjour [Prénom],\n\nComment maintenir la qualité quand le volume augmente ? Pour des {persona}, {context} freine beaucoup d'initiatives.\n\n{secteur} standardise la qualité tout en maintenant la personnalisation.\n\nUn échange ?\n\nCordialement,\n[Votre nom]",
            "Storytelling":f"Objet : Il a envoyé 500 messages — zéro plainte, 43 RDV\n\nBonjour [Prénom],\n\nKarim avait 500 contacts qu'il n'osait pas contacter. {context}.\n\nAvec {secteur} : séquence calibrée, ton juste, qualité constante.\n\n500 envois. Zéro plainte. 43 RDV qualifiés.\n\nMême assurance ?\n\n[Votre nom]"
        },
        "retention":{
            "Percutant":f"Objet : Vos anciens clients vous attendent — et vous les ignorez\n\nBonjour [Prénom],\n\nAcquérir un client coûte 5x plus cher que d'en garder un. Pourtant, des {persona} laissent leurs clients partir sans un mot. {context}.\n\n{secteur} génère des séquences de réengagement personnalisées.\n\nC'est du CA déjà payé qui vous attend.\n\n[Votre nom]",
            "Professionnel":f"Objet : Maximiser la valeur client par le réengagement\n\nBonjour [Prénom],\n\nLa réactivation des clients existants est un levier sous-exploité. {context} est souvent la cause d'un taux de rétention insuffisant.\n\n{secteur} crée des séquences de suivi personnalisées. Impact : +35% de rétention en 90 jours.\n\nCordialement,\n[Votre nom]",
            "Storytelling":f"Objet : Elle a réactivé 60 clients dormants en 2 semaines\n\nBonjour [Prénom],\n\nAmina gérait des {persona}. Ses clients achetaient une fois, puis disparaissaient. {context}.\n\nAvec {secteur} : séquence de 3 emails de réengagement personnalisés.\n\n60 clients réactivés, 23 nouveaux achats. Sans un seul nouveau prospect.\n\n[Votre nom]"
        }
    }
    pt = tpls.get(prob_id, tpls["time"])
    return pt.get(tone, list(pt.values())[0])

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
DEFAULTS = {
    "page": "landing",
    "authenticated": False,
    "subscribed": False,
    "user_name": "",
    "user_email": "",
    "current_plan": "",
    "join_date": datetime.now().strftime("%d/%m/%Y"),
    "history": [],
    "last_generated": "",
    "gen_count": 0,
    "daily_counts": {},
    "problems_used": {},
    "show_register": False,
    "pending_name": "",
    "pending_email": "",
    "selected_problem": None,
    "gen_inputs": {},
    "show_payment_from": "",
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

def go(page):
    st.session_state.page = page
    st.rerun()

# ─────────────────────────────────────────────
# HELPERS UI
# ─────────────────────────────────────────────
def render_stars():
    return STAR_SVG

def back_btn(label="← Retour", target=None):
    if st.button(label, key=f"back_{label}_{target}"):
        if target:
            go(target)
        else:
            st.session_state.history_stack = getattr(st.session_state, 'history_stack', [])

def nav_header(show_back=None, back_label="← Retour"):
    st.markdown(f"""
    <div style="background:rgba(10,15,30,0.97);backdrop-filter:blur(10px);padding:14px 32px;
    display:flex;justify-content:space-between;align-items:center;
    margin:-16px -16px 32px;border-bottom:1px solid rgba(255,255,255,0.08);position:sticky;top:0;z-index:100;">
        <div style="font-size:20px;font-weight:900;background:linear-gradient(135deg,#6366f1,#8b5cf6);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;">ClientBoost AI</div>
        <div style="font-size:13px;color:#64748b;">12 000+ utilisateurs actifs</div>
    </div>
    """, unsafe_allow_html=True)
    if show_back:
        if st.button(back_label, key=f"hdr_back_{show_back}"):
            go(show_back)

# ═══════════════════════════════════════════════════════
# PAGE : LANDING
# ═══════════════════════════════════════════════════════
if st.session_state.page == "landing":
    nav_header()

    # HERO
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0a0f1e,#1e1b4b,#0a0f1e);border-radius:32px;padding:80px 40px;text-align:center;margin-bottom:60px;">
        <div style="display:inline-block;background:rgba(99,102,241,0.15);border:1px solid rgba(99,102,241,0.3);
        border-radius:999px;padding:6px 18px;font-size:13px;color:#a5b4fc;font-weight:600;margin-bottom:24px;">
            Nouveau — 7 frameworks de vente intégrés
        </div>
        <h1 style="font-size:58px;font-weight:900;color:white;line-height:1.1;margin:0 0 20px;">
            Multipliez vos revenus<br>
            <span style="background:linear-gradient(135deg,#6366f1,#a78bfa,#ec4899);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;">avec les bons mots.</span>
        </h1>
        <p style="font-size:19px;color:#94a3b8;max-width:600px;margin:0 auto 36px;line-height:1.6;">
            ClientBoost AI génère des messages de vente percutants en 10 secondes.
            Conçu pour résoudre les 7 problèmes qui bloquent votre croissance.
        </p>
        <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:16px;">
            <div style="background:rgba(255,255,255,0.08);border-radius:12px;padding:10px 18px;color:white;font-size:14px;">
                <svg style="vertical-align:middle;margin-right:6px;" width="16" height="16" viewBox="0 0 24 24" fill="#FBBF24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                Génération en 10 secondes
            </div>
            <div style="background:rgba(255,255,255,0.08);border-radius:12px;padding:10px 18px;color:white;font-size:14px;">
                <svg style="vertical-align:middle;margin-right:6px;" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#a78bfa" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
                7 frameworks de vente
            </div>
            <div style="background:rgba(255,255,255,0.08);border-radius:12px;padding:10px 18px;color:white;font-size:14px;">
                <svg style="vertical-align:middle;margin-right:6px;" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                6 langues
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 7 PROBLÈMES
    st.markdown("""
    <div style="text-align:center;margin-bottom:40px;">
        <span style="background:#ede9fe;color:#6d28d9;border-radius:999px;padding:4px 16px;font-size:12px;font-weight:700;">
            CLIQUEZ SUR UN PROBLÈME POUR EN SAVOIR PLUS
        </span>
        <h2 style="font-size:36px;font-weight:900;color:#0f172a;margin:12px 0 8px;">
            L'une de ces situations vous parle ?
        </h2>
        <p style="color:#64748b;font-size:16px;max-width:560px;margin:0 auto;">
            ClientBoost AI a été conçu pour éliminer chacune d'elles.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for i, p in enumerate(PROBLEMS):
        with [c1, c2, c3, c4][i % 4]:
            st.markdown(f"""
            <div class="{p['css']}" style="min-height:160px;margin-bottom:12px;">
                <div style="margin-bottom:10px;">{p['icon_svg']}</div>
                <div style="font-size:15px;font-weight:800;margin-bottom:6px;">{p['title']}</div>
                <div style="font-size:12px;opacity:0.85;line-height:1.4;font-style:italic;">"{p['hook']}"</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Découvrir la solution →", key=f"land_{p['id']}", use_container_width=True):
                st.session_state.selected_problem = p
                go("problem_detail")

    st.write("")

    # TÉMOIGNAGES
    st.markdown("""
    <div style="text-align:center;margin:60px 0 32px;">
        <span style="background:#ffedd5;color:#c2410c;border-radius:999px;padding:4px 16px;font-size:12px;font-weight:700;">PREUVES SOCIALES</span>
        <h2 style="font-size:34px;font-weight:900;color:#0f172a;margin:12px 0 8px;">Ils ont transformé leur prospection</h2>
    </div>
    """, unsafe_allow_html=True)
    tc1, tc2, tc3 = st.columns(3)
    for i, (col, t) in enumerate(zip([tc1,tc2,tc3,tc1,tc2,tc3], TESTIMONIALS)):
        with col:
            st.markdown(f"""
            <div class="testimonial-card" style="margin-bottom:16px;">
                <div style="margin-bottom:10px;">{STAR_SVG}</div>
                <div style="font-size:13px;color:#374151;line-height:1.6;margin-bottom:14px;font-style:italic;">"{t['text']}"</div>
                <div style="background:#f0fdf4;border-radius:8px;padding:6px 12px;margin-bottom:14px;">
                    <span style="font-size:12px;font-weight:700;color:#15803d;">
                        <svg style="vertical-align:middle;margin-right:4px;" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#15803d" stroke-width="2.5"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>
                        {t['result']}
                    </span>
                </div>
                <div style="display:flex;align-items:center;gap:10px;">
                    <img src="{t['photo']}" style="width:44px;height:44px;border-radius:50%;object-fit:cover;border:2px solid #e8ecf0;" onerror="this.style.display='none'">
                    <div>
                        <div style="font-size:13px;font-weight:700;color:#0f172a;">{t['name']}</div>
                        <div style="font-size:11px;color:#64748b;">{t['role']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # CTA FINAL
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0f172a,#1e1b4b);border-radius:32px;padding:64px 40px;text-align:center;margin:48px 0;">
        <div style="font-size:13px;font-weight:700;color:#a5b4fc;text-transform:uppercase;letter-spacing:2px;margin-bottom:16px;">PRÊT À PASSER À L'ACTION ?</div>
        <h2 style="font-size:44px;font-weight:900;color:white;margin:0 0 16px;line-height:1.1;">
            Commence à multiplier<br>
            <span style="background:linear-gradient(135deg,#6366f1,#a78bfa,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">
                tes revenus maintenant.
            </span>
        </h2>
        <p style="color:#94a3b8;font-size:17px;max-width:500px;margin:0 auto 32px;line-height:1.6;">
            12 000+ entrepreneurs ont déjà arrêté de prospecter à l'aveugle. Ton premier message en 60 secondes.
        </p>
    </div>
    """, unsafe_allow_html=True)

    _, cta_col, _ = st.columns([1, 2, 1])
    with cta_col:
        if st.button("Commence à multiplier tes revenus maintenant", type="primary", use_container_width=True):
            go("auth")
    st.write("")
    _, lc, _ = st.columns([1, 2, 1])
    with lc:
        if st.button("J'ai déjà un compte — Me connecter", use_container_width=True):
            st.session_state.show_register = False
            go("auth")
    st.stop()

# ═══════════════════════════════════════════════════════
# PAGE : DÉTAIL PROBLÈME
# ═══════════════════════════════════════════════════════
if st.session_state.page == "problem_detail":
    p = st.session_state.selected_problem
    if not p:
        go("landing")

    nav_header(show_back="landing", back_label="← Retour aux problèmes")

    # HERO DU PROBLÈME
    st.markdown(f"""
    <div class="{p['css']}" style="padding:48px;border-radius:28px;margin-bottom:32px;text-align:center;">
        <div style="margin-bottom:16px;display:flex;justify-content:center;">{p['icon_svg']}</div>
        <div style="font-size:12px;font-weight:700;opacity:0.7;text-transform:uppercase;letter-spacing:2px;margin-bottom:10px;">
            Le problème
        </div>
        <h1 style="font-size:42px;font-weight:900;color:white;margin:0 0 16px;line-height:1.1;">
            {p['title']}
        </h1>
        <p style="font-size:20px;color:rgba(255,255,255,0.85);font-style:italic;margin:0;">
            "{p['hook']}"
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_desc, col_solution = st.columns([1, 1])

    with col_desc:
        st.markdown(f"""
        <div style="background:white;border-radius:20px;padding:32px;border:1px solid #e8ecf0;height:100%;box-shadow:0 2px 8px rgba(0,0,0,0.06);">
            <div style="font-size:11px;font-weight:700;color:{p['color']};text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">
                LE PROBLÈME EN DETAIL
            </div>
            <p style="font-size:16px;color:#374151;line-height:1.8;margin:0 0 24px;">
                {p['desc']}
            </p>
            <div style="background:#f8fafc;border-radius:12px;padding:16px;border-left:4px solid {p['color']};">
                <div style="font-size:12px;font-weight:700;color:{p['color']};margin-bottom:6px;">
                    <svg style="vertical-align:middle;margin-right:4px;" width="14" height="14" viewBox="0 0 24 24" fill="#FBBF24"><path d="M9 21h6m-6-3h6M12 3a6 6 0 0 1 4.47 10.06c-.62.62-1.47 1.3-1.47 2.94v.5H9v-.5c0-1.64-.85-2.32-1.47-2.94A6 6 0 0 1 12 3z"/></svg>
                    CONSEIL EXPERT
                </div>
                <p style="font-size:13px;color:#64748b;margin:0;line-height:1.6;">{p['tip']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_solution:
        # STATS
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#0f172a,#1e1b4b);border-radius:20px;padding:32px;margin-bottom:16px;">
            <div style="font-size:11px;font-weight:700;color:#a5b4fc;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px;">
                RÉSULTATS AVEC CLIENTBOOST
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:20px;">
                {''.join([f'''<div style="text-align:center;background:rgba(255,255,255,0.08);border-radius:12px;padding:16px;">
                    <div style="font-size:28px;font-weight:900;color:{p['color']};">{s[0]}</div>
                    <div style="font-size:11px;color:#94a3b8;margin-top:4px;line-height:1.3;">{s[1]}</div>
                </div>''' for s in p['stats']])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:white;border-radius:20px;padding:28px;border:2px solid {p['color']}30;box-shadow:0 4px 20px rgba(0,0,0,0.06);">
            <div style="font-size:11px;font-weight:700;color:{p['color']};text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">
                LA SOLUTION CLIENTBOOST
            </div>
            <p style="font-size:15px;color:#0f172a;font-weight:600;line-height:1.7;margin:0 0 16px;">
                {p['solution']}
            </p>
            <div style="display:flex;align-items:center;gap:8px;font-size:13px;color:{p['color']};font-weight:700;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="{p['color']}" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                Framework utilisé : {p['framework']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown("""
    <div style="text-align:center;margin:32px 0 16px;">
        <h3 style="font-size:24px;font-weight:800;color:#0f172a;margin:0 0 8px;">
            Prêt à résoudre ce problème ?
        </h3>
        <p style="color:#64748b;font-size:15px;margin:0;">
            Générez votre premier message en 60 secondes.
        </p>
    </div>
    """, unsafe_allow_html=True)

    _, btn_col, _ = st.columns([1, 2, 1])
    with btn_col:
        if st.button(f"Résoudre — {p['title']}", type="primary", use_container_width=True):
            # Si pas connecté → auth → paiement → générateur
            if not st.session_state.authenticated:
                st.session_state.show_register = True
                go("auth")
            else:
                go("generator")

    st.stop()

# ═══════════════════════════════════════════════════════
# PAGE : AUTH
# ═══════════════════════════════════════════════════════
if not st.session_state.authenticated:
    nav_header(show_back="landing", back_label="← Retour à l'accueil")

    st.markdown("""
    <div style="text-align:center;padding:20px 0 32px;">
        <div style="font-size:44px;font-weight:900;background:linear-gradient(135deg,#6366f1,#8b5cf6,#ec4899);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;">ClientBoost AI</div>
        <p style="color:#64748b;font-size:16px;margin-top:8px;">Le générateur qui résout vos 7 problèmes de vente.</p>
    </div>
    """, unsafe_allow_html=True)

    _, col_form, _ = st.columns([1, 1.2, 1])
    with col_form:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)

        if not st.session_state.show_register:
            st.markdown("<h3 style='color:#0f172a;margin-top:0;text-align:center;'>Connexion</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#64748b;text-align:center;font-size:14px;margin-bottom:24px;'>Bon retour parmi nous !</p>", unsafe_allow_html=True)
            email_in = st.text_input("Email", placeholder="vous@exemple.com", key="login_email")
            pwd_in = st.text_input("Mot de passe", type="password", placeholder="••••••••", key="login_pwd")
            if st.button("Se connecter", type="primary", use_container_width=True):
                if email_in and pwd_in:
                    st.session_state.authenticated = True
                    st.session_state.user_name = email_in.split("@")[0].capitalize()
                    st.session_state.user_email = email_in
                    st.session_state.subscribed = True
                    go("dashboard")
                else:
                    st.error("Veuillez remplir tous les champs.")
            st.markdown("<hr style='margin:20px 0;border-color:#f1f5f9;'>", unsafe_allow_html=True)
            if st.button("Pas encore de compte ? S'inscrire →", use_container_width=True):
                st.session_state.show_register = True
                st.rerun()
        else:
            st.markdown("<h3 style='color:#0f172a;margin-top:0;text-align:center;'>Créer un compte</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#64748b;text-align:center;font-size:14px;margin-bottom:24px;'>Gratuit. Sans carte bancaire pour commencer.</p>", unsafe_allow_html=True)
            name_in = st.text_input("Prénom", placeholder="Votre prénom", key="reg_name")
            email_in2 = st.text_input("Email", placeholder="vous@exemple.com", key="reg_email")
            pwd_in2 = st.text_input("Mot de passe", type="password", placeholder="Minimum 8 caractères", key="reg_pwd")
            if st.button("Créer mon compte", type="primary", use_container_width=True):
                if name_in and email_in2 and pwd_in2:
                    st.session_state.pending_name = name_in
                    st.session_state.pending_email = email_in2
                    st.session_state.authenticated = True
                    st.session_state.user_name = name_in.capitalize()
                    st.session_state.user_email = email_in2
                    st.session_state.join_date = datetime.now().strftime("%d/%m/%Y")
                    st.session_state.subscribed = True
                    go("welcome")
                else:
                    st.error("Veuillez remplir tous les champs.")
            st.markdown("<hr style='margin:20px 0;border-color:#f1f5f9;'>", unsafe_allow_html=True)
            if st.button("← Déjà un compte ? Se connecter", use_container_width=True):
                st.session_state.show_register = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ═══════════════════════════════════════════════════════
# PAGE : PRICING / PAIEMENT (OBLIGATOIRE)
# ═══════════════════════════════════════════════════════
if st.session_state.page == "pricing":
    nav_header()

    st.markdown(f"""
    <div style="text-align:center;margin-bottom:40px;">
        <div style="background:#fef9c3;color:#a16207;border-radius:999px;padding:6px 20px;font-size:13px;font-weight:700;display:inline-block;margin-bottom:16px;">
            Bonjour {st.session_state.user_name} — Choisissez votre plan pour accéder au générateur
        </div>
        <h2 style="font-size:36px;font-weight:900;color:#0f172a;margin:0 0 8px;">
            Un plan. Des résultats immédiats.
        </h2>
        <p style="color:#64748b;font-size:16px;margin:0;">Accès immédiat dès votre souscription. Annulable à tout moment.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    for col, plan in zip([c1, c2, c3], PLANS):
        with col:
            pop = '<span style="background:#6366f1;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;display:inline-block;margin-bottom:10px;">POPULAIRE</span>' if plan["popular"] else ""
            border = "border:2px solid #6366f1;" if plan["popular"] else "border:2px solid #e8ecf0;"
            st.markdown(f"""
            <div class="price-card" style="{border}padding:32px 24px;margin-bottom:12px;">
                <div style="font-size:15px;font-weight:700;color:#64748b;margin-bottom:8px;">{plan['name']}</div>
                {pop}
                <div class="price-amount">{plan['price']}</div>
                <div style="font-size:14px;color:#64748b;margin-bottom:20px;">{plan['period']}</div>
                <hr style="border-color:#f1f5f9;margin:16px 0;">
                {''.join(f'<div class="feature-item" style="color:{"#374151" if f.startswith("✔") else "#cbd5e1"};">{f}</div>' for f in plan['features'])}
            </div>
            """, unsafe_allow_html=True)
            if st.button(plan["cta"], key=f"select_plan_{plan['name']}", use_container_width=True, type="primary" if plan["popular"] else "secondary"):
                st.session_state.current_plan = plan["name"]
                go("payment")

    st.stop()

# ═══════════════════════════════════════════════════════
# PAGE : PAIEMENT
# ═══════════════════════════════════════════════════════
if st.session_state.page == "payment":
    nav_header(show_back="pricing", back_label="← Changer de plan")

    plan_obj = next((p for p in PLANS if p["name"] == st.session_state.current_plan), PLANS[1])

    st.markdown(f"""
    <div style="max-width:560px;margin:0 auto;">
        <div style="text-align:center;margin-bottom:32px;">
            <div style="background:#f0fdf4;color:#15803d;border-radius:999px;padding:6px 20px;font-size:13px;font-weight:700;display:inline-block;margin-bottom:12px;">
                Plan sélectionné : {plan_obj['name']} — {plan_obj['price']}/mois
            </div>
            <h2 style="font-size:30px;font-weight:900;color:#0f172a;margin:0 0 8px;">Finaliser votre abonnement</h2>
            <p style="color:#64748b;font-size:14px;margin:0;">Paiement 100% sécurisé. Annulable à tout moment.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, pay_col, _ = st.columns([1, 2, 1])
    with pay_col:
        st.markdown("""
        <div style="background:white;border-radius:20px;padding:32px;border:2px solid #6366f1;box-shadow:0 12px 40px rgba(99,102,241,0.15);">
            <div style="font-size:14px;font-weight:700;color:#0f172a;margin-bottom:20px;">
                <svg style="vertical-align:middle;margin-right:6px;" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#6366f1" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>
                Informations de paiement
            </div>
        </div>
        """, unsafe_allow_html=True)
        card_name = st.text_input("Nom sur la carte", placeholder="Jean Dupont")
        card_num = st.text_input("Numéro de carte", placeholder="4242 4242 4242 4242")
        cc1, cc2 = st.columns(2)
        with cc1:
            card_exp = st.text_input("Expiration", placeholder="MM/AA")
        with cc2:
            card_cvv = st.text_input("CVV", placeholder="123", type="password")

        st.markdown(f"""
        <div style="background:#f5f3ff;border-radius:12px;padding:14px;margin:12px 0;text-align:center;">
            <div style="font-size:20px;font-weight:900;color:#6366f1;">{plan_obj['price']}<span style="font-size:14px;font-weight:500;color:#64748b;">/mois</span></div>
            <div style="font-size:12px;color:#64748b;margin-top:4px;">Plan {plan_obj['name']} • Renouvelé le 28 de chaque mois</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Confirmer et accéder — {plan_obj['price']}/mois", type="primary", use_container_width=True):
            with st.spinner("Traitement du paiement..."):
                time.sleep(1.5)
            st.session_state.subscribed = True
            st.session_state.join_date = datetime.now().strftime("%d/%m/%Y")
            go("welcome")

    st.stop()

# ═══════════════════════════════════════════════════════
# PAGE : BIENVENUE (après paiement)
# ═══════════════════════════════════════════════════════
if st.session_state.page == "welcome":
    nav_header()
    renewal = (datetime.now() + timedelta(days=30)).replace(day=28).strftime("%d/%m/%Y")
    plan_obj = next((p for p in PLANS if p["name"] == st.session_state.current_plan), PLANS[1])

    _, wc, _ = st.columns([1, 2, 1])
    with wc:
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#0f172a,#1e1b4b);border-radius:24px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,0.3);">
            <div style="background:linear-gradient(135deg,#6366f1,#8b5cf6);padding:40px;text-align:center;">
                <svg style="margin-bottom:12px;" width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5">
                    <path d="M5.8 11.3L2 22l10.7-3.79"/><path d="M4 3h.01"/><path d="M22 8h.01"/><path d="M15 2h.01"/>
                    <path d="M22 20h.01"/><path d="m22 2-2.24.75a2.9 2.9 0 0 0-1.96 3.12c.1.86-.57 1.63-1.45 1.63h-.38c-.86 0-1.6.6-1.76 1.44L14 10"/>
                </svg>
                <h2 style="color:white;font-size:26px;font-weight:800;margin:0 0 6px;">
                    Bienvenue, {st.session_state.user_name} !
                </h2>
                <p style="color:rgba(255,255,255,0.8);font-size:14px;margin:0;">
                    Plan {st.session_state.current_plan} activé avec succès
                </p>
            </div>
            <div style="padding:32px;">
                <div style="background:rgba(255,255,255,0.06);border-radius:12px;padding:18px;margin-bottom:16px;">
                    <div style="font-size:12px;color:#94a3b8;font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;">
                        Email de bienvenue envoyé à {st.session_state.user_email}
                    </div>
                    <div style="font-size:14px;font-weight:700;color:white;margin-bottom:6px;">
                        Objet : {EMAIL_WELCOME['subject']}
                    </div>
                    <div style="font-size:12px;color:#94a3b8;line-height:1.6;">
                        {EMAIL_WELCOME['body'].format(name=st.session_state.user_name)[:300]}...
                    </div>
                </div>
                <div style="background:rgba(99,102,241,0.15);border-radius:12px;padding:16px;margin-bottom:16px;border:1px solid rgba(99,102,241,0.3);">
                    <div style="font-size:13px;color:white;margin-bottom:4px;">
                        Plan <strong>{st.session_state.current_plan}</strong> — {plan_obj['price']}/mois
                    </div>
                    <div style="font-size:12px;color:#94a3b8;">
                        Prochain renouvellement : <strong style="color:white;">{renewal}</strong>
                    </div>
                    <div style="font-size:11px;color:#64748b;margin-top:6px;">
                        Un email de rappel sera envoyé le 28 de chaque mois.
                    </div>
                </div>
                <div style="font-size:14px;color:#e2e8f0;font-weight:600;margin-bottom:10px;">Par où commencer :</div>
                <div style="display:flex;flex-direction:column;gap:8px;">
                    <div style="background:rgba(255,255,255,0.05);border-radius:10px;padding:10px 14px;font-size:13px;color:#e2e8f0;">
                        1. Allez dans le <strong>Générateur</strong>
                    </div>
                    <div style="background:rgba(255,255,255,0.05);border-radius:10px;padding:10px 14px;font-size:13px;color:#e2e8f0;">
                        2. Sélectionnez <strong>le problème de votre client</strong>
                    </div>
                    <div style="background:rgba(255,255,255,0.05);border-radius:10px;padding:10px 14px;font-size:13px;color:#e2e8f0;">
                        3. Générez votre <strong>premier message en 60 secondes</strong>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("Accéder au Dashboard", type="primary", use_container_width=True):
            go("dashboard")
    st.stop()

# ═══════════════════════════════════════════════════════
# SIDEBAR (utilisateurs connectés & abonnés)
# ═══════════════════════════════════════════════════════
with st.sidebar:
    level = get_level(st.session_state.gen_count)
    st.markdown(f"""
    <div style="padding:20px 0 10px;">
        <div style="font-size:20px;font-weight:900;color:white;margin-bottom:4px;">ClientBoost AI</div>
        <div style="background:rgba(255,255,255,0.08);border-radius:10px;padding:12px;margin-top:12px;">
            <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;">Connecté</div>
            <div style="font-size:15px;font-weight:700;color:white;">{st.session_state.user_name}</div>
            <div style="font-size:12px;color:#64748b;">{st.session_state.current_plan}</div>
        </div>
        <div style="background:rgba(99,102,241,0.15);border-radius:10px;padding:12px;margin-top:10px;text-align:center;">
            <div style="font-size:13px;font-weight:800;color:{level['color']};">{level['name']}</div>
            <div style="font-size:26px;font-weight:900;color:white;margin:4px 0;">{st.session_state.gen_count}</div>
            <div style="font-size:11px;color:#64748b;">messages générés</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    for pid, label in [("dashboard","Dashboard"),("generator","Générateur"),("history","Historique"),("emails","Emails Auto"),("subscription","Abonnement"),("settings","Paramètres")]:
        if st.button(label, key=f"nav_{pid}", use_container_width=True, type="primary" if st.session_state.page==pid else "secondary"):
            go(pid)
    st.divider()
    if st.button("Déconnexion", use_container_width=True):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()

# ═══════════════════════════════════════════════════════
# PAGE : DASHBOARD
# ═══════════════════════════════════════════════════════
if st.session_state.page == "dashboard":
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

    lvl_color = level["color"]
    lvl_name = level["name"]
    st.markdown(f"<h2 style='color:#0f172a;margin-bottom:4px;'>Bonjour, {st.session_state.user_name}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748b;margin-bottom:20px;'>Membre depuis le {st.session_state.join_date} • Plan <strong>{st.session_state.current_plan}</strong> • Niveau <strong style='color:{lvl_color};'>{lvl_name}</strong></p>", unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    for col, val, lbl, col_color in zip([m1,m2,m3,m4],
        [st.session_state.gen_count, today_count, len(st.session_state.problems_used), len(st.session_state.history)],
        ["Messages générés","Aujourd'hui","Problèmes explorés","Sauvegardés"],
        ["#6366f1","#f59e0b","#10b981","#ec4899"]):
        with col:
            st.markdown(f"""<div class="metric-box">
                <div style="font-size:32px;font-weight:900;color:{col_color};">{val}</div>
                <div style="font-size:11px;color:#64748b;font-weight:600;text-transform:uppercase;margin-top:4px;">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.write("")

    if PLOTLY_OK:
        col_g, col_l = st.columns([1, 2])
        with col_g:
            st.markdown("<h4 style='color:#0f172a;margin-bottom:8px;'>Niveau de croissance</h4>", unsafe_allow_html=True)
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=st.session_state.gen_count,
                title={"text": f"<b>{lvl_name}</b>", "font": {"size": 16}},
                number={"font": {"size": 36, "color": lvl_color}, "suffix": " msg"},
                gauge={
                    "axis": {"range": [0, max(61, st.session_state.gen_count+5)]},
                    "bar": {"color": lvl_color, "thickness": 0.3},
                    "bgcolor": "white", "borderwidth": 0,
                    "steps": [
                        {"range":[0,5],"color":"#f1f5f9"},
                        {"range":[5,15],"color":"#e0f2fe"},
                        {"range":[15,30],"color":"#ede9fe"},
                        {"range":[30,61],"color":"#fef9c3"},
                    ],
                }
            ))
            fig_gauge.update_layout(height=260, margin=dict(l=20,r=20,t=50,b=20), paper_bgcolor="white", font={"family":"Inter"})
            st.plotly_chart(fig_gauge, use_container_width=True, config={"displayModeBar":False})

            if next_level:
                remaining = next_level["min"] - st.session_state.gen_count
                st.markdown(f"""<div style="background:#f5f3ff;border-radius:12px;padding:12px;text-align:center;border:1px solid #ede9fe;">
                    <div style="font-size:11px;color:#6d28d9;font-weight:700;text-transform:uppercase;">Prochain</div>
                    <div style="font-size:15px;font-weight:800;color:#4c1d95;margin:4px 0;">{next_level['name']}</div>
                    <div style="background:#ddd6fe;border-radius:999px;height:8px;margin:8px 0;overflow:hidden;">
                        <div style="width:{progress}%;height:8px;background:linear-gradient(135deg,#6366f1,#8b5cf6);border-radius:999px;"></div>
                    </div>
                    <div style="font-size:12px;color:#7c3aed;">Plus que <strong>{remaining}</strong> message(s)</div>
                </div>""", unsafe_allow_html=True)

        with col_l:
            st.markdown("<h4 style='color:#0f172a;margin-bottom:8px;'>Activité sur 7 jours</h4>", unsafe_allow_html=True)
            days_labels, days_counts = [], []
            for i in range(6, -1, -1):
                d = datetime.now() - timedelta(days=i)
                key = d.strftime("%Y-%m-%d")
                days_labels.append(d.strftime("%a %d"))
                c = st.session_state.daily_counts.get(key, 0)
                if st.session_state.gen_count > 0 and c == 0 and i > 0:
                    c = random.randint(0, max(1, st.session_state.gen_count//5))
                days_counts.append(c)
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(x=days_labels, y=days_counts, mode="lines+markers",
                name="Messages", line=dict(color="#6366f1", width=3, shape="spline"),
                marker=dict(size=8, color="#6366f1", line=dict(color="white", width=2)),
                fill="tozeroy", fillcolor="rgba(99,102,241,0.08)"))
            fig_line.update_layout(height=260, margin=dict(l=10,r=10,t=20,b=20),
                paper_bgcolor="white", plot_bgcolor="white", font=dict(family="Inter", size=12),
                showlegend=False,
                xaxis=dict(showgrid=False, tickfont=dict(size=11, color="#64748b")),
                yaxis=dict(showgrid=True, gridcolor="#f1f5f9", tickfont=dict(size=11, color="#64748b")))
            st.plotly_chart(fig_line, use_container_width=True, config={"displayModeBar":False})

        st.write("")

        col_radar, col_donut = st.columns([3, 2])
        with col_radar:
            st.markdown("<h4 style='color:#0f172a;margin-bottom:8px;'>Couverture des 7 problèmes</h4>", unsafe_allow_html=True)
            pnames = [p["title"] for p in PROBLEMS]
            pvals = [st.session_state.problems_used.get(p["id"], 0) for p in PROBLEMS]
            fig_radar = go.Figure(go.Scatterpolar(
                r=pvals+[pvals[0]], theta=pnames+[pnames[0]],
                fill="toself", fillcolor="rgba(99,102,241,0.15)",
                line=dict(color="#6366f1", width=2), marker=dict(size=6, color="#6366f1")))
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, max(max(pvals),1)+1], tickfont=dict(size=9, color="#94a3b8"), gridcolor="#e2e8f0"),
                    angularaxis=dict(tickfont=dict(size=10, color="#374151"), gridcolor="#e8ecf0"),
                    bgcolor="white"),
                height=280, margin=dict(l=30,r=30,t=20,b=20),
                paper_bgcolor="white", showlegend=False, font=dict(family="Inter"))
            st.plotly_chart(fig_radar, use_container_width=True, config={"displayModeBar":False})

        with col_donut:
            st.markdown("<h4 style='color:#0f172a;margin-bottom:8px;'>Répartition</h4>", unsafe_allow_html=True)
            dvals = [max(st.session_state.problems_used.get(p["id"],0),0) for p in PROBLEMS]
            dcolors = [p["color"] for p in PROBLEMS] if sum(dvals)>0 else ["#e2e8f0"]*7
            if sum(dvals)==0: dvals = [1]*7
            fig_donut = go.Figure(go.Pie(
                labels=[p["title"] for p in PROBLEMS], values=dvals, hole=0.55,
                marker=dict(colors=dcolors, line=dict(color="white", width=2)),
                textinfo="none",
                hovertemplate="<b>%{label}</b><br>%{value} msg<extra></extra>"))
            total_real = sum(st.session_state.problems_used.values())
            fig_donut.add_annotation(text=f"<b>{total_real}</b><br>msg", x=0.5, y=0.5, showarrow=False, font=dict(size=16, color="#0f172a", family="Inter"))
            fig_donut.update_layout(height=280, margin=dict(l=10,r=10,t=20,b=20), paper_bgcolor="white", showlegend=False, font=dict(family="Inter"))
            st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar":False})

        st.write("")
        st.markdown("<h4 style='color:#0f172a;margin-bottom:8px;'>Performance par problème</h4>", unsafe_allow_html=True)
        fig_bar = go.Figure(go.Bar(
            y=[p["title"] for p in PROBLEMS],
            x=[st.session_state.problems_used.get(p["id"],0) for p in PROBLEMS],
            orientation="h",
            marker=dict(color=[p["color"] for p in PROBLEMS], line=dict(color="white", width=1)),
            text=[f"{st.session_state.problems_used.get(p['id'],0)} msg" for p in PROBLEMS],
            textposition="outside", textfont=dict(size=11, color="#64748b")))
        fig_bar.update_layout(height=260, margin=dict(l=10,r=60,t=10,b=20),
            paper_bgcolor="white", plot_bgcolor="white", font=dict(family="Inter", size=12),
            xaxis=dict(showgrid=True, gridcolor="#f1f5f9", zeroline=False),
            yaxis=dict(showgrid=False, tickfont=dict(size=11, color="#374151")), showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar":False})

    else:
        st.info("Installez plotly pour les graphiques : `pip install plotly`")

    st.write("")
    # Badges
    st.markdown("<h4 style='color:#0f172a;margin-bottom:12px;'>Badges</h4>", unsafe_allow_html=True)
    badge_cols = st.columns(4)
    badges_all = [
        (1,"Premier message","#dbeafe","#1d4ed8","Générer 1 message",st.session_state.gen_count>=1),
        (5,"En feu !","#ffedd5","#c2410c","5 messages",st.session_state.gen_count>=5),
        (10,"Prospecteur","#fef9c3","#a16207","10 messages",st.session_state.gen_count>=10),
        (25,"Closer","#f0fdf4","#15803d","25 messages",st.session_state.gen_count>=25),
        (50,"Expert","#f5f3ff","#6d28d9","50 messages",st.session_state.gen_count>=50),
        (3,"Polyvalent","#fef2f2","#b91c1c","3 problèmes",len(st.session_state.problems_used)>=3),
        (7,"Maitre des 7","#fff7ed","#c2410c","7 problèmes",len(st.session_state.problems_used)>=7),
        (5,"Archiviste","#f0fdf4","#166534","5 sauvegardés",len(st.session_state.history)>=5),
    ]
    for i, (thresh, name, bg, color, req, unlocked) in enumerate(badges_all):
        with badge_cols[i%4]:
            opacity = "1" if unlocked else "0.3"
            st.markdown(f"""<div style="background:{bg};border-radius:12px;padding:12px;margin-bottom:8px;opacity:{opacity};text-align:center;">
                <div style="font-size:12px;font-weight:700;color:{color};">{name}</div>
                <div style="font-size:10px;color:#94a3b8;margin-top:2px;">{'Débloqué' if unlocked else req}</div>
            </div>""", unsafe_allow_html=True)

    st.write("")
    _, cta_c, _ = st.columns([1,2,1])
    with cta_c:
        if st.button("Générer un message", type="primary", use_container_width=True):
            go("generator")

# ═══════════════════════════════════════════════════════
# PAGE : GÉNÉRATEUR
# ═══════════════════════════════════════════════════════
elif st.session_state.page == "generator":
    st.markdown("<h2 style='color:#0f172a;margin-bottom:4px;'>Générateur de messages</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;margin-bottom:28px;'>Choisissez un problème → configurez → obtenez votre message.</p>", unsafe_allow_html=True)

    st.markdown("<h4 style='color:#0f172a;margin-bottom:12px;'>Étape 1 — Quel est le problème de votre prospect ?</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;font-size:13px;margin-bottom:16px;'>Cliquez sur un problème pour voir sa description complète avant de générer.</p>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for i, p in enumerate(PROBLEMS):
        with [c1,c2,c3,c4][i%4]:
            is_sel = st.session_state.selected_problem and st.session_state.selected_problem["id"] == p["id"]
            extra = " prob-selected" if is_sel else ""
            st.markdown(f"""<div class="{p['css']}{extra}" style="min-height:140px;margin-bottom:8px;">
                <div style="margin-bottom:8px;">{p['icon_svg']}</div>
                <div style="font-size:13px;font-weight:800;margin-bottom:4px;">{p['title']}</div>
                <div style="font-size:11px;opacity:0.85;line-height:1.4;">{p['hook']}</div>
            </div>""", unsafe_allow_html=True)
            if st.button("Voir + Générer" if not is_sel else "Sélectionné", key=f"gen_prob_{p['id']}", use_container_width=True, type="primary" if is_sel else "secondary"):
                st.session_state.selected_problem = p
                st.session_state.last_generated = ""
                go("problem_generator")

# ═══════════════════════════════════════════════════════
# PAGE : PROBLÈME + FORMULAIRE (page dédiée)
# ═══════════════════════════════════════════════════════
elif st.session_state.page == "problem_generator":
    p = st.session_state.selected_problem
    if not p:
        go("generator")

    if st.button("← Changer de problème", key="back_gen"):
        go("generator")

    # Header du workspace
    st.markdown(f"""
    <div class="{p['ws']}" style="margin-bottom:24px;">
        <div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;">
            <div class="{p['css']}" style="padding:14px;border-radius:14px;display:inline-flex;">{p['icon_svg']}</div>
            <div>
                <div style="font-size:11px;font-weight:700;color:{p['color']};text-transform:uppercase;letter-spacing:1px;">Workspace — Framework {p['framework']}</div>
                <div style="font-size:20px;font-weight:800;color:#0f172a;">{p['title']}</div>
                <div style="font-size:14px;color:#64748b;font-style:italic;">"{p['hook']}"</div>
            </div>
        </div>
        <div style="background:rgba(255,255,255,0.8);border-radius:12px;padding:14px;margin-bottom:10px;">
            <p style="font-size:13px;color:#374151;margin:0 0 8px;line-height:1.6;">{p['desc']}</p>
            <p style="font-size:13px;font-weight:700;color:{p['color']};margin:0;">Solution : {p['solution']}</p>
        </div>
        <div style="background:rgba(255,255,255,0.5);border-radius:10px;padding:10px;">
            <span style="font-size:12px;color:#64748b;">Conseil : {p['tip']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='color:#0f172a;'>Configurez votre contexte</h4>", unsafe_allow_html=True)
    ca, cb = st.columns(2)
    with ca:
        v1 = st.text_input(p['fields'][0], placeholder=p['placeholders'][0], key="gi_v1")
        v2 = st.text_input(p['fields'][1], placeholder=p['placeholders'][1], key="gi_v2")
    with cb:
        v3 = st.text_area(p['fields'][2], placeholder=p['placeholders'][2], height=110, key="gi_v3")
        tone = st.selectbox("Style du message", ["Percutant","Professionnel","Storytelling"], key="gi_tone")

    st.write("")
    if st.button(f"Générer mon message — {p['title']}", type="primary", use_container_width=True):
        if v1 and v2 and v3:
            with st.spinner(f"Application du framework {p['framework']}..."):
                time.sleep(1.5)
            result = generate_message(p["id"], v1, v2, v3, tone)
            st.session_state.last_generated = result
            st.session_state.gen_count += 1
            today = datetime.now().strftime("%Y-%m-%d")
            st.session_state.daily_counts[today] = st.session_state.daily_counts.get(today,0)+1
            st.session_state.problems_used[p["id"]] = st.session_state.problems_used.get(p["id"],0)+1
            st.session_state.gen_inputs = {"secteur":v1,"persona":v2,"context":v3,"tone":tone}
            go("result")
        else:
            st.warning("Veuillez remplir tous les champs.")

# ═══════════════════════════════════════════════════════
# PAGE : RÉSULTAT (page dédiée)
# ═══════════════════════════════════════════════════════
elif st.session_state.page == "result":
    p = st.session_state.selected_problem
    if not st.session_state.last_generated:
        go("generator")

    level = get_level(st.session_state.gen_count)

    if st.button("← Modifier le message", key="back_result"):
        go("problem_generator")

    # Header résultat
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0f172a,#1e1b4b);border-radius:20px;padding:28px;margin-bottom:24px;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
            <div>
                <div style="font-size:12px;color:#a5b4fc;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">
                    Message généré avec le framework {p['framework'] if p else 'AIDA'}
                </div>
                <div style="font-size:20px;font-weight:800;color:white;">Votre message est prêt</div>
                <div style="font-size:13px;color:#94a3b8;margin-top:4px;">
                    Copiez, personnalisez [Prénom], envoyez.
                </div>
            </div>
            <div style="background:rgba(99,102,241,0.2);border-radius:12px;padding:12px 20px;text-align:center;">
                <div style="font-size:11px;color:#a5b4fc;font-weight:700;text-transform:uppercase;">Votre niveau</div>
                <div style="font-size:18px;font-weight:900;color:{level['color']};">{level['name']}</div>
                <div style="font-size:22px;font-weight:900;color:white;">{st.session_state.gen_count}</div>
                <div style="font-size:11px;color:#64748b;">messages générés</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Le message
    st.text_area("", value=st.session_state.last_generated, height=340, key="result_output")

    # Actions
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("Sauvegarder dans l'historique", use_container_width=True):
            st.session_state.history.insert(0, {
                "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "problem": p["title"] if p else "–",
                "problem_id": p["id"] if p else "",
                "color": p["color"] if p else "#6366f1",
                "content": st.session_state.last_generated
            })
            st.success("Sauvegardé !")
    with col_b:
        if st.button("Générer une variante", type="primary", use_container_width=True):
            inp = st.session_state.gen_inputs
            tones = ["Percutant","Professionnel","Storytelling"]
            new_tone = random.choice([t for t in tones if t != inp.get("tone","Percutant")])
            result = generate_message(p["id"], inp.get("secteur",""), inp.get("persona",""), inp.get("context",""), new_tone)
            st.session_state.last_generated = result
            st.session_state.gen_count += 1
            today = datetime.now().strftime("%Y-%m-%d")
            st.session_state.daily_counts[today] = st.session_state.daily_counts.get(today,0)+1
            st.rerun()
    with col_c:
        if st.button("Nouveau problème", use_container_width=True):
            st.session_state.selected_problem = None
            st.session_state.last_generated = ""
            go("generator")

    # Conseil sur le résultat
    if p:
        st.markdown(f"""
        <div style="background:{p['color']}12;border-radius:14px;padding:18px;margin-top:16px;border:1px solid {p['color']}30;">
            <div style="font-size:12px;font-weight:700;color:{p['color']};text-transform:uppercase;margin-bottom:6px;">
                Conseil pour ce message
            </div>
            <p style="font-size:13px;color:#374151;margin:0;line-height:1.6;">{p['tip']}</p>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# PAGE : HISTORIQUE
# ═══════════════════════════════════════════════════════
elif st.session_state.page == "history":
    st.markdown("<h2 style='color:#0f172a;'>Historique</h2>", unsafe_allow_html=True)
    if not st.session_state.history:
        st.markdown("""<div class="card" style="text-align:center;padding:60px;">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5" style="margin-bottom:12px;"><path d="M22 13V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h8"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/><path d="M19 16l2 2 4-4"/></svg>
            <p style="color:#64748b;font-size:16px;margin:0;">Aucun message sauvegardé. Commencez par générer un message !</p>
        </div>""", unsafe_allow_html=True)
    else:
        ci, cc = st.columns([4,1])
        with ci: st.markdown(f"<span style='background:#dcfce7;color:#15803d;border-radius:999px;padding:4px 14px;font-size:12px;font-weight:700;'>{len(st.session_state.history)} message(s)</span>", unsafe_allow_html=True)
        with cc:
            if st.button("Tout effacer", use_container_width=True):
                st.session_state.history = []
                st.rerun()
        st.write("")
        for i, item in enumerate(st.session_state.history):
            color = item.get("color", "#6366f1")
            with st.expander(f"{item.get('problem','–')} — {item['date']}"):
                st.text_area("", value=item["content"], height=220, key=f"h_{i}")

# ═══════════════════════════════════════════════════════
# PAGE : EMAILS AUTO
# ═══════════════════════════════════════════════════════
elif st.session_state.page == "emails":
    st.markdown("<h2 style='color:#0f172a;'>Emails Automatiques</h2>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Email de bienvenue", "Email de renouvellement (28 du mois)"])
    renewal_date = (datetime.now() + timedelta(days=30)).replace(day=28).strftime("%d/%m/%Y")
    level = get_level(st.session_state.gen_count)
    plan_obj = next((p for p in PLANS if p["name"]==st.session_state.current_plan), PLANS[1])
    next_plan_obj = PLANS[min(PLANS.index(plan_obj)+1, len(PLANS)-1)]
    with tab1:
        st.markdown(f"""<div class="email-preview">
            <div class="email-header"><div style="font-size:20px;font-weight:800;">ClientBoost AI</div></div>
            <strong>Objet : {EMAIL_WELCOME['subject']}</strong>
            <hr style="border-color:#e8ecf0;margin:16px 0;">
            <pre style="font-family:'Inter',sans-serif;white-space:pre-wrap;font-size:14px;color:#374151;line-height:1.7;">{EMAIL_WELCOME['body'].format(name=st.session_state.user_name)}</pre>
        </div>""", unsafe_allow_html=True)
    with tab2:
        st.markdown(f"""<div class="email-preview">
            <div class="email-header" style="background:linear-gradient(135deg,#f97316,#ea580c);"><div style="font-size:20px;font-weight:800;">ClientBoost AI</div></div>
            <strong>Objet : {EMAIL_RENEWAL['subject']}</strong>
            <hr style="border-color:#e8ecf0;margin:16px 0;">
            <pre style="font-family:'Inter',sans-serif;white-space:pre-wrap;font-size:14px;color:#374151;line-height:1.7;">{EMAIL_RENEWAL['body'].format(
                name=st.session_state.user_name, plan=st.session_state.current_plan,
                renewal_date=renewal_date, msg_count=st.session_state.gen_count,
                problems_used=len(st.session_state.problems_used), level=level['name'],
                price=plan_obj['price']+'/mois', next_plan=next_plan_obj['name'],
                next_feature='générations illimitées' if next_plan_obj['name']=='Pro' else '5 sièges')}</pre>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# PAGE : ABONNEMENT
# ═══════════════════════════════════════════════════════
elif st.session_state.page == "subscription":
    st.markdown("<h2 style='color:#0f172a;'>Tarifs & Abonnement</h2>", unsafe_allow_html=True)
    plan_obj = next((p for p in PLANS if p["name"]==st.session_state.current_plan), PLANS[1])
    renewal = (datetime.now() + timedelta(days=30)).replace(day=28).strftime("%d/%m/%Y")
    st.markdown(f"""<div style="background:#f0fdf4;border-radius:12px;padding:16px;margin-bottom:24px;border-left:4px solid #22c55e;">
        <strong style="color:#15803d;">Plan actuel : {st.session_state.current_plan} — {plan_obj['price']}/mois</strong>
        <p style="color:#64748b;font-size:13px;margin:4px 0 0;">Renouvellement le <strong>{renewal}</strong> • Rappel email le 28 de chaque mois.</p>
    </div>""", unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    for col,plan in zip([c1,c2,c3],PLANS):
        with col:
            is_cur = plan["name"]==st.session_state.current_plan
            border = "border:2px solid #22c55e;" if is_cur else ("border:2px solid #6366f1;" if plan["popular"] else "border:2px solid #e8ecf0;")
            cur_badge = '<span style="background:#22c55e;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;display:inline-block;margin-bottom:8px;">PLAN ACTUEL</span>' if is_cur else ""
            pop_badge = '<span style="background:#6366f1;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;display:inline-block;margin-bottom:8px;">POPULAIRE</span>' if plan["popular"] and not is_cur else ""
            st.markdown(f"""<div class="price-card" style="{border}">
                <div style="font-size:15px;font-weight:700;color:#64748b;margin-bottom:8px;">{plan['name']}</div>
                {cur_badge}{pop_badge}
                <div class="price-amount">{plan['price']}</div>
                <div style="font-size:14px;color:#64748b;margin-bottom:16px;">{plan['period']}</div>
                <hr style="border-color:#f1f5f9;margin:12px 0;">
                {''.join(f'<div class="feature-item" style="color:{"#374151" if f.startswith("✔") else "#cbd5e1"};">{f}</div>' for f in plan['features'])}
            </div>""", unsafe_allow_html=True)
            if not is_cur:
                if st.button(f"Passer au {plan['name']}", key=f"switch_{plan['name']}", use_container_width=True, type="primary" if plan["popular"] else "secondary"):
                    st.session_state.current_plan = plan["name"]
                    st.success(f"Abonnement mis à jour : {plan['name']} — {plan['price']}/mois")

# ═══════════════════════════════════════════════════════
# PAGE : PARAMÈTRES
# ═══════════════════════════════════════════════════════
elif st.session_state.page == "settings":
    st.markdown("<h2 style='color:#0f172a;'>Paramètres</h2>", unsafe_allow_html=True)
    st.write("")
    st.markdown("""<div class="card"><h4 style="color:#0f172a;margin-top:0;">Profil</h4>""", unsafe_allow_html=True)
    new_name = st.text_input("Prénom", value=st.session_state.user_name)
    st.markdown(f"<p style='color:#64748b;font-size:13px;'>Email : {st.session_state.user_email}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""<div class="card"><h4 style="color:#0f172a;margin-top:0;">API Anthropic (optionnel)</h4>""", unsafe_allow_html=True)
    st.text_input("Clé API", type="password", placeholder="sk-ant-...")
    st.markdown("<p style='font-size:13px;color:#64748b;'>Ajoutez votre clé pour utiliser le vrai moteur Claude AI. <a href='https://console.anthropic.com' target='_blank'>Obtenir une clé →</a></p></div>", unsafe_allow_html=True)
    level = get_level(st.session_state.gen_count)
    renewal = (datetime.now() + timedelta(days=30)).replace(day=28).strftime("%d/%m/%Y")
    st.markdown(f"""<div class="card"><h4 style="color:#0f172a;margin-top:0;">Votre compte</h4>
        <p style="color:#475569;">Membre depuis : <strong>{st.session_state.join_date}</strong></p>
        <p style="color:#475569;">Plan : <strong>{st.session_state.current_plan}</strong></p>
        <p style="color:#475569;">Renouvellement : <strong>{renewal}</strong></p>
        <p style="color:#475569;">Niveau : <strong>{level['name']}</strong></p>
        <p style="color:#475569;">Messages : <strong>{st.session_state.gen_count}</strong></p>
        <p style="color:#475569;">Problèmes : <strong>{len(st.session_state.problems_used)} / 7</strong></p>
    </div>""", unsafe_allow_html=True)
    if st.button("Enregistrer", type="primary"):
        st.session_state.user_name = new_name
        st.success("Paramètres enregistrés !")
