import streamlit as st
import time
import random
from datetime import datetime

# ─────────────────────────────────────────────
# 1. CONFIG
# ─────────────────────────────────────────────
st.set_page_config(page_title="ClientBoost AI", page_icon="🚀", layout="wide", initial_sidebar_state="expanded")

# ─────────────────────────────────────────────
# 2. CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

section[data-testid="stSidebar"] { background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); }
section[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
.main .block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1100px; }

.card { background:white; border-radius:16px; padding:28px; border:1px solid #e2e8f0; box-shadow:0 1px 3px rgba(0,0,0,0.06),0 4px 16px rgba(0,0,0,0.04); margin-bottom:20px; }
.card-blue { background:linear-gradient(135deg,#0ea5e9,#2563eb); border-radius:16px; padding:28px; margin-bottom:20px; }
.badge { display:inline-block; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:600; background:#dbeafe; color:#1d4ed8; margin-bottom:8px; }
.badge-green { background:#dcfce7; color:#15803d; }

.stat-box { background:white; border-radius:12px; padding:20px; text-align:center; border:1px solid #e2e8f0; }
.stat-number { font-size:32px; font-weight:800; color:#0ea5e9; }
.stat-label { font-size:13px; color:#64748b; margin-top:4px; }

.price-card { background:white; border:2px solid #e2e8f0; border-radius:20px; padding:32px 24px; text-align:center; transition:all 0.3s; }
.price-card:hover { border-color:#0ea5e9; transform:translateY(-4px); box-shadow:0 12px 40px rgba(14,165,233,0.15); }
.price-card.popular { border-color:#0ea5e9; background:linear-gradient(135deg,#f0f9ff,#e0f2fe); }
.price-amount { font-size:42px; font-weight:800; color:#0f172a; }
.price-period { font-size:14px; color:#64748b; }
.feature-item { text-align:left; padding:7px 0; font-size:14px; color:#374151; border-bottom:1px solid #f1f5f9; }
.feature-item:last-child { border-bottom:none; }

.stButton > button[kind="primary"] {
    background:linear-gradient(135deg,#0ea5e9,#2563eb) !important;
    border:none !important; border-radius:10px !important;
    font-weight:600 !important; font-size:15px !important; padding:12px 28px !important;
}
.stButton > button[kind="primary"]:hover { transform:translateY(-1px) !important; box-shadow:0 8px 25px rgba(14,165,233,0.4) !important; }
.stTextInput > div > div > input, .stTextArea > div > div > textarea {
    border-radius:10px !important; border:1.5px solid #e2e8f0 !important; font-size:14px !important;
}
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
    border-color:#0ea5e9 !important; box-shadow:0 0 0 3px rgba(14,165,233,0.1) !important;
}
footer { visibility:hidden; } #MainMenu { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 3. LES 7 PROBLÈMES — cœur du produit
# ─────────────────────────────────────────────
PROBLEMS = {
    "en": [
        {
            "id": "time", "icon": "⏱️", "title": "Time", "bg": "#dbeafe", "color": "#1d4ed8",
            "label": "I spend too much time writing messages",
            "desc": "You write prospecting messages one by one for hours instead of closing deals.",
            "solution_title": "⚡ Generate in 5 seconds — Save hours every day",
            "solution": "ClientBoost AI writes a complete, personalized sales message in under 5 seconds. What used to take 30 minutes per prospect now takes one click. Focus on closing — let AI handle the writing.",
            "angle": "time"
        },
        {
            "id": "money", "icon": "💸", "title": "Money / ROI", "bg": "#dcfce7", "color": "#15803d",
            "label": "My campaigns don't convert, I'm losing money",
            "desc": "Your campaigns don't convert. You burn ad budget or can't afford a copywriting agency.",
            "solution_title": "💰 Stop burning budget — Start converting",
            "solution": "ClientBoost AI applies proven frameworks (AIDA, PAS, FAB) so every message is built to convert. No agency fees. No wasted spend. Just messages that generate revenue.",
            "angle": "money"
        },
        {
            "id": "skill", "icon": "🧠", "title": "Skill", "bg": "#fef9c3", "color": "#a16207",
            "label": "I don't know how to write a good sales message",
            "desc": "You don't know how to write a killer hook, apply AIDA, or overcome writer's block.",
            "solution_title": "🎓 Expert copywriting — Zero skills required",
            "solution": "ClientBoost AI embeds 10+ proven sales frameworks automatically. Just fill in your product, persona and pain point — AI handles hooks, structure, CTAs and persuasion. No experience needed.",
            "angle": "skill"
        },
        {
            "id": "growth", "icon": "📈", "title": "Growth / Leads", "bg": "#f0fdf4", "color": "#166534",
            "label": "My pipeline is empty, I need more clients",
            "desc": "Your sales funnel is empty. You urgently need new leads and faster revenue.",
            "solution_title": "🚀 Fill your pipeline — Fast",
            "solution": "Generate 10, 50 or 100 personalized outreach messages in minutes. Target your exact persona with messages tailored to their pain points. More outreach = more conversations = more clients.",
            "angle": "growth"
        },
        {
            "id": "frustration", "icon": "😤", "title": "Frustration", "bg": "#fef2f2", "color": "#b91c1c",
            "label": "I hate cold outreach, I never get replies",
            "desc": "You hate cold outreach, feel awkward sending 'pushy' messages, and get zero replies.",
            "solution_title": "😊 Outreach you're proud to send",
            "solution": "ClientBoost AI writes messages that feel natural, empathetic and human — not salesy. Your prospects will feel understood, not pitched. Result: higher reply rates and outreach you actually enjoy.",
            "angle": "frustration"
        },
        {
            "id": "risk", "icon": "🛡️", "title": "Risk / Reputation", "bg": "#f5f3ff", "color": "#6d28d9",
            "label": "I'm afraid of burning my prospect list",
            "desc": "You fear burning your prospect list with low-quality messages or looking unprofessional.",
            "solution_title": "✅ Professional quality — Every single time",
            "solution": "Every message is polished, on-brand and professional. Built-in tone controls ensure you never send something you'd regret. Protect your reputation while prospecting at scale.",
            "angle": "risk"
        },
        {
            "id": "retention", "icon": "🔄", "title": "Retention", "bg": "#fff7ed", "color": "#c2410c",
            "label": "I struggle to re-engage my existing clients",
            "desc": "You struggle to re-engage existing clients with newsletters or follow-up offers.",
            "solution_title": "💌 Re-engage and maximize client lifetime value",
            "solution": "ClientBoost AI generates not just cold outreach — but follow-up sequences, re-engagement emails and upsell messages. Turn silent clients into repeat buyers.",
            "angle": "retention"
        },
    ],
    "fr": [
        {
            "id": "time", "icon": "⏱️", "title": "Temps", "bg": "#dbeafe", "color": "#1d4ed8",
            "label": "Je perds trop de temps à rédiger mes messages",
            "desc": "Vous rédigez vos messages de prospection un par un pendant des heures au lieu de signer des contrats.",
            "solution_title": "⚡ Génération en 5 secondes — Économisez des heures chaque jour",
            "solution": "ClientBoost AI génère un message de vente complet et personnalisé en moins de 5 secondes. Ce qui vous prenait 30 minutes par prospect ne prend plus qu'un clic. Concentrez-vous sur la signature, l'IA s'occupe de la rédaction.",
            "angle": "time"
        },
        {
            "id": "money", "icon": "💸", "title": "Argent / ROI", "bg": "#dcfce7", "color": "#15803d",
            "label": "Mes campagnes ne convertissent pas, je perds de l'argent",
            "desc": "Vos campagnes ne convertissent pas. Vous brûlez votre budget pub ou n'avez pas les moyens d'une agence.",
            "solution_title": "💰 Arrêtez de brûler votre budget — Commencez à convertir",
            "solution": "ClientBoost AI applique des frameworks éprouvés (AIDA, PAS, FAB) pour que chaque message soit conçu pour convertir. Plus de frais d'agence. Plus de budget gaspillé. Juste des messages qui génèrent du chiffre.",
            "angle": "money"
        },
        {
            "id": "skill", "icon": "🧠", "title": "Compétences", "bg": "#fef9c3", "color": "#a16207",
            "label": "Je ne sais pas rédiger un bon message de vente",
            "desc": "Vous ne savez pas rédiger une accroche percutante, appliquer AIDA, ou surmonter la page blanche.",
            "solution_title": "🎓 Copywriting expert — Aucune compétence requise",
            "solution": "ClientBoost AI intègre plus de 10 frameworks de vente éprouvés. Renseignez simplement votre produit, votre persona et sa douleur — l'IA gère les accroches, la structure et la persuasion. Aucune expérience requise.",
            "angle": "skill"
        },
        {
            "id": "growth", "icon": "📈", "title": "Croissance / Leads", "bg": "#f0fdf4", "color": "#166634",
            "label": "Mon pipeline est vide, j'ai besoin de clients",
            "desc": "Votre tunnel de vente est vide. Vous avez besoin de nouveaux leads et de revenus rapidement.",
            "solution_title": "🚀 Remplissez votre pipeline — Rapidement",
            "solution": "Générez 10, 50 ou 100 messages personnalisés en quelques minutes. Ciblez votre persona exact avec des messages adaptés à ses douleurs. Plus de prospection = plus de conversations = plus de clients.",
            "angle": "growth"
        },
        {
            "id": "frustration", "icon": "😤", "title": "Frustration", "bg": "#fef2f2", "color": "#b91c1c",
            "label": "Je déteste la prospection, je n'ai aucune réponse",
            "desc": "Vous détestez la prospection à froid, vous sentez mal à l'aise et ne recevez aucune réponse.",
            "solution_title": "😊 Une prospection dont vous serez fier",
            "solution": "ClientBoost AI rédige des messages naturels, empathiques et humains — pas racoleurs. Vos prospects se sentiront compris, pas démarchés. Résultat : un meilleur taux de réponse et une prospection que vous apprécierez enfin.",
            "angle": "frustration"
        },
        {
            "id": "risk", "icon": "🛡️", "title": "Risque / Réputation", "bg": "#f5f3ff", "color": "#6d28d9",
            "label": "J'ai peur de griller ma base de prospects",
            "desc": "Vous craignez de griller votre liste avec des messages de mauvaise qualité ou de paraître non professionnel.",
            "solution_title": "✅ Qualité professionnelle — À chaque fois",
            "solution": "Chaque message généré est soigné, professionnel et cohérent avec votre image. Les contrôles de ton intégrés garantissent que vous n'enverrez jamais un message que vous regretteriez.",
            "angle": "risk"
        },
        {
            "id": "retention", "icon": "🔄", "title": "Rétention", "bg": "#fff7ed", "color": "#c2410c",
            "label": "J'ai du mal à réengager mes clients existants",
            "desc": "Vous avez du mal à réengager vos clients existants avec des newsletters ou des offres de suivi.",
            "solution_title": "💌 Réengagez et maximisez la valeur client",
            "solution": "ClientBoost AI génère aussi des séquences de relance, des emails de réengagement et des messages d'upsell. Transformez vos clients silencieux en acheteurs réguliers.",
            "angle": "retention"
        },
    ]
}

# ─────────────────────────────────────────────
# 4. TEMPLATES PAR PROBLÈME (EN + FR x 3 tons)
# ─────────────────────────────────────────────
TEMPLATES = {
    "time": {
        "en": {
            "Professional": "Subject: Give your team back 10 hours a week\n\nHi [First Name],\n\nI work with {cible} who waste dozens of hours every month writing tasks that should take minutes.\n\nSpecifically: {probleme}\n\n{secteur} solves this in one click. Our clients reclaim an average of 10+ hours per week — redirected entirely toward closing deals.\n\nWould a 20-minute call this week make sense?\n\nBest,\n[Your Name]",
            "Casual": "Hey [First Name] 👋\n\nHow much time do you lose every week on {probleme}?\n\nI ask because {cible} I work with had the same issue. {secteur} cut that time by 80%.\n\nWorth a 5-minute chat?\n\n[Your Name]",
            "Urgent": "⚡ [First Name] — every hour counts.\n\nWhile you're stuck on {probleme}, your competitors are moving faster.\n\n{secteur} gives {cible} their time back — instantly.\n\nLet's talk this week.\n\n[Your Name]"
        },
        "fr": {
            "Professionnel": "Objet : Récupérez 10h par semaine pour votre équipe\n\nBonjour [Prénom],\n\nJe travaille avec des {cible} qui perdent des dizaines d'heures chaque mois sur des tâches qui devraient prendre quelques minutes.\n\nConcrètement : {probleme}\n\n{secteur} règle ça en un clic. Nos clients récupèrent en moyenne 10h+ par semaine, entièrement redirigées vers la signature de contrats.\n\nUn échange de 20 minutes cette semaine ?\n\nCordialement,\n[Votre nom]",
            "Décontracté": "Salut [Prénom] 👋\n\nCombien d'heures perdez-vous chaque semaine sur {probleme} ?\n\nJe pose la question parce que les {cible} avec qui je travaille avaient le même souci. {secteur} a réduit ce temps de 80%.\n\nÇa vaut 5 minutes ?\n\n[Votre nom]",
            "Urgent": "⚡ [Prénom] — chaque heure compte.\n\nPendant que vous gérez {probleme}, vos concurrents avancent plus vite.\n\n{secteur} rend du temps aux {cible} — immédiatement.\n\nParlons-en cette semaine.\n\n[Votre nom]"
        }
    },
    "money": {
        "en": {
            "Professional": "Subject: Your campaigns deserve better results\n\nHi [First Name],\n\nI see it often: {cible} investing real budget into outreach, only to face {probleme}.\n\nThe problem isn't your product — it's the message.\n\n{secteur} applies AIDA and PAS frameworks to every message, turning cold prospects into warm conversations. Our clients typically see a 3x improvement in response rates within 30 days.\n\nWorth exploring?\n\n[Your Name]",
            "Casual": "Hey [First Name],\n\nStill struggling with {probleme}?\n\nI've helped {cible} fix this exact issue with {secteur}. Better messages = better ROI. Simple.\n\nWant to see how?\n\n[Your Name]",
            "Urgent": "🔥 [First Name] — your budget is leaking.\n\nEvery day with {probleme} is money left on the table.\n\n{secteur} helps {cible} convert more, spend less, and scale faster.\n\nLet's fix this — this week.\n\n[Your Name]"
        },
        "fr": {
            "Professionnel": "Objet : Vos campagnes méritent de meilleurs résultats\n\nBonjour [Prénom],\n\nJe le vois trop souvent : des {cible} qui investissent un vrai budget dans leur prospection, pour faire face à {probleme}.\n\nLe problème n'est pas votre produit — c'est le message.\n\n{secteur} applique AIDA et PAS à chaque message, transformant des prospects froids en conversations qualifiées. Nos clients voient généralement une amélioration 3x de leur taux de réponse en 30 jours.\n\nCela mérite-t-il qu'on en parle ?\n\n[Votre nom]",
            "Décontracté": "Salut [Prénom],\n\nToujours confronté à {probleme} ?\n\nJ'ai aidé des {cible} à régler exactement ce problème avec {secteur}. De meilleurs messages = un meilleur ROI. Simple.\n\nVous voulez voir comment ?\n\n[Votre nom]",
            "Urgent": "🔥 [Prénom] — votre budget fuit.\n\nChaque jour avec {probleme} est de l'argent perdu.\n\n{secteur} aide les {cible} à convertir plus, dépenser moins et scaler plus vite.\n\nRéglons ça — cette semaine.\n\n[Votre nom]"
        }
    },
    "skill": {
        "en": {
            "Professional": "Subject: You don't need to be a copywriter to sell\n\nHi [First Name],\n\nMost {cible} I talk to are experts in their field — but when it comes to {probleme}, they're stuck.\n\nThat's not a talent gap. It's a tool gap.\n\n{secteur} handles the copywriting for you: hooks, structure, persuasion — all built in. You provide the context; the AI does the rest.\n\nNo learning curve. No blank page. Just results.\n\nWant to try?\n\n[Your Name]",
            "Casual": "Hey [First Name] 👋\n\nBe honest — how much time do you waste staring at a blank screen because of {probleme}?\n\n{secteur} fixes that instantly. I've seen {cible} go from blank page to ready-to-send in under a minute.\n\nLet me show you.\n\n[Your Name]",
            "Urgent": "📝 [First Name] — stop struggling with {probleme}.\n\nYou're an expert in what you do. Writing copy shouldn't be your problem.\n\n{secteur} gives {cible} professional-grade messages in seconds.\n\nStart today.\n\n[Your Name]"
        },
        "fr": {
            "Professionnel": "Objet : Vous n'avez pas besoin d'être copywriter pour vendre\n\nBonjour [Prénom],\n\nLa plupart des {cible} que je rencontre sont experts dans leur domaine — mais face à {probleme}, ils sont bloqués.\n\nCe n'est pas un manque de talent. C'est un manque d'outil.\n\n{secteur} s'occupe du copywriting à votre place : accroches, structure, persuasion — tout est intégré. Vous fournissez le contexte, l'IA fait le reste.\n\nAucune courbe d'apprentissage. Plus de page blanche. Juste des résultats.\n\nEnvie d'essayer ?\n\n[Votre nom]",
            "Décontracté": "Salut [Prénom] 👋\n\nSoyons honnêtes — combien de temps perdez-vous à fixer un écran blanc à cause de {probleme} ?\n\n{secteur} règle ça instantanément. J'ai vu des {cible} passer de la page blanche au message prêt à envoyer en moins d'une minute.\n\nLaissez-moi vous montrer.\n\n[Votre nom]",
            "Urgent": "📝 [Prénom] — arrêtez de lutter avec {probleme}.\n\nVous êtes expert dans votre domaine. La rédaction ne devrait pas être votre problème.\n\n{secteur} donne aux {cible} des messages professionnels en secondes.\n\nCommencez aujourd'hui.\n\n[Votre nom]"
        }
    },
    "growth": {
        "en": {
            "Professional": "Subject: Your pipeline deserves more attention\n\nHi [First Name],\n\nA common pattern with {cible}: great offer, but {probleme} keeps the pipeline from growing.\n\nThe math is simple — more personalized outreach = more conversations = more clients.\n\n{secteur} lets you generate 50+ tailored messages in the time it used to take to write one. Imagine what that does to your pipeline.\n\nShall we talk?\n\n[Your Name]",
            "Casual": "Hey [First Name],\n\nIf {probleme} is holding your growth back, the fix is simple.\n\n{secteur} helps {cible} scale their outreach without scaling their effort.\n\n10x the messages. Same time invested. Chat?\n\n[Your Name]",
            "Urgent": "📈 [First Name] — your competitors are outreaching you.\n\nWhile {probleme} slows you down, others fill their pipeline daily.\n\n{secteur} gives {cible} the volume advantage — now.\n\nLet's talk today.\n\n[Your Name]"
        },
        "fr": {
            "Professionnel": "Objet : Votre pipeline mérite plus d'attention\n\nBonjour [Prénom],\n\nUn schéma courant chez les {cible} : une super offre, mais {probleme} empêche le pipeline de croître.\n\nLa logique est simple — plus de prospection personnalisée = plus de conversations = plus de clients.\n\n{secteur} vous permet de générer 50+ messages personnalisés dans le temps qu'il fallait pour en écrire un seul. Imaginez l'impact.\n\nOn en parle ?\n\n[Votre nom]",
            "Décontracté": "Salut [Prénom],\n\nSi {probleme} freine votre croissance, la solution est simple.\n\n{secteur} aide les {cible} à scaler leur prospection sans scaler leurs efforts.\n\n10x les messages. Même temps investi. On se fait un appel ?\n\n[Votre nom]",
            "Urgent": "📈 [Prénom] — vos concurrents prospectent plus vite que vous.\n\nPendant que {probleme} vous ralentit, d'autres remplissent leur pipeline chaque jour.\n\n{secteur} donne aux {cible} l'avantage du volume — maintenant.\n\nParlons-en aujourd'hui.\n\n[Votre nom]"
        }
    },
    "frustration": {
        "en": {
            "Professional": "Subject: Outreach that feels human (because it is)\n\nHi [First Name],\n\nI hear this from {cible} constantly: {probleme}.\n\nThe reason? Most outreach sounds like a template — because it is.\n\n{secteur} generates messages built around your prospect's specific situation, not generic scripts. The result: outreach that feels personal, earns trust, and gets replies.\n\nWant to see the difference?\n\n[Your Name]",
            "Casual": "Hey [First Name] 👋\n\nIf {probleme} sounds familiar — I get it.\n\nI've helped dozens of {cible} go from zero replies to real conversations — without being salesy.\n\n{secteur} makes that shift easy. Want to try?\n\n[Your Name]",
            "Urgent": "📬 [First Name] — your inbox should be fuller.\n\nIf {probleme} is your reality right now, something needs to change.\n\n{secteur} helps {cible} send messages people actually want to reply to.\n\nLet's fix your reply rate — this week.\n\n[Your Name]"
        },
        "fr": {
            "Professionnel": "Objet : Une prospection humaine qui obtient des réponses\n\nBonjour [Prénom],\n\nJ'entends constamment ça de la part des {cible} : {probleme}.\n\nLa raison ? La plupart des messages ressemblent à des templates — parce que c'est ce qu'ils sont.\n\n{secteur} génère des messages construits autour de la situation spécifique du prospect, pas des scripts génériques. Résultat : une prospection qui inspire confiance et obtient des réponses.\n\nVous voulez voir la différence ?\n\n[Votre nom]",
            "Décontracté": "Salut [Prénom] 👋\n\nSi {probleme} vous parle — je comprends.\n\nJ'ai aidé des dizaines de {cible} à passer de zéro réponse à de vraies conversations — sans être racoleurs.\n\n{secteur} rend ce changement facile. Envie d'essayer ?\n\n[Votre nom]",
            "Urgent": "📬 [Prénom] — votre boîte de réception devrait être plus remplie.\n\nSi {probleme} est votre réalité en ce moment, quelque chose doit changer.\n\n{secteur} aide les {cible} à envoyer des messages auxquels les gens ont vraiment envie de répondre.\n\nRéglons votre taux de réponse — cette semaine.\n\n[Votre nom]"
        }
    },
    "risk": {
        "en": {
            "Professional": "Subject: Prospect at scale without risking your reputation\n\nHi [First Name],\n\nFor {cible}, reputation is everything. And {probleme} puts that at risk every time you hit send.\n\n{secteur} builds quality controls into every message: right tone, right framing, right professionalism — automatically.\n\nScale your outreach with confidence. Your brand stays protected.\n\nWant to see how it works?\n\n[Your Name]",
            "Casual": "Hey [First Name],\n\nEver hesitated before hitting send because of {probleme}?\n\n{secteur} removes that hesitation. Every message it generates is something you'd be proud to put your name on.\n\nNo more second-guessing.\n\n[Your Name]",
            "Urgent": "🛡️ [First Name] — protect your reputation while scaling.\n\n{probleme} shouldn't be a risk every time you prospect.\n\n{secteur} guarantees professional-quality messages for {cible} — every time.\n\nLet's talk.\n\n[Your Name]"
        },
        "fr": {
            "Professionnel": "Objet : Prospectez à grande échelle sans risquer votre réputation\n\nBonjour [Prénom],\n\nPour les {cible}, la réputation est tout. Et {probleme} la met en danger à chaque envoi.\n\n{secteur} intègre des contrôles de qualité dans chaque message : bon ton, bon cadrage, bon niveau de professionnalisme — automatiquement.\n\nScalez votre prospection en toute confiance. Votre image reste protégée.\n\nVous voulez voir comment ça fonctionne ?\n\n[Votre nom]",
            "Décontracté": "Salut [Prénom],\n\nVous avez déjà hésité avant d'envoyer un message à cause de {probleme} ?\n\n{secteur} supprime cette hésitation. Chaque message généré est quelque chose dont vous serez fier.\n\nFini le doute.\n\n[Votre nom]",
            "Urgent": "🛡️ [Prénom] — protégez votre réputation en scalant.\n\n{probleme} ne devrait pas être un risque à chaque prospection.\n\n{secteur} garantit des messages de qualité professionnelle pour les {cible} — à chaque fois.\n\nParlons-en.\n\n[Votre nom]"
        }
    },
    "retention": {
        "en": {
            "Professional": "Subject: Your existing clients are your biggest growth lever\n\nHi [First Name],\n\nMost {cible} focus entirely on new leads — while {probleme} quietly erodes their existing revenue base.\n\nThe truth: re-engaging an existing client costs 5x less than acquiring a new one.\n\n{secteur} generates personalized follow-up sequences, re-engagement emails and upsell messages that make existing clients feel valued — and buy again.\n\nLet's unlock the revenue already in your client base.\n\n[Your Name]",
            "Casual": "Hey [First Name] 👋\n\nQuick insight: your best future clients might already be your current ones.\n\nIf {probleme} is a challenge, {secteur} helps {cible} re-engage their base with messages that feel personal and timely.\n\nWant to see some examples?\n\n[Your Name]",
            "Urgent": "🔄 [First Name] — your existing clients are going cold.\n\nEvery week without a touchpoint is a week closer to churn.\n\n{secteur} helps {cible} stay top-of-mind with the right message at the right time.\n\nLet's talk today.\n\n[Your Name]"
        },
        "fr": {
            "Professionnel": "Objet : Vos clients existants sont votre plus grand levier de croissance\n\nBonjour [Prénom],\n\nLa plupart des {cible} se concentrent sur de nouveaux leads — pendant que {probleme} érode silencieusement leur base existante.\n\nLa vérité : réengager un client existant coûte 5x moins cher qu'en acquérir un nouveau.\n\n{secteur} génère des séquences de suivi personnalisées, des emails de réengagement et des messages d'upsell qui donnent envie à vos clients de revenir.\n\nDébloquons les revenus déjà présents dans votre base.\n\n[Votre nom]",
            "Décontracté": "Salut [Prénom] 👋\n\nVos meilleurs futurs clients sont peut-être déjà vos clients actuels.\n\nSi {probleme} est un défi, {secteur} aide les {cible} à réengager leur base avec des messages personnalisés et bien timés.\n\nVous voulez voir des exemples ?\n\n[Votre nom]",
            "Urgent": "🔄 [Prénom] — vos clients existants se refroidissent.\n\nChaque semaine sans contact les rapproche du désabonnement.\n\n{secteur} aide les {cible} à rester présents au bon moment avec le bon message.\n\nParlons-en aujourd'hui.\n\n[Votre nom]"
        }
    }
}

def generate_copy(secteur, cible, probleme, langue, tone, angle):
    lang_key = "fr" if langue == "Français" else "en"
    templates = TEMPLATES.get(angle, TEMPLATES["time"])
    lang_templates = templates.get(lang_key, templates["en"])
    tone_map = {"Professionnel": "Professionnel", "Décontracté": "Décontracté", "Urgent": "Urgent",
                "Professional": "Professional", "Casual": "Casual"}
    tone_key = tone if tone in lang_templates else list(lang_templates.keys())[0]
    template = lang_templates[tone_key]
    return template.format(secteur=secteur, cible=cible, probleme=probleme)


# ─────────────────────────────────────────────
# 5. TRADUCTIONS UI
# ─────────────────────────────────────────────
T = {
    "en": {
        "tagline": "Turn your prospects into loyal customers — instantly.",
        "description": "Stop sending generic messages. ClientBoost AI targets your prospect's core pain point to craft high-impact, personalized sales copy that triggers real results.",
        "motivation": "Don't sell a product. Sell the solution to your customer's deepest pain.",
        "cta": "🚀 Generate My First Message",
        "nav_home": "🏠 Home", "nav_gen": "🚀 Generator", "nav_sub": "💳 Subscription",
        "nav_hist": "📜 History", "nav_set": "⚙️ Settings",
        "gen_title": "🚀 AI Sales Copy Generator",
        "step1": "Step 1 — What problem does your client have?",
        "step2": "Step 2 — Tell us about your offer",
        "solution_label": "✅ How ClientBoost AI solves this:",
        "secteur_lbl": "Your product / service", "secteur_ph": "e.g., SEO Agency, Fitness App, HR SaaS...",
        "cible_lbl": "Your ideal customer", "cible_ph": "e.g., Marketing Directors, Freelancers...",
        "tone_lbl": "Tone of voice",
        "gen_btn": "✨ Generate Sales Copy",
        "gen_warn": "Please select a problem and fill in all fields.",
        "gen_ready": "Your copy — ready to use:",
        "save_btn": "💾 Save to History", "saved_ok": "✅ Saved!",
        "sub_title": "Pricing & Plans",
        "hist_title": "Generation History", "hist_empty": "No generations yet. Go to the Generator!",
        "hist_clear": "🗑️ Clear History",
        "set_title": "Settings", "set_api": "Anthropic API Key (optional)",
        "set_api_info": "Add your key to unlock real Claude AI generations.",
        "set_save": "Save", "set_saved": "✅ Saved!",
        "problems_title": "7 Problems We Solve",
        "familiar": "Does any of this sound familiar?",
        "familiar_sub": "ClientBoost AI was built to eliminate every single one of these.",
        "sel_problem": "Select the problem to solve",
    },
    "fr": {
        "tagline": "Transformez vos prospects en clients fidèles — instantanément.",
        "description": "Arrêtez d'envoyer des messages génériques. ClientBoost AI cible la douleur exacte de votre prospect pour rédiger des messages de vente percutants qui génèrent de vraies ventes.",
        "motivation": "Ne vendez pas un produit. Vendez la solution à la douleur la plus profonde de votre client.",
        "cta": "🚀 Générer mon premier message",
        "nav_home": "🏠 Accueil", "nav_gen": "🚀 Générateur", "nav_sub": "💳 Abonnement",
        "nav_hist": "📜 Historique", "nav_set": "⚙️ Paramètres",
        "gen_title": "🚀 Générateur IA de messages de vente",
        "step1": "Étape 1 — Quel est le problème de votre client ?",
        "step2": "Étape 2 — Parlez-nous de votre offre",
        "solution_label": "✅ Comment ClientBoost AI résout ça :",
        "secteur_lbl": "Votre produit / service", "secteur_ph": "Ex : Agence SEO, App Fitness, SaaS RH...",
        "cible_lbl": "Votre client idéal", "cible_ph": "Ex : Directeurs Marketing, Freelances...",
        "tone_lbl": "Ton du message",
        "gen_btn": "✨ Générer mon message de vente",
        "gen_warn": "Veuillez sélectionner un problème et remplir tous les champs.",
        "gen_ready": "Votre message prêt à utiliser :",
        "save_btn": "💾 Sauvegarder", "saved_ok": "✅ Sauvegardé !",
        "sub_title": "Tarifs & Abonnement",
        "hist_title": "Historique", "hist_empty": "Aucune génération pour l'instant. Allez dans le Générateur !",
        "hist_clear": "🗑️ Effacer l'historique",
        "set_title": "Paramètres", "set_api": "Clé API Anthropic (optionnel)",
        "set_api_info": "Ajoutez votre clé pour utiliser le vrai moteur Claude AI.",
        "set_save": "Enregistrer", "set_saved": "✅ Enregistré !",
        "problems_title": "7 Problèmes Résolus",
        "familiar": "Vous reconnaissez-vous dans ces situations ?",
        "familiar_sub": "ClientBoost AI a été conçu pour éliminer chacun d'eux.",
        "sel_problem": "Sélectionnez le problème à résoudre",
    }
}

# ─────────────────────────────────────────────
# 6. SESSION STATE
# ─────────────────────────────────────────────
for k, v in {"page": "home", "history": [], "last_generated": "", "api_key": "", "gen_count": 0, "selected_problem_id": None}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─────────────────────────────────────────────
# 7. SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:20px 0 10px;">
        <p style="font-size:26px; font-weight:800; margin:0; color:white;">🚀 ClientBoost</p>
        <p style="font-size:13px; color:#94a3b8; margin:4px 0 0;">AI Sales Copy Generator</p>
    </div>""", unsafe_allow_html=True)
    st.divider()

    langue_cible = st.selectbox("🌐 Target Language", ["English", "Français", "Español", "Deutsch", "Italiano", "Português"], index=0)
    ui = "fr" if langue_cible == "Français" else "en"
    tr = T[ui]
    problems_list = PROBLEMS[ui]

    st.divider()
    st.markdown("<p style='font-size:11px; color:#64748b; font-weight:600; text-transform:uppercase; letter-spacing:1px;'>Navigation</p>", unsafe_allow_html=True)

    for pid, label in [("home", tr["nav_home"]), ("generator", tr["nav_gen"]), ("subscription", tr["nav_sub"]), ("history", tr["nav_hist"]), ("settings", tr["nav_set"])]:
        if st.button(label, key=f"nav_{pid}", use_container_width=True, type="primary" if st.session_state.page == pid else "secondary"):
            st.session_state.page = pid
            st.rerun()

    st.divider()
    st.markdown(f"""
    <div style="background:rgba(14,165,233,0.1); border-radius:12px; padding:16px; text-align:center;">
        <p style="font-size:28px; font-weight:800; color:#38bdf8; margin:0;">{st.session_state.gen_count}</p>
        <p style="font-size:12px; color:#94a3b8; margin:4px 0 0;">messages generated</p>
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# 8. PAGES
# ─────────────────────────────────────────────

# ── HOME ──
if st.session_state.page == "home":
    st.markdown("""<div style="font-size:64px; font-weight:800; background:linear-gradient(135deg,#0ea5e9,#2563eb); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-align:center; line-height:1.1; margin-bottom:16px;">ClientBoost AI</div>""", unsafe_allow_html=True)
    st.markdown(f"""<div style="font-size:20px; color:#475569; text-align:center; max-width:680px; margin:0 auto 32px; line-height:1.6;">{tr['tagline']}</div>""", unsafe_allow_html=True)

    # Stats
    for col, num, label in zip(st.columns(4), ["12k+", "3.8x", "7", "98%"], ["Messages generated", "Reply rate boost", "Problems solved", "Satisfaction"]):
        with col:
            st.markdown(f"""<div class="stat-box"><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>""", unsafe_allow_html=True)

    st.write("")
    col_left, col_right = st.columns([3, 2])
    with col_left:
        st.markdown(f"""<div class="card"><span class="badge">✦ What it does</span><h3 style="color:#0f172a; margin:8px 0 12px; font-size:22px;">Stop sending copy-paste messages</h3><p style="color:#475569; line-height:1.7; font-size:15px;">{tr['description']}</p></div>""", unsafe_allow_html=True)
    with col_right:
        st.markdown(f"""<div class="card-blue"><p style="font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:1px; opacity:0.8; margin-bottom:12px; color:white;">💡 Mindset</p><p style="font-size:18px; font-style:italic; line-height:1.6; margin:0; color:white;">"{tr['motivation']}"</p></div>""", unsafe_allow_html=True)

    # 7 problèmes
    st.write("")
    st.markdown(f"""
    <div style="text-align:center; margin-bottom:24px;">
        <span class="badge">✦ {tr['problems_title']}</span>
        <h3 style="color:#0f172a; font-size:26px; margin:10px 0 4px;">{tr['familiar']}</h3>
        <p style="color:#64748b; font-size:15px; margin:0;">{tr['familiar_sub']}</p>
    </div>""", unsafe_allow_html=True)

    # Ligne 1 : 4 problèmes
    cols = st.columns(4)
    for col, p in zip(cols, problems_list[:4]):
        with col:
            st.markdown(f"""
            <div style="background:{p['bg']}; border-radius:14px; padding:20px; margin-bottom:16px; min-height:170px;">
                <p style="font-size:28px; margin:0 0 8px;">{p['icon']}</p>
                <p style="font-size:13px; font-weight:700; color:{p['color']}; text-transform:uppercase; letter-spacing:0.5px; margin:0 0 6px;">{p['title']}</p>
                <p style="font-size:13px; color:#374151; line-height:1.5; margin:0 0 10px;">{p['desc']}</p>
                <p style="font-size:12px; font-weight:600; color:{p['color']}; margin:0;">→ {p['solution_title'].split('—')[0].strip()}</p>
            </div>""", unsafe_allow_html=True)

    # Ligne 2 : 3 problèmes centrés
    _, c1, c2, c3, _ = st.columns([0.5, 1, 1, 1, 0.5])
    for col, p in zip([c1, c2, c3], problems_list[4:]):
        with col:
            st.markdown(f"""
            <div style="background:{p['bg']}; border-radius:14px; padding:20px; margin-bottom:16px; min-height:170px;">
                <p style="font-size:28px; margin:0 0 8px;">{p['icon']}</p>
                <p style="font-size:13px; font-weight:700; color:{p['color']}; text-transform:uppercase; letter-spacing:0.5px; margin:0 0 6px;">{p['title']}</p>
                <p style="font-size:13px; color:#374151; line-height:1.5; margin:0 0 10px;">{p['desc']}</p>
                <p style="font-size:12px; font-weight:600; color:{p['color']}; margin:0;">→ {p['solution_title'].split('—')[0].strip()}</p>
            </div>""", unsafe_allow_html=True)

    st.write("")
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button(tr["cta"], type="primary", use_container_width=True):
            st.session_state.page = "generator"
            st.rerun()


# ── GENERATOR ──
elif st.session_state.page == "generator":
    st.markdown(f"<h2 style='color:#0f172a;'>{tr['gen_title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<span class='badge'>Language: {langue_cible}</span>", unsafe_allow_html=True)
    st.write("")

    # STEP 1 — Sélection du problème
    st.markdown(f"<h4 style='color:#0f172a; margin-bottom:4px;'>{tr['step1']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748b; font-size:14px; margin-bottom:16px;'>{tr['sel_problem']}</p>", unsafe_allow_html=True)

    selected_problem = None
    cols_p = st.columns(4)
    for i, p in enumerate(problems_list):
        with cols_p[i % 4]:
            is_sel = st.session_state.selected_problem_id == p["id"]
            if st.button(f"{p['icon']} {p['title']}", key=f"prob_{p['id']}", use_container_width=True, type="primary" if is_sel else "secondary"):
                st.session_state.selected_problem_id = p["id"]
                st.session_state.last_generated = ""
                st.rerun()

    # Affichage de la solution
    if st.session_state.selected_problem_id:
        selected_problem = next((p for p in problems_list if p["id"] == st.session_state.selected_problem_id), None)
        if selected_problem:
            st.markdown(f"""
            <div style="background:{selected_problem['bg']}; border-left:4px solid {selected_problem['color']}; border-radius:12px; padding:20px; margin:16px 0;">
                <p style="font-size:14px; font-weight:700; color:{selected_problem['color']}; margin:0 0 8px;">{selected_problem['solution_title']}</p>
                <p style="font-size:14px; color:#374151; line-height:1.6; margin:0;">{selected_problem['solution']}</p>
            </div>""", unsafe_allow_html=True)

    st.write("")

    # STEP 2 — Détails
    st.markdown(f"<h4 style='color:#0f172a; margin-bottom:12px;'>{tr['step2']}</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        secteur = st.text_input(f"🏢 {tr['secteur_lbl']}", placeholder=tr["secteur_ph"])
        cible = st.text_input(f"🎯 {tr['cible_lbl']}", placeholder=tr["cible_ph"])
    with col2:
        default_prob = selected_problem["label"] if selected_problem else ""
        probleme = st.text_area("⚡ " + ("Main pain point" if ui == "en" else "Douleur principale"), value=default_prob, height=100)
        tones = ["Professional", "Casual", "Urgent"] if ui == "en" else ["Professionnel", "Décontracté", "Urgent"]
        tone = st.selectbox(f"🎨 {tr['tone_lbl']}", tones)

    st.write("")
    if st.button(tr["gen_btn"], type="primary", use_container_width=True):
        if not st.session_state.selected_problem_id:
            st.warning("⚠️ " + ("Please select a problem in Step 1 first." if ui == "en" else "Veuillez d'abord sélectionner un problème à l'étape 1."))
        elif secteur and cible and probleme:
            with st.spinner("✨ " + ("Crafting your personalized copy..." if ui == "en" else "Rédaction de votre message personnalisé...")):
                time.sleep(1.8)
            result = generate_copy(secteur, cible, probleme, langue_cible, tone, selected_problem["angle"])
            st.session_state.last_generated = result
            st.session_state.gen_count += 1
            st.success("✅ " + ("Your copy is ready!" if ui == "en" else "Votre message est prêt !"))
        else:
            st.warning(tr["gen_warn"])

    if st.session_state.last_generated:
        st.write("")
        st.markdown(f"**{tr['gen_ready']}**")
        st.text_area("", value=st.session_state.last_generated, height=300, key="output_area")
        col_a, _ = st.columns([1, 3])
        with col_a:
            if st.button(tr["save_btn"], use_container_width=True):
                st.session_state.history.insert(0, {
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "secteur": secteur if secteur else "–",
                    "cible": cible if cible else "–",
                    "langue": langue_cible,
                    "tone": tone,
                    "problem": selected_problem["title"] if selected_problem else "–",
                    "content": st.session_state.last_generated
                })
                st.success(tr["saved_ok"])


# ── SUBSCRIPTION ──
elif st.session_state.page == "subscription":
    st.markdown(f"<h2 style='color:#0f172a;'>💳 {tr['sub_title']}</h2>", unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="price-card">
            <p style="font-size:13px;color:#64748b;font-weight:600;text-transform:uppercase;letter-spacing:1px;">🥉 Standard</p>
            <div class="price-amount">$9</div><div class="price-period">/ month</div>
            <hr style="margin:20px 0;border-color:#f1f5f9;">
            <div class="feature-item">✅ 50 generations / month</div>
            <div class="feature-item">✅ All 7 problem templates</div>
            <div class="feature-item">✅ 3 languages</div>
            <div class="feature-item">✅ History (30 days)</div>
            <div class="feature-item">❌ Priority support</div>
        </div>""", unsafe_allow_html=True)
        st.write("")
        st.button("Select Standard", key="b1", use_container_width=True)
    with c2:
        st.markdown("""<div class="price-card popular">
            <p style="font-size:13px;color:#0284c7;font-weight:600;text-transform:uppercase;letter-spacing:1px;">🥈 Pro</p>
            <span style="background:#0ea5e9;color:white;font-size:11px;font-weight:700;padding:3px 10px;border-radius:999px;">POPULAR</span>
            <div class="price-amount" style="margin-top:8px;">$29</div><div class="price-period">/ month</div>
            <hr style="margin:20px 0;border-color:#bae6fd;">
            <div class="feature-item">✅ Unlimited generations</div>
            <div class="feature-item">✅ All 7 problem templates</div>
            <div class="feature-item">✅ All 6 languages</div>
            <div class="feature-item">✅ History (1 year)</div>
            <div class="feature-item">✅ Priority support</div>
        </div>""", unsafe_allow_html=True)
        st.write("")
        st.button("⚡ Upgrade to Pro", key="b2", type="primary", use_container_width=True)
    with c3:
        st.markdown("""<div class="price-card">
            <p style="font-size:13px;color:#64748b;font-weight:600;text-transform:uppercase;letter-spacing:1px;">🥇 Agency</p>
            <div class="price-amount">$79</div><div class="price-period">/ month</div>
            <hr style="margin:20px 0;border-color:#f1f5f9;">
            <div class="feature-item">✅ Unlimited generations</div>
            <div class="feature-item">✅ All 7 problem templates</div>
            <div class="feature-item">✅ All 6 languages</div>
            <div class="feature-item">✅ Unlimited history</div>
            <div class="feature-item">✅ Priority support + API</div>
        </div>""", unsafe_allow_html=True)
        st.write("")
        st.button("Contact Sales", key="b3", use_container_width=True)


# ── HISTORY ──
elif st.session_state.page == "history":
    st.markdown(f"<h2 style='color:#0f172a;'>📜 {tr['hist_title']}</h2>", unsafe_allow_html=True)
    if not st.session_state.history:
        st.markdown(f"""<div class="card" style="text-align:center;padding:60px;">
            <p style="font-size:48px;margin:0;">📭</p>
            <p style="color:#64748b;font-size:16px;margin-top:12px;">{tr['hist_empty']}</p>
        </div>""", unsafe_allow_html=True)
    else:
        col_info, col_clear = st.columns([4, 1])
        with col_info:
            st.markdown(f"<span class='badge badge-green'>{len(st.session_state.history)} generation(s)</span>", unsafe_allow_html=True)
        with col_clear:
            if st.button(tr["hist_clear"], use_container_width=True):
                st.session_state.history = []
                st.rerun()
        st.write("")
        for i, item in enumerate(st.session_state.history):
            prob = f"  |  🎯 {item.get('problem','–')}" if item.get('problem') else ""
            with st.expander(f"📄 {item['secteur']} → {item['cible']}  |  {item['date']}  |  {item['langue']}{prob}"):
                st.text_area("", value=item["content"], height=220, key=f"hist_{i}")


# ── SETTINGS ──
elif st.session_state.page == "settings":
    st.markdown(f"<h2 style='color:#0f172a;'>⚙️ {tr['set_title']}</h2>", unsafe_allow_html=True)
    st.write("")
    st.markdown("""<div class="card"><h4 style="color:#0f172a;margin-top:0;">🔑 API Configuration</h4>""", unsafe_allow_html=True)
    api_key = st.text_input(tr["set_api"], type="password", value=st.session_state.api_key)
    st.markdown(f"""<p style="font-size:13px;color:#64748b;">{tr['set_api_info']} — <a href="https://console.anthropic.com" target="_blank">console.anthropic.com</a></p></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="card"><h4 style="color:#0f172a;margin-top:0;">📊 Stats</h4>
        <p style="color:#475569;">Total generations: <strong>{st.session_state.gen_count}</strong></p>
        <p style="color:#475569;">Saved to history: <strong>{len(st.session_state.history)}</strong></p>
    </div>""", unsafe_allow_html=True)
    if st.button(tr["set_save"], type="primary"):
        st.session_state.api_key = api_key
        st.success(tr["set_saved"])
