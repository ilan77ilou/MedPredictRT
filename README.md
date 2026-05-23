# MedPredictRT

Prototype d'API de prédiction médicale en temps réel.

## Objectif

MedPredictRT est un projet personnel de démonstration autour de l'intelligence artificielle appliquée à la santé.

Le projet montre comment structurer une API capable de recevoir des constantes patient simulées, calculer un score de risque et retourner une réponse exploitable par un futur tableau de bord.

Ce projet n'est pas un dispositif médical certifié. Il ne doit pas être utilisé pour prendre une décision médicale réelle.

## Fonctionnalités actuelles

- API FastAPI
- endpoint de santé `/`
- endpoint de prédiction `/predict`
- validation des données avec Pydantic
- scoring déterministe de démonstration
- séparation entre API et logique de modèle
- structure prête pour entraînement, streaming, dashboard et tests

## Données utilisées

Le projet utilise uniquement des données simulées.

Aucune donnée patient réelle n'est stockée dans ce dépôt.

## Architecture cible

```text
Données patient simulées
        ↓
API FastAPI
        ↓
Prétraitement
        ↓
Moteur de scoring
        ↓
Réponse JSON
        ↓
Dashboard / alertes
```

## Stack

| Domaine | Technologie |
|---|---|
| Backend | FastAPI |
| Validation | Pydantic |
| Modèle démonstrateur | Python |
| Données | NumPy / Pandas |
| Machine Learning cible | scikit-learn / PyTorch |
| Déploiement cible | Docker |

## Installation

```bash
git clone https://github.com/ilan77ilou/MedPredictRT.git
cd MedPredictRT
pip install -r requirements.txt
```

## Lancement

```bash
python -m uvicorn api.main:app --reload
```

Documentation API :

```text
http://127.0.0.1:8000/docs
```

## Exemple de requête

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": "demo-001",
    "heart_rate": 112,
    "oxygen_level": 92,
    "respiratory_rate": 24,
    "blood_pressure": 145
  }'
```

## Exemple de réponse

```json
{
  "patient_id": "demo-001",
  "risk_score": 0.47,
  "risk_level": "moderate",
  "detected_factors": [
    "elevated_heart_rate",
    "low_oxygen_level",
    "elevated_respiratory_rate",
    "elevated_blood_pressure"
  ],
  "model_type": "deterministic_demo_scoring"
}
```

## Roadmap

- ajouter des tests unitaires
- ajouter Docker
- ajouter un dashboard simple
- créer un jeu de données synthétiques
- remplacer le scoring de démonstration par un modèle entraîné
- ajouter une simulation de flux temps réel

## Auteur

Développé par Ilan Assaraf.

Projet personnel de démonstration IA / backend / santé numérique.

## Licence

MIT
