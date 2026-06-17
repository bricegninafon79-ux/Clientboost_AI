# app.py
import streamlit as st

# Configuration de la page
st.set_page_config(page_title="⚡️ IA Copywriting Suite", layout="wide")

st.title("⚡️ IA Copywriting Suite")
st.caption("Sélectionnez un levier marketing pour générer des textes à forte conversion basés sur notre framework précis en 3 champs.")

# ==========================================
# 1. LA BASE DE DONNÉES DES 7 CAS D'USAGE
# ==========================================
MARKETING_PROBLEMS = [
    {
        "id": "instagram_bio",
        "title": "📢 Instagram Bio",
        "description": "Crée une bio Instagram percutante qui accroche le visiteur et le pousse à cliquer sur le lien de la boutique grâce à une phrase de motivation ou une promesse forte.",
        "fields": [
            {"label": "Motivational Headline / Strong Promise", "placeholder": "e.g., Become the absolute best version of yourself everyday.", "description": "La phrase de motivation ou promesse forte qui donne envie d'agir."},
            {"label": "The Destination / Value Proposition", "placeholder": "e.g., Join 10,000+ people crushing their fitness goals.", "description": "Ce qu'ils vont découvrir s'ils rejoignent le mouvement."},
            {"label": "Urgent Call To Action", "placeholder": "e.g., Start your transformation journey right here 👇", "description": "L'appel à l'action direct pour pousser à cliquer immédiatement sur le lien juste en dessous."}
        ]
    },
    {
        "id": "1st_tiktok_post",
        "title": "📢 1st TikTok Post",
        "description": "Génère un script complet (texte écran, voix-off, visuel) pour ton tout premier post TikTok basé sur une situation du quotidien ou une tendance.",
        "fields": [
            {"label": "Relatable hook problem or TikTok trend", "placeholder": "e.g., POV: Your phone battery dies right when you start GPS navigation", "description": "Le problème quotidien ou le format de tendance pour que l'utilisateur s'arrête."},
            {"label": "Product name being showcased", "placeholder": "e.g., VoltMax Ultra Slim Powerbank", "description": "Le nom du produit mis en avant dans la vidéo."},
            {"label": "Visual action taking place in first 2 seconds", "placeholder": "e.g., Slamming a dead phone on the desk out of frustration", "description": "L'action visuelle de départ pour synchroniser le texte et l'image."}
        ]
    },
    {
        "id": "shopify_product_description",
        "title": "📢 Shopify Product Description",
        "description": "Rédige une page de vente e-commerce complète qui transforme les visiteurs en acheteurs en insistant sur leurs frustrations.",
        "fields": [
            {"label": "Product Name & Core Function", "placeholder": "e.g., AuraGlow LED Mirror - Smart makeup mirror with adjustable lighting", "description": "Le nom de ton produit et ce à quoi il sert de manière simple."},
            {"label": "Target Customer's Pain Point", "placeholder": "e.g., Bad lighting in the bathroom making makeup look patchy or unnatural", "description": "Le problème majeur ou la frustration quotidienne de ton client cible."},
            {"label": "Unfair advantage or unique feature", "placeholder": "e.g., True-color lighting technology mimicking natural sunlight with a 10x magnetic zoom", "description": "L'avantage unique qui rend ton produit supérieur aux autres."}
        ]
    },
    {
        "id": "cart_abandonment_email",
        "title": "📢 Cart Abandonment Email",
        "description": "Crée un email de relance automatique pour récupérer les clients qui ont quitté le panier au moment de payer.",
        "fields=[
            {"label": "Name of items left in shopping cart", "placeholder": "e.g., Wireless Massage Gun", "description": "Le rappel textuel exact de l'objet oublié dans le panier."},
            {"label": "Urgency countdown / Time limit", "placeholder": "e.g., 47 minutes", "description": "La limite de temps avant que leur panier ou le stock ne soit expiré."},
            {"label": "Extra customer checkout incentive", "placeholder": "e.g., Free Shipping + Extra 10% off automated coupon", "description": "Le petit cadeau ou code promo exclusif pour éliminer l'objection du prix."}
        ]
    },
    {
        "id": "cold_dm_message",
        "title": "📢 Cold DM Customer Message",
        "description": "Génère un message d'approche privé (Instagram, TikTok) ultra-personnalisé pour démarcher sans vendre de force.",
        "fields": [
            {"label": "Target niche or account type", "placeholder": "e.g., Fitness Influencers / Fashion Stores", "description": "Le type de compte ou la niche de la personne que tu contactes."},
            {"label": "Personalized compliment / Icebreaker angle", "placeholder": "e.g., Their latest reel about leg day workouts", "description": "Le compliment ou le détail précis de leur contenu pour briser la glace."},
            {"label": "Irresistible offer / Collaboration value", "placeholder": "e.g., Sending 3 free product samples with no strings attached", "description": "L'offre gratuite ou l'avantage immédiat que tu leur apportes."}
        ]
    },
    {
        "id": "6s_video_script",
        "title": "📢 6s Video Script",
        "description": "Crée un script vidéo ultra-court et rythmé (format B-roll / Reels) pour capter l'attention en un éclair.",
        "fields": [
            {"label": "Aggressive 2-second hook text", "placeholder": "e.g., Stop buying expensive teeth whitening kits...", "description": "La phrase choc ou provocante des 2 premières secondes pour stopper le scroll."},
            {"label": "Main lightning-fast result", "placeholder": "e.g., White teeth in exactly 6 seconds", "description": "Le bénéfice ou résultat immédiat affiché au milieu de la vidéo."},
            {"label": "Call to action overlay", "placeholder": "e.g., Click 'Shop Now' before stock ends", "description": "L'appel à l'action flash qui s'affiche à la fin de la vidéo."}
        ]
    },
    {
        "id": "facebook_ads_hook",
        "title": "📢 Facebook Ads Hook",
        "description": "Rédige les premières lignes textuelles d'une publicité Facebook pour bousculer les croyances de ton audience.",
        "fields": [
            {"label": "Target Audience or Customer Persona", "placeholder": "e.g., Busy remote workers with back pain", "description": "L'audience ou le profil type du client à qui s'adresse la publicité."},
            {"label": "The big alternative / What they are currently doing wrong", "placeholder": "e.g., Buying expensive ergonomic chairs that don't fix posture", "description": "La fausse solution ou la mauvaise habitude actuelle de la cible."},
            {"label": "The direct benefit of the product", "placeholder": "e.g., Instantly straightens the spine with a lightweight daily brace", "description": "La promise principale et le bénéfice direct apporté par ton produit."}
        ]
    }
]

