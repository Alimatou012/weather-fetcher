# Utiliser une image de base légère
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir la variable d'environnement pour la clé API
ENV OPENWEATHER_API_KEY="your_openweather_api_key_here"

# Exécuter le script
CMD ["python", "main.py"]
