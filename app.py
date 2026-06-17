# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(
    title="IA Copywriting Suite API",
    description="Backend Python mis à jour avec les 7 cas d'usage optimisés"
)

# ==========================================
# 1. STRUCTURES DE DONNÉES (Modèles Pydantic)
# ==========================================
class Field(BaseModel):
    label: str
    placeholder: str
    description: str

class MarketingProblem(BaseModel):
    id: str
    title: str
    description: str
    fields: List[Field]

class GenerationRequest(BaseModel):
    problem_id: str
    inputs: Dict[str, str]

# ==========================================
# 2. BASE DE DONNÉES DES 7 CAS D'USAGE CORRIGÉE
# ==========================================
MARKETING_PROBLEMS: List[MarketingProblem] = [
    MarketingProblem(
        id="instagram_bio",
        title="📢 Instagram Bio",
        description="Crée une bio Instagram percutante qui accroche le visiteur et le pousse à cliquer sur le lien de la boutique grâce à une phrase de motivation ou une promesse forte.",
        fields=[
            Field(
                label="Motivational Headline / Strong Promise", 
                placeholder="e.g., Become the absolute best version of yourself everyday.", 
                description="La phrase de motivation ou promesse forte qui donne envie d'agir."
            ),
            Field(
                label="The Destination / Value Proposition", 
                placeholder="e.g., Join 10,000+ people crushing their fitness goals.", 
                description="Ce qu'ils vont découvrir s'ils rejoignent le mouvement."
            ),
            Field(
                label="Urgent Call To Action", 
                placeholder="e.g., Start your transformation journey right here 👇", 
                description="L'appel à l'action direct pour pousser à cliquer immédiatement sur le lien juste en dessous."
            )
        ]
    ),
    MarketingProblem(
        id="1st_tiktok_post",
        title="📢 1st TikTok Post",
        description="Génère un script complet (texte écran, voix-off, visuel) pour ton tout premier post TikTok basé sur une situation du quotidien ou une tendance.",
        fields=[
            Field(
                label="Relatable hook problem or TikTok trend", 
                placeholder="e.g., POV: Your phone battery dies right when you start GPS navigation", 
                description="Le problème quotidien ou le format de tendance pour que l'utilisateur s'arrête."
            ),
            Field(
                label="Product name being showcased", 
                placeholder="e.g., VoltMax Ultra Slim Powerbank", 
                description="Le nom du produit mis en avant dans la vidéo."
            ),
            Field(
                label="Visual action taking place in first 2 seconds", 
                placeholder="e.g., Slamming a dead phone on the desk out of frustration", 
                description="L'action visuelle de départ pour synchroniser le texte et l'image."
            )
        ]
    ),
    MarketingProblem(
        id="shopify_product_description",
        title="📢 Shopify Product Description",
        description="Rédige une page de vente e-commerce complète qui transforme les visiteurs en acheteurs en insistant sur leurs frustrations.",
        fields=[
            Field(
                label="Product Name & Core Function", 
                placeholder="e.g., AuraGlow LED Mirror - Smart makeup mirror with adjustable lighting", 
                description="Le nom de ton produit et ce à quoi il sert de manière simple."
            ),
            Field(
                label="Target Customer's Pain Point", 
                placeholder="e.g., Bad lighting in the bathroom making makeup look patchy or unnatural", 
                description="Le problème majeur ou la frustration quotidienne de ton client cible."
            ),
            Field(
                label="Unfair advantage or unique feature", 
                placeholder="e.g., True-color lighting technology mimicking natural sunlight with a 10x magnetic zoom", 
                description="L'avantage unique qui rend ton produit supérieur aux autres."
            )
        ]
    ),
    MarketingProblem(
        id="cart_abandonment_email",
        title="📢 Cart Abandonment Email",
        description="Crée un email de relance automatique pour récupérer les clients qui ont quitté le panier au moment de payer.",
        fields=[
            Field(
                label="Name of items left in shopping cart", 
                placeholder="e.g., Wireless Massage Gun", 
                description="Le rappel textuel exact de l'objet oublié dans le panier."
            ),
            Field(
                label="Urgency countdown / Time limit", 
                placeholder="e.g., 47 minutes", 
                description="La limite de temps avant que leur panier ou le stock ne soit expiré."
            ),
            Field(
                label="Extra customer checkout incentive", 
                placeholder="e.g., Free Shipping + Extra 10% off automated coupon", 
                description="Le petit cadeau ou code promo exclusif pour éliminer l'objection du prix."
            )
        ]
    ),
    MarketingProblem(
        id="cold_dm_message",
        title="📢 Cold DM Customer Message",
        description="Génère un message d'approche privé (Instagram, TikTok) ultra-personnalisé pour démarcher sans vendre de force.",
        fields=[
            Field(
                label="Target niche or account type", 
                placeholder="e.g., Fitness Influencers / Fashion Stores", 
                description="Le type de compte ou la niche de la personne que tu contactes."
            ),
            Field(
                label="Personalized compliment / Icebreaker angle", 
                placeholder="e.g., Their latest reel about leg day workouts", 
                description="Le compliment ou le détail précis de leur contenu pour briser la glace."
            ),
            Field(
                label="Irresistible offer / Collaboration value", 
                placeholder="e.g., Sending 3 free product samples with no strings attached", 
                description="L'offre gratuite ou l'avantage immédiat que tu leur apportes."
            )
        ]
    ),
    MarketingProblem(
        id="6s_video_script",
        title="📢 6s Video Script",
        description="Crée un script vidéo ultra-court et rythmé (format B-roll / Reels) pour capter l'attention en un éclair.",
        fields=[
            Field(
                label="Aggressive 2-second hook text", 
                placeholder="e.g., Stop buying expensive teeth whitening kits...", 
                description="La phrase choc ou provocante des 2 premières secondes pour stopper le scroll."
            ),
            Field(
                label="Main lightning-fast result", 
                placeholder="e.g., White teeth in exactly 6 seconds", 
                description="Le bénéfice ou résultat immédiat affiché au milieu de la vidéo."
            ),
            Field(
                label="Call to action overlay", 
                placeholder="e.g., Click 'Shop Now' before stock ends", 
                description="L'appel à l'action flash qui s'affiche à la fin de la vidéo."
            )
        ]
    ),
    MarketingProblem(
        id="facebook_ads_hook",
        title="📢 Facebook Ads Hook",
        description="Rédige les premières lignes textuelles d'une publicité Facebook pour bousculer les croyances de ton audience.",
        fields=[
            Field(
                label="Target Audience or Customer Persona", 
                placeholder="e.g., Busy remote workers with back pain", 
                description="L'audience ou le profil type du client à qui s'adresse la publicité."
            ),
            Field(
                label="The big alternative / What they are currently doing wrong", 
                placeholder="e.g., Buying expensive ergonomic chairs that don't fix posture", 
                description="La fausse solution ou la mauvaise habitude actuelle de la cible."
            ),
            Field(
                label="The direct benefit of the product", 
                placeholder="e.g., Instantly straightens the spine with a lightweight daily brace", 
                description="La promesse principale et le bénéfice direct apporté par ton produit."
            )
        ]
    )
]