# ==========================================
# 2. INTERFACE GRAPHIQUE (Streamlit)
# ==========================================
# Création des colonnes (Sidebar gauche et Zone droite)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🤖 Leviers disponibles")
    problem_titles = [p["title"] for p in MARKETING_PROBLEMS]
    selected_title = st.radio("Choisir un outil :", problem_titles, label_visibility="collapsed")
    
    # Récupérer l'outil sélectionné
    selected_problem = next(p for p in MARKETING_PROBLEMS if p["title"] == selected_title)

with col2:
    st.header(selected_problem["title"])
    st.write(selected_problem["description"])
    st.divider()

    # Formulaire dynamique
    form_values = {}
    with st.form(key=f"form_{selected_problem['id']}"):
        for field in selected_problem["fields"]:
            form_values[field["label"]] = st.text_input(
                label=field["label"],
                placeholder=field["placeholder"],
                help=field["description"]
            )
        
        submit_button = st.form_submit_button(label="Générer la copie magique 🚀", use_container_width=True)

    # Logique de génération (directement dans le fichier)
    if submit_button:
        if any(val.strip() == "" for val in form_values.values()):
            st.warning("⚠️ Veuillez remplir tous les champs.")
        else:
            with st.spinner("Génération de la pépite en cours... ⚙️"):
                
                # Formatage du texte de simulation (Ici tu pourras greffer ton API OpenAI plus tard)
                summary_inputs = "\n".join([f"- {k} : {v}" for k, v in form_values.items()])
                
                generated_text = (
                    f"✨ [Résultat IA - Framework {selected_problem['title']}]\n\n"
                    f"Données prises en compte :\n{summary_inputs}\n\n"
                    f"👉 [Texte Final Haute Conversion] :\n"
                    f"\"Voici votre texte de vente optimisé pour la conversion. Prêt à être publié !\""
                )
                
                st.success("🎯 Contenu généré avec succès :")
                st.text_area(label="Résultat final", value=generated_text, height=250)

