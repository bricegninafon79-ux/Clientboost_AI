import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="ClientBoost Shopify", page_icon="🛍️", layout="wide")

# STATE
if "page" not in st.session_state: st.session_state.page = "home"
if "content_type" not in st.session_state: st.session_state.content_type = ""
if "level" not in st.session_state: st.session_state.level = ""
if "tone" not in st.session_state: st.session_state.tone = "💥 Cash & Agressif"
if "paid" not in st.session_state: st.session_state.paid = False

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

# MOTEUR COPY NICHE SHOPIFY
def generate_shopify_content(content_type, product, audience, level, tone):
    # Dictionnaires de modificateurs selon la tonalité choisie
    tone_intro = {
        "💥 Cash & Agressif": "🔥 ALERTE OFFRE : ",
        "🧠 Scientifique & Expert": "📊 ANALYSE TECHNIQUE : ",
        "🎯 Humoristique & Décalé": "🤪 ALERTE PÉPITE : "
    }
    
    hooks = {
        "basic": f"Tu galères à vendre ton produit ({product}) auprès des {audience} ?",
        "premium": f"Arrête de publier du contenu qui fait 0 vente pour ton {product}.",
        "ultra": f"Tes concurrents s'enrichissent avec le {product}. Pas toi. On change ça maintenant."
    }

    # Variations de contenu selon le ton
    if tone == "🧠 Scientifique & Expert":
        desc_ultra = f"🔬 ÉTUDE DE CAS : Pourquoi le {product} surpasse toutes les alternatives du marché.\n\nDéveloppé spécifiquement pour répondre aux exigences des {audience}.\n\n🧠 LES FAITS SCIENTIFIQUES :\n1. Efficacité ciblée prouvée en moins de 24h.\n2. Ergonomie brevetée adaptée pour {audience}.\n3. Garantie clinique de 30 jours."
        tiktok_ultra = f"👑 FORMULE PARFAITE POUR {product} :\nHOOK 0-2s : 'Voici la science derrière le problème des {audience}...'\nCORPS 2-4s : Démo macro du produit. Explication claire du bénéfice mécanique.\nPREUVE 4-5s : 'Recommandé par 98% des spécialistes.'\nCTA 5-6s : 'Commandez votre fiche technique (Lien en bio).'"
    elif tone == "🎯 Humoristique & Décalé":
        desc_ultra = f"⚠️ ALERTE : Le {product} risque de rendre tes proches jaloux.\n\nLes {audience} qui l'ont testé ont complètement vrillé.\n\n🧠 LES AVANTAGES (SANS BLABLA) :\n1. Règle ton problème avant que tu aies le temps de râler.\n2. Validé à 100% par la commu des {audience}.\n3. Si tu n'aimes pas, on te rembourse (et on pleure un coup)."
        tiktok_ultra = f"👑 FORMULE VIRALE POUR {product} :\nHOOK 0-2s : Rire ou situation absurde + 'Dis-moi que tu es un {audience} sans me dire que tu es un {audience}...'\nCORPS 2-4s : Montrer la galère quotidienne VS la facilité avec le {product}.\nPREUVE 4-5s : 'Même ton chat va vouloir te le piquer.'\nCTA 5-6s : 'Lien en bio avant que le boss supprime la page.'"
    else: # Cash & Agressif (Par défaut)
        desc_ultra = f"⚠️ ATTENTION : Le {product} crée une dépendance au confort.\n\nLes {audience} qui l'essaient ne reviennent jamais en arrière.\n\n🧠 POURQUOI ÇA MARCHE :\n1. Supprime ton problème majeur en moins de 24h.\n2. Conçu sur-mesure pour briser la frustration des {audience}.\n3. Zéro risque : Garantie totale satisfait ou remboursé.\n\n⚡ STOCK EXTRÊME : Plus que 47 unités. Ton concurrent est déjà en train d'acheter."
        tiktok_ultra = f"👑 FORMULE CHOC POUR {product} :\nHOOK 0-2s : Rupture visuelle + 'Arrête de scroller si tu fais partie des {audience}...'\nCORPS 2-4s : Focus problème -> Le {product} détruit ce problème instantanément.\nPREUVE 4-5s : 'Déjà +1000 {audience} l'utilisent au quotidien.'\nCTA 5-6s : 'Profite de -50% aujourd'hui uniquement (Lien en bio).'"

    templates = {
        "📢 1er post TikTok": {
            "basic": f"""🔥 HOOK: "POV: Tu as trouvé ce {product} et ta vie a changé"
🎯 SCRIPT 6s: Montrer la frustration -> Sortir le {product} -> Montrer le résultat magique
📝 CTA: "Lien en bio avant la rupture de stock" """,
            "premium": f"""🚀 HOOK: "3 raisons pour lesquelles les {audience} s'arrachent ce {product}"
🎯 SCRIPT: Douleur (2s) + Solution {product} (2s) + Résultat/Bénéfice (2s)
💎 ANGLES RECOMMANDÉS: Avant/Après percutant ou Unboxing ultra dynamique
[CTA]: "Clique sur le lien en bio, expédié sous 24h" """,
            "ultra": tiktok_ultra
        },
        "📢 Description produit Shopify": {
            "basic": f"Transforme ton quotidien avec le {product}. Recommandé pour les {audience}. Achetez aujourd'hui !",
            "premium": f"Découvre le {product} - Le choix n'1 des {audience}. \n\n✅ Bénéfice 1 : Un gain de temps absolu au quotidien\n✅ Bénéfice 2 : Conçu avec des matériaux durables et premium\n✅ Bénéfice 3 : Garantie 30 jours satisfait ou remboursé.\nRejoins la communauté !",
            "ultra": desc_ultra
        },
        "📢 Bio Instagram": {
            "basic": f"On aide les {audience} grâce au {product} | DM pour commander 🛍️",
            "premium": f"🛍️ L'incontournable {product} pour les {audience}\n🚚 Livraison rapide avec suivi\n⭐ Plus de 200 avis clients vérifiés\n👇 Profite de la réduction ici",
            "ultra": f"Arrête de chercher. Commence à en profiter.\nLe {product} = Ton meilleur raccourci quotidien ⚡\nValidé par des centaines de {audience}.\n🎁 -20% sur ton premier achat avec le code : VIP20\n👇 Lien juste ici"
        },
        "📢 Message DM client froid": {
            "basic": f"Salut ! J'ai vu que tu aimais ce style de produits. Tu veux des infos sur le {product} ?",
            "premium": f"Hello ! Petite question rapide pour un ou une {audience} : Tu galères souvent avec ce problème ? \nNotre {product} a réglé ça pour des centaines de personnes. Je t'envoie la démo ?",
            "ultra": f"Lecture 3 secondes : {product} = le game changer ultime pour les {audience}.\n\nOn permet aux profils comme le tien d'exploser leurs résultats cette semaine.\n\nRÉPONDS 'INFO' et je t'envoie les accès privés."
        },
        "📢 Email abandon panier": {
            "basic": f"Tu as oublié quelque chose ? Ton {product} t'attend encore dans ton panier. Finalise ta commande !",
            "premium": f"Hé... ton {product} va être remis en vente.\nPanier réservé pendant 2 heures seulement. Les {audience} s'arrachent ce produit.\n[Finaliser ma commande] + Livraison offerte si tu agis maintenant.",
            "ultra": f"DERNIER RAPPEL : Le {product} est presque en rupture complète.\n\nDes {audience} ont validé 12 nouvelles commandes ces dernières minutes.\nTon panier expire dans exactement 47 minutes.\n\n[RÉCUPÉRER MON PANIER] ou laisse un autre concurrent en profiter."
        },
        "📢 Script vidéo 6s": {
            "basic": f"0-2s : Plan frustration/douleur\n2-4s : Apparition dynamique du {product}\n4-6s : Plan grand sourire + texte incrusté 'Lien en bio'",
            "premium": f"HOOK : 'Fatigué de perdre du temps ?'\nDÉMO 2s : Le {product} utilisé de manière satisfaisante\nPREUVE : Texte 'Avant / Après' clair\nCTA : 'Disponible immédiatement via le lien en bio'",
            "ultra": f"0-1s : TEXTE CHOC 'POV: Tu as enfin trouvé le secret des {audience}'\n1-3s : Plan ultra-serré sur le {product} résolvant le problème en vitesse x2\n3-5s : Client soulagé + gros plan sur le résultat impeccable\n5-6s : '-50% UNIQUEMENT CE SOIR - Lien en bio'"
        },
        "📢 Hook Facebook Ads": {
            "basic": f"Arrête de gaspiller ton budget publicitaire dans des produits moins performants que le {product}.",
            "premium": f"Les {audience} commandent ce {product} en masse. Voici la raison cachée...",
            "ultra": f"Ton principal concurrent fait un carton avec ce {product}.\nPas toi.\nReprends l'avantage sur tes publicités avec ce script de 6s →"
        }
    }

    # Génération automatique des hashtags SEO selon le produit
    niche_keyword = product.lower().replace(" ", "")
    hashtags = f"\n\n#️⃣ TAGS RECOMMANDÉS : #{niche_keyword} #ecomfrance #shopifyfrance #tiktokmademebuyit #dropshippingfr #astuce{niche_keyword}"

    return f"{tone_intro[tone]}{hooks[level]}\n\n{templates[content_type][level]}{hashtags}"