# ==========================================
# 3. ENDPOINTS API
# ==========================================
@app.get("/api/problems", response_model=List[MarketingProblem])
def get_all_problems():
    """Renvoie la liste des outils avec les nouveaux champs mis à jour."""
    return MARKETING_PROBLEMS

@app.post("/api/generate")
def generate_copywriting(payload: GenerationRequest):
    """Prend les 3 champs modifiés et renvoie la réponse."""
    problem = next((p for p in MARKETING_PROBLEMS if p.id == payload.problem_id), None)
    if not problem:
        raise HTTPException(status_code=404, detail="Outil de copywriting introuvable")
    
    # Construction dynamique basée sur les 3 nouveaux inputs de l'utilisateur
    user_inputs_summary = [f"- {key}: {val}" for key, val in payload.inputs.items()]
    summary_text = "\n".join(user_inputs_summary)
    
    generated_text = (
        f"🎯 [CONTENU GÉNÉRÉ AVEC SUCCÈS]\n"
        f"Outil utilisé : {problem.title}\n\n"
        f"Données de contexte analysées :\n{summary_text}\n\n"
        f"📝 [Copie Finale] :\n"
        f"Ceci est ton texte final optimisé à forte conversion. Prêt à être déployé !"
    )
    
    return {"status": "success", "generated_text": generated_text}
