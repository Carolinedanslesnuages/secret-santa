import json
import os
import random
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def load_participants_from_json(filename="participants.json"):
    """Charge les participants depuis un fichier JSON."""
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            participants = json.load(json_file)
        print(f"Participants chargés depuis {filename}.")
        return participants
    except Exception as e:
        print(f"Erreur lors du chargement des participants : {e}")
        exit(1)

def send_email(to_email, santa_name, recipient_name, recipient_preferences):
    """Envoie un email individuel au participant."""
    subject = "🧪 : [TEST] Secret Santa 🎅"
    body = f"""Bonjour {santa_name},

Vous êtes le Secret Santa de {recipient_name} 🎁.
Voici quelques informations sur {recipient_name} pour vous aider à choisir un cadeau :

- Snack préféré : {recipient_preferences.get('snack', 'Non spécifié')}
- Genre de livre préféré : {recipient_preferences.get('book', 'Non spécifié')}
- Série ou film actuel : {recipient_preferences.get('movie', 'Non spécifié')}
- Préférence pour les boissons : {recipient_preferences.get('drink', 'Non spécifié')}
- Hobby : {recipient_preferences.get('hobby', 'Non spécifié')}
- Application favorite : {recipient_preferences.get('app', 'Non spécifié')}
- Super-pouvoir préféré : {recipient_preferences.get('superpower', 'Non spécifié')}
- Collation TV favorite : {recipient_preferences.get('snack_tv', 'Non spécifié')}
- Genre musical préféré : {recipient_preferences.get('music', 'Non spécifié')}
- Préférence pour le cadeau : {recipient_preferences.get('gift_preference', 'Non spécifié')}

🎄 Petit rappel : Venez avec votre plus beau pull de Noël pour ajouter encore plus de magie à cet événement festif ! 🎅🎁

Joyeux Noël ! 🎄
"""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
            print(f"Email envoyé avec succès à {to_email}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email à {to_email} : {e}")

def send_associations_email(associations):
    """
    Envoie un email contenant toutes les associations du Secret Santa.
    """
    subject = "Associations Secret Santa 🎅"
    
    body = "Voici les associations du Secret Santa :\n\n"
    for santa, recipient in associations.items():
        body += f"{santa} -> {recipient}\n"

    body += "\nAmusez-vous bien ! 🎄🎁"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS  # L'email est envoyé à vous-même

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
            print("Email avec les associations envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email avec les associations : {e}")

def generate_associations(participants):
    """Génère des associations pour le Secret Santa."""
    # Extraire les noms des participants
    names = [p["name"] for p in participants]

    def is_valid_pairing(participants, names):
        """Vérifie que chaque participant a un seul Santa et qu'il n'est pas son propre Santa."""
        for i, person in enumerate(participants):
            if person["name"] == names[i]:
                return False
        return True

    max_attempts = 1000
    attempts = 0

    # Réessayer jusqu'à ce qu'une association valide soit trouvée ou que la limite soit atteinte
    while attempts < max_attempts:
        random.shuffle(names)
        if is_valid_pairing(participants, names):
            associations = {person["name"]: names[i] for i, person in enumerate(participants)}
            return associations
        attempts += 1

    # Si aucune association valide n'est trouvée après plusieurs tentatives
    raise Exception("Impossible de générer des associations valides après plusieurs tentatives.")

# Bloc principal
if __name__ == "__main__":
    participants = load_participants_from_json()
    associations = generate_associations(participants)
    print("Associations générées :", associations)

    # Envoyer les emails individuels aux participants
    for person in participants:
        santa_name = person["name"]
        recipient_name = associations[santa_name]
        recipient = next(p for p in participants if p["name"] == recipient_name)
        send_email(person["email"], santa_name, recipient_name, recipient["preferences"])

    # Envoyer un email avec toutes les associations
    send_associations_email(associations)

    print("Tous les emails de Secret Santa ont été envoyés ! 🎅🎁")