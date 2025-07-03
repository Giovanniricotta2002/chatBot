# Chatbot Intent Classification – Guide d'installation et d'exécution

Ce projet propose un pipeline complet pour la classification d'intentions en français, avec enrichissement dynamique du dataset, prétraitement avancé, et évaluation détaillée.

## Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)

## Installation

1. **Cloner le dépôt ou placer les fichiers dans un dossier**
1. Installer les dépendances :

```bash
pip install -r requirements.txt
```

3. (Optionnel) Installer le modèle spaCy français si vous souhaitez utiliser les fonctions avancées NLP :

```bash
python -m spacy download fr_core_news_sm
```

## Enrichissement du dataset

Pour générer ou enrichir automatiquement le dataset YAML avec des exemples variés (y compris des phrases dynamiques avec Faker) :

```bash
python3 enrich_dataset.py
```

Cela mettra à jour le fichier `dataset.yaml` avec de nouveaux exemples pour chaque intention.

## Exécution du pipeline principal

Pour entraîner, évaluer et tester le classificateur d'intentions :

```bash
python3 rendu3.py
```

Le script :

- Charge le dataset YAML
- Prétraite les phrases
- Entraîne le modèle de classification
- Affiche un rapport d'évaluation détaillé (précision, rappel, F1, matrice de confusion)
- Effectue des tests obligatoires sur des phrases clés

## Exemple de sortie (rapport d'évaluation)

```bash
[IntentClassifierEvaluator] Début de l'évaluation...
[IntentClassifierEvaluator] Nombre total d'exemples: ...
[IntentClassifierEvaluator] Nombre d'intentions: ...
[IntentClassifierEvaluator] Détail des classes: ...

📊 Données d'entraînement préparées:
   - Nombre d'exemples: ...
   - Intentions disponibles: ...
     • salutation: ... exemples
     • menu: ... exemples
     ...
[IntentClassifierEvaluator] Split train/test stratifié 80/20...
[IntentClassifierEvaluator] Taille train: ..., test: ...
[IntentClassifierEvaluator] Prédiction sur le test set...

[IntentClassifierEvaluator] Résultats sur le test set:
  - Précision: 0.95
  - Précision (weighted): 0.95
  - Rappel (weighted): 0.95
  - F1-score (weighted): 0.95

Matrice de confusion:
[[5 0 0 ...]
 [0 4 0 ...]
 ...]

Rapport détaillé:
              precision    recall  f1-score   support
   ...

🎯 Objectif atteint ! Précision > 80%

[IntentClassifierEvaluator] Évaluation terminée!
============================================================

[IntentClassifierEvaluator] Lancement des tests obligatoires...
...
✅ Tous les tests obligatoires ont été exécutés.
============================================================
```

> **Remarque :** Les valeurs exactes dépendent de votre dataset et de l'enrichissement généré.

## Personnalisation

- Modifiez `dataset.yaml` pour ajouter/éditer des intentions ou exemples.
- Modifiez `enrich_dataset.py` pour ajuster les templates ou la génération dynamique.

## Rapport d'évaluation avec métriques

