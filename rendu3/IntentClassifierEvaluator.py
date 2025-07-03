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
        """
        Évalue le classificateur sur le dataset fourni.
        - Si le dataset est suffisant, effectue un split train/test (80/20) stratifié.
        - Sinon, effectue une validation croisée Leave-One-Out.
        Affiche précision, rappel, F1-score, matrice de confusion et rapport détaillé.
        """

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
            scores = cross_val_score(self.classifier.pipeline, np.array(self.texts), np.array(self.labels), cv=loo, scoring='accuracy')
            print(f"Précision Leave-One-Out: {scores.mean():.2f} ± {scores.std():.2f}")
            if scores.mean() > 0.8:
                print(f"🎯 Objectif atteint ! Précision > 80%")
            else:
                print(f"❌ Objectif non atteint. Précision: {scores.mean()*100:.1f}%")
        else:
            X_train, X_test, y_train, y_test = train_test_split(
                self.texts, self.labels, test_size=0.2, random_state=42, stratify=self.labels)
            self.classifier.train(X_train, y_train)
            y_pred = self.classifier.pipeline.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            prec = precision_score(y_test, y_pred, average='weighted', zero_division=0)
            rec = recall_score(y_test, y_pred, average='weighted', zero_division=0)
            f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
            print(f"\nPrécision: {acc:.2f}")
            print(f"Rappel: {rec:.2f}")
            print(f"F1-score: {f1:.2f}")
            print(f"\nMatrice de confusion:")
            print(confusion_matrix(y_test, y_pred))
            print(f"\nRapport détaillé:\n{classification_report(y_test, y_pred)}")
            if acc > 0.8:
                print(f"🎯 Objectif atteint ! Précision > 80%")
            else:
                print(f"❌ Objectif non atteint. Précision: {acc*100:.1f}%")
        print("\n✅ Évaluation terminée!")
        print("=" * 60)

    def test_obligatoires(self):
        """
        Entraîne le classificateur sur toutes les données et prédit l'intention
        pour un ensemble de phrases de test obligatoires. Affiche le résultat pour chaque phrase.
        """
        # Toujours entraîner sur tout le dataset avant les tests obligatoires
        self.classifier.train(self.texts, self.labels)
        print("\n🧪 Tests obligatoires sur des phrases personnalisées :")
        test_phrases = [
            "Bonsoir, je souhaiterais voir votre menu",
            "À quelle heure fermez-vous le dimanche ?",
            "Combien coûte une pizza Regina ?",
            "Je veux commander trois pizzas margherita"
        ]
        for phrase in test_phrases:
            prediction = self.classifier.predict(phrase)
            print(f"  → '{phrase}'  =>  intention prédite : {prediction[0]}")
