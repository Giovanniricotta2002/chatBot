import nltk
import re
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Télécharger les ressources NLTK nécessaires
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("Téléchargement de la ressource 'punkt'...")
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    print("Téléchargement de la ressource 'stopwords'...")
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    print("Téléchargement de la ressource 'punkt_tab'...")
    nltk.download('punkt_tab')

def tokenize_message(text):
    """
    Tokenise un message en mots et phrases.
    
    Args:
        text (str): Le texte à tokeniser
        
    Returns:
        dict: Dictionnaire contenant les tokens de mots et phrases
    """
    words = word_tokenize(text, language='french')
    sentences = sent_tokenize(text, language='french')
    
    return {
        'words': words,
        'sentences': sentences
    }

def normalize_text(text):
    """
    Normalise le texte selon les consignes :
    - Conversion en minuscules
    - Suppression de la ponctuation
    - Suppression des espaces multiples
    
    Args:
        text (str): Le texte à normaliser
        
    Returns:
        str: Le texte normalisé
    """
    # Conversion en minuscules
    text = text.lower()
    
    # Suppression de la ponctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Suppression des espaces multiples
    text = re.sub(r'\s+', ' ', text)
    
    # Suppression des espaces en début et fin
    text = text.strip()
    
    return text

def remove_stopwords(tokens, language='french'):
    """
    Retire les mots vides du français.
    
    Args:
        tokens (list): Liste des tokens à filtrer
        language (str): Langue des stop words (défaut: 'french')
        
    Returns:
        list: Liste des tokens sans les mots vides
    """
    stop_words = set(stopwords.words(language))
    
    # Filtrer les tokens qui ne sont pas des mots vides
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    
    return filtered_tokens

def stem_tokens(tokens, language='french'):
    """
    Réduit les mots à leur racine.
    
    Args:
        tokens (list): Liste des tokens à raciner
        language (str): Langue pour le stemmer (défaut: 'french')
        
    Returns:
        list: Liste des tokens racinés
    """
    stemmer = SnowballStemmer(language)
    
    # Appliquer le stemming à chaque token
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    return stemmed_tokens

def preprocess_message(text):
    """
    Fonction principale qui applique tout le preprocessing.
    
    Args:
        text (str): Le message à préprocesser
        
    Returns:
        dict: Dictionnaire contenant toutes les étapes du preprocessing
    """
    print(f"\n📝 Message original: '{text}'")
    
    # 1. Tokenisation
    tokens_data = tokenize_message(text)
    print(f"🔤 Tokens (mots): {tokens_data['words']}")
    print(f"📄 Tokens (phrases): {tokens_data['sentences']}")
    
    # 2. Normalisation
    normalized_text = normalize_text(text)
    print(f"🔄 Texte normalisé: '{normalized_text}'")
    
    # 3. Tokenisation du texte normalisé
    normalized_tokens = word_tokenize(normalized_text, language='french')
    print(f"🔤 Tokens normalisés: {normalized_tokens}")
    
    # 4. Suppression des mots vides
    filtered_tokens = remove_stopwords(normalized_tokens)
    print(f"🚫 Sans mots vides: {filtered_tokens}")
    
    # 5. Stemming
    stemmed_tokens = stem_tokens(filtered_tokens)
    print(f"🌱 Après stemming: {stemmed_tokens}")
    
    return {
        'original': text,
        'tokens': tokens_data,
        'normalized': normalized_text,
        'normalized_tokens': normalized_tokens,
        'filtered_tokens': filtered_tokens,
        'stemmed_tokens': stemmed_tokens
    }

# Tests selon les consignes
if __name__ == "__main__":
    print("🤖 Module de Preprocessing NLTK pour ChatBot")
    print("=" * 60)
    
    # Messages de test selon les consignes
    test_messages = [
        "Bonjour ! J'aimerais commander une pizza margherita s'il vous plaît.",
        "Pouvez-vous me dire les horaires d'ouverture de votre restaurant ?",
        "Je voudrais annuler ma commande précédente, merci beaucoup."
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n🧪 TEST {i}")
        print("-" * 40)
        result = preprocess_message(message)
        print("-" * 60)
    
    print("\n✅ Tests terminés!")