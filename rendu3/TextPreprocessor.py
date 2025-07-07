import nltk
import re
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

class TextPreprocessor:
    """
    Classe pour le preprocessing de texte avec NLTK.
    
    Cette classe fournit des méthodes pour nettoyer et préparer
    les messages utilisateurs pour un système de chatbot.
    """
    
    def __init__(self, language='french', download_resources=True):
        """
        Initialise le preprocesseur de texte.
        
        Args:
            language (str): Langue pour le traitement (défaut: 'french')
            download_resources (bool): Télécharger automatiquement les ressources NLTK
        """
        self.language = language
        self.stemmer = SnowballStemmer(language)
        self.stop_words = None
        
        if download_resources:
            self._download_nltk_resources()
            
        # Charger les stop words
        try:
            self.stop_words = set(stopwords.words(language))
        except LookupError:
            print(f"Attention: Stop words pour '{language}' non disponibles")
            self.stop_words = set()
    
    def _download_nltk_resources(self):
        """Télécharge les ressources NLTK nécessaires."""
        resources = ['punkt', 'stopwords']
        
        for resource in resources:
            try:
                if resource == 'punkt':
                    nltk.data.find('tokenizers/punkt')
                elif resource == 'stopwords':
                    nltk.data.find('corpora/stopwords')
            except LookupError:
                print(f"Téléchargement de la ressource '{resource}'...")
                nltk.download(resource)
    
    def tokenize_message(self, text):
        """
        Tokenise un message en mots et phrases.
        
        Args:
            text (str): Le texte à tokeniser
            
        Returns:
            dict: Dictionnaire contenant les tokens de mots et phrases
        """
        words = word_tokenize(text, language=self.language)
        sentences = sent_tokenize(text, language=self.language)
        
        return {
            'words': words,
            'sentences': sentences
        }
    
    def normalize_text(self, text):
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
    
    def remove_stopwords(self, tokens):
        """
        Retire les mots vides.
        
        Args:
            tokens (list): Liste des tokens à filtrer
            
        Returns:
            list: Liste des tokens sans les mots vides
        """
        if not self.stop_words:
            return tokens
            
        # Filtrer les tokens qui ne sont pas des mots vides
        filtered_tokens = [token for token in tokens if token.lower() not in self.stop_words]
        
        return filtered_tokens
    
    def stem_tokens(self, tokens):
        """
        Réduit les mots à leur racine.
        
        Args:
            tokens (list): Liste des tokens à raciner
            
        Returns:
            list: Liste des tokens racinés
        """
        # Appliquer le stemming à chaque token
        stemmed_tokens = [self.stemmer.stem(token) for token in tokens]
        
        return stemmed_tokens
    
    def preprocess_message(self, text, verbose=True):
        """
        Fonction principale qui applique tout le preprocessing.
        
        Args:
            text (str): Le message à préprocesser
            verbose (bool): Afficher les étapes de preprocessing
            
        Returns:
            dict: Dictionnaire contenant toutes les étapes du preprocessing
        """
        if verbose:
            print(f"\n📝 Message original: '{text}'")
        
        # 1. Tokenisation
        tokens_data = self.tokenize_message(text)
        if verbose:
            print(f"🔤 Tokens (mots): {tokens_data['words']}")
            print(f"📄 Tokens (phrases): {tokens_data['sentences']}")
        
        # 2. Normalisation
        normalized_text = self.normalize_text(text)
        if verbose:
            print(f"🔄 Texte normalisé: '{normalized_text}'")
        
        # 3. Tokenisation du texte normalisé
        normalized_tokens = word_tokenize(normalized_text, language=self.language)
        if verbose:
            print(f"🔤 Tokens normalisés: {normalized_tokens}")
        
        # 4. Suppression des mots vides
        filtered_tokens = self.remove_stopwords(normalized_tokens)
        if verbose:
            print(f"🚫 Sans mots vides: {filtered_tokens}")
        
        # 5. Stemming
        stemmed_tokens = self.stem_tokens(filtered_tokens)
        if verbose:
            print(f"🌱 Après stemming: {stemmed_tokens}")
        
        return {
            'original': text,
            'tokens': tokens_data,
            'normalized': normalized_text,
            'normalized_tokens': normalized_tokens,
            'filtered_tokens': filtered_tokens,
            'stemmed_tokens': stemmed_tokens
        }
    
    def process_batch(self, texts, verbose=False):
        """
        Traite une liste de textes en lot.
        
        Args:
            texts (list): Liste des textes à traiter
            verbose (bool): Afficher les détails pour chaque texte
            
        Returns:
            list: Liste des résultats de preprocessing
        """
        results = []
        for text in texts:
            result = self.preprocess_message(text, verbose=verbose)
            results.append(result)
        return results
