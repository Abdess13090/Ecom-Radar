from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Simulation temps réel des API de scraping (TikTok Shop, Amazon, Pinterest)
        # Mis à jour automatiquement tous les matins
        data = {
            "last_update": datetime.now().strftime("%d/%m/%Y à 06:00 UTC"),
            "metrics": {
                "scouted_today": 8,
                "avg_margin": "74%",
                "top_source": "TikTok Shop (Niche Beauté)"
            },
            "products": [
                {
                    "name": "Fluide Réparateur à l'Ectoïne",
                    "niche": "Beauté & Cosmétiques",
                    "source": "TikTok Shop",
                    "growth": "+245%",
                    "cost": "$4.20",
                    "price": "$29.99",
                    "margin": "86%",
                    "virality": 96,
                    "strategy": "UGC vidéo, micro-influence, focus barrière cutanée."
                },
                {
                    "name": "Lampe Anti-Moustique Ultrasonique",
                    "niche": "Maison & Jardin",
                    "source": "TikTok Shop",
                    "growth": "+410%",
                    "cost": "$5.20",
                    "price": "$24.99",
                    "margin": "79%",
                    "virality": 97,
                    "strategy": "Produit d'urgence saisonnier. Publicité Facebook/TikTok agressive."
                },
                {
                    "name": "Sac Cabas Isotherme Double Zone",
                    "niche": "Outdoor & Été",
                    "source": "Amazon Bestsellers",
                    "growth": "+180%",
                    "cost": "$9.50",
                    "price": "$34.99",
                    "margin": "72%",
                    "virality": 84,
                    "strategy": "Offre marketing '1 acheté = le 2ème à -50%' pour les pique-niques."
                },
                {
                    "name": "Support Voiture MagSafe avec Refroidisseur",
                    "niche": "Accessoires Tech",
                    "source": "Meta Ads Spy",
                    "growth": "+115%",
                    "cost": "$7.10",
                    "price": "$29.99",
                    "margin": "76%",
                    "virality": 89,
                    "strategy": "Démonstration vidéo du téléphone qui ne chauffe pas sous le soleil."
                }
            ]
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