```bash
$ python3 rendu3.py

📂 Contenu du fichier YAML:
intentions:
  au_revoir:
  - merci beaucoup
  - merci et au revoir
  - merci et à bientôt
  - bonne soirée
  - merci et à plus
  - bonne continuation
  - merci et bonne nuit
  - merci et bonne continuation
  - à une prochaine fois
  - merci et à tout à l'heure
  - à bientôt
  - merci
  - merci pour tout
  - bonne fin de journée
  - au revoir
  - à la prochaine fois
  - à plus
  - merci et bonne fin de journée
  - bonne nuit
  - merci et bonne journée
  - à la prochaine
  - à tout à l'heure
  - bonne journée
  - Merci Alphonse !
  - merci et à une prochaine fois
  - merci et à la prochaine
  - à plus tard
  - merci et bonne soirée
  - bye
  - merci et à plus tard
  commande:
  - je veux commander pour une réunion s'il vous plaît
  - je veux commander pour demain s'il vous plaît
  - je passe commande pour emporter
  - je veux commander une entrée
  - je veux commander une salade
  - je veux commander un dessert pour ce soir
  - je veux commander un plat principal pour emporter
  - commande pour deux personnes s'il vous plaît
  - je passe commande pour ce soir
  - je commande une pizza pour emporter
  - je veux commander une pizza pour emporter
  - je veux commander pour un événement pour emporter
  - je veux
  - je voudrais commander pour ce soir
  - je passe commande s'il vous plaît
  - je commande
  - je veux commander une pizza
  - je veux passer commande pour emporter
  - je passe commande
  - commande pour deux personnes pour emporter
  - je passe une commande groupée pour ce soir
  - j'aimerais commander s'il vous plaît
  - je commande une pizza
  - je veux commander pour un déjeuner s'il vous plaît
  - commande pour deux personnes
  - je veux commander pour un événement s'il vous plaît
  - j'aimerais
  - puis-je passer une commande s'il vous plaît
  - j'aimerais commander pour emporter
  - je veux commander pour ce midi pour emporter
  horaires:
  - à quelle heure fermez-vous le samedi ?
  - quand fermez-vous
  - à quelle heure puis-je venir ?
  - à quelle heure puis-je commander ?
  - quels sont vos horaires
  - êtes-vous ouverts les jours fériés ?
  - c'est ouvert le dimanche
  - quels sont vos horaires d'ouverture ?
  - vos horaires exceptionnels ?
  - fermeture
  - à quelle heure se termine le service ?
  - à quelle heure ouvrez-vous
  - êtes-vous ouverts le soir ?
  - êtes-vous ouverts ce soir ?
  - horaire
  - vos heures d'ouverture ?
  - êtes-vous ouverts en semaine ?
  - vos horaires spéciaux ?
  - vos horaires pour les fêtes ?
  - heures d'ouverture
  - vos horaires pendant les vacances ?
  - ouvert
  - quand puis-je venir ?
  - à quelle heure fermez-vous le soir
  - vos horaires
  - êtes-vous ouverts pendant les vacances ?
  - êtes-vous ouverts le midi ?
  - vos horaires d'ouverture le week-end ?
  - êtes-vous ouverts aujourd'hui ?
  - quels sont vos horaires de fermeture ?
  menu:
  - je veux voir ce que vous servez s'il vous plaît
  - quels plats recommandez-vous ? s'il vous plaît
  - je veux voir la carte complète
  - carte s'il vous plaît
  - je veux voir la carte spéciale s'il vous plaît
  - montrez-moi la carte s'il vous plaît
  - affichez la carte
  - menu
  - qu'avez-vous à proposer ?
  - montrez-moi vos spécialités s'il vous plaît
  - montrez-moi le menu
  - je veux voir la carte du jour s'il vous plaît
  - qu'est-ce qu'il y a à manger s'il vous plaît
  - quels sont vos plats s'il vous plaît
  - je veux connaître vos menus
  - je veux voir le menu
  - je veux voir la carte complète s'il vous plaît
  - je souhaite voir la carte s'il vous plaît
  - je souhaite voir la carte
  - que proposez-vous
  - affichez la carte s'il vous plaît
  - que proposez-vous s'il vous plaît
  - je veux connaître vos menus s'il vous plaît
  - je veux voir la carte des desserts s'il vous plaît
  - montrez-moi le menu s'il vous plaît
  - vos plats s'il vous plaît
  - carte
  - je veux voir le menu s'il vous plaît
  - vos plats
  - qu'est-ce qu'il y a à manger
  prix:
  - quel est le prix
  - combien coûte une pizza 4 fromages ?
  - combien coûte une pizza calzone ?
  - prix d'une pizza
  - combien
  - quel est le prix total ?
  - combien coûte une pizza
  - combien coûte un plat principal ?
  - combien coûte une pizza hawaïenne ?
  - combien coûte une pizza napolitaine ?
  - combien coûte une pizza royale ?
  - combien coûte une entrée ?
  - coût
  - combien coûte une pizza spéciale ?
  - combien coûte une boisson ?
  - combien coûte un menu complet ?
  - prix
  - combien dois-je payer ?
  - combien coûte un menu enfant ?
  - combien pour deux menus ?
  - combien coûte une pizza margherita ?
  - combien coûte une pizza végétarienne ?
  - combien ça coûte
  - combien coûte un dessert ?
  - quel est le tarif d'un menu ?
  - quel est le prix d'un dessert ?
  - combien coûte une pizza pepperoni ?
  - tarif
  - c'est combien
  - combien pour une boisson ?
  salutation:
  - salut à toutes tout le monde
  - bonjour cher ami à tous
  - coucou tout le monde
  - bonjour cher ami
  - salut à tous tout le monde
  - bien le bonjour tout le monde
  - salut la team à tous
  - salut les copains tout le monde
  - bonjour à tous et à toutes à tous
  - hey à tous
  - salutations tout le monde
  - bien le bonjour à tous
  - Salut
  - bonne soirée à tous
  - bonjour à tous à tous
  - coucou
  - bien le bonjour
  - salutations
  - Bonjour
  - bonsoir
  - salut à tous
  - hello
  - hey tout le monde
  - bonjour tout le monde
  - Hello
  - bonjour tout le monde tout le monde
  - Bonsoir
  - salut à toi tout le monde
  - hello tout le monde
  - salutations à tous

✅ Fichier YAML lu avec succès!

🤖 Classe IntentClassifier - Module de Classification d'Intentions
============================================================
📦 Préparation des données d'entraînement...

[IntentClassifierEvaluator] Début de l'évaluation...
[IntentClassifierEvaluator] Nombre total d'exemples: 180
[IntentClassifierEvaluator] Nombre d'intentions: 6
[IntentClassifierEvaluator] Détail des classes: Counter({'salutation': 30, 'menu': 30, 'commande': 30, 'horaires': 30, 'prix': 30, 'au_revoir': 30})

📊 Données d'entraînement préparées:
   - Nombre d'exemples: 180
   - Intentions disponibles: {'salutation', 'commande', 'horaires', 'au_revoir', 'menu', 'prix'}
     • salutation: 30 exemples
     • commande: 30 exemples
     • horaires: 30 exemples
     • au_revoir: 30 exemples
     • menu: 30 exemples
     • prix: 30 exemples
[IntentClassifierEvaluator] Split train/test stratifié 80/20...
[IntentClassifierEvaluator] Taille train: 144, test: 36
[IntentClassifier] Entraînement sur 144 exemples...
[IntentClassifier] Entraînement terminé.
[IntentClassifierEvaluator] Prédiction sur le test set...

[IntentClassifierEvaluator] Résultats sur le test set:
  - Précision: 1.00
  - Précision (weighted): 1.00
  - Rappel (weighted): 1.00
  - F1-score (weighted): 1.00

Matrice de confusion:
[[6 0 0 0 0 0]
 [0 6 0 0 0 0]
 [0 0 6 0 0 0]
 [0 0 0 6 0 0]
 [0 0 0 0 6 0]
 [0 0 0 0 0 6]]

Rapport détaillé:
              precision    recall  f1-score   support

   au_revoir       1.00      1.00      1.00         6
    commande       1.00      1.00      1.00         6
    horaires       1.00      1.00      1.00         6
        menu       1.00      1.00      1.00         6
        prix       1.00      1.00      1.00         6
  salutation       1.00      1.00      1.00         6

    accuracy                           1.00        36
   macro avg       1.00      1.00      1.00        36
weighted avg       1.00      1.00      1.00        36

🎯 Objectif atteint ! Précision > 80%

[IntentClassifierEvaluator] Évaluation terminée!
============================================================

[IntentClassifierEvaluator] Lancement des tests obligatoires...
[IntentClassifierEvaluator] Nombre d'exemples d'entraînement: 180
[IntentClassifierEvaluator] Nombre d'intentions: 6
[IntentClassifier] Entraînement sur 180 exemples...
[IntentClassifier] Entraînement terminé.
[IntentClassifierEvaluator] Classifieur entraîné sur tout le dataset pour les tests obligatoires.

🧪 Tests obligatoires sur des phrases personnalisées :
[IntentClassifierEvaluator] Test sur: 'Bonjour !'
[IntentClassifier] Prédiction pour: 'Bonjour !'
  → 'Bonjour !'  =>  intention prédite : salutation
[IntentClassifierEvaluator] Test sur: 'Salut à tous'
[IntentClassifier] Prédiction pour: 'Salut à tous'
  → 'Salut à tous'  =>  intention prédite : salutation
[IntentClassifierEvaluator] Test sur: 'Coucou, comment ça va ?'
[IntentClassifier] Prédiction pour: 'Coucou, comment ça va ?'
  → 'Coucou, comment ça va ?'  =>  intention prédite : salutation
[IntentClassifierEvaluator] Test sur: 'Hey tout le monde'
[IntentClassifier] Prédiction pour: 'Hey tout le monde'
  → 'Hey tout le monde'  =>  intention prédite : salutation
[IntentClassifierEvaluator] Test sur: 'Puis-je voir la carte ?'
[IntentClassifier] Prédiction pour: 'Puis-je voir la carte ?'
  → 'Puis-je voir la carte ?'  =>  intention prédite : menu
[IntentClassifierEvaluator] Test sur: 'Qu'est-ce qu'il y a à manger ?'
[IntentClassifier] Prédiction pour: 'Qu'est-ce qu'il y a à manger ?'
  → 'Qu'est-ce qu'il y a à manger ?'  =>  intention prédite : menu
[IntentClassifierEvaluator] Test sur: 'Affichez-moi le menu s'il vous plaît'
[IntentClassifier] Prédiction pour: 'Affichez-moi le menu s'il vous plaît'
  → 'Affichez-moi le menu s'il vous plaît'  =>  intention prédite : menu
[IntentClassifierEvaluator] Test sur: 'Je veux commander trois pizzas margherita'
[IntentClassifier] Prédiction pour: 'Je veux commander trois pizzas margherita'
  → 'Je veux commander trois pizzas margherita'  =>  intention prédite : commande
[IntentClassifierEvaluator] Test sur: 'Je voudrais commander un menu pour deux personnes'
[IntentClassifier] Prédiction pour: 'Je voudrais commander un menu pour deux personnes'
  → 'Je voudrais commander un menu pour deux personnes'  =>  intention prédite : commande
[IntentClassifierEvaluator] Test sur: 'Commande pour emporter, s'il vous plaît'
[IntentClassifier] Prédiction pour: 'Commande pour emporter, s'il vous plaît'
  → 'Commande pour emporter, s'il vous plaît'  =>  intention prédite : commande
[IntentClassifierEvaluator] Test sur: 'À quelle heure ouvrez-vous le matin ?'
[IntentClassifier] Prédiction pour: 'À quelle heure ouvrez-vous le matin ?'
  → 'À quelle heure ouvrez-vous le matin ?'  =>  intention prédite : horaires
[IntentClassifierEvaluator] Test sur: 'Êtes-vous ouverts le dimanche ?'
[IntentClassifier] Prédiction pour: 'Êtes-vous ouverts le dimanche ?'
  → 'Êtes-vous ouverts le dimanche ?'  =>  intention prédite : horaires
[IntentClassifierEvaluator] Test sur: 'Quand fermez-vous ce soir ?'
[IntentClassifier] Prédiction pour: 'Quand fermez-vous ce soir ?'
  → 'Quand fermez-vous ce soir ?'  =>  intention prédite : horaires
[IntentClassifierEvaluator] Test sur: 'Quel est le prix d'une pizza 4 fromages ?'
[IntentClassifier] Prédiction pour: 'Quel est le prix d'une pizza 4 fromages ?'
  → 'Quel est le prix d'une pizza 4 fromages ?'  =>  intention prédite : prix
[IntentClassifierEvaluator] Test sur: 'C'est combien pour un menu complet ?'
[IntentClassifier] Prédiction pour: 'C'est combien pour un menu complet ?'
  → 'C'est combien pour un menu complet ?'  =>  intention prédite : prix
[IntentClassifierEvaluator] Test sur: 'Combien coûte une boisson ?'
[IntentClassifier] Prédiction pour: 'Combien coûte une boisson ?'
  → 'Combien coûte une boisson ?'  =>  intention prédite : prix
[IntentClassifierEvaluator] Test sur: 'Merci, au revoir !'
[IntentClassifier] Prédiction pour: 'Merci, au revoir !'
  → 'Merci, au revoir !'  =>  intention prédite : au_revoir
[IntentClassifierEvaluator] Test sur: 'Bonne journée à vous'
[IntentClassifier] Prédiction pour: 'Bonne journée à vous'
  → 'Bonne journée à vous'  =>  intention prédite : au_revoir
[IntentClassifierEvaluator] Test sur: 'À la prochaine !'
[IntentClassifier] Prédiction pour: 'À la prochaine !'
  → 'À la prochaine !'  =>  intention prédite : au_revoir
[IntentClassifierEvaluator] Test sur: 'Bye bye'
[IntentClassifier] Prédiction pour: 'Bye bye'
  → 'Bye bye'  =>  intention prédite : au_revoir

✅ Tous les tests obligatoires ont été exécutés.
============================================================
```
