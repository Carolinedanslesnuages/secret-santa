# Secret Santa 🎅🎁

Ce projet est un script Python permettant d'organiser un **Secret Santa** de manière simple et automatisée (enfin, presque ...). Il génère aléatoirement des paires entre les participants et leur envoie des emails pour leur notifier qui ils doivent gâter. 🎄

## Fonctionnalités ✨
- Génération aléatoire des associations Secret Santa.
- Assurance qu'aucun participant n'est son propre Secret Santa.
- Envoi d'emails personnalisés à chaque participant.
- Récapitulatif des associations envoyé à l'organisateur.

---

## Prérequis 🛠️
1. **Python 3.7 ou supérieur** doit être installé sur votre système.

### Configuration ⚙️

**1. Variables d’environnement**

Créez un fichier .env à la racine du projet avec les informations suivantes :
```env
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-email-password
```

Ces informations permettent au script d’envoyer des emails via le compte configuré.

**2. Participants**

Créez un fichier participants.json dans le format suivant :
```json
[
    {
        "name": "Alice",
        "email": "alice@example.com",
        "preferences": {
            "snack": "Chocolat",
            "book": "Fiction",
            "movie": "Stranger Things",
            "drink": "Café",
            "hobby": "Sport",
            "app": "Réseaux sociaux",
            "superpower": "Téléportation",
            "snack_tv": "Bonbons",
            "music": "Jazz",
            "gift_preference": "Un cadeau personnalisé"
        }
    },
    {
        "name": "Bob",
        "email": "bob@example.com",
        "preferences": {
            "snack": "Chips",
            "book": "Non-fiction",
            "movie": "Game of Thrones",
            "drink": "Thé",
            "hobby": "Dessin/Peinture",
            "app": "Jeux",
            "superpower": "Voler",
            "snack_tv": "Popcorn",
            "music": "Rock",
            "gift_preference": "Un cadeau amusant"
        }
    }
]
```

### Utilisation 🚀

**1. Lancer le script :**

Exécutez le script Python :

```bash
python secret_santa.py
```


**2. Le script :**
   - Génère les associations entre participants.
   - Envoie un email individuel à chaque participant avec les détails de son destinataire.
   - Envoie un récapitulatif des associations à l’organisateur.

**Exemple de Résultat:** 📝

Exemple d’association :

```
Alice -> Bob
Bob -> Charlie
Charlie -> Alice
```
Exemple d’email :

```
	Objet : [TEST] Secret Santa 🎅

	Bonjour Alice,

	Vous êtes le Secret Santa de Bob 🎁. Voici quelques informations sur Bob pour vous aider à choisir un cadeau :
•	Snack préféré : Chips
•	Genre de livre préféré : Non-fiction
•	Série ou film actuel : Game of Thrones
•	Préférence pour les boissons : Thé
•	…

```

### Contribuer 🤝✨

Avez-vous une idée brillante pour améliorer le script ? 
Une fonctionnalité secrète à ajouter ? 
Ou simplement envie de corriger un petit bug qui vous dérange ? Super ! 
Voici comment vous pouvez nous aider à rendre ce projet encore plus magique :

	1.	Forkez le dépôt 🪄 pour obtenir votre propre copie.
	2.	Créez une branche légendaire 🌟 avec votre fonctionnalité incroyable :

git checkout -b feature/ma-fonctionnalite


	3.	Soumettez une Pull Request 🚀, et laissez la magie opérer !

Toutes les idées sont les bienvenues, qu’elles soient petites ou audacieuses. Parce que Secret Santa, c’est aussi du partage !

Licence 📜✨

Ce projet est sous licence MIT, ce qui signifie :
	•	Vous pouvez l’utiliser.
	•	Vous pouvez le modifier.
	•	Vous pouvez le partager avec qui vous voulez.
	•	Bref, faites-vous plaisir ! 🎁

Remerciements 🎉❤️

Un énorme merci à vous d’utiliser ce script et de participer à la magie des fêtes ! Grâce à vous, des sourires vont illuminer les visages, et des cadeaux géniaux trouveront leur chemin sous le sapin. 🎄🎅

N’oubliez pas : les plus beaux cadeaux viennent toujours du cœur (mais une boîte de chocolats fonctionne aussi très bien). 🍫✨

🎁 Bon Secret Santa ! Et n’oubliez pas votre pull de Noël. 😉
