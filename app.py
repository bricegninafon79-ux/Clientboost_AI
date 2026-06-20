import streamlit as st
import time
import random
from datetime import datetime, timedelta
import json

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(page_title="ClientBoost AI", page_icon="🚀", layout="wide", initial_sidebar_state="expanded")

# ─────────────────────────────────────────────
# CSS GLOBAL
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.main .block-container { padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1150px; }

section[data-testid="stSidebar"] { background: linear-gradient(180deg, #0a0f1e 0%, #0f172a 60%, #1a1f35 100%) !important; border-right: 1px solid rgba(255,255,255,0.06); }
section[data-testid="stSidebar"] * { color: #e2e8f0 !important; }

.stButton > button[kind="primary"] { background: linear-gradient(135deg,#6366f1,#8b5cf6) !important; border:none !important; border-radius:10px !important; font-weight:700 !important; color:white !important; transition: all 0.2s !important; }
.stButton > button[kind="primary"]:hover { transform:translateY(-2px) !important; box-shadow:0 8px 25px rgba(99,102,241,0.4) !important; }
.stTextInput > div > div > input, .stTextArea > div > div > textarea { border-radius:10px !important; border:1.5px solid #e2e8f0 !important; font-size:14px !important; }
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus { border-color:#6366f1 !important; box-shadow:0 0 0 3px rgba(99,102,241,0.1) !important; }
.stSelectbox > div > div { border-radius:10px !important; border:1.5px solid #e2e8f0 !important; }

footer { visibility:hidden; } #MainMenu { visibility:hidden; }

/* CARDS */
.card { background:white; border-radius:20px; padding:28px; border:1px solid #e8ecf0; box-shadow:0 2px 8px rgba(0,0,0,0.06); margin-bottom:20px; }
.card-dark { background:#0f172a; border-radius:20px; padding:28px; margin-bottom:20px; }
.badge { display:inline-block; padding:4px 14px; border-radius:999px; font-size:12px; font-weight:700; background:#ede9fe; color:#6d28d9; margin-bottom:8px; }
.badge-green { background:#dcfce7; color:#15803d; }
.badge-orange { background:#ffedd5; color:#c2410c; }
.badge-blue { background:#dbeafe; color:#1d4ed8; }

/* METRIC BOXES */
.metric-box { background:white; border-radius:16px; padding:22px; text-align:center; border:1px solid #e8ecf0; box-shadow:0 2px 8px rgba(0,0,0,0.05); transition: all 0.2s; }
.metric-box:hover { transform:translateY(-3px); box-shadow:0 8px 24px rgba(0,0,0,0.1); }
.metric-num { font-size:36px; font-weight:900; }
.metric-label { font-size:12px; color:#64748b; margin-top:4px; font-weight:600; text-transform:uppercase; letter-spacing:0.5px; }
.metric-change { font-size:12px; margin-top:6px; font-weight:600; }

/* PROGRESS BAR */
.prog-wrap { background:#f1f5f9; border-radius:999px; height:10px; margin:8px 0; overflow:hidden; }
.prog-fill { height:10px; border-radius:999px; }

/* LEVEL BADGE */
.level-badge { display:inline-flex; align-items:center; gap:8px; background:linear-gradient(135deg,#6366f1,#8b5cf6); color:white; border-radius:12px; padding:10px 18px; font-weight:800; font-size:16px; }

/* HISTORY ITEM */
.hist-item { background:#f8fafc; border-radius:12px; padding:16px 20px; margin-bottom:10px; border-left:4px solid #6366f1; }
.hist-meta { font-size:12px; color:#64748b; margin-bottom:4px; }

/* AUTH FORM */
.auth-container { max-width:460px; margin:0 auto; background:white; border-radius:24px; padding:40px; border:1px solid #e8ecf0; box-shadow:0 8px 40px rgba(0,0,0,0.08); }

/* PROBLEM CARDS (chacune unique) */
.prob-time { background:linear-gradient(135deg,#1e3a5f,#2563eb); border-radius:20px; padding:24px; color:white; cursor:pointer; transition:all 0.3s; border:3px solid transparent; }
.prob-money { background:linear-gradient(135deg,#064e3b,#059669); border-radius:20px; padding:24px; color:white; cursor:pointer; transition:all 0.3s; border:3px solid transparent; }
.prob-skill { background:linear-gradient(135deg,#451a03,#d97706); border-radius:20px; padding:24px; color:white; cursor:pointer; transition:all 0.3s; border:3px solid transparent; }
.prob-growth { background:linear-gradient(135deg,#0f172a,#6366f1); border-radius:20px; padding:24px; color:white; cursor:pointer; transition:all 0.3s; border:3px solid transparent; }
.prob-frustration { background:linear-gradient(135deg,#4c0519,#dc2626); border-radius:20px; padding:24px; color:white; cursor:pointer; transition:all 0.3s; border:3px solid transparent; }
.prob-risk { background:linear-gradient(135deg,#2e1065,#7c3aed); border-radius:20px; padding:24px; color:white; cursor:pointer; transition:all 0.3s; border:3px solid transparent; }
.prob-retention { background:linear-gradient(135deg,#431407,#ea580c); border-radius:20px; padding:24px; color:white; cursor:pointer; transition:all 0.3s; border:3px solid transparent; }
.prob-selected { border:3px solid white !important; box-shadow:0 0 0 3px rgba(255,255,255,0.4), 0 12px 40px rgba(0,0,0,0.3) !important; transform:translateY(-4px); }

/* GENERATOR WORKSPACE */
.workspace-time { background:linear-gradient(135deg,#eff6ff,#dbeafe); border:2px solid #3b82f6; border-radius:20px; padding:28px; }
.workspace-money { background:linear-gradient(135deg,#f0fdf4,#dcfce7); border:2px solid #22c55e; border-radius:20px; padding:28px; }
.workspace-skill { background:linear-gradient(135deg,#fffbeb,#fef3c7); border:2px solid #f59e0b; border-radius:20px; padding:28px; }
.workspace-growth { background:linear-gradient(135deg,#f5f3ff,#ede9fe); border:2px solid #8b5cf6; border-radius:20px; padding:28px; }
.workspace-frustration { background:linear-gradient(135deg,#fff1f2,#ffe4e6); border:2px solid #f43f5e; border-radius:20px; padding:28px; }
.workspace-risk { background:linear-gradient(135deg,#faf5ff,#f3e8ff); border:2px solid #a855f7; border-radius:20px; padding:28px; }
.workspace-retention { background:linear-gradient(135deg,#fff7ed,#ffedd5); border:2px solid #f97316; border-radius:20px; padding:28px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 7 PROBLÈMES — reformulés, accrocheurs, uniques
# ─────────────────────────────────────────────
PROBLEMS = [
    {
        "id": "time",
        "icon": "⏳",
        "title": "Temps qui s'évapore",
        "hook": "Vous passez 3h à rédiger ce qui devrait prendre 3 minutes.",
        "desc": "Chaque message de prospection vous prend une éternité. Résultat : vous prospectez peu, vous signez peu. Votre temps vaut trop pour être gaspillé sur du copier-coller.",
        "solution": "ClientBoost génère un message complet, personnalisé et percutant en 10 secondes chrono. Récupérez vos heures. Concentrez-vous sur les deals.",
        "color_class": "prob-time",
        "workspace_class": "workspace-time",
        "color": "#2563eb",
        "accent": "#1e40af",
        "emoji_bg": "🕐",
        "framework": "AIDA",
        "tip": "💡 Astuce : un message court (< 150 mots) obtient 2x plus de réponses qu'un long discours.",
        "fields": ["Votre secteur / produit", "Votre persona cible", "Ce qui vous prend le plus de temps"],
        "placeholders": ["Ex : Coach business, Agence web, SaaS RH", "Ex : Directeurs marketing, Freelances débordés", "Ex : Rédiger mes emails de prospection chaque matin"]
    },
    {
        "id": "money",
        "icon": "💸",
        "title": "Budget qui s'évapore",
        "hook": "Vous investissez. Vous n'encaissez pas. Quelque chose cloche.",
        "desc": "Vos pubs tournent, vos emails partent, mais les conversions ne suivent pas. Vous payez une agence qui pond des messages génériques. Stop. Le problème n'est pas votre offre — c'est le message.",
        "solution": "ClientBoost applique AIDA, PAS et le storytelling pour transformer chaque euro investi en vrai retour sur investissement. Fini les dépenses à perte.",
        "color_class": "prob-money",
        "workspace_class": "workspace-money",
        "color": "#059669",
        "accent": "#064e3b",
        "emoji_bg": "💰",
        "framework": "PAS",
        "tip": "💡 Framework PAS : Problème → Agitation → Solution. Le plus efficace pour convertir à froid.",
        "fields": ["Votre offre / produit", "Votre client idéal", "Où vous perdez de l'argent actuellement"],
        "placeholders": ["Ex : Formation en ligne, Logiciel B2B, Service de comptabilité", "Ex : TPE qui veulent croître, E-commerçants débutants", "Ex : Mes pubs Facebook ne convertissent pas"]
    },
    {
        "id": "skill",
        "icon": "🧠",
        "title": "Page blanche paralysante",
        "hook": "Vous savez ce que vous vendez. Vous ne savez pas comment le dire.",
        "desc": "Syndrome de la page blanche, accroches fades, messages qui ne donnent pas envie de répondre. Écrire pour vendre est un métier. Vous n'êtes pas obligé de le maîtriser — juste d'avoir le bon outil.",
        "solution": "ClientBoost intègre 10+ frameworks de copywriting (AIDA, PAS, FAB, storytelling) pour que chaque message soit structuré pour convaincre. Même si vous n'avez jamais écrit une ligne de vente.",
        "color_class": "prob-skill",
        "workspace_class": "workspace-skill",
        "color": "#d97706",
        "accent": "#92400e",
        "emoji_bg": "✍️",
        "framework": "FAB",
        "tip": "💡 Framework FAB : Feature → Advantage → Benefit. Traduisez les fonctionnalités en bénéfices concrets.",
        "fields": ["Votre produit / service", "Votre persona", "Votre blocage principal à l'écriture"],
        "placeholders": ["Ex : Outil de gestion de projet, Coaching carrière", "Ex : Entrepreneurs solo, Managers d'équipes", "Ex : Je ne sais pas par quoi commencer mon message"]
    },
    {
        "id": "growth",
        "icon": "📈",
        "title": "Pipeline à sec",
        "hook": "Votre offre est bonne. Votre agenda est vide. C'est urgent.",
        "desc": "Pas assez de leads, pas assez de conversations, pas assez de contrats signés. Votre tunnel de vente ressemble à un désert. La croissance ne se produit pas par hasard — elle se fabrique, avec les bons messages, au bon moment.",
        "solution": "Générez 10, 50 ou 100 messages de prospection hyper-ciblés en quelques minutes. Chaque message est adapté à la douleur exacte de votre persona. Volume + personnalisation = pipeline plein.",
        "color_class": "prob-growth",
        "workspace_class": "workspace-growth",
        "color": "#7c3aed",
        "accent": "#4c1d95",
        "emoji_bg": "🚀",
        "framework": "Storytelling",
        "tip": "💡 Storytelling : commencez par une situation que votre prospect vit, pas par votre produit.",
        "fields": ["Votre secteur", "Votre client idéal (persona)", "Quel résultat vous promettez en X jours ?"],
        "placeholders": ["Ex : Agence SEO, Consultant RH, Application mobile", "Ex : Startups en phase de croissance, PME de 10-50 salariés", "Ex : +30% de leads qualifiés en 30 jours"]
    },
    {
        "id": "frustration",
        "icon": "😤",
        "title": "Prospection que vous détestez",
        "hook": "Vous envoyez. Silence radio. Encore et encore.",
        "desc": "La prospection à froid vous épuise. Vous vous sentez intrusif, vous n'obtenez aucune réponse, et chaque relance ressemble à une humiliation. Ce n'est pas vous le problème. C'est la façon dont vous abordez vos prospects.",
        "solution": "ClientBoost crée des messages empathiques qui parlent à vos prospects — pas à leur boîte mail. Des messages qu'ils ont envie de lire. Des conversations qu'ils ont envie d'avoir. Une prospection dont vous serez fier.",
        "color_class": "prob-frustration",
        "workspace_class": "workspace-frustration",
        "color": "#dc2626",
        "accent": "#7f1d1d",
        "emoji_bg": "💬",
        "framework": "Empathy Map",
        "tip": "💡 Empathy Map : pensez à ce que votre prospect ressent, craint et désire avant d'écrire une seule ligne.",
        "fields": ["Votre produit / service", "Votre persona cible", "Pourquoi vos messages n'obtiennent pas de réponse ?"],
        "placeholders": ["Ex : Logiciel de facturation, Formation marketing digital", "Ex : Artisans indépendants, PME sans équipe marketing", "Ex : Mes messages semblent trop commerciaux ou génériques"]
    },
    {
        "id": "risk",
        "icon": "🛡️",
        "title": "Réputation en jeu",
        "hook": "Un mauvais message peut griller 100 prospects d'un coup.",
        "desc": "Vous avez peur d'envoyer un message qui fait fuir, qui paraît non professionnel, ou qui brûle définitivement votre base de contacts. Cette peur vous paralyse. Et pendant ce temps, vos concurrents prospectent.",
        "solution": "ClientBoost garantit des messages calibrés : bon ton, bonne structure, bon niveau de professionnnalisme. Prospectez à grande échelle avec la certitude de ne jamais envoyer quelque chose dont vous auriez honte.",
        "color_class": "prob-risk",
        "workspace_class": "workspace-risk",
        "color": "#7c3aed",
        "accent": "#3b0764",
        "emoji_bg": "🔐",
        "framework": "Trust Builder",
        "tip": "💡 Trust Builder : commencez par démontrer que vous comprenez leur situation avant de parler de vous.",
        "fields": ["Votre secteur / produit", "Votre persona", "Ce que vous craignez le plus d'envoyer"],
        "placeholders": ["Ex : Cabinet de conseil, Agence de communication", "Ex : Grands comptes, Décideurs C-level", "Ex : Un message trop agressif qui me fait passer pour un spammeur"]
    },
    {
        "id": "retention",
        "icon": "🔄",
        "title": "Clients qui disparaissent",
        "hook": "Acquérir un client coûte 5x plus cher que d'en garder un. Et vous les perdez.",
        "desc": "Vos clients existants ne rachètent pas. Vos anciens clients vous ont oublié. Vous n'avez aucun système de suivi ou de réengagement. Chaque client perdu, c'est du chiffre d'affaires qui s'évapore silencieusement.",
        "solution": "ClientBoost génère des séquences de relance, newsletters de réengagement et offres de suivi personnalisées. Transformez vos clients silencieux en ambassadeurs et acheteurs réguliers.",
        "color_class": "prob-retention",
        "workspace_class": "workspace-retention",
        "color": "#ea580c",
        "accent": "#7c2d12",
        "emoji_bg": "💎",
        "framework": "Lifecycle Marketing",
        "tip": "💡 Lifecycle : un client existant a 60-70% de chance d'acheter à nouveau si vous restez présent au bon moment.",
        "fields": ["Votre produit / service", "Vos clients existants (profil)", "Quand avez-vous eu de leurs nouvelles pour la dernière fois ?"],
        "placeholders": ["Ex : Service d'abonnement, Formation, Consulting", "Ex : Clients achetés il y a 3-6 mois, Anciens abonnés", "Ex : Il y a plus de 2 mois, je n'ai aucun suivi automatique"]
    }
]

# ─────────────────────────────────────────────
# GÉNÉRATEUR DE MESSAGES — sans API, vrais frameworks
# ─────────────────────────────────────────────
def generate_message(prob_id, secteur, persona, context, tone):
    templates = {
        "time": {
            "Percutant": f"""Objet : Récupérez 10h par semaine — sans embaucher

Bonjour [Prénom],

Une question directe : combien d'heures avez-vous passé cette semaine à rédiger des messages au lieu de les envoyer ?

Pour la plupart des {persona}, c'est entre 5 et 15h perdues. Chaque semaine.

Chez {secteur}, on a réglé ça avec une approche simple : {context} ne devrait pas vous coûter votre temps — ça devrait vous rapporter de l'argent.

Nos clients récupèrent en moyenne 8h par semaine dès le premier mois.

Je vous montre comment en 20 minutes. Cette semaine ?

[Votre nom]""",
            "Professionnel": f"""Objet : Optimisation de votre processus de prospection

Bonjour [Prénom],

En travaillant avec des {persona}, j'ai identifié un pattern récurrent : {context} monopolise un temps précieux qui devrait être alloué à la conversion.

{secteur} propose une solution structurée pour réduire ce temps de 80%, tout en améliorant la qualité et la personnalisation des messages.

Seriez-vous disponible pour un échange de 20 minutes cette semaine ? Je vous présente notre approche avec des résultats concrets.

Cordialement,
[Votre nom]""",
            "Storytelling": f"""Objet : "Je passais 3h par jour à rédiger des emails..."

Bonjour [Prénom],

C'est ce que m'a dit Sarah, directrice commerciale chez une startup SaaS, il y a 6 mois.

Elle gérait une équipe de {persona} qui noyait dans {context}. Résultat : prospection au ralenti, pipeline vide, moral en berne.

Aujourd'hui avec {secteur}, son équipe génère 3x plus de messages en 1/5 du temps.

Votre situation ressemble à celle de Sarah ?

Un appel de 15 minutes pour voir si on peut faire pareil pour vous ?

[Votre nom]"""
        },
        "money": {
            "Percutant": f"""Objet : Votre budget marketing a une fuite — voici où

Bonjour [Prénom],

Chaque mois, des {persona} me montrent leurs campagnes : budget investi, résultats décevants.

Le diagnostic est presque toujours le même : {context}. Le problème n'est pas le produit. C'est le message.

{secteur} applique les frameworks PAS et AIDA pour que chaque euro dépensé génère un retour mesurable. Nos clients voient en moyenne +40% de conversion dans les 30 premiers jours.

Vous continuez à perdre ou on en parle cette semaine ?

[Votre nom]""",
            "Professionnel": f"""Objet : Amélioration du ROI de vos campagnes

Bonjour [Prénom],

L'analyse de campagnes similaires à celles des {persona} révèle systématiquement le même frein : {context}.

{secteur} résout ce problème en appliquant des frameworks de copywriting éprouvés (PAS, AIDA, FAB) à chaque message, réduisant le coût d'acquisition et augmentant le taux de conversion.

Je serais ravi de vous présenter des cas concrets lors d'un échange de 20 minutes.

Cordialement,
[Votre nom]""",
            "Storytelling": f"""Objet : Il a réduit son coût d'acquisition de 60% — sans augmenter son budget

Bonjour [Prénom],

Marc, consultant pour {persona}, investissait 2 000€/mois en pub. Résultat : 3-4 clients. Rentabilité nulle.

Son problème : {context}. Le message ne convertissait pas.

Avec {secteur}, il a revu sa copie. Même budget. Même cible. Messages restructurés avec PAS.

Résultat en 30 jours : 9 clients. CAC divisé par 3.

Vous voulez que je vous montre exactement ce qu'on a changé ?

[Votre nom]"""
        },
        "skill": {
            "Percutant": f"""Objet : Vous n'avez pas besoin d'apprendre le copywriting

Bonjour [Prénom],

Le copywriting est un métier. Vous en avez déjà un.

Pourtant, des {persona} passent des heures à lutter avec {context} — alors qu'il existe des frameworks précis pour ça.

{secteur} intègre AIDA, PAS, FAB et le storytelling directement dans la génération de vos messages. Renseignez votre contexte. Obtenez un message structuré pour convaincre. En 10 secondes.

Plus de page blanche. Plus de doute. Juste des messages qui fonctionnent.

Envie d'un test en direct ?

[Votre nom]""",
            "Professionnel": f"""Objet : La structure qui transforme vos messages en rendez-vous

Bonjour [Prénom],

La majorité des {persona} que j'accompagne partagent le même défi : {context}. Non par manque d'expertise métier, mais faute d'une méthode de rédaction éprouvée.

{secteur} pallie ce manque en intégrant automatiquement les frameworks de vente les plus efficaces (AIDA, FAB, Storytelling) dans chaque message généré.

Résultat : des messages structurés, percutants et prêts à l'envoi — sans courbe d'apprentissage.

Un échange de 20 minutes pour vous montrer le processus ?

Cordialement,
[Votre nom]""",
            "Storytelling": f"""Objet : "Je ne savais pas quoi écrire — maintenant mes messages convertissent à 30%"

Bonjour [Prénom],

Julie, {persona[:-1] if persona.endswith('s') else persona} indépendante, passait 2h par message. {context} la paralysait complètement.

Elle a essayé {secteur}. Premier message généré : un rendez-vous pris dans les 24h.

Le secret ? Le framework FAB appliqué automatiquement : Feature, Advantage, Benefit. Le prospect comprend immédiatement ce qu'il gagne.

Vous voulez le même résultat dès demain ?

[Votre nom]"""
        },
        "growth": {
            "Percutant": f"""Objet : Votre pipeline mérite mieux que le silence

Bonjour [Prénom],

Un pipeline vide, c'est une entreprise en danger. Pour des {persona}, {context} est souvent ce qui bloque la croissance.

Avec {secteur}, générez 50 messages personnalisés dans le temps où vous en écriviez 1. Chaque message cible la douleur exacte de votre persona. Chaque envoi est une opportunité.

Volume + personnalisation = pipeline qui explose.

15 minutes pour voir comment ça marche pour votre secteur ?

[Votre nom]""",
            "Professionnel": f"""Objet : Stratégie de génération de leads pour {persona}

Bonjour [Prénom],

La croissance d'un pipeline qualifié repose sur deux piliers : le volume de prises de contact et la qualité des messages. Pour les {persona}, {context} limite souvent les deux simultanément.

{secteur} permet de multiplier le volume de prospection par 10 tout en maintenant un niveau de personnalisation élevé, grâce à des frameworks de storytelling adaptés à chaque persona.

Je vous propose un échange de 20 minutes pour analyser votre situation actuelle et vous présenter une approche concrète.

Cordialement,
[Votre nom]""",
            "Storytelling": f"""Objet : De 3 leads/mois à 47 en 60 jours — voici comment

Bonjour [Prénom],

Thomas gère une équipe de {persona}. Il y a 3 mois, {context} limitait leur prospection à 3-4 leads qualifiés par mois.

Frustration maximale. Croissance bloquée.

Avec {secteur}, son équipe a commencé à générer des messages ciblés en masse — sans sacrifier la personnalisation.

60 jours plus tard : 47 leads qualifiés. Pipeline rempli. Équipe remotivée.

Vous voulez qu'on reproduise ça pour vous ?

[Votre nom]"""
        },
        "frustration": {
            "Percutant": f"""Objet : Arrêtez d'envoyer des messages que vous détestez écrire

Bonjour [Prénom],

La prospection à froid, pour des {persona}, c'est souvent la tâche la plus redoutée de la semaine. {context}. Et quand les réponses ne viennent pas, la frustration monte.

Le problème ? Les messages génériques se sentent à des kilomètres. Vos prospects aussi.

{secteur} génère des messages qui parlent à vos prospects — pas à leur filtre anti-spam. Empathiques. Directs. Humains.

Résultat : des réponses. Et une prospection dont vous serez fier.

On en parle ?

[Votre nom]""",
            "Professionnel": f"""Objet : Augmentez votre taux de réponse sans paraître intrusif

Bonjour [Prénom],

Les {persona} que j'accompagne partagent souvent la même réticence : {context}. Cette hésitation, légitime, impacte directement leur activité commerciale.

{secteur} aborde la prospection par l'empathie : chaque message est construit autour de la situation réelle du prospect, pas autour de votre offre. Le résultat est une approche perçue comme pertinente, pas intrusive.

Je vous propose de vous montrer la différence en 20 minutes.

Cordialement,
[Votre nom]""",
            "Storytelling": f"""Objet : "J'avais honte d'envoyer mes messages" — jusqu'à ce qu'il change d'approche

Bonjour [Prénom],

Pierre, {persona[:-1] if persona.endswith('s') else persona}, évitait la prospection depuis 6 mois. {context}. Il se sentait comme un spammeur.

En changeant son approche avec {secteur} — messages centrés sur la douleur du prospect, pas sur son produit — tout a changé.

Ses prospects lui répondaient pour le remercier de l'"approche différente". Son taux de réponse est passé de 2% à 18%.

Vous voulez ressentir la même chose ?

[Votre nom]"""
        },
        "risk": {
            "Percutant": f"""Objet : Prospectez à grande échelle sans mettre votre réputation en jeu

Bonjour [Prénom],

Pour des {persona}, un mauvais message peut griller une relation, une base de contacts, ou une réputation construite en années. {context} — cette peur est légitime.

{secteur} intègre des contrôles de qualité automatiques : bon ton, bonne structure, niveau de professionnalisme calibré selon votre secteur.

Résultat : vous prospectez avec confiance. Votre image reste intacte.

On vous montre comment ?

[Votre nom]""",
            "Professionnel": f"""Objet : Prospection à grande échelle sans compromis sur la qualité

Bonjour [Prénom],

La scalabilité de la prospection pose un défi réel aux {persona} : comment maintenir un niveau de qualité irréprochable quand le volume augmente ? {context} — ce risque freine beaucoup d'initiatives.

{secteur} répond à cette problématique en standardisant la qualité tout en maintenant la personnalisation. Chaque message respecte votre positionnement, votre ton et vos standards professionnels.

Un échange de 20 minutes pour vous présenter notre approche ?

Cordialement,
[Votre nom]""",
            "Storytelling": f"""Objet : Il a envoyé 500 messages — zéro plainte, 43 rendez-vous

Bonjour [Prénom],

Karim, consultant pour {persona}, avait une base de 500 contacts qu'il n'osait pas contacter. {context} — il craignait de tout brûler en une campagne ratée.

Avec {secteur}, il a construit une séquence de messages calibrée : ton juste, personnalisation réelle, qualité constante sur les 500 envois.

Résultat : zéro désabonnement, zéro plainte, 43 rendez-vous qualifiés.

Vous voulez la même assurance ?

[Votre nom]"""
        },
        "retention": {
            "Percutant": f"""Objet : Vos anciens clients sont votre meilleure source de revenus — et vous les ignorez

Bonjour [Prénom],

Acquérir un nouveau client coûte 5x plus cher que d'en garder un existant. Pourtant, des {persona} laissent leurs clients partir sans un mot. {context}.

{secteur} génère des séquences de réengagement personnalisées : le bon message, au bon moment, avec le bon ton. Vos clients existants se souviennent de vous. Ils rachètent.

C'est du chiffre d'affaires déjà payé qui vous attend.

On en parle ?

[Votre nom]""",
            "Professionnel": f"""Objet : Stratégie de réengagement pour maximiser la valeur client

Bonjour [Prénom],

L'analyse du comportement des {persona} révèle un levier sous-exploité : la réactivation des clients existants. {context} est souvent la cause d'un taux de rétention insuffisant.

{secteur} permet de créer des séquences de suivi personnalisées — newsletters, offres de renouvellement, messages de réengagement — calibrées selon le cycle de vie du client.

L'impact moyen constaté : +35% de taux de rétention dans les 90 premiers jours.

Un échange pour vous présenter notre approche ?

Cordialement,
[Votre nom]""",
            "Storytelling": f"""Objet : Elle a réactivé 60 clients dormants en 2 semaines

Bonjour [Prénom],

Amina gère une activité de consulting pour {persona}. Ses clients achetaient une fois, puis disparaissaient. {context}. Elle n'avait aucun système de suivi.

Elle a utilisé {secteur} pour créer une séquence de 3 emails de réengagement, personnalisés selon le profil de chaque client.

En 2 semaines : 60 clients réactivés, 23 nouveaux achats. Sans prospecter un seul nouveau contact.

Vous avez des clients dormants qui n'attendent qu'un message ?

[Votre nom]"""
        }
    }

    prob_templates = templates.get(prob_id, templates["time"])
    tone_key = tone if tone in prob_templates else list(prob_templates.keys())[0]
    return prob_templates[tone_key]

# ─────────────────────────────────────────────
# NIVEAUX DE CROISSANCE
# ─────────────────────────────────────────────
LEVELS = [
    {"name": "Débutant", "icon": "🌱", "min": 0, "max": 5, "color": "#64748b"},
    {"name": "Prospecteur", "icon": "🔥", "min": 6, "max": 15, "color": "#f59e0b"},
    {"name": "Closer", "icon": "⚡", "min": 16, "max": 30, "color": "#3b82f6"},
    {"name": "Expert", "icon": "🚀", "min": 31, "max": 60, "color": "#8b5cf6"},
    {"name": "Maître", "icon": "👑", "min": 61, "max": 999, "color": "#f43f5e"},
]

def get_level(count):
    for lvl in LEVELS:
        if lvl["min"] <= count <= lvl["max"]:
            return lvl
    return LEVELS[-1]

def get_next_level(count):
    for i, lvl in enumerate(LEVELS):
        if lvl["min"] <= count <= lvl["max"]:
            return LEVELS[i+1] if i+1 < len(LEVELS) else None
    return None

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
defaults = {
    "page": "auth",
    "authenticated": False,
    "user_name": "",
    "user_email": "",
    "history": [],
    "last_generated": "",
    "gen_count": 0,
    "selected_problem_id": None,
    "show_register": False,
    "daily_counts": {},
    "problems_used": {},
    "join_date": datetime.now().strftime("%d/%m/%Y"),
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─────────────────────────────────────────────
# PAGE AUTH
# ─────────────────────────────────────────────
if not st.session_state.authenticated:
    st.markdown("""
    <div style="text-align:center; padding:40px 0 20px;">
        <div style="font-size:56px; font-weight:900; background:linear-gradient(135deg,#6366f1,#8b5cf6,#ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">ClientBoost AI</div>
        <p style="color:#64748b; font-size:18px; margin-top:8px;">Le générateur de messages de vente qui résout vos 7 problèmes.</p>
    </div>
    """, unsafe_allow_html=True)

    _, col_form, _ = st.columns([1, 1.2, 1])
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
                else:
                    st.error("Veuillez remplir tous les champs.")
            st.markdown("<hr style='margin:20px 0; border-color:#f1f5f9;'>", unsafe_allow_html=True)
            if st.button("Pas encore de compte ? S'inscrire →", use_container_width=True):
                st.session_state.show_register = True
                st.rerun()
        else:
            st.markdown("<h3 style='color:#0f172a; margin-top:0; text-align:center;'>✨ Créer un compte</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#64748b; text-align:center; font-size:14px; margin-bottom:24px;'>Gratuit. Sans carte bancaire.</p>", unsafe_allow_html=True)
            name = st.text_input("Prénom", placeholder="Votre prénom")
            email = st.text_input("Email", placeholder="vous@exemple.com")
            password = st.text_input("Mot de passe", type="password", placeholder="Minimum 8 caractères")
            if st.button("🎉 Créer mon compte", type="primary", use_container_width=True):
                if name and email and password:
                    st.session_state.authenticated = True
                    st.session_state.user_name = name.capitalize()
                    st.session_state.user_email = email
                    st.session_state.page = "dashboard"
                    st.session_state.join_date = datetime.now().strftime("%d/%m/%Y")
                    st.rerun()
                else:
                    st.error("Veuillez remplir tous les champs.")
            st.markdown("<hr style='margin:20px 0; border-color:#f1f5f9;'>", unsafe_allow_html=True)
            if st.button("← Déjà un compte ? Se connecter", use_container_width=True):
                st.session_state.show_register = False
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ─────────────────────────────────────────────
# SIDEBAR (après auth)
# ─────────────────────────────────────────────
with st.sidebar:
    level = get_level(st.session_state.gen_count)
    st.markdown(f"""
    <div style="padding:20px 0 10px;">
        <div style="font-size:22px; font-weight:900; color:white; margin-bottom:4px;">🚀 ClientBoost AI</div>
        <div style="background:rgba(255,255,255,0.08); border-radius:10px; padding:12px; margin-top:12px;">
            <div style="font-size:12px; color:#94a3b8; margin-bottom:4px;">CONNECTÉ EN TANT QUE</div>
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

    nav_items = [
        ("dashboard", "📊 Dashboard"),
        ("generator", "✨ Générateur"),
        ("history", "📜 Historique"),
        ("subscription", "💳 Abonnement"),
        ("settings", "⚙️ Paramètres"),
    ]
    for pid, label in nav_items:
        if st.button(label, key=f"nav_{pid}", use_container_width=True, type="primary" if st.session_state.page == pid else "secondary"):
            st.session_state.page = pid
            st.rerun()

    st.divider()
    if st.button("🚪 Déconnexion", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

# ─────────────────────────────────────────────
# PAGE : DASHBOARD
# ─────────────────────────────────────────────
if st.session_state.page == "dashboard":
    level = get_level(st.session_state.gen_count)
    next_level = get_next_level(st.session_state.gen_count)

    st.markdown(f"<h2 style='color:#0f172a; margin-bottom:4px;'>Bonjour, {st.session_state.user_name} 👋</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748b; font-size:15px; margin-bottom:24px;'>Voici l'évolution de votre activité depuis le {st.session_state.join_date}</p>", unsafe_allow_html=True)

    # Niveau actuel
    progress = 0
    if next_level:
        total = next_level["min"] - level["min"]
        done = st.session_state.gen_count - level["min"]
        progress = int((done / total) * 100) if total > 0 else 100
    else:
        progress = 100

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0f172a,#1e1b4b); border-radius:20px; padding:28px; margin-bottom:24px;">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:16px;">
            <div style="font-size:48px;">{level['icon']}</div>
            <div>
                <div style="font-size:12px; color:#94a3b8; font-weight:600; text-transform:uppercase; letter-spacing:1px;">Niveau actuel</div>
                <div style="font-size:28px; font-weight:900; color:{level['color']};">{level['name']}</div>
                <div style="font-size:14px; color:#94a3b8;">{st.session_state.gen_count} messages générés au total</div>
            </div>
        </div>
        <div style="background:rgba(255,255,255,0.1); border-radius:999px; height:12px; overflow:hidden;">
            <div style="width:{progress}%; height:12px; background:linear-gradient(135deg,#6366f1,#8b5cf6); border-radius:999px; transition:width 0.5s;"></div>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:8px;">
            <span style="font-size:12px; color:#64748b;">{level['name']} ({level['min']} msg)</span>
            <span style="font-size:12px; color:#6366f1; font-weight:700;">{progress}%</span>
            <span style="font-size:12px; color:#64748b;">{'Niveau Max 👑' if not next_level else f"{next_level['name']} ({next_level['min']} msg)"}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Métriques clés
    today = datetime.now().strftime("%Y-%m-%d")
    today_count = st.session_state.daily_counts.get(today, 0)
    problems_solved = len(st.session_state.problems_used)
    saved_count = len(st.session_state.history)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="metric-box">
            <div class="metric-num" style="color:#6366f1;">{st.session_state.gen_count}</div>
            <div class="metric-label">Messages générés</div>
            <div class="metric-change" style="color:#10b981;">Total cumulé</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="metric-box">
            <div class="metric-num" style="color:#f59e0b;">{today_count}</div>
            <div class="metric-label">Aujourd'hui</div>
            <div class="metric-change" style="color:#64748b;">Sessions du jour</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="metric-box">
            <div class="metric-num" style="color:#10b981;">{problems_solved}</div>
            <div class="metric-label">Problèmes explorés</div>
            <div class="metric-change" style="color:#64748b;">sur 7 disponibles</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class="metric-box">
            <div class="metric-num" style="color:#ec4899;">{saved_count}</div>
            <div class="metric-label">Messages sauvegardés</div>
            <div class="metric-change" style="color:#64748b;">dans l'historique</div>
        </div>""", unsafe_allow_html=True)

    st.write("")

    col_left, col_right = st.columns([3, 2])
    with col_left:
        # Progression par problème
        st.markdown("<h4 style='color:#0f172a; margin-bottom:16px;'>📊 Utilisation par problème</h4>", unsafe_allow_html=True)
        for p in PROBLEMS:
            count = st.session_state.problems_used.get(p["id"], 0)
            pct = min(int((count / max(st.session_state.gen_count, 1)) * 100), 100) if st.session_state.gen_count > 0 else 0
            st.markdown(f"""
            <div style="margin-bottom:14px;">
                <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="font-size:13px; font-weight:600; color:#374151;">{p['icon']} {p['title']}</span>
                    <span style="font-size:12px; color:#64748b; font-weight:700;">{count} msg</span>
                </div>
                <div class="prog-wrap">
                    <div class="prog-fill" style="width:{pct}%; background:linear-gradient(135deg,{p['color']},{p['color']}88);"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_right:
        # Badges & achievements
        st.markdown("<h4 style='color:#0f172a; margin-bottom:16px;'>🏆 Badges débloqués</h4>", unsafe_allow_html=True)
        badges = []
        if st.session_state.gen_count >= 1: badges.append(("🎯", "Premier message", "#dbeafe", "#1d4ed8"))
        if st.session_state.gen_count >= 5: badges.append(("🔥", "En feu !", "#ffedd5", "#c2410c"))
        if st.session_state.gen_count >= 10: badges.append(("⚡", "Prospecteur", "#fef9c3", "#a16207"))
        if st.session_state.gen_count >= 25: badges.append(("🚀", "Closer", "#f0fdf4", "#15803d"))
        if st.session_state.gen_count >= 50: badges.append(("👑", "Expert", "#f5f3ff", "#6d28d9"))
        if len(st.session_state.problems_used) >= 3: badges.append(("🧩", "Polyvalent", "#fef2f2", "#b91c1c"))
        if len(st.session_state.problems_used) >= 7: badges.append(("💎", "Maître des 7", "#fff7ed", "#c2410c"))
        if saved_count >= 5: badges.append(("📚", "Collectionneur", "#f5f3ff", "#6d28d9"))

        if badges:
            for icon, name, bg, color in badges:
                st.markdown(f"""
                <div style="background:{bg}; border-radius:10px; padding:10px 14px; margin-bottom:8px; display:flex; align-items:center; gap:10px;">
                    <span style="font-size:20px;">{icon}</span>
                    <span style="font-size:13px; font-weight:700; color:{color};">{name}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background:#f8fafc; border-radius:12px; padding:20px; text-align:center; color:#94a3b8;">
                <div style="font-size:32px;">🔒</div>
                <p style="font-size:13px; margin:8px 0 0;">Générez votre premier message pour débloquer des badges !</p>
            </div>
            """, unsafe_allow_html=True)

        # Prochain objectif
        if next_level:
            remaining = next_level["min"] - st.session_state.gen_count
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#ede9fe,#ddd6fe); border-radius:12px; padding:16px; margin-top:16px; text-align:center;">
                <div style="font-size:12px; font-weight:700; color:#6d28d9; text-transform:uppercase; letter-spacing:0.5px;">Prochain niveau</div>
                <div style="font-size:24px; margin:6px 0;">{next_level['icon']}</div>
                <div style="font-size:16px; font-weight:800; color:#4c1d95;">{next_level['name']}</div>
                <div style="font-size:13px; color:#6d28d9; margin-top:4px;">Plus que <strong>{remaining}</strong> message(s) !</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    _, cta_col, _ = st.columns([1, 2, 1])
    with cta_col:
        if st.button("✨ Générer un nouveau message", type="primary", use_container_width=True):
            st.session_state.page = "generator"
            st.rerun()

# ─────────────────────────────────────────────
# PAGE : GÉNÉRATEUR
# ─────────────────────────────────────────────
elif st.session_state.page == "generator":
    st.markdown("<h2 style='color:#0f172a; margin-bottom:4px;'>✨ Générateur de messages</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; margin-bottom:24px;'>Sélectionnez le problème de votre client, configurez votre contexte, obtenez un message percutant.</p>", unsafe_allow_html=True)

    # ÉTAPE 1 — Sélection du problème
    st.markdown("<h4 style='color:#0f172a;'>Étape 1 — Quel est le problème principal de votre prospect ?</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:13px; margin-bottom:16px;'>Chaque problème a son propre espace de travail et ses propres frameworks.</p>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    cols_map = [col1, col2, col3, col4]
    for i, p in enumerate(PROBLEMS):
        with cols_map[i % 4]:
            is_sel = st.session_state.selected_problem_id == p["id"]
            extra = " prob-selected" if is_sel else ""
            st.markdown(f"""
            <div class="{p['color_class']}{extra}" style="margin-bottom:12px; min-height:130px;">
                <div style="font-size:28px; margin-bottom:8px;">{p['icon']}</div>
                <div style="font-size:13px; font-weight:800; margin-bottom:6px;">{p['title']}</div>
                <div style="font-size:11px; opacity:0.85; line-height:1.4;">{p['hook']}</div>
            </div>
            """, unsafe_allow_html=True)
            btn_label = "✅ Sélectionné" if is_sel else "Choisir"
            if st.button(btn_label, key=f"prob_{p['id']}", use_container_width=True, type="primary" if is_sel else "secondary"):
                st.session_state.selected_problem_id = p["id"]
                st.session_state.last_generated = ""
                st.rerun()

    # ESPACE DE TRAVAIL UNIQUE PAR PROBLÈME
    if st.session_state.selected_problem_id:
        prob = next((p for p in PROBLEMS if p["id"] == st.session_state.selected_problem_id), None)
        if prob:
            st.write("")
            st.markdown(f"""
            <div class="{prob['workspace_class']}">
                <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
                    <span style="font-size:36px;">{prob['emoji_bg']}</span>
                    <div>
                        <div style="font-size:11px; font-weight:700; color:{prob['color']}; text-transform:uppercase; letter-spacing:1px;">Workspace — {prob['title']}</div>
                        <div style="font-size:18px; font-weight:800; color:#0f172a;">{prob['hook']}</div>
                    </div>
                </div>
                <div style="background:rgba(255,255,255,0.7); border-radius:12px; padding:14px; margin-bottom:16px;">
                    <div style="font-size:13px; color:#374151; line-height:1.6;">{prob['desc']}</div>
                    <div style="font-size:13px; font-weight:700; color:{prob['color']}; margin-top:10px;">✅ {prob['solution']}</div>
                </div>
                <div style="background:rgba(255,255,255,0.5); border-radius:10px; padding:12px;">
                    <span style="font-size:13px; color:#64748b;">{prob['tip']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.write("")
            st.markdown("<h4 style='color:#0f172a;'>Étape 2 — Configurez votre contexte</h4>", unsafe_allow_html=True)

            col_a, col_b = st.columns(2)
            with col_a:
                val1 = st.text_input(f"🏢 {prob['fields'][0]}", placeholder=prob['placeholders'][0])
                val2 = st.text_input(f"🎯 {prob['fields'][1]}", placeholder=prob['placeholders'][1])
            with col_b:
                val3 = st.text_area(f"⚡ {prob['fields'][2]}", placeholder=prob['placeholders'][2], height=110)
                tone = st.selectbox("🎨 Style du message", ["Percutant", "Professionnel", "Storytelling"])

            st.write("")
            if st.button(f"✨ Générer mon message — {prob['title']}", type="primary", use_container_width=True):
                if val1 and val2 and val3:
                    with st.spinner(f"Application du framework {prob['framework']}..."):
                        time.sleep(1.5)
                    result = generate_message(prob["id"], val1, val2, val3, tone)
                    st.session_state.last_generated = result
                    st.session_state.gen_count += 1
                    today = datetime.now().strftime("%Y-%m-%d")
                    st.session_state.daily_counts[today] = st.session_state.daily_counts.get(today, 0) + 1
                    st.session_state.problems_used[prob["id"]] = st.session_state.problems_used.get(prob["id"], 0) + 1
                    level = get_level(st.session_state.gen_count)
                    st.success(f"✅ Message généré avec le framework **{prob['framework']}** ! Niveau actuel : {level['icon']} {level['name']}")
                else:
                    st.warning("⚠️ Veuillez remplir tous les champs.")

    if st.session_state.last_generated:
        st.write("")
        st.markdown("<h4 style='color:#0f172a;'>Votre message — prêt à envoyer :</h4>", unsafe_allow_html=True)
        st.text_area("", value=st.session_state.last_generated, height=320, key="output_area")
        col_s, _ = st.columns([1, 3])
        with col_s:
            if st.button("💾 Sauvegarder dans l'historique", use_container_width=True):
                prob = next((p for p in PROBLEMS if p["id"] == st.session_state.selected_problem_id), None)
                st.session_state.history.insert(0, {
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "problem": prob["title"] if prob else "–",
                    "problem_icon": prob["icon"] if prob else "📄",
                    "content": st.session_state.last_generated
                })
                st.success("✅ Sauvegardé !")

# ─────────────────────────────────────────────
# PAGE : HISTORIQUE
# ─────────────────────────────────────────────
elif st.session_state.page == "history":
    st.markdown("<h2 style='color:#0f172a;'>📜 Historique</h2>", unsafe_allow_html=True)
    if not st.session_state.history:
        st.markdown("""<div class="card" style="text-align:center; padding:60px;">
            <p style="font-size:48px; margin:0;">📭</p>
            <p style="color:#64748b; font-size:16px; margin-top:12px;">Aucun message sauvegardé pour l'instant.</p>
        </div>""", unsafe_allow_html=True)
    else:
        col_i, col_c = st.columns([4, 1])
        with col_i:
            st.markdown(f"<span class='badge badge-green'>{len(st.session_state.history)} message(s) sauvegardé(s)</span>", unsafe_allow_html=True)
        with col_c:
            if st.button("🗑️ Tout effacer", use_container_width=True):
                st.session_state.history = []
                st.rerun()
        st.write("")
        for i, item in enumerate(st.session_state.history):
            icon = item.get("problem_icon", "📄")
            prob_name = item.get("problem", "–")
            with st.expander(f"{icon} {prob_name}  —  {item['date']}"):
                st.text_area("", value=item["content"], height=240, key=f"h_{i}")

# ─────────────────────────────────────────────
# PAGE : ABONNEMENT
# ─────────────────────────────────────────────
elif st.session_state.page == "subscription":
    st.markdown("<h2 style='color:#0f172a;'>💳 Tarifs & Abonnement</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Passez à la vitesse supérieure pour débloquer le générateur IA illimité.</p>", unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns(3)
    plans = [
        ("🥉 Standard", "$9", "/ mois", ["✅ 50 générations / mois", "✅ 7 frameworks inclus", "✅ 3 langues", "✅ Historique 30 jours", "❌ Support prioritaire"]),
        ("🥈 Pro", "$29", "/ mois", ["✅ Générations illimitées", "✅ 7 frameworks inclus", "✅ 6 langues", "✅ Historique 1 an", "✅ Support prioritaire"]),
        ("🥇 Agence", "$79", "/ mois", ["✅ Générations illimitées", "✅ 7 frameworks inclus", "✅ 6 langues", "✅ Historique illimité", "✅ Support + API dédiée"]),
    ]
    for col, (name, price, period, features) in zip([c1, c2, c3], plans):
        with col:
            popular = "popular" if "Pro" in name else ""
            st.markdown(f"""<div class="card {'popular' if popular else ''}" style="text-align:center; {'border:2px solid #6366f1;' if popular else ''}">
                <p style="font-size:14px; font-weight:700; color:#64748b; margin:0 0 4px;">{name}</p>
                {'<span style="background:#6366f1;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;">POPULAIRE</span>' if popular else ''}
                <div style="font-size:42px; font-weight:900; color:#0f172a; margin:12px 0 4px;">{price}</div>
                <div style="font-size:14px; color:#64748b; margin-bottom:20px;">{period}</div>
                <hr style="border-color:#f1f5f9; margin:16px 0;">
                {''.join(f'<div style="text-align:left;padding:7px 0;font-size:14px;color:#374151;border-bottom:1px solid #f1f5f9;">{f}</div>' for f in features)}
            </div>""", unsafe_allow_html=True)
            label = "⚡ Passer au Pro" if popular else "Sélectionner"
            st.button(label, key=f"plan_{name}", use_container_width=True, type="primary" if popular else "secondary")

# ─────────────────────────────────────────────
# PAGE : PARAMÈTRES
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
    st.markdown("<p style='font-size:13px; color:#64748b;'>Ajoutez votre clé pour utiliser le vrai moteur Claude AI. <a href='https://console.anthropic.com' target='_blank'>Obtenir une clé →</a></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    level = get_level(st.session_state.gen_count)
    st.markdown(f"""<div class="card"><h4 style="color:#0f172a; margin-top:0;">📊 Votre progression</h4>
        <p style="color:#475569;">Membre depuis : <strong>{st.session_state.join_date}</strong></p>
        <p style="color:#475569;">Niveau actuel : <strong>{level['icon']} {level['name']}</strong></p>
        <p style="color:#475569;">Messages générés : <strong>{st.session_state.gen_count}</strong></p>
        <p style="color:#475569;">Messages sauvegardés : <strong>{len(st.session_state.history)}</strong></p>
        <p style="color:#475569;">Problèmes explorés : <strong>{len(st.session_state.problems_used)} / 7</strong></p>
    </div>""", unsafe_allow_html=True)

    if st.button("✅ Enregistrer", type="primary"):
        st.session_state.user_name = new_name
        st.success("Paramètres enregistrés !")
