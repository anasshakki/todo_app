# Mini Application de Gestion de Tâches (Flask)

Ce projet est une mini application web de type **To-do List**, développée en **Python** avec le framework **Flask** et une base de données **SQLite**.  
Elle permet de gérer simplement des tâches (ajout, modification, suppression, statut terminé/en attente).

---

## Fonctionnalités

- Ajouter une tâche avec un titre, une description et une date d’échéance  
- Afficher la liste des tâches :
  - Tâches en attente  
  - Tâches terminées  
- Marquer une tâche comme terminée  
- Modifier une tâche existante  
- Supprimer une tâche (avec un petit effet visuel en JavaScript)  
- Interface avec un style simple en HTML/CSS (arrière plan bleu ciel) 

---

## Technologies utilisées

- **Python (Flask)** – Back-end  
- **SQLite** – Base de données  
- **HTML / CSS** – Interface utilisateur  
- **JavaScript** – Effets visuels  

---

## Structure du projet

```
todo_app/
│
├── app.py          # Application Flask principale
├── init_db.py      # Script pour initialiser la base de données
├── tasks.db        # Base SQLite
├── README.md       # Documentation du projet
│
├── templates/
│   ├── index.html  # Page principale
│   └── edit.html   # Page de modification
│
└── static/
    ├── style.css   # Feuille de style CSS
    └── script.js   # Script JavaScript (effet suppression)
```

---

## Installation et lancement du projet

```bash
# 1. Créer un environnement virtuel
python -m venv venv

# 2. Activer l’environnement (Windows)
venv\Scripts\activate

# 3. Installer les dépendances
pip install flask

# 4. Initialiser la base de données
python init_db.py

# 5. Lancer l’application
python app.py

# 6. Ouvrir dans le navigateur
http://127.0.0.1:5000
```

---

## Aperçu

Page principale :  
![Aperçu de la To-do List](screenshots/interface.png)

---

## Auteur

Projet réalisé par Anass HAKKI dans le cadre d’un exercice pratique.
