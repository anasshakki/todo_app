# Mini Application de Gestion de Tâches (Flask)

Ce projet est une mini application web de type "To-do List" réalisée en Python avec le framework Flask.

## Fonctionnalités
- Ajouter une tâche avec titre, description, date d’échéance
- Afficher les tâches en attente et terminées
- Marquer une tâche comme terminée
- Supprimer une tâche
- Modifier une tâche (optionnel)

## Technologies utilisées
- Python (Flask)
- SQLite (base de données)
- HTML / CSS

## Structure du projet : 

todo_app/
│
├── app.py # Fichier principal Flask
├── init_db.py # Script pour créer la base de données
├── tasks.db # Fichier SQLite
│
├── templates/
│ └── index.html # Page HTML
│
├── static/
│ └── style.css # Style CSS


## Lancer le projet localement

```bash
# 1. Créer un environnement virtuel (si pas déjà fait)
python -m venv venv

# 2. Activer l’environnement
venv\Scripts\activate

# 3. Installer Flask
pip install flask

# 4. Créer la base de données
python init_db.py

# 5. Lancer le serveur
python app.py

# 6. Ouvrir dans le navigateur
http://127.0.0.1:5000

# Fonctionnalités

-> Ajouter une tâche

-> Marquer comme terminée

-> Supprimer une tâche

# Auteur :
Mohamed Anass HAKKI
Génie informatique 3A

