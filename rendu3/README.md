# 🤖 Preprocessing avec NLTK pour ChatBot

> **Durée estimée :** 45 minutes

## 📋 Objectif

Créer un module de preprocessing robuste qui nettoie et prépare les messages utilisateurs pour un système de chatbot en français.

## 🚀 Fonctionnalités à implémenter

### 1. 🔤 Tokenisation

Diviser le texte en unités plus petites (mots et phrases).

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_message(text):
    """
    Tokenise un message en mots et phrases.
    
    Args:
        text (str): Le texte à tokeniser
        
    Returns:
        dict: Dictionnaire contenant les tokens de mots et phrases
    """
    # Implémenter la tokenisation en mots et phrases
    pass
```

### 2. 🔄 Normalisation

Standardiser le format du texte pour un traitement uniforme.

**Étapes de normalisation :**

- ✅ Conversion en minuscules
- ✅ Suppression de la ponctuation
- ✅ Suppression des espaces multiples
- ✅ Suppression des caractères spéciaux

### 3. 🚫 Suppression des mots vides (Stop Words)

Éliminer les mots qui n'apportent pas de valeur sémantique.

```python
from nltk.corpus import stopwords

def remove_stopwords(tokens, language='french'):
    """
    Retire les mots vides du français.
    
    Args:
        tokens (list): Liste des tokens à filtrer
        language (str): Langue des stop words (défaut: 'french')
        
    Returns:
        list: Liste des tokens sans les mots vides
    """
    # Retirer les mots vides français
    pass
```

### 4. 🌱 Racinisation (Stemming)

Réduire les mots à leur forme racine pour améliorer la correspondance.

```python
from nltk.stem import SnowballStemmer

def stem_tokens(tokens, language='french'):
    """
    Réduit les mots à leur racine.
    
    Args:
        tokens (list): Liste des tokens à raciner
        language (str): Langue pour le stemmer (défaut: 'french')
        
    Returns:
        list: Liste des tokens racinés
    """
    # Réduire les mots à leur racine
    pass
```

## 🧪 Tests à réaliser

Voici les phrases de test pour valider votre implémentation :

### Exemples d'entrée

1. **Commande de restaurant :**

   ```text
   "Bonjour ! J'aimerais commander une pizza margherita s'il vous plaît."
   ```

2. **Demande d'information :**

   ```text
   "Pouvez-vous me dire les horaires d'ouverture de votre restaurant ?"
   ```

3. **Annulation de commande :**

   ```text
   "Je voudrais annuler ma commande précédente, merci beaucoup."
   ```

## 📦 Installation des dépendances

```bash
pip install -r requirements.txt
```

## 🔧 Utilisation

```python
from rendu3 import preprocess_message

# Exemple d'utilisation
message = "Bonjour ! J'aimerais commander une pizza margherita s'il vous plaît."
processed = preprocess_message(message)
print(processed)
```

## 📁 Structure du projet

```text
rendu3/
├── README.md          # Ce fichier
├── rendu3.py         # Module principal de preprocessing
└── requirements.txt   # Dépendances Python
```

## 📚 Ressources utiles

- [Documentation NLTK](https://www.nltk.org/)
- [NLTK French Stop Words](https://www.nltk.org/book/ch02.html)
- [SnowballStemmer Documentation](https://www.nltk.org/api/nltk.stem.html)
