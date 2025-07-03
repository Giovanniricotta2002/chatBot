"""
nlp_processor
=============

Module d'analyse linguistique avancée pour chatbot français utilisant spaCy.

Ce module fournit la classe NLPProcessor, qui permet d'effectuer l'analyse morpho-syntaxique, l'extraction d'entités nommées et l'analyse des dépendances sur des textes en français.

Dépendances :
- spacy

Exemple d'utilisation :
    >>> nlp = NLPProcessor()
    >>> result = nlp.full_analysis("Bonjour, je m'appelle Paul.")
"""

import spacy
from typing import Dict, List, Any

class NLPProcessor:
    """
    Classe pour l'analyse linguistique avancée avec spaCy.
    
    Cette classe fournit des méthodes pour l'analyse morpho-syntaxique,
    la reconnaissance d'entités nommées et l'analyse des dépendances syntaxiques.
    """
    
    def __init__(self, model_name="fr_core_news_sm"):
        print(f"[NLPProcessor] Chargement du modèle spaCy '{model_name}'...")
        """
        Initialise le processeur NLP.
        
        Args:
            model_name (str): Nom du modèle spaCy à charger
        """
        try:
            self.nlp = spacy.load(model_name)
            print(f"✅ Modèle spaCy '{model_name}' chargé avec succès")
        except OSError:
            print(f"❌ Erreur: Le modèle '{model_name}' n'est pas installé")
            print("💡 Installez-le avec: python -m spacy download fr_core_news_sm")
            raise
    
    def analyze_pos(self, text: str) -> Dict[str, Any]:
        print(f"[NLPProcessor] Analyse POS pour: '{text}'")
        """
        Analyse les parties du discours et retourne les entités nommées.
        
        Args:
            text (str): Le texte à analyser
            
        Returns:
            dict: Dictionnaire contenant l'analyse POS et les entités
        """
        doc = self.nlp(text)
        
        # Analyse des parties du discours
        pos_analysis = []
        for token in doc:
            pos_analysis.append({
                'text': token.text,
                'lemma': token.lemma_,
                'pos': token.pos_,
                'tag': token.tag_,
                'dep': token.dep_,
                'is_alpha': token.is_alpha,
                'is_stop': token.is_stop,
                'is_punct': token.is_punct,
                'shape': token.shape_
            })
        
        # Entités nommées
        entities = []
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_,
                'start': ent.start_char,
                'end': ent.end_char
            })
        
        return {
            'pos_analysis': pos_analysis,
            'entities': entities,
            'doc_info': {
                'length': len(doc),
                'sentences': len(list(doc.sents))
            }
        }
    
    def extract_entities(self, text: str) -> Dict[str, List[Dict]]:
        print(f"[NLPProcessor] Extraction des entités pour: '{text}'")
        """
        Extraire personnes, lieux, organisations, etc.
        
        Args:
            text (str): Le texte à analyser
            
        Returns:
            dict: Dictionnaire des entités par catégorie
        """
        doc = self.nlp(text)
        
        entities_by_type = {
            'PERSON': [],      # Personnes
            'ORG': [],         # Organisations
            'GPE': [],         # Entités géopolitiques (pays, villes)
            'LOC': [],         # Lieux
            'DATE': [],        # Dates
            'TIME': [],        # Temps
            'MONEY': [],       # Montants
            'MISC': []         # Divers
        }
        
        for ent in doc.ents:
            entity_info = {
                'text': ent.text,
                'start': ent.start_char,
                'end': ent.end_char,
                'label_': ent.label_
            }
            
            if ent.label_ in entities_by_type:
                entities_by_type[ent.label_].append(entity_info)
            else:
                entities_by_type['MISC'].append(entity_info)
        
        # Supprimer les catégories vides
        return {k: v for k, v in entities_by_type.items() if v}
    
    def analyze_dependencies(self, text: str) -> Dict[str, Any]:
        print(f"[NLPProcessor] Analyse des dépendances pour: '{text}'")
        """
        Analyser la structure syntaxique.
        
        Args:
            text (str): Le texte à analyser
            
        Returns:
            dict: Dictionnaire contenant l'analyse des dépendances
        """
        doc = self.nlp(text)
        
        dependencies = []
        for token in doc:
            dep_info = {
                'text': token.text,
                'pos': token.pos_,
                'dep': token.dep_,
                'head': token.head.text,
                'children': [child.text for child in token.children],
                'is_root': token.dep_ == 'ROOT'
            }
            dependencies.append(dep_info)
        
        # Identifier les racines (verbes principaux)
        roots = [token.text for token in doc if token.dep_ == 'ROOT']
        
        # Phrases
        sentences = []
        for sent in doc.sents:
            sent_info = {
                'text': sent.text,
                'root': sent.root.text,
                'start': sent.start_char,
                'end': sent.end_char
            }
            sentences.append(sent_info)
        
        return {
            'dependencies': dependencies,
            'roots': roots,
            'sentences': sentences,
            'tree_structure': self._build_dependency_tree(doc)
        }
    
    def _build_dependency_tree(self, doc) -> List[Dict]:
        """
        Construit un arbre des dépendances simplifié.
        
        Args:
            doc: Document spaCy
            
        Returns:
            list: Structure arborescente des dépendances
        """
        tree = []
        for token in doc:
            if token.dep_ == 'ROOT':
                tree.append(self._get_subtree(token))
        return tree
    
    def _get_subtree(self, token) -> Dict:
        """
        Récupère le sous-arbre d'un token.
        
        Args:
            token: Token spaCy
            
        Returns:
            dict: Sous-arbre du token
        """
        return {
            'text': token.text,
            'pos': token.pos_,
            'dep': token.dep_,
            'children': [self._get_subtree(child) for child in token.children]
        }
    
    def full_analysis(self, text: str, verbose: bool = True) -> Dict[str, Any]:
        print(f"[NLPProcessor] Analyse complète pour: '{text}'")
        """
        Analyse complète d'un texte.
        
        Args:
            text (str): Le texte à analyser
            verbose (bool): Afficher les détails
            
        Returns:
            dict: Analyse complète
        """
        if verbose:
            print(f"\n📝 Analyse du texte: '{text}'")
            print("=" * 60)
        
        # Analyses
        pos_result = self.analyze_pos(text)
        entities_result = self.extract_entities(text)
        dependencies_result = self.analyze_dependencies(text)
        
        if verbose:
            self._print_analysis_results(pos_result, entities_result, dependencies_result)
        
        return {
            'original_text': text,
            'pos_analysis': pos_result,
            'entities': entities_result,
            'dependencies': dependencies_result
        }
    
    def _print_analysis_results(self, pos_result, entities_result, dependencies_result):
        """Affiche les résultats d'analyse de manière formatée."""
        
        print("\n🔤 ANALYSE MORPHO-SYNTAXIQUE:")
        print("-" * 40)
        for token in pos_result['pos_analysis']:
            if token['is_alpha']:  # Afficher seulement les mots
                print(f"  {token['text']:15} | {token['pos']:8} | {token['lemma']:15} | {token['dep']:10}")
        
        print("\n👤 ENTITÉS NOMMÉES:")
        print("-" * 40)
        if entities_result:
            for entity_type, entities in entities_result.items():
                print(f"  {entity_type}:")
                for entity in entities:
                    print(f"    - {entity['text']} ({entity['label_']})")
        else:
            print("  Aucune entité détectée")
        
        print("\n🌳 DÉPENDANCES SYNTAXIQUES:")
        print("-" * 40)
        for sent in dependencies_result['sentences']:
            print(f"  Phrase: {sent['text']}")
            print(f"  Racine: {sent['root']}")
        
        print("\n🔗 RELATIONS:")
        print("-" * 40)
        for dep in dependencies_result['dependencies']:
            if dep['is_root']:
                print(f"  ROOT: {dep['text']} ({dep['pos']})")
            elif dep['dep'] in ['nsubj', 'dobj', 'iobj']:  # Relations importantes
                print(f"  {dep['dep']}: {dep['text']} ← {dep['head']}")