# HEADER
st.markdown("<div class='title'>🛍️ ClientBoost Shopify</div>", unsafe_allow_html=True)
st.markdown("<div class='trust'>2,941 débutants Shopify • Contenu qui vend en 6s • No signup</div>", unsafe_allow_html=True)

# HOME
if st.session_state.page == "home":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("## ❌ T'es débutant Shopify?")
    st.write("❌ Tes posts TikTok font 12 vues")
    st.write("❌ Ta description produit = 0 vente")
    st.write("❌ Tu sais pas quoi écrire pour vendre")
    st.write("---")
    st.write("💡 L'IA génère du contenu à haute conversion pour ton produit e-commerce en 6 secondes chrono.")
    if st.button("🚀 Générer mon 1er contenu qui vend"):
        st.session_state.page = "content"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# CONTENT TYPE
elif st.session_state.page == "content":
    st.subheader("💡 Quel contenu tu veux créer AUJOURD'HUI?")
    content_types = [
        "📢 1er post TikTok",
        "📢 Description produit Shopify",
        "📢 Bio Instagram",
        "📢 Message DM client froid",
        "📢 Email abandon panier",
        "📢 Script vidéo 6s",
        "📢 Hook Facebook Ads"
    ]
    st.session_state.content_type = st.radio("Choisis une option :", content_types)
    
    col_back, col_next = st.columns([1, 4])
    with col_back:
        if st.button("⬅ Retour"):
            st.session_state.page = "home"
            st.rerun()
    with col_next:
        if st.button("Continuer vers l'offre →"):
            st.session_state.page = "levels"
            st.rerun()

