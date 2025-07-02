def interface_chatbot():
    """Interface interactive pour le chatbot pizzeria"""
    print("=" * 50)
    print("🍕 PIZZA BOT - Chatbot Pizzeria 🍕")
    print("=" * 50)
    print("Tapez 'quit' ou 'exit' pour quitter le programme")
    print("-" * 50)
    
    while True:
        try:
            # Demander à l'utilisateur de saisir un message
            user_input = input("\nVous: ").strip()
            
            # Vérifier si l'utilisateur veut quitter
            if user_input.lower() in ['quit', 'exit', 'quitter', 'sortir']:
                print("\nBot: Merci de votre visite ! À bientôt chez Pizza Bot ! 🍕")
                break
            
            # Vérifier que l'entrée n'est pas vide
            if not user_input:
                print("Bot: Pouvez-vous répéter ? Je n'ai rien entendu.")
                continue
            
            # Obtenir la réponse du chatbot
            response = chatbot_pizzeria(user_input)
            print(f"Bot: {response}")
            
        except KeyboardInterrupt:
            print("\n\nBot: Au revoir ! Merci de votre visite ! 🍕")
            break
        except Exception as e:
            print(f"Bot: Désolé, une erreur s'est produite : {e}")

def chatbot_pizzeria(message):
    message = message.lower()
    
    if "bonjour" in message or "salut" in message:
        return "Bonjour ! Bienvenue chez Pizza Bot. Comment puis-je vous aider ?"
    
    elif "menu" in message or "carte" in message:
        return "Voici notre menu : Margherita (12€), Regina (14€), Calzone (16€)..."
    elif "horraire" in message or "ouverture" in message:
        return "Nous sommes ouverts du lundi au samedi de 11h à 22h."
    elif "commande" in message or "commander" in message:
        return "Pour passer une commande, veuillez nous appeler au 01 23 45 67 89."
    elif "menu" in message:
        return "Notre menu comprend : Margherita (12€), Regina (14€), Calzone (16€)..."

# Lancer l'interface interactive si le script est exécuté directement
if __name__ == "__main__":
    interface_chatbot()