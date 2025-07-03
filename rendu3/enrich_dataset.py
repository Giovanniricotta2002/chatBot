import yaml
import random
from faker import Faker

fake = Faker('fr_FR')

# Synonymes et templates par intention (avec Faker)
enrich_templates = {
    "salutation": [
        "bonjour", "salut", "hello", "coucou", "bien le bonjour", "hey", "yo", "salutations",
        "bonsoir", "salut à tous", "bonjour tout le monde", "salut les amis", "bienvenue", "bonne journée", "bonne soirée",
        "salut à vous", "bonjour à tous", "salut tout le monde", "bonjour la compagnie", "salut la team", "bonjour à vous tous", "salut les copains", "bonjour à toutes et à tous", "salut la famille", "bonjour à la team", "salut à toi", "bonjour cher ami", "salut cher ami", "bonjour à tous et à toutes", "salut à toutes et à tous", "bonjour à toutes", "salut à toutes",
        f"Bonjour {fake.first_name()}", f"Salut à {fake.city()}", f"Coucou {fake.first_name()} et {fake.first_name()} !", f"Hey la team {fake.city()} !"
    ],
    "menu": [
        "je veux voir le menu", "affichez la carte", "montrez-moi le menu", "quels sont vos plats", "que proposez-vous", "qu'est-ce qu'il y a à manger", "vos plats", "carte",
        "pouvez-vous me montrer la carte ?", "je voudrais consulter le menu", "qu'avez-vous à proposer ?", "quels sont les menus disponibles ?", "je souhaite voir la carte", "montrez-moi vos spécialités", "quels plats recommandez-vous ?",
        "je peux avoir la carte ?", "je veux voir ce que vous servez", "je souhaite voir vos plats", "montrez-moi la carte s'il vous plaît", "je veux consulter la carte", "je veux voir la liste des plats", "pouvez-vous afficher le menu ?", "je veux connaître vos menus", "je veux voir la carte du jour", "quels sont les plats du jour ?", "je veux voir la carte complète", "je veux voir la carte des boissons", "je veux voir la carte des desserts", "je veux voir la carte spéciale", "je veux voir la carte enfant",
        f"{fake.first_name()} veut voir le menu", f"Quels plats à {fake.city()} ?", f"Menu spécial pour {fake.date(pattern='%d/%m/%Y')} ?"
    ],
    "commande": [
        "je veux commander une pizza", "je commande une pizza", "j'aimerais commander", "je voudrais commander", "puis-je passer une commande", "je passe commande", "commande pour deux personnes", "je souhaite commander un menu",
        "je voudrais commander à emporter", "je veux passer commande", "je souhaite réserver une commande", "je commande pour ce soir", "je veux commander une boisson", "je passe une commande groupée", "je veux commander un dessert",
        "je veux commander une salade", "je veux commander une entrée", "je veux commander un plat principal", "je veux commander un menu enfant", "je veux commander une pizza à emporter", "je veux commander pour ce midi", "je veux commander pour ce soir", "je veux commander pour demain", "je veux commander pour une fête", "je veux commander pour un anniversaire", "je veux commander pour un événement", "je veux commander pour une réunion", "je veux commander pour une soirée", "je veux commander pour un déjeuner", "je veux commander pour un dîner",
        f"{fake.first_name()} commande {random.randint(1, 5)} pizza(s)", f"Commande de {random.randint(1, 5)} pizza(s) à {fake.time(pattern='%H:%M')}"
    ],
    "horaires": [
        "quels sont vos horaires", "à quelle heure ouvrez-vous", "quand fermez-vous", "heures d'ouverture", "c'est ouvert le dimanche", "vos horaires", "à quelle heure fermez-vous le soir",
        "êtes-vous ouverts aujourd'hui ?", "vos horaires d'ouverture le week-end ?", "à quelle heure fermez-vous le samedi ?", "quand puis-je venir ?", "êtes-vous ouverts ce soir ?", "vos heures d'ouverture ?", "à quelle heure commencez-vous à servir ?",
        "quels sont vos horaires d'ouverture ?", "quels sont vos horaires de fermeture ?", "à quelle heure puis-je venir ?", "à quelle heure puis-je commander ?", "à quelle heure commence le service ?", "à quelle heure se termine le service ?", "êtes-vous ouverts en semaine ?", "êtes-vous ouverts le soir ?", "êtes-vous ouverts le midi ?", "êtes-vous ouverts les jours fériés ?", "êtes-vous ouverts pendant les vacances ?", "vos horaires pendant les vacances ?", "vos horaires spéciaux ?", "vos horaires exceptionnels ?", "vos horaires pour les fêtes ?",
        f"À quelle heure ouvrez-vous le {fake.date(pattern='%d/%m/%Y')} ?", f"Êtes-vous ouverts à {fake.time(pattern='%H:%M')} ?"
    ],
    "prix": [
        "combien coûte une pizza", "quel est le prix", "c'est combien", "prix d'une pizza", "tarif", "combien ça coûte", "coût",
        "quel est le tarif d'un menu ?", "combien pour une boisson ?", "c'est combien la livraison ?", "quel est le prix d'un dessert ?", "combien dois-je payer ?", "quel est le prix total ?", "combien pour deux menus ?",
        "combien coûte un menu enfant ?", "combien coûte un menu complet ?", "combien coûte une entrée ?", "combien coûte un plat principal ?", "combien coûte un dessert ?", "combien coûte une boisson ?", "combien coûte une pizza spéciale ?", "combien coûte une pizza margherita ?", "combien coûte une pizza 4 fromages ?", "combien coûte une pizza royale ?", "combien coûte une pizza végétarienne ?", "combien coûte une pizza napolitaine ?", "combien coûte une pizza calzone ?", "combien coûte une pizza pepperoni ?", "combien coûte une pizza hawaïenne ?",
        f"Quel est le prix d'une pizza {random.choice(['margherita', 'royale', 'calzone', 'pepperoni'])} ?", f"Combien pour {random.randint(1, 5)} pizzas ?"
    ],
    "au_revoir": [
        "au revoir", "bye", "merci", "bonne journée", "à bientôt", "à la prochaine", "bonne soirée",
        "merci beaucoup", "bonne continuation", "à plus tard", "à la prochaine fois", "bonne fin de journée", "merci et au revoir", "à plus",
        "bonne nuit", "à tout à l'heure", "à une prochaine fois", "merci pour tout", "merci et bonne journée", "merci et bonne soirée", "merci et à bientôt", "merci et à la prochaine", "merci et bonne continuation", "merci et à plus tard", "merci et à plus", "merci et bonne fin de journée", "merci et à une prochaine fois", "merci et à tout à l'heure", "merci et bonne nuit",
        f"Merci {fake.first_name()} !", f"Bonne journée à {fake.city()} !"
    ]
}

