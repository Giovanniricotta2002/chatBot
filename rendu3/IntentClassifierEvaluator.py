"""
IntentClassifierEvaluator
========================

Module d'évaluation pour classificateur d'intentions de chatbot.

Ce module fournit la classe IntentClassifierEvaluator, qui permet d'évaluer un modèle de classification d'intentions (scikit-learn compatible) sur un jeu de données français, avec split train/test ou Leave-One-Out, et tests obligatoires.

Dépendances :
- scikit-learn
- numpy
- collections

Exemple d'utilisation :
    >>> evaluator = IntentClassifierEvaluator(clf, texts, labels)
    >>> evaluator.evaluate()
    >>> evaluator.test_obligatoires()
"""

from collections import Counter
import numpy as np
from sklearn.model_selection import train_test_split, LeaveOneOut, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

class IntentClassifierEvaluator:
    """
    Classe utilitaire pour évaluer un classificateur d'intentions (IntentClassifier)
    sur un jeu de données, avec gestion automatique du split train/test ou
    validation croisée Leave-One-Out selon la taille du dataset.
    Fournit aussi des tests obligatoires sur des phrases personnalisées.
    """
    def __init__(self, classifier, texts, labels):
        """
        Initialise l'évaluateur avec un classificateur, les textes et les labels.
        
        Args:
            classifier: Instance de la classe IntentClassifier (ou pipeline compatible sklearn).
            texts (list of str): Liste des phrases d'entraînement.
            labels (list of str): Liste des labels/intents correspondants.
        """
        self.classifier = classifier
        self.texts = texts
        self.labels = labels

    def evaluate(self):
        print("\n[IntentClassifierEvaluator] Début de l'évaluation...")
        print(f"[IntentClassifierEvaluator] Nombre total d'exemples: {len(self.texts)}")
        print(f"[IntentClassifierEvaluator] Nombre d'intentions: {len(set(self.labels))}")
        print(f"[IntentClassifierEvaluator] Détail des classes: {Counter(self.labels)}")

        class_counts = Counter(self.labels)
        min_samples_per_class = min(class_counts.values())
        total_classes = len(class_counts)
        test_size = max(1, int(0.2 * len(self.texts)))

        print(f"\n📊 Données d'entraînement préparées:")
        print(f"   - Nombre d'exemples: {len(self.texts)}")
        print(f"   - Intentions disponibles: {set(self.labels)}")
        for intention in set(self.labels):
            count = self.labels.count(intention)
            print(f"     • {intention}: {count} exemples")

        if len(self.texts) == 0:
            print("❌ Aucune donnée d'entraînement trouvée dans le dataset!")
            return

        if test_size < total_classes or min_samples_per_class < 2:
            print("\n⚠️  Dataset trop petit ou test set trop petit pour un split train/test stratifié.")
            print(f"   - Total d'exemples: {len(self.texts)}")
            print(f"   - Nombre de classes: {total_classes}")
            print(f"   - Minimum d'exemples par classe: {min_samples_per_class}")
            print(f"   - Taille du test set calculée: {test_size}")
            print(f"   - Utilisation de validation croisée Leave-One-Out.")
            loo = LeaveOneOut()
            print("[IntentClassifierEvaluator] Lancement de la validation croisée Leave-One-Out...")
            scores = cross_val_score(self.classifier.pipeline, np.array(self.texts), np.array(self.labels), cv=loo, scoring='accuracy')
            print(f"[IntentClassifierEvaluator] Résultats Leave-One-Out: scores={scores}")
            print(f"Précision Leave-One-Out: {scores.mean():.2f} ± {scores.std():.2f}")
            if scores.mean() > 0.8:
                print(f"🎯 Objectif atteint ! Précision > 80%")
            else:
                print(f"❌ Objectif non atteint. Précision: {scores.mean()*100:.1f}%")
        else:
            print("[IntentClassifierEvaluator] Split train/test stratifié 80/20...")
            X_train, X_test, y_train, y_test = train_test_split(
                self.texts, self.labels, test_size=0.2, random_state=42, stratify=self.labels)
            print(f"[IntentClassifierEvaluator] Taille train: {len(X_train)}, test: {len(X_test)}")
            self.classifier.train(X_train, y_train)
            print("[IntentClassifierEvaluator] Prédiction sur le test set...")
            y_pred = self.classifier.pipeline.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
            rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
            f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
            print(f"\n[IntentClassifierEvaluator] Résultats sur le test set:")
            print(f"  - Précision: {acc:.2f}")
            print(f"  - Précision (weighted): {prec:.2f}")
            print(f"  - Rappel (weighted): {rec:.2f}")
            print(f"  - F1-score (weighted): {f1:.2f}")
            print(f"\nMatrice de confusion:")
            print(confusion_matrix(y_test, y_pred))
            print(f"\nRapport détaillé:\n{classification_report(y_test, y_pred)}")
            if acc > 0.8:
                print(f"🎯 Objectif atteint ! Précision > 80%")
            else:
                print(f"❌ Objectif non atteint. Précision: {acc*100:.1f}%")
        print("\n[IntentClassifierEvaluator] Évaluation terminée!")
        print("=" * 60)

    def test_obligatoires(self):
        print("\n[IntentClassifierEvaluator] Lancement des tests obligatoires...")
        print(f"[IntentClassifierEvaluator] Nombre d'exemples d'entraînement: {len(self.texts)}")
        print(f"[IntentClassifierEvaluator] Nombre d'intentions: {len(set(self.labels))}")
        # Toujours entraîner sur tout le dataset avant les tests obligatoires
        self.classifier.train(self.texts, self.labels)
        print("[IntentClassifierEvaluator] Classifieur entraîné sur tout le dataset pour les tests obligatoires.")
        print("\n🧪 Tests obligatoires sur des phrases personnalisées :")
        test_phrases = [
            # salutation
            "Bonjour !",
            "Salut à tous",
            "Coucou, comment ça va ?",
            "Hey tout le monde",
            # menu
            "Puis-je voir la carte ?",
            "Qu'est-ce qu'il y a à manger ?",
            "Affichez-moi le menu s'il vous plaît",
            # commande
            "Je veux commander trois pizzas margherita",
            "Je voudrais commander un menu pour deux personnes",
            "Commande pour emporter, s'il vous plaît",
            # horaires
            "À quelle heure ouvrez-vous le matin ?",
            "Êtes-vous ouverts le dimanche ?",
            "Quand fermez-vous ce soir ?",
            # prix
            "Quel est le prix d'une pizza 4 fromages ?",
            "C'est combien pour un menu complet ?",
            "Combien coûte une boisson ?",
            # au_revoir
            "Merci, au revoir !",
            "Bonne journée à vous",
            "À la prochaine !",
            "Bye bye"
        ]
        for phrase in test_phrases:
            print(f"[IntentClassifierEvaluator] Test sur: '{phrase}'")
            prediction = self.classifier.predict(phrase)
            print(f"  → '{phrase}'  =>  intention prédite : {prediction[0]}")
        print("\n✅ Tous les tests obligatoires ont été exécutés.")
        print("=" * 60)
