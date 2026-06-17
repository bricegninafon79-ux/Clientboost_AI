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

# MOTEUR DE COPYWRITING AVEC ARCHITECTURES ADAPTÉES ET UNIQUES
def generate_shopify_content(content_type, product, audience, level, tone):
    
    # --- BLOCK 1 : BIO INSTAGRAM (Format court, percutant, listes d'emojis, puces, max 150 car.) ---
    if content_type == "📢 Bio Instagram":
        if tone == "💥 Cash & Agressif":
            return f"❌ Marre des alternatives bas de gamme ?\n🛍️ Voici le {product} original pour les {audience}.\n⚡ -20% sur TOUT le site avec le code : REBELLE20\n👇 Ne rate pas l'offre unique"
        elif tone == "🧠 Scientifique & Expert":
            return f"🔬 Expertise & Qualité certifiée\n💡 Solution n°1 pour les {audience} exigeants.\n🌱 Conception ergonomique du {product} breveté\n👇 Découvrez notre étude clinique"
        else:
            return f"🤪 On est désolés pour votre banquier...\n🔥 Le {product} qui fait vriller tous les {audience}.\n📦 Livraison gratuite (parce qu'on est sympas)\n👇 Craquez ici"

    # --- BLOCK 2 : DESCRIPTION PRODUIT SHOPIFY (Format long, marketing de structure, bénéfices) ---
    elif content_type == "📢 Description produit Shopify":
        intro = f"Découvrez le {product}, conçu spécifiquement pour transformer le quotidien des {audience}."
        if tone == "🧠 Scientifique & Expert":
            return f"{intro}\n\n📊 POURQUOI CE PRODUIT EST RECOMMANDÉ PAR LES EXPERTS :\nNotre formule/mécanisme cible précisément la frustration majeure des {audience}. Contrairement aux produits standards, il intègre des composants premium testés en laboratoire.\n\n✅ AVANTAGES TECHNIQUES :\n- Efficacité mesurable en moins de 24 heures.\n- Matériaux durables hypoallergéniques adaptés pour {audience}.\n- Garantie satisfait ou remboursé de 30 jours.\n\n📦 Inclus dans votre colis : 1x {product}, 1x Guide d'utilisation expert."
        elif tone == "🎯 Humoristique & Décalé":
            return f"{intro}\n\n⚠️ ALERTE : Ce produit risque de rendre vos voisins extrêmement jaloux.\n\nOn sait ce que vous vous dites : 'Encore un gadget'. Sauf que le {product} a déjà fait perdre la tête à plus de 1000 {audience}. \n\n🔥 POURQUOI VOUS EN AVEZ BESOIN :\n- Règle votre problème avant que vous ayez le temps de râler.\n- Validé à 100% par la communauté.\n- Si vous n'aimez pas, on vous rembourse (et on pleure un bon coup)."
        else:
            return f"{intro}\n\n⚠️ ATTENTION : Le {product} est victime de son succès. Stock ultra-limité.\n\nLes {audience} qui franchissent le pas ne reviennent jamais en arrière. C'est l'arme secrète qu'il manquait à votre routine.\n\n🧠 LES 3 PILIERS DE NOTRE SUCCÈS :\n1. Éradique la douleur principale des {audience}.\n2. Un design épuré, robuste et redoutablement efficace.\n3. Zéro risque : Garantie totale ou remboursement immédiat.\n\n⚡ Plus que 47 unités disponibles avant la prochaine rupture de stock."

    # --- BLOCK 3 : SCRIPT VIDÉO TIKTOK & REELS (Format minuté avec indications de plans et voix off) ---
    elif content_type in ["📢 1er post TikTok", "📢 Script vidéo 6s"]:
        if tone == "🧠 Scientifique & Expert":
            return f"🎬 SCRIPT VIDÉO DE CONVERSION (Niveau : {level})\n\n⏱️ 0s - 2s [Plan macro serré] \n🗣️ Voix off : 'Voici la vérité scientifique que les marques vous cachent sur le problème des {audience}...'\n\n⏱️ 2s - 4s [Démonstration produit en action lente]\n🗣️ Voix off : 'Le {product} utilise un mécanisme breveté pour agir instantanément.'\n\n⏱️ 4s - 6s [Texte incrusté : Testé & Approuvé]\n🗣️ Voix off : 'Cliquez en bio pour voir l'analyse complète des laboratoires.'"
        elif tone == "🎯 Humoristique & Décalé":
            return f"🎬 SCRIPT VIRAL HUMOUR (Niveau : {level})\n\n⏱️ 0s - 2s [Gros plan visage fatigué + objet qui tombe] \n🗣️ Voix off : 'Dis-moi que tu es un {audience} sans me dire que tu es un {audience}...'\n\n⏱️ 2s - 4s [Transition rapide vers un sourire éclatant avec le {product}]\n🗣️ Voix off : 'Quand ce petit {product} sauve littéralement ta santé mentale.'\n\n⏱️ 4s - 6s [Plan sur le lien en bio pointé du doigt]\n🗣️ Voix off : 'Profite du stock avant que mon patron ne supprime la page !'"
        else:
            return f"🎬 SCRIPT CHOC ACQUISITION (Niveau : {level})\n\n⏱️ 0s - 2s [Rupture visuelle forte / Geste brusque]\n🗣️ Voix off : 'Arrête immédiatement de scroller si tu fais partie des {audience} !'\n\n⏱️ 2s - 4s [Focus sur le produit résolvant le problème en vitesse x2]\n🗣️ Voix off : 'Ce {product} est en train de briser toutes les frustrations du marché.'\n\n⏱️ 4s - 6s [Texte clignotant : -50% CE SOIR]\n🗣️ Voix off : 'Profite de l'offre de lancement via le lien en bio !'"

    # --- BLOCK 4 : EMAIL ABANDON PANIER (Format épistolaire, accroche mail, lien cliquable, sentiment d'urgence) ---
    elif content_type == "📢 Email abandon panier":
        sujet = f"🛒 Objet : Ton panier pour {product} expire dans 47 minutes..."
        if tone == "🧠 Scientifique & Expert":
            return f"{sujet}\n\nBonjour,\n\nNous avons remarqué que vous n'avez pas finalisé la configuration de votre {product}.\n\nEn tant que {audience}, vous savez que négliger ce problème engendre des complications au quotidien. Notre solution a été optimisée pour vous éviter cela.\n\nVotre panier technique est réservé pour quelques heures encore.\n\n[🔬 Finaliser ma commande sécurisée]"
        elif tone == "🎯 Humoristique & Décalé":
            return f"{sujet}\n\nHey ! 👋\n\nTon {product} se sent terriblement seul et abandonné au fond de ton panier... \n\nLes autres {audience} l'achètent en masse et on va bientôt devoir lui trouver un nouveau propriétaire si tu ne viens pas le chercher.\n\nNe le laisse pas filer, on t'offre la livraison pour sceller votre réconciliation !\n\n[🎁 Sauver mon panier de la solitude]"
        else:
            return f"{sujet}\n\n⚠️ DERNIER AVERTISSEMENT\n\nLe {product} que tu as laissé de côté est presque en rupture complète de stock.\n\nPlusieurs {audience} ont validé leur panier ces dernières minutes. Passé ce délai, ton exemplaire sera attribué au client suivant.\n\n[⚡ Récupérer mon panier avant qu'il ne soit trop tard]"

    # --- BLOCK 5 : MESSAGES DM ET HOOKS ADS (Formats accrocheurs de prospection courts) ---
    else: 
        if tone == "🧠 Scientifique & Expert":
            return f"📊 Message ciblé pour {audience} :\n'Bonjour, suite à nos analyses des besoins chez les {audience}, nous avons développé une approche mécanique via le {product}. Souhaitez-vous recevoir notre documentation technique ?'"
        elif tone == "🎯 Humoristique & Décalé":
            return f"🤪 Approche décalée :\n'Avis aux {audience} : On a créé le {product} pour arrêter de souffrir en silence. Promis, ça fait moins mal que de regarder son compte en banque. Tu veux la vidéo démo ?'"
        else:
            return f"💥 Accroche Cash :\n'Ton concurrent direct utilise déjà le {product} pour cibler les {audience} pendant que tu hésites. Ne reste pas à la traîne. Réponds INFO pour voir notre étude de cas.'"

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
    st.write("💡 L'IA génère du contenu à haute conversion adapté au format exact de ton choix (TikTok, Bio, Shopify).")
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
        st.markdown("<div class='card' style='text-align:center;'><h3>🥉 BASIC</h3><h2 style='color:#9CA3AF;'>$5</h2><p>Structure simple pour démarrer.</p></div>", unsafe_allow_html=True)
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
        st.markdown("<div class='card' style='text-align:center; border: 1px solid #FACC15;'><h3>🥇 ULTRA 👑</h3><h2 style='color:#FACC15;'>$29</h2><p>Formule complète + Secrets de psychologie.</p></div>", unsafe_allow_html=True)
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
                # CORRECTIF : On prépare l'affichage des bulles pour le prochain rechargement
                st.session_state.trigger_balloons = True
                st.rerun()
    else:
        # CORRECTIF DES BULLES : Déclenchement propre au moment du rendu de la page payée
        if st.session_state.get("trigger_balloons", False):
            st.balloons()
            st.session_state.trigger_balloons = False # On éteint le trigger pour ne pas spammer

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

        # RELANCE ABONNEMENT EN FIN DE MOIS (DU 28 AU 31)
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

        # CONFIGURATION DES PARAMÈTRES
        st.write("### ⚙️ Personnalise tes données de vente")
        
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            product = st.text_input("Nom exact de ton produit Shopify", placeholder="Ex: Correcteur de posture magique")
        with col_in2:
            audience = st.text_input("Qui est ton client idéal ? (Audience)", placeholder="Ex: travailleurs de bureau mal de dos")
            
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
            st.rerun()

st.caption("Built by kēllønę 🔗💨 | ClientBoost Shopify v3")
