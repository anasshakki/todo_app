# Mini Application de Gestion de Tâches (Flask)

Ce projet est une mini application web de type **"To-do List"** réalisée en **Python** avec le framework **Flask**.

## Fonctionnalités
- Ajouter une tâche avec titre, description et date d’échéance
- Afficher la liste des tâches :
  - Tâches en attente
  - Tâches terminées
- Marquer une tâche comme terminée
- Modifier une tâche
- Supprimer une tâche (avec effet visuel en JavaScript)
- Interface améliorée avec un background et un peu de style CSS

## Technologies utilisées
- Python (Flask)
- SQLite (base de données)
- HTML / CSS
- JavaScript (pour les effets visuels)

## Structure du projet
todo_app/
  app.py   # Fichier principal Flask
  init_db.py  # Script pour créer la base de données
  tasks.db  # Base SQLite
  README.md  # Documentation

  templates/
     └── index.html  # Page principale
     └── edit.html  # Page pour modifier une tâche

  static/
  
     └── style.css # Feuille de style CSS (background bleu + mise en forme)
     └── script.js # Script JavaScript (effet suppression)

## Installation et lancement du projet

```bash
# 1. Créer un environnement virtuel (si pas déjà fait)
python -m venv venv

# 2. Activer l’environnement
venv\Scripts\activate   # sous Windows
source venv/bin/activate   # sous Linux / Mac

# 3. Installer Flask
pip install flask

# 4. Initialiser la base de données
python init_db.py

# 5. Lancer l’application
python app.py

## 📸 Aperçu de l'application

Voici un aperçu de l'interface de l'application :

![Interface de l'application](screenshots/interface.png)


# 6. Ouvrir dans le navigateur
http://127.0.0.1:5000


# Auteur :
Mohamed Anass HAKKI
Génie informatique 3A
POLYTECH MARSEILLE

