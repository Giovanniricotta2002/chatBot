import yaml
import random

# Synonymes et templates par intention
enrich_templates = {
    "salutation": [
        "bonjour", "salut", "hello", "coucou", "bien le bonjour", "hey", "yo", "salutations",
        "bonsoir", "salut à tous", "bonjour tout le monde", "salut les amis", "bienvenue", "bonne journée", "bonne soirée",
        "salut à vous", "bonjour à tous", "salut tout le monde", "bonjour la compagnie", "salut la team", "bonjour à vous tous", "salut les copains", "bonjour à toutes et à tous", "salut la famille", "bonjour à la team", "salut à toi", "bonjour cher ami", "salut cher ami", "bonjour à tous et à toutes", "salut à toutes et à tous", "bonjour à toutes", "salut à toutes"
    ],
    "menu": [
        "je veux voir le menu", "affichez la carte", "montrez-moi le menu", "quels sont vos plats", "que proposez-vous", "qu'est-ce qu'il y a à manger", "vos plats", "carte",
        "pouvez-vous me montrer la carte ?", "je voudrais consulter le menu", "qu'avez-vous à proposer ?", "quels sont les menus disponibles ?", "je souhaite voir la carte", "montrez-moi vos spécialités", "quels plats recommandez-vous ?",
        "je peux avoir la carte ?", "je veux voir ce que vous servez", "je souhaite voir vos plats", "montrez-moi la carte s'il vous plaît", "je veux consulter la carte", "je veux voir la liste des plats", "pouvez-vous afficher le menu ?", "je veux connaître vos menus", "je veux voir la carte du jour", "quels sont les plats du jour ?", "je veux voir la carte complète", "je veux voir la carte des boissons", "je veux voir la carte des desserts", "je veux voir la carte spéciale", "je veux voir la carte enfant"
    ],
    "commande": [
        "je veux commander une pizza", "je commande une pizza", "j'aimerais commander", "je voudrais commander", "puis-je passer une commande", "je passe commande", "commande pour deux personnes", "je souhaite commander un menu",
        "je voudrais commander à emporter", "je veux passer commande", "je souhaite réserver une commande", "je commande pour ce soir", "je veux commander une boisson", "je passe une commande groupée", "je veux commander un dessert",
        "je veux commander une salade", "je veux commander une entrée", "je veux commander un plat principal", "je veux commander un menu enfant", "je veux commander une pizza à emporter", "je veux commander pour ce midi", "je veux commander pour ce soir", "je veux commander pour demain", "je veux commander pour une fête", "je veux commander pour un anniversaire", "je veux commander pour un événement", "je veux commander pour une réunion", "je veux commander pour une soirée", "je veux commander pour un déjeuner", "je veux commander pour un dîner"
    ],
    "horaires": [
        "quels sont vos horaires", "à quelle heure ouvrez-vous", "quand fermez-vous", "heures d'ouverture", "c'est ouvert le dimanche", "vos horaires", "à quelle heure fermez-vous le soir",
        "êtes-vous ouverts aujourd'hui ?", "vos horaires d'ouverture le week-end ?", "à quelle heure fermez-vous le samedi ?", "quand puis-je venir ?", "êtes-vous ouverts ce soir ?", "vos heures d'ouverture ?", "à quelle heure commencez-vous à servir ?",
        "quels sont vos horaires d'ouverture ?", "quels sont vos horaires de fermeture ?", "à quelle heure puis-je venir ?", "à quelle heure puis-je commander ?", "à quelle heure commence le service ?", "à quelle heure se termine le service ?", "êtes-vous ouverts en semaine ?", "êtes-vous ouverts le soir ?", "êtes-vous ouverts le midi ?", "êtes-vous ouverts les jours fériés ?", "êtes-vous ouverts pendant les vacances ?", "vos horaires pendant les vacances ?", "vos horaires spéciaux ?", "vos horaires exceptionnels ?", "vos horaires pour les fêtes ?"
    ],
    "prix": [
        "combien coûte une pizza", "quel est le prix", "c'est combien", "prix d'une pizza", "tarif", "combien ça coûte", "coût",
        "quel est le tarif d'un menu ?", "combien pour une boisson ?", "c'est combien la livraison ?", "quel est le prix d'un dessert ?", "combien dois-je payer ?", "quel est le prix total ?", "combien pour deux menus ?",
        "combien coûte un menu enfant ?", "combien coûte un menu complet ?", "combien coûte une entrée ?", "combien coûte un plat principal ?", "combien coûte un dessert ?", "combien coûte une boisson ?", "combien coûte une pizza spéciale ?", "combien coûte une pizza margherita ?", "combien coûte une pizza 4 fromages ?", "combien coûte une pizza royale ?", "combien coûte une pizza végétarienne ?", "combien coûte une pizza napolitaine ?", "combien coûte une pizza calzone ?", "combien coûte une pizza pepperoni ?", "combien coûte une pizza hawaïenne ?"
    ],
    "au_revoir": [
        "au revoir", "bye", "merci", "bonne journée", "à bientôt", "à la prochaine", "bonne soirée",
        "merci beaucoup", "bonne continuation", "à plus tard", "à la prochaine fois", "bonne fin de journée", "merci et au revoir", "à plus",
        "bonne nuit", "à tout à l'heure", "à une prochaine fois", "merci pour tout", "merci et bonne journée", "merci et bonne soirée", "merci et à bientôt", "merci et à la prochaine", "merci et bonne continuation", "merci et à plus tard", "merci et à plus", "merci et bonne fin de journée", "merci et à une prochaine fois", "merci et à tout à l'heure", "merci et bonne nuit"
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
            elif intent == "salutation":
                phrase = random.choice([
                    phrase,
                    f"{phrase} à tous",
                    f"{phrase} tout le monde"
                ])
            elif intent == "menu":
                phrase = random.choice([
                    phrase,
                    f"{phrase} s'il vous plaît"
                ])
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
    enrich_dataset("dataset.yaml", n_variants=30)