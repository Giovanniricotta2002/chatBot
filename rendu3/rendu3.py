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
    # print("🤖 Classe TextPreprocessor - Module de Preprocessing NLTK")
    # print("=" * 60)
    
    # # Initialiser le preprocesseur
    # preprocessor = TextPreprocessor(language='french', download_resources=True)
    
    # # Messages de test selon les consignes
    # test_messages = [
    #     "Bonjour ! J'aimerais commander une pizza margherita s'il vous plaît.",
    #     "Pouvez-vous me dire les horaires d'ouverture de votre restaurant ?",
    #     "Je voudrais annuler ma commande précédente, merci beaucoup.",
    #     "   Bonjour, j'ai une question concernant ma commande        .",
    # ]
    
    # print("\n📋 Tests individuels avec verbose:")
    # for i, message in enumerate(test_messages, 1):
    #     print(f"\n🧪 TEST {i}")
    #     print("-" * 40)
    #     result = preprocessor.preprocess_message(message, verbose=True)
    #     print("-" * 60)
    
    # print("\n📦 Test de traitement en lot:")
    # print("-" * 40)
    # batch_results = preprocessor.process_batch(test_messages, verbose=False)
    
    # print("*=*" * 60)
    # print("\n🧠 Tests des fonctions spaCy:")
    # print("=" * 60)
    
    # # Initialiser le processeur NLP
    # nlp_processor = NLPProcessor()
    
    # # Test d'une phrase avec spaCy
    # test_sentence = [
    #     "Marie Dupont travaille chez Google à Paris.",
    #     "Bonjour ! J'aimerais commander une pizza margherita s'il vous plaît.",
    #     "Pouvez-vous me dire les horaires d'ouverture de votre restaurant ?",
    #     "Je voudrais annuler ma commande précédente, merci beaucoup.",
    #     "Bonjour, j'ai une question concernant ma commande.",
    # ]
    
    # for i, sentence in enumerate(test_sentence, 1):
    #     print(f"\n📝 Phrase de test {i}: '{sentence}'")
        
    #     # Test analyse POS
    #     print("\n🔤 Analyse morpho-syntaxique:")
    #     pos_result = nlp_processor.analyze_pos(sentence)
    #     for token in pos_result['pos_analysis']:
    #         if token['is_alpha']:
    #             print(f"  {token['text']:12} | {token['pos']:8} | {token['lemma']:12} | {token['dep']:8}")
        
    #     # Test entités nommées
    #     print("\n👤 Entités nommées:")
    #     entities = nlp_processor.extract_entities(sentence)
    #     for entity_type, entity_list in entities.items():
    #         print(f"  {entity_type}: {[e['text'] for e in entity_list]}")
        
    #     # Test dépendances
    #     print("\n🌳 Dépendances syntaxiques:")
    #     deps = nlp_processor.analyze_dependencies(sentence)
    #     print(f"  Racines: {deps['roots']}")
    #     print("-" * 50)
        
    # print("\n✅ Tests terminés!")

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