# LEVELS
elif st.session_state.page == "levels":
    st.subheader("💎 Choisis la puissance de ton copywriting")
    st.write(f"### Format sélectionné : {st.session_state.content_type}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='card' style='text-align:center;'><h3>🥉 BASIC</h3><h2 style='color:#9CA3AF;'>$5</h2><p>Structure simple & rapide pour démarrer.</p></div>", unsafe_allow_html=True)
        if st.button("Choisir l'offre Basic"): 
            st.session_state.level = "basic"
            st.session_state.page = "payment"
            st.rerun()
            
    with col2:
        st.markdown("<div class='card' style='text-align:center; border: 1px solid #F97316;'><h3>🥈 PRO ⭐</h3><h2 style='color:#F97316;'>$15</h2><p>Taux de conversion boosté par x2.3.</p></div>", unsafe_allow_html=True)
        if st.button("Choisir l'offre Pro"): 
            st.session_state.level = "premium"
            st.session_state.page = "payment"
            st.rerun()
            
    with col3:
        st.markdown("<div class='card' style='text-align:center; border: 1px solid #FACC15;'><h3>🥇 ULTRA 👑</h3><h2 style='color:#FACC15;'>$29</h2><p>Formule virale complète + Secrets de psychologie.</p></div>", unsafe_allow_html=True)
        if st.button("Choisir l'offre Ultra"): 
            st.session_state.level = "ultra"
            st.session_state.page = "payment"
            st.rerun()
            
    st.write("---")
    if st.button("⬅ Modifier le type de contenu"):
        st.session_state.page = "content"
        st.rerun()