def faker_phrase(intent):
    """Génère une phrase réaliste avec Faker selon l'intention."""
    plats = [
        "pizza margherita", "pizza 4 fromages", "pizza royale", "pizza végétarienne", "pizza napolitaine", "pizza calzone", "pizza pepperoni", "pizza hawaïenne", "salade César", "tarte aux pommes", "tiramisu", "coca-cola", "jus d'orange", "eau minérale", "menu enfant", "menu complet", "entrée du jour", "plat du jour", "dessert du jour"
    ]
    if intent == "salutation":
        return random.choice([
            f"Bonjour {fake.first_name()}",
            f"Salut à {fake.city()}",
            f"Coucou {fake.first_name()} et {fake.first_name()} !",
            f"Hey la team {fake.city()} !"
        ])
    if intent == "menu":
        return random.choice([
            f"{fake.first_name()} veut voir le menu",
            f"Quels plats à {fake.city()} ?",
            f"Menu spécial pour {fake.date(pattern='%d/%m/%Y')} ?"
        ])
    if intent == "commande":
        return random.choice([
            f"{fake.first_name()} commande {random.randint(1, 5)} {random.choice(plats)}",
            f"Commande de {random.randint(1, 5)} {random.choice(plats)} à {fake.time(pattern='%H:%M')}"
        ])
    if intent == "horaires":
        return random.choice([
            f"À quelle heure ouvrez-vous le {fake.date(pattern='%d/%m/%Y')} ?",
            f"Êtes-vous ouverts à {fake.time(pattern='%H:%M')} ?"
        ])
    if intent == "prix":
        return random.choice([
            f"Quel est le prix d'une {random.choice(plats)} ?",
            f"Combien pour {random.randint(1, 5)} {random.choice(plats)} ?"
        ])
    if intent == "au_revoir":
        return random.choice([
            f"Merci {fake.first_name()} !",
            f"Bonne journée à {fake.city()} !"
        ])
    return ""

def enrich_dataset(yaml_path, n_variants=12, max_attempts_per_intent=1000):
    print(f"\n📥 Lecture du dataset depuis {yaml_path} ...")
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    print(f"\n🚀 Début de l'enrichissement pour chaque intention...")
    for intent, variants in enrich_templates.items():
        print(f"\n➡️  Intention : '{intent}'")
        if "intentions" not in data:
            data["intentions"] = {}
        if intent not in data["intentions"]:
            data["intentions"][intent] = []
        current = set(data["intentions"][intent])
        print(f"   - Exemples existants : {len(current)}")
        attempts = 0
        while len(current) < n_variants and attempts < max_attempts_per_intent:
            if random.random() < 0.25:
                phrase = faker_phrase(intent)
                print(f"   [Faker] {phrase}")
            else:
                phrase = random.choice(variants)
                print(f"   [Template] {phrase}")
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
            if phrase not in current:
                print(f"   + Ajouté : {phrase}")
            current.add(phrase)
            attempts += 1
        print(f"   → Total généré pour '{intent}' : {len(current)} exemples")
        if len(current) < n_variants:
            print(f"⚠️  Impossible de générer {n_variants} variantes uniques pour l'intention '{intent}'. Uniquement {len(current)} générées.")
        data["intentions"][intent] = list(current)

    print("\n💾 Enrichissement terminé, sauvegarde du dataset...")
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
    print("✅ Dataset enrichi et sauvegardé !")

if __name__ == "__main__":
    variants = random.randrange(10, 30)
    print(f"\n==============================")
    print(f"Enrichissement du dataset avec {variants} variantes par intention...")
    print(f"==============================\n")
    enrich_dataset("dataset.yaml", n_variants=variants)