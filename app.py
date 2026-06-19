import streamlit as st

# 1. CONFIGURATION DE LA PAGE (Doit toujours être la première commande Streamlit)
st.set_page_config(
    page_title="ClientBoost AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INITIALISATION DE L'ÉTAT DE SESSION ---
# Permet de garder en mémoire l'étape ou les données si l'utilisateur change d'onglet
if "page_actuelle" not in st.session_state:
    st.session_state.page_actuelle = "🚀 Générateur"
if "paiement_effectue" not in st.session_state:
    st.session_state.paiement_effectue = False


# --- BARRE LATÉRALE : MENU, TRADUCTION & OPTIONS ---
with st.sidebar:
    st.title("🚀 ClientBoost AI")
    st.write("Le générateur de messages de vente intelligent.")
    st.write("---")
    
    # ÉTAPE 1 : Choix de la langue (Traduction automatique)
    st.subheader("🌐 Traduction")
    langue_cible = st.selectbox(
        "Langue de génération :",
        ["Français", "English", "Español", "Deutsch", "Italiano", "Português"],
        help="L'IA rédigera automatiquement votre message dans cette langue."
    )
    
    st.write("---")
    
    # ÉTAPE 2 : Menu de navigation principal
    st.subheader("🧭 Navigation")
    page_selectionnee = st.radio(
        "Aller à :",
        ["🚀 Générateur", "💳 Mon Abonnement", "📜 Historique", "⚙️ Paramètres"],
        label_visibility="collapsed"
    )
    st.session_state.page_actuelle = page_selectionnee


# --- CONTENU PRINCIPAL DE L'APPLICATION ---

# PAGE 1 : LE GÉNÉRATEUR IA
if st.session_state.page_actuelle == "🚀 Générateur":
    st.title("🔮 Espace de Génération IA")
    st.write(f"Configurez votre campagne. L'IA rédigera votre contenu en : **{langue_cible}**.")
    st.write("---")
    
    # Formulaire utilisateur
    col1, col2 = st.columns(2)
    
    with col1:
        secteur = st.text_input(
            "Votre secteur d'activité / Produit :", 
            placeholder="Ex: Agence SEO, Coach de fitness, SaaS RH..."
        )
        cible = st.text_input(
            "Qui est votre client idéal (Persona) ?", 
            placeholder="Ex: Directeurs Marketing, Particuliers voulant perdre du poids..."
        )
        
    with col2:
        probleme = st.text_area(
            "Quel est le problème principal de votre client ?", 
            placeholder="Ex: Ils n'ont pas le temps de gérer leurs réseaux sociaux, ils manquent de visibilité..."
        )
    
    # Bouton de génération
    st.write("")
    if st.button("✨ Générer mon message de vente", type="primary", use_container_width=True):
        if secteur and probleme and cible:
            with st.spinner(f"L'IA rédige votre message de vente en {langue_cible}..."):
                
                # --- EXEMPLE DE STRUCTURE DE PROMPT POUR TON IA ---
                # C'est ici qu'on intègre dynamiquement la langue choisie
                prompt_complet = f"""
                Tu es un copywriter expert. Rédige un message de vente persuasif.
                Secteur : {secteur}
                Cible : {cible}
                Problème à résoudre : {probleme}
                
                CONSIGNE CRITIQUE : Tu dois obligatoirement rédiger l'intégralité du message en {langue_cible}.
                """
                
                # Simulation de la réponse de l'IA (à remplacer par ton appel API OpenAI / Claude etc.)
                import time
                time.sleep(2) # Simule l'attente
                
                # Affichage du résultat
                st.success(f"✅ Votre message a été généré avec succès en {langue_cible} !")
                st.text_area(
                    "Votre message prêt à copier :", 
                    value=f"[Exemple de message persuasif rédigé en {langue_cible} basé sur le problème : '{probleme}']", 
                    height=200
                )
        else:
            st.warning("⚠️ Veuillez remplir tous les champs avant de lancer la génération.")


# PAGE 2 : MON ABONNEMENT / PAIEMENT
elif st.session_state.page_actuelle == "💳 Mon Abonnement":
    st.title("💳 Tarifs & Abonnement")
    st.write("Passez à la vitesse supérieure pour débloquer des générations illimitées.")
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🥉 Plan Standard")
        st.write("**9€ / mois**")
        st.write("- 20 générations par mois\n- Support par email")
        st.button("Choisir Standard", key="plan_1")
        
    with col2:
        st.markdown("### 🥈 Plan Pro (Populaire)")
        st.write("**29€ / mois**")
        st.write("- Générations illimitées\n- Accès aux prompts avancés\n- Support prioritaire")
        if st.button("Débloquer le Plan Pro", type="primary", key="plan_2"):
            st.session_state.paiement_effectue = True
            st.success("💳 Simulation de paiement réussie ! Compte passé en PRO.")
            
    with col3:
        st.markdown("### 🥇 Plan Agence")
        st.write("**79€ / mois**")
        st.write("- Multi-comptes équipe\n- Intégration API personnalisée\n- Support 24/7")
        st.button("Choisir Agence", key="plan_3")


# PAGE 3 : HISTORIQUE
elif st.session_state.page_actuelle == "📜 Historique":
    st.title("📜 Historique de vos générations")
    st.write("Retrouvez ici tous les textes que vous avez générés précédemment.")
    st.write("---")
    st.info("Aucun historique pour le moment. Lancez votre première génération !")


# PAGE 4 : PARAMÈTRES
elif st.session_state.page_actuelle == "⚙️ Paramètres":
    st.title("⚙️ Paramètres du compte")
    st.write("Gérez la configuration de votre application SaaS.")
    st.write("---")
    api_key = st.text_input("Clé API OpenAI (Optionnel)", type="password")
    st.caption("Laissez vide si vous utilisez l'API par défaut du SaaS.")
