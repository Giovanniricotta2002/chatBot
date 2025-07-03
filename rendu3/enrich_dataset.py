import yaml
import random

# Synonymes et templates par intention
enrich_templates = {
    "salutation": [
        "bonjour", "salut", "hello", "coucou", "bien le bonjour", "hey", "yo", "salutations"
    ],
    "menu": [
        "je veux voir le menu", "affichez la carte", "montrez-moi le menu", "quels sont vos plats", "que proposez-vous", "qu'est-ce qu'il y a à manger", "vos plats", "carte"
    ],
    "commande": [
        "je veux commander une pizza", "je commande une pizza", "j'aimerais commander", "je voudrais commander", "puis-je passer une commande", "je passe commande", "commande pour deux personnes", "je souhaite commander un menu"
    ],
    "horaires": [
        "quels sont vos horaires", "à quelle heure ouvrez-vous", "quand fermez-vous", "heures d'ouverture", "c'est ouvert le dimanche", "vos horaires", "à quelle heure fermez-vous le soir"
    ],
    "prix": [
        "combien coûte une pizza", "quel est le prix", "c'est combien", "prix d'une pizza", "tarif", "combien ça coûte", "coût"
    ],
    "au_revoir": [
        "au revoir", "bye", "merci", "bonne journée", "à bientôt", "à la prochaine", "bonne soirée"
    ]
}

def enrich_dataset(yaml_path, n_variants=12, max_attempts_per_intent=1000):
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    for intent, variants in enrich_templates.items():
        # Crée la clé si elle n'existe pas
        if "intentions" not in data:
            data["intentions"] = {}
        if intent not in data["intentions"]:
            data["intentions"][intent] = []
        # Ajoute des variantes jusqu'à n_variants ou jusqu'à épuisement des possibilités
        current = set(data["intentions"][intent])
        attempts = 0
        while len(current) < n_variants and attempts < max_attempts_per_intent:
            phrase = random.choice(variants)
            # Ajoute un prénom, un mot de politesse, ou une variante simple
            if intent == "commande":
                phrase = random.choice([
                    phrase,
                    f"{phrase} s'il vous plaît",
                    f"{phrase} pour emporter",
                    f"{phrase} pour ce soir"
                ])
                print(f"Enrichissement de l'intention '{intent}': {phrase}")
            elif intent == "salutation":
                phrase = random.choice([
                    phrase,
                    f"{phrase} à tous",
                    f"{phrase} tout le monde"
                ])
                print(f"Enrichissement de l'intention '{intent}': {phrase}")
            elif intent == "menu":
                phrase = random.choice([
                    phrase,
                    f"{phrase} s'il vous plaît"
                ])
                print(f"Enrichissement de l'intention '{intent}': {phrase}")
            current.add(phrase)
            attempts += 1
        if len(current) < n_variants:
            print(f"⚠️  Impossible de générer {n_variants} variantes uniques pour l'intention '{intent}'. Uniquement {len(current)} générées.")
        data["intentions"][intent] = list(current)

    # Sauvegarde le dataset enrichi
    print("Enrichissement terminé, sauvegarde du dataset...")
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
    print("✅ Dataset enrichi et sauvegardé !")

if __name__ == "__main__":
    enrich_dataset("dataset.yaml", n_variants=15)