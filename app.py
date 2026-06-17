import React, { useState } from 'react';

// ==========================================
// 1. DÉFINITION DES TYPES (TypeScript)
// ==========================================
interface Field {
  label: string;
  placeholder: string;
  description: string;
}

interface MarketingProblem {
  id: string;
  title: string;
  description: string;
  fields: Field[];
}

// ==========================================
// 2. BASE DE DONNÉES DES 7 CAS D'USAGE
// ==========================================
const MARKETING_PROBLEMS: MarketingProblem[] = [
  {
    id: "instagram_bio",
    title: "📢 Instagram Bio",
    description: "Crée une bio Instagram percutante qui accroche le visiteur et le pousse à cliquer sur le lien de la boutique grâce à une phrase de motivation ou une promesse forte.",
    fields: [
      {
        label: "Motivational Headline / Strong Promise",
        placeholder: "e.g., Become the absolute best version of yourself everyday.",
        description: "La phrase de motivation ou promesse forte qui donne envie d'agir."
      },
      {
        label: "The Destination / Value Proposition",
        placeholder: "e.g., Join 10,000+ people crushing their fitness goals.",
        description: "Ce qu'ils vont découvrir s'ils rejoignent le mouvement."
      },
      {
        label: "Urgent Call To Action",
        placeholder: "e.g., Start your transformation journey right here 👇",
        description: "L'appel à l'action direct pour pousser à cliquer immédiatement sur le lien juste en dessous."
      }
    ]
  },
  {
    id: "1st_tiktok_post",
    title: "📢 1st TikTok Post",
    description: "Génère un script complet (texte écran, voix-off, visuel) pour ton tout premier post TikTok basé sur une situation du quotidien ou une tendance.",
    fields: [
      {
        label: "Relatable hook problem or TikTok trend",
        placeholder: "e.g., POV: Your phone battery dies right when you start GPS navigation",
        description: "Le problème quotidien ou le format de tendance pour que l'utilisateur s'arrête."
      },
      {
        label: "Product name being showcased",
        placeholder: "e.g., VoltMax Ultra Slim Powerbank",
        description: "Le nom du produit mis en avant dans la vidéo."
      },
      {
        label: "Visual action taking place in first 2 seconds",
        placeholder: "e.g., Slamming a dead phone on the desk out of frustration",
        description: "L'action visuelle de départ pour synchroniser le texte et l'image."
      }
    ]
  },
  {
    id: "shopify_product_description",
    title: "📢 Shopify Product Description",
    description: "Rédige une page de vente e-commerce complète qui transforme les visiteurs en acheteurs en insistant sur leurs frustrations.",
    fields: [
      {
        label: "Product Name & Core Function",
        placeholder: "e.g., AuraGlow LED Mirror - Smart makeup mirror with adjustable lighting",
        description: "Le nom de ton produit et ce à quoi il sert de manière simple."
      },
      {
        label: "Target Customer's Pain Point",
        placeholder: "e.g., Bad lighting in the bathroom making makeup look patchy or unnatural",
        description: "Le problème majeur ou la frustration quotidienne de ton client cible."
      },
      {
        label: "Unfair advantage or unique feature",
        placeholder: "e.g., True-color lighting technology mimicking natural sunlight with a 10x magnetic zoom",
        description: "L'avantage unique qui rend ton produit supérieur aux autres."
      }
    ]
  },
  {
    id: "cart_abandonment_email",
    title: "📢 Cart Abandonment Email",
    description: "Crée un email de relance automatique pour récupérer les clients qui ont quitté le panier au moment de payer.",
    fields: [
      {
        label: "Name of items left in shopping cart",
        placeholder: "e.g., Wireless Massage Gun",
        description: "Le rappel textuel exact de l'objet oublié dans le panier."
      },
      {
        label: "Urgency countdown / Time limit",
        placeholder: "e.g., 47 minutes",
        description: "La limite de temps avant que leur panier ou le stock ne soit expiré."
      },
      {
        label: "Extra customer checkout incentive",
        placeholder: "e.g., Free Shipping + Extra 10% off automated coupon",
        description: "Le petit cadeau ou code promo exclusif pour éliminer l'objection du prix."
      }
    ]
  },
  {
    id: "cold_dm_message",
    title: "📢 Cold DM Customer Message",
    description: "Génère un message d'approche privé (Instagram, TikTok) ultra-personnalisé pour démarcher sans vendre de force.",
    fields: [
      {
        label: "Target niche or account type",
        placeholder: "e.g., Fitness Influencers / Fashion Stores",
        description: "Le type de compte ou la niche de la personne que tu contactes."
      },
      {
        label: "Personalized compliment / Icebreaker angle",
        placeholder: "e.g., Their latest reel about leg day workouts",
        description: "Le compliment ou le détail précis de leur contenu pour briser la glace."
      },
      {
        label: "Irresistible offer / Collaboration value",
        placeholder: "e.g., Sending 3 free product samples with no strings attached",
        description: "L'offre gratuite ou l'avantage immédiat que tu leur apportes."
      }
    ]
  },
  {
    id: "6s_video_script",
    title: "📢 6s Video Script",
    description: "Crée un script vidéo ultra-court et rythmé (format B-roll / Reels) pour capter l'attention en un éclair.",
    fields: [
      {
        label: "Aggressive 2-second hook text",
        placeholder: "e.g., Stop buying expensive teeth whitening kits...",
        description: "La phrase choc ou provocante des 2 premières secondes pour stopper le scroll."
      },
      {
        label: "Main lightning-fast result",
        placeholder: "e.g., White teeth in exactly 6 seconds",
        description: "Le bénéfice ou résultat immédiat affiché au milieu de la vidéo."
      },
      {
        label: "Call to action overlay",
        placeholder: "e.g., Click 'Shop Now' before stock ends",
        description: "L'appel à l'action flash qui s'affiche à la fin de la vidéo."
      }
    ]
  },
  {
    id: "facebook_ads_hook",
    title: "📢 Facebook Ads Hook",
    description: "Rédige les premières lignes textuelles d'une publicité Facebook pour bousculer les croyances de ton audience.",
    fields: [
      {
        label: "Target Audience or Customer Persona",
        placeholder: "e.g., Busy remote workers with back pain",
        description: "L'audience ou le profil type du client à qui s'adresse la publicité."
      },
      {
        label: "The big alternative / What they are currently doing wrong",
        placeholder: "e.g., Buying expensive ergonomic chairs that don't fix posture",
        description: "La fausse solution ou la mauvaise habitude actuelle de la cible."
      },
      {
        label: "The direct benefit of the product",
        placeholder: "e.g., Instantly straightens the spine with a lightweight daily brace",
        description: "La promesse principale et le bénéfice direct apporté par ton produit."
      }
    ]
  }
];

