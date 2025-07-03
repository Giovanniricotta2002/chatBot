#!/bin/bash

# Script d'installation du modèle spaCy français
echo "🚀 Installation du modèle spaCy français..."

# Installer spaCy si pas déjà fait
pip install spacy>=3.4.0

# Télécharger et installer le modèle français
echo "📥 Téléchargement du modèle fr_core_news_sm..."
python -m spacy download fr_core_news_sm

echo "✅ Installation terminée!"
echo "💡 Vous pouvez maintenant utiliser le modèle avec:"
echo "   import spacy"
echo "   nlp = spacy.load('fr_core_news_sm')"