# PAYMENT + RESULT
elif st.session_state.page == "payment":
    if not st.session_state.paid:
        st.warning("🔒 Débloque la puissance de l'IA")
        st.info("💳 Passerelle Lemon Squeezy sécurisée - Test avec la carte : 4242 4242 4242 4242")
        
        col_pay_back, col_pay_trigger = st.columns([1, 4])
        with col_pay_back:
            if st.button("⬅ Retour"):
                st.session_state.page = "levels"
                st.rerun()
        with col_pay_trigger:
            if st.button("💳 Valider le paiement de Démo ($0)"):
                st.session_state.paid = True
                st.rerun()
    else:
        # 1. EXPÉRIENCE CLIENT DE FOLIE : NOTIFICATION WOW
        if "wow_shown" not in st.session_state:
            st.balloons()
            st.session_state.wow_shown = True

        st.markdown("""
        <div style="background: linear-gradient(135deg, #1e1b4b 0%, #111827 100%); padding: 25px; border-radius: 16px; border: 2px solid #F97316; margin-bottom: 25px;">
            <h3 style="color: #FACC15; margin-top: 0;">🎉 Paiement validé ! Bienvenue dans l'élite de Shopify.</h3>
            <p style="color: #F3F4F6; font-size: 16px; line-height: 1.6;">
                Merci pour ta confiance. Tu viens d'activer l'algorithme de conversion utilisé secrètement par le <b>top 1% des e-commerçants</b>. 
            </p>
            <p style="color: #9CA3AF; font-size: 14px; font-style: italic;">
                👀 Prépare-toi... Ce que l'IA va te sortir dans quelques secondes va littéralement ringardiser tes anciens textes. Tes concurrents ne sont pas prêts.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # 2. RELANCE ABONNEMENT EN FIN DE MOIS (DU 28 AU 31)
        if datetime.now().day >= 28:
            st.markdown("""
            <div style="background-color: #7c2d12; padding: 20px; border-radius: 12px; border-left: 5px solid #f97316; margin-bottom: 25px;">
                <h4 style="color: #ffedd5; margin: 0 0 5px 0;">⏳ Fin de mois imminente : Ne perds pas tes accès exclusifs !</h4>
                <p style="color: #fed7aa; font-size: 14px; margin: 0 0 12px 0;">
                    Ton pass unique arrive bientôt à échéance. Sécurise ton business et passe sur l'abonnement mensuel pour générer du contenu pro en illimité.
                </p>
                <a href="https://ton-lien-de-paiement-stripe.com" target="_blank" style="background-color: #f97316; color: white; padding: 10px 18px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 13px; display: inline-block;">
                    🚀 Activer mon Pass Mensuel (-30% inclus)
                </a>
            </div>
            """, unsafe_allow_html=True)

        # 3. CRÉATION DU CONTENU ET CONFIGURATION DES PARAMÈTRES
        st.write("### ⚙️ Personnalise tes données de vente")
        
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            product = st.text_input("Nom exact de ton produit Shopify", placeholder="Ex: Correcteur de posture magique")
        with col_in2:
            audience = st.text_input("Qui est ton client idéal ? (Audience)", placeholder="Ex: travailleurs de bureau mal de dos")
            
        # LE SÉLECTEUR DE TONALITÉ
        st.session_state.tone = st.selectbox(
            "Style et Tonalité de l'IA :", 
            ["💥 Cash & Agressif", "🧠 Scientifique & Expert", "🎯 Humoristique & Décalé"]
        )

        if st.button("🚀 Libérer la puissance de l'IA"):
            if product and audience:
                result = generate_shopify_content(
                    st.session_state.content_type, 
                    product, 
                    audience, 
                    st.session_state.level,
                    st.session_state.tone
                )
                st.session_state.generated_result = result
            else:
                st.error("⚠️ Erreur : Remplis d'abord le nom du produit et ton audience cible !")

        # AFFICHAGE DU RÉSULTAT COPIABLE EN 1 CLIC
        if "generated_result" in st.session_state:
            result_text = st.session_state.generated_result
            
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("🚀 Ton contenu prêt à vendre")
            st.text_area("Copie le contenu ci-dessous :", result_text, height=380, key="out")
            
            col_copy, col_download = st.columns(2)
            with col_copy:
                # Échappement des caractères spéciaux JavaScript pour un bouton ultra stable
                escaped_result = result_text.replace('`', '\\`').replace('$', '\\$').replace('\n', '\\n')
                components.html(f"""
                <button onclick="navigator.clipboard.writeText(`{escaped_result}`)"
                style="background: linear-gradient(90deg, #F97316 0%, #FACC15 100%); color:white; border:none; padding:12px; border-radius:8px; cursor:pointer; font-weight:bold; width:100%; font-size:15px; height: 45px;">
                📋 Copier le texte en 1 clic
                </button>
                """, height=55)
                
            with col_download:
                st.download_button(
                    label="⬇ Télécharger au format .txt", 
                    data=result_text, 
                    file_name="clientboost_copywriting.txt",
                    use_container_width=True
                )
            st.markdown("</div>", unsafe_allow_html=True)

        st.write("---")
        if st.button("🔄 Réinitialiser et créer un autre texte"):
            st.session_state.page = "home"
            st.session_state.paid = False
            if "generated_result" in st.session_state: del st.session_state.generated_result
            if "wow_shown" in st.session_state: del st.session_state.wow_shown
            st.rerun()

st.caption("Built by kēllønę 🔗💨 | ClientBoost Shopify v3")
    
