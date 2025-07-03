"""
rendu3
======

Script principal pour l'orchestration du pipeline de classification d'intentions chatbot.

Ce script charge le dataset YAML, initialise les modules de prétraitement, classification, NLP et évaluation, et exécute les tests principaux.

Dépendances :
- yaml
- intent_classifier
- TextPreprocessor
- nlp_processor
- IntentClassifierEvaluator

Exemple d'utilisation :
    $ python rendu3.py
"""

from TextPreprocessor import TextPreprocessor
from nlp_processor import NLPProcessor
from intent_classifier import IntentClassifier
from IntentClassifierEvaluator import IntentClassifierEvaluator
import yaml

def readFile():
    with open('dataset.yaml', 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
            print("📂 Contenu du fichier YAML:")
            print(yaml.dump(data, default_flow_style=False, allow_unicode=True))
            return data
        except yaml.YAMLError as e:
            print(f"Erreur lors de la lecture du fichier YAML: {e}")
            return None

def classify_intent_with_preprocessing(message, preprocessor, classifier):
    """
    Applique le préprocessing puis la classification d'intention.
    Args:
        message (str): Le message utilisateur à analyser.
        preprocessor (TextPreprocessor): Instance du préprocesseur.
        classifier (IntentClassifier): Instance du classificateur.
    Returns:
        tuple: (intention prédite, probabilités)
    """
    processed_message = preprocessor.normalize_text(message)
    intent = classifier.predict(processed_message)
    confidence = classifier.predict_proba(processed_message)
    return intent, confidence

# Tests et exemples d'utilisation
if __name__ == "__main__":
    # Charger et afficher le dataset
    dataset = readFile()
    print("✅ Fichier YAML lu avec succès!")
    
    print("\n🤖 Classe IntentClassifier - Module de Classification d'Intentions")
    print("=" * 60)
    classifier = IntentClassifier()
    
    print("📦 Préparation des données d'entraînement...")
    # for intent_data in dataset:
    #     intent = intent_data['intent']
    #     examples = intent_data['examples']
    #     classifier.train(intent, examples)
    
    # Préparer les données d'entraînement à partir du dataset YAML
    texts = []
    labels = []
    if dataset and 'intentions' in dataset:
        for intention, examples in dataset['intentions'].items():
            for example in examples:
                texts.append(example)
                labels.append(intention)

    if len(texts) > 0:
        # Utilisation de la classe d'évaluation
        evaluator = IntentClassifierEvaluator(classifier, texts, labels)
        evaluator.evaluate()
        evaluator.test_obligatoires()
    else:
        print("❌ Aucune donnée d'entraînement trouvée dans le dataset!")