// ==========================================
// 3. COMPOSANT D'INTERFACE PRINCIPAL
// ==========================================
export default function CopywritingDashboard() {
  const [selectedProblem, setSelectedProblem] = useState<MarketingProblem>(MARKETING_PROBLEMS[0]);
  const [formValues, setFormValues] = useState<{ [key: string]: string }>({});
  const [isGenerating, setIsGenerating] = useState<boolean>(false);
  const [aiResult, setAiResult] = useState<string>("");

  // Switch d'outil (reset les inputs et le résultat précédent)
  const handleProblemChange = (problemId: string) => {
    const problem = MARKETING_PROBLEMS.find(p => p.id === problemId);
    if (problem) {
      setSelectedProblem(problem);
      setFormValues({});
      setAiResult("");
    }
  };

  // Capture des entrées du formulaire
  const handleInputChange = (label: string, value: string) => {
    setFormValues(prev => ({ ...prev, [label]: value }));
  };

  // Soumission et appel de génération (Simulé - Prêt pour Fetch/Axios)
  const handleGenerate = (e: React.FormEvent) => {
    e.preventDefault();
    setIsGenerating(true);
    setAiResult("");

    setTimeout(() => {
      setIsGenerating(false);
      // Exemple de formatage de sortie propre
      const inputsReview = Object.entries(formValues)
        .map(([key, val]) => `📍 ${key} : "${val}"`)
        .join('\n');

      setAiResult(
        `✨ [Copie Optimisée Rédaction IA]\n\n` +
        `Framework appliqué avec succès pour : ${selectedProblem.title}\n` +
        `----------------------------------------\n` +
        `${inputsReview}\n\n` +
        `👉 [Votre Texte Final] : "Imaginez pouvoir accomplir cela en un clic. Découvrez notre méthode exclusive dès aujourd'hui. Cliquez sur le lien ci-dessous pour transformer vos résultats immédiatement."`
      );
    }, 1200);
  };

  return (
    <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '40px 20px', fontFamily: 'system-ui, sans-serif', color: '#1a1a1a' }}>
      
      {/* Header */}
      <header style={{ marginBottom: '40px', borderBottom: '1px solid #eaeaea', paddingBottom: '20px' }}>
        <h1 style={{ fontSize: '28px', fontWeight: '800', marginBottom: '8px', letterSpacing: '-0.5px' }}>⚡️ IA Copywriting Suite</h1>
        <p style={{ color: '#666', margin: 0, fontSize: '16px' }}>Sélectionnez un levier marketing pour générer des textes à forte conversion basés sur notre framework précis en 3 champs.</p>
      </header>

      {/* Grid de mise en page */}
      <div style={{ display: 'grid', gridTemplateColumns: '340px 1fr', gap: '35px' }}>
        
        {/* Navigation latérale gauche */}
        <aside>
          <h3 style={{ fontSize: '12px', textTransform: 'uppercase', color: '#888', letterSpacing: '1.2px', marginBottom: '15px', fontWeight: '700' }}>
            Leviers de conversion ({MARKETING_PROBLEMS.length})
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {MARKETING_PROBLEMS.map((problem) => (
              <button
                key={problem.id}
                type="button"
                onClick={() => handleProblemChange(problem.id)}
                style={{
                  padding: '14px 16px',
                  borderRadius: '10px',
                  border: '1px solid',
                  borderColor: selectedProblem.id === problem.id ? '#0066cc' : '#e0e0e0',
                  backgroundColor: selectedProblem.id === problem.id ? '#f0f7ff' : '#flex',
                  color: selectedProblem.id === problem.id ? '#0066cc' : '#333',
                  textAlign: 'left',
                  fontWeight: selectedProblem.id === problem.id ? '600' : '500',
                  fontSize: '14px',
                  cursor: 'pointer',
                  transition: 'all 0.15s ease-in-out',
                  boxShadow: selectedProblem.id === problem.id ? '0 2px 4px rgba(0,102,204,0.08)' : 'none'
                }}
              >
                {problem.title}
              </button>
            ))}
          </div>
        </aside>

        {/* Espace de travail central droit */}
        <main style={{ backgroundColor: '#ffffff', padding: '35px', borderRadius: '14px', border: '1px solid #eaeaea', boxShadow: '0 4px 12px rgba(0,0,0,0.02)' }}>
          
          {/* Entête du problème sélectionné */}
          <div style={{ marginBottom: '30px', borderBottom: '1px solid #f5f5f5', paddingBottom: '20px' }}>
            <h2 style={{ fontSize: '24px', fontWeight: '700', margin: '0 0 10px 0', color: '#111' }}>{selectedProblem.title}</h2>
            <p style={{ color: '#555', fontSize: '15px', lineHeight: '1.6', margin: 0 }}>{selectedProblem.description}</p>
          </div>

          {/* Formulaire dynamique */}
          <form onSubmit={handleGenerate} style={{ display: 'flex', flexDirection: 'column', gap: '22px' }}>
            {selectedProblem.fields.map((field, index) => (
              <div key={index} style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                <label style={{ fontWeight: '600', fontSize: '14px', color: '#222' }}>
                  {field.label} <span style={{ color: '#ff4d4f' }}>*</span>
                </label>
                <input
                  type="text"
                  required
                  placeholder={field.placeholder}
                  value={formValues[field.label] || ''}
                  onChange={(e) => handleInputChange(field.label, e.target.value)}
                  style={{
                    padding: '14px',
                    borderRadius: '8px',
                    border: '1px solid #d9d9d9',
                    fontSize: '15px',
                    outline: 'none',
                    transition: 'border-color 0.2s',
                    backgroundColor: '#fafafa'
                  }}
                  onFocus={(e) => (e.target.style.borderColor = '#0066cc')}
                  onBlur={(e) => (e.target.style.borderColor = '#d9d9d9')}
                />
                <span style={{ fontSize: '13px', color: '#666', fontStyle: 'italic' }}>{field.description}</span>
              </div>
            ))}

            {/* Bouton CTA d'envoi */}
            <button
              type="submit"
              disabled={isGenerating}
              style={{
                marginTop: '12px',
                padding: '15px',
                borderRadius: '8px',
                border: 'none',
                backgroundColor: '#0066cc',
                color: '#ffffff',
                fontSize: '16px',
                fontWeight: '600',
                cursor: isGenerating ? 'not-allowed' : 'pointer',
                opacity: isGenerating ? 0.7 : 1,
                boxShadow: '0 4px 10px rgba(0, 102, 204, 0.2)',
                transition: 'all 0.2s'
              }}
            >
              {isGenerating ? 'Génération de la pépite en cours... ⚙️' : 'Générer la copie magique 🚀'}
            </button>
          </form>

          {/* Zone d'affichage du résultat de l'IA */}
          {aiResult && (
            <div style={{ marginTop: '35px', padding: '24px', backgroundColor: '#f8faff', borderLeft: '4px solid #0066cc', borderRadius: '8px', borderTop: '1px solid #e6f0fa', borderRight: '1px solid #e6f0fa', borderBottom: '1px solid #e6f0fa' }}>
              <h4 style={{ margin: '0 0 12px 0', color: '#0066cc', fontWeight: '700', fontSize: '15px' }}>🎯 Contenu généré prêt pour la conversion :</h4>
              <pre style={{ whiteSpace: 'pre-wrap', fontFamily: 'monospace', fontSize: '14px', lineHeight: '1.6', margin: 0, color: '#2c3e50', backgroundColor: '#ffffff', padding: '15px', borderRadius: '6px', border: '1px solid #e2e8f0' }}>{aiResult}</pre>
            </div>
          )}
        </main>

      </div>
    </div>
  );
}