# Tests et exemples d'utilisation
if __name__ == "__main__":
    print("🧠 Module NLP Processor - Analyse linguistique avec spaCy")
    print("=" * 70)
    
    # Initialiser le processeur
    try:
        processor = NLPProcessor()
    except OSError:
        print("❌ Impossible de charger le modèle spaCy")
        exit(1)
    
    # 5 phrases de test différentes
    test_sentences = [
        "Bonjour ! J'aimerais commander une pizza margherita s'il vous plaît.",
        "Pouvez-vous me dire les horaires d'ouverture de votre restaurant ?",
        "Je voudrais annuler ma commande précédente, merci beaucoup.",
        "Marie Dupont travaille chez Google à Paris depuis janvier 2023.",
        "Le président Emmanuel Macron s'est rendu à Berlin hier pour rencontrer Angela Merkel."
    ]
    
    print(f"\n📋 Tests sur {len(test_sentences)} phrases différentes:")
    
    for i, sentence in enumerate(test_sentences, 1):
        print(f"\n{'='*70}")
        print(f"🧪 TEST {i}")
        print(f"{'='*70}")
        
        result = processor.full_analysis(sentence, verbose=True)
        
        print(f"\n✅ Test {i} terminé")
    
    print(f"\n🎉 Tous les tests terminés!")
    print("\n💡 Utilisation:")
    print("```python")
    print("processor = NLPProcessor()")
    print("result = processor.full_analysis('Votre texte ici')")
    print("entities = processor.extract_entities('Votre texte')")
    print("dependencies = processor.analyze_dependencies('Votre texte')")
    print("```")
