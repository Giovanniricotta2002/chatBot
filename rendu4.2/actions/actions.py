from typing import Dict, Text, List, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
import re
from datetime import datetime, timedelta
import logging

# Configuration du logging
logger = logging.getLogger(__name__)

class ValidateReservationForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_reservation_form"
    
    def validate_nom(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valide le nom du client."""
        if not slot_value or len(slot_value.strip()) < 2:
            dispatcher.utter_message(text="Veuillez indiquer un nom valide (au moins 2 caractères).")
            return {"nom": None}
        
        # Nettoyer le nom (enlever espaces en trop, capitaliser)
        nom_clean = " ".join(slot_value.strip().split()).title()
        return {"nom": nom_clean}
    
    def validate_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valide la date de réservation."""
        try:
            # Formats acceptés : "demain", "aujourd'hui", "lundi", "15/07", "15 juillet"
            date_str = slot_value.lower().strip()
            aujourd_hui = datetime.now()
            
            # Gestion des mots-clés
            if date_str in ["aujourd'hui", "ce soir"]:
                date_reservation = aujourd_hui
            elif date_str == "demain":
                date_reservation = aujourd_hui + timedelta(days=1)
            elif date_str in ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]:
                jours_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
                jour_cible = jours_semaine.index(date_str)
                jour_actuel = aujourd_hui.weekday()
                
                if jour_cible == 1:  # Mardi - restaurant fermé
                    dispatcher.utter_message(text="Désolé, nous sommes fermés le mardi. Choisissez un autre jour.")
                    return {"date": None}
                
                jours_jusqu_cible = (jour_cible - jour_actuel) % 7
                if jours_jusqu_cible == 0:
                    jours_jusqu_cible = 7
                date_reservation = aujourd_hui + timedelta(days=jours_jusqu_cible)
            else:
                # Tentative de parsing de formats de date courants
                formats = ["%d/%m", "%d-%m", "%d %m", "%d/%m/%Y", "%d-%m-%Y"]
                date_reservation = None
                
                for fmt in formats:
                    try:
                        if len(date_str.split('/')) == 2 or len(date_str.split('-')) == 2:
                            date_reservation = datetime.strptime(f"{date_str}/{aujourd_hui.year}", f"{fmt}/%Y")
                        else:
                            date_reservation = datetime.strptime(date_str, fmt)
                        break
                    except ValueError:
                        continue
                
                if not date_reservation:
                    dispatcher.utter_message(text="Format de date non reconnu. Utilisez 'demain', 'lundi' ou '15/07'.")
                    return {"date": None}
            
            # Vérifier que la date n'est pas dans le passé
            if date_reservation.date() < aujourd_hui.date():
                dispatcher.utter_message(text="Impossible de réserver dans le passé. Choisissez une date future.")
                return {"date": None}
            
            # Vérifier que ce n'est pas un mardi
            if date_reservation.weekday() == 1:
                dispatcher.utter_message(text="Nous sommes fermés le mardi. Choisissez un autre jour.")
                return {"date": None}
            
            # Limite de réservation à 30 jours
            if (date_reservation - aujourd_hui).days > 30:
                dispatcher.utter_message(text="Nous acceptons les réservations jusqu'à 30 jours à l'avance.")
                return {"date": None}
            
            return {"date": date_reservation.strftime("%d/%m/%Y")}
            
        except Exception as e:
            logger.error(f"Erreur validation date: {e}")
            dispatcher.utter_message(text="Format de date invalide. Essayez 'demain' ou '15/07'.")
            return {"date": None}
    
    def validate_nombre_personnes(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valide le nombre de personnes."""
        try:
            # Gestion des mots en texte
            mots_nombres = {
                "un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4, 
                "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10
            }
            
            slot_str = str(slot_value).lower().strip()
            
            if slot_str in mots_nombres:
                nombre = mots_nombres[slot_str]
            else:
                nombre = int(slot_value)
            
            if 1 <= nombre <= 10:
                return {"nombre_personnes": str(nombre)}
            elif nombre > 10:
                dispatcher.utter_message(text="Pour les groupes de plus de 10 personnes, veuillez nous appeler directement.")
                return {"nombre_personnes": None}
            else:
                dispatcher.utter_message(text="Le nombre de personnes doit être au moins 1.")
                return {"nombre_personnes": None}
                
        except ValueError:
            dispatcher.utter_message(text="Veuillez indiquer un nombre valide (ex: 2, 'deux').")
            return {"nombre_personnes": None}
    
    def validate_heure(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valide l'heure de réservation."""
        try:
            # Patterns pour différents formats d'heure
            patterns = [
                r'(\d{1,2})[h:](\d{2})',  # 18h30, 18:30
                r'(\d{1,2})h',            # 18h
                r'(\d{1,2}):(\d{2})',     # 18:30
                r'(\d{1,2})\.(\d{2})',    # 18.30
                r'(\d{1,2})$'             # 18
            ]
            
            slot_str = slot_value.lower().strip()
            heure, minute = None, 0
            
            for pattern in patterns:
                match = re.match(pattern, slot_str)
                if match:
                    heure = int(match.group(1))
                    if len(match.groups()) > 1 and match.group(2):
                        minute = int(match.group(2))
                    break
            
            if heure is None:
                dispatcher.utter_message(text="Format d'heure non reconnu. Utilisez 19h, 19h30 ou 19:30.")
                return {"heure": None}
            
            # Vérifier les horaires d'ouverture selon le jour
            date_slot = tracker.get_slot("date")
            if date_slot:
                try:
                    date_res = datetime.strptime(date_slot, "%d/%m/%Y")
                    jour_semaine = date_res.weekday()
                    
                    # Horaires différents selon le jour
                    if jour_semaine in [0, 2, 3]:  # Lundi, mercredi, jeudi
                        heure_min, heure_max = 18, 22
                        if heure == 22 and minute > 30:
                            heure_max_minute = 30
                        else:
                            heure_max_minute = 59
                    elif jour_semaine in [4, 5]:  # Vendredi, samedi
                        heure_min, heure_max = 18, 23
                        heure_max_minute = 59
                    elif jour_semaine == 6:  # Dimanche
                        heure_min, heure_max = 18, 22
                        heure_max_minute = 59
                    else:  # Mardi - fermé
                        dispatcher.utter_message(text="Nous sommes fermés le mardi.")
                        return {"heure": None}
                except:
                    # Horaires par défaut
                    heure_min, heure_max = 18, 22
                    heure_max_minute = 59
            else:
                heure_min, heure_max = 18, 22
                heure_max_minute = 59
            
            if heure < heure_min or heure > heure_max:
                dispatcher.utter_message(text=f"Nos horaires de réservation sont de {heure_min}h à {heure_max}h.")
                return {"heure": None}
            
            if heure == heure_max and minute > heure_max_minute:
                dispatcher.utter_message(text=f"Dernière réservation à {heure_max}h{heure_max_minute:02d}.")
                return {"heure": None}
            
            if 0 <= minute <= 59:
                if minute == 0:
                    return {"heure": f"{heure}h"}
                else:
                    return {"heure": f"{heure}h{minute:02d}"}
            else:
                dispatcher.utter_message(text="Minutes invalides. Utilisez un format comme 19h30.")
                return {"heure": None}
                
        except Exception as e:
            logger.error(f"Erreur validation heure: {e}")
            dispatcher.utter_message(text="Format d'heure invalide. Essayez 19h ou 19h30.")
            return {"heure": None}

class ActionReservationComplete(Action):
    def name(self) -> Text:
        return "action_reservation_complete"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            # Récupérer les slots
            nom = tracker.get_slot("nom")
            date = tracker.get_slot("date")
            heure = tracker.get_slot("heure")
            nombre_personnes = tracker.get_slot("nombre_personnes")
            
            # Vérifier que tous les slots sont présents
            if not all([nom, date, heure, nombre_personnes]):
                dispatcher.utter_message(text="Désolé, il manque des informations pour votre réservation.")
                return []
            
            # Créer un ID de réservation plus robuste
            timestamp = datetime.now().strftime("%H%M")
            reservation_id = f"RES{hash(f'{nom}{date}{heure}{timestamp}') % 10000:04d}"
            
            # Calculer le jour de la semaine pour la confirmation
            try:
                date_obj = datetime.strptime(date, "%d/%m/%Y")
                jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
                jour_semaine = jours[date_obj.weekday()]
            except:
                jour_semaine = ""
            
            message = f"""
✅ **Réservation confirmée !**

📋 **Détails de votre réservation :**
• **ID de réservation** : `{reservation_id}`
• **Nom** : {nom}
• **Date** : {jour_semaine} {date}
• **Heure** : {heure}
• **Nombre de personnes** : {nombre_personnes}

🍕 **Informations importantes :**
• Merci d'arriver 5 minutes avant l'heure de réservation
• En cas d'empêchement, prévenez-nous au moins 2h à l'avance
• Conservez votre ID de réservation : `{reservation_id}`

Nous vous attendons avec plaisir ! 😊
            """
            
            dispatcher.utter_message(text=message.strip())
            
            # Log de la réservation
            logger.info(f"Réservation créée - ID: {reservation_id}, Nom: {nom}, Date: {date}, Heure: {heure}, Personnes: {nombre_personnes}")
            
            return []
            
        except Exception as e:
            logger.error(f"Erreur lors de la création de réservation: {e}")
            dispatcher.utter_message(text="Désolé, une erreur s'est produite lors de la confirmation. Veuillez réessayer.")
            return []


class ActionDonnerPrix(Action):
    """Action pour donner les prix des pizzas."""
    
    def name(self) -> Text:
        return "action_donner_prix"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Prix des pizzas
        prix = {
            "margherita": "12€",
            "regina": "14€", 
            "calzone": "15€",
            "quatre saisons": "16€",
            "napolitaine": "13€"
        }
        
        # Extraire l'entité produit du dernier message
        produit = None
        entities = tracker.latest_message.get('entities', [])
        for entity in entities:
            if entity.get('entity') == 'produit':
                produit = entity.get('value', '').lower()
                break
        
        if produit and produit in prix:
            message = f"La pizza {produit.title()} coûte {prix[produit]}."
        else:
            message = """🍕 **Nos prix :**

• Margherita : 12€
• Regina : 14€
• Napolitaine : 13€
• Calzone : 15€
• Quatre Saisons : 16€

Toutes nos pizzas sont faites maison avec des ingrédients frais !"""
        
        dispatcher.utter_message(text=message)
        return []


class ActionAnnulerReservation(Action):
    """Action pour annuler une réservation."""
    
    def name(self) -> Text:
        return "action_annuler_reservation"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = """
Pour annuler votre réservation, vous pouvez :

📞 **Nous appeler** au 01 23 45 67 89
💬 **Nous donner votre ID de réservation** ici
🕐 **Délai** : Au moins 2h avant votre réservation

Quel est votre ID de réservation ?
        """
        
        dispatcher.utter_message(text=message.strip())
        return []