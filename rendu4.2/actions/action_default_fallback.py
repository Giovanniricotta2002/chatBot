class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Compter les fallbacks consécutifs
        fallback_count = 0
        for event in reversed(tracker.events):
            if event.get("name") == "action_default_fallback":
                fallback_count += 1
            else:
                break
        
        if fallback_count == 0:
            message = "Je n'ai pas bien compris. Pouvez-vous reformuler votre demande ?"
        elif fallback_count == 1:
            message = """Je ne comprends toujours pas. Voici ce que je peux faire :
            • Prendre une réservation
            • Montrer le menu
            • Donner les horaires d'ouverture
            • Donner les prix"""
        else:
            message = "Je vous transfère vers un agent humain pour vous aider."
            # Logique d'escalade vers humain
        
        dispatcher.utter_message(text=message)
        return []