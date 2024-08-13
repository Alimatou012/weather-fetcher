
# Weather Fetcher

## Description
Un script Python qui récupère les données météo d'une ville en utilisant l'API OpenWeatherMap et les affiche dans un format lisible.

## Prérequis
- Python 3.x
- Docker (facultatif, si vous souhaitez utiliser un conteneur)

## Installation

Clonez le repository et installez les dépendances :

```bash
git clone https://github.com/username/weather-fetcher.git
cd weather-fetcher
pip install -r requirements.txt
```

Cette commande installe toutes les bibliothèques Python nécessaires listées dans le fichier `requirements.txt`.

### Obtention de la Clé API

Pour utiliser le script, il faut avoir une clé API de OpenWeatherMap. Voici comment obtenir une clé API :

1. **Inscription :**
   - Rendez-vous sur [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
   - Créez un compte ou connectez-vous sur OpenWeatherMap.

2. **Obtenir une Clé API :**
   - Accédez à la section "API keys" depuis le tableau de bord utilisateur.
   - Cliquez sur "Create key" pour générer une nouvelle clé API.
   - Donnez un nom à la clé et cliquez sur "Generate" pour la créer.
   - Une fois générée, copiez la clé API pour configurer le script.

## Configuration

Configurer le script avec la clé API. Voici deux méthodes pour le faire :

### 1. Utilisation des Variables d'Environnement

Définir la clé API comme variable d'environnement permet au script de la récupérer automatiquement.

- **Sur Windows (PowerShell) :**
   ```powershell
   $env:OPENWEATHER_API_KEY="votre_cle_api_ici"
   ```

- **Sur Linux/MacOS :**
   ```bash
   export OPENWEATHER_API_KEY="votre_cle_api_ici"
   ```

### 2. Modification Directe du Code

Pour des tests rapides, vous pouvez inclure directement la clé API dans le script Python, bien que ce ne soit pas recommandé pour un usage à long terme.

- Modifiez le fichier `main.py` :
- Ouvrez le fichier `main.py` et remplacez la valeur de `api_key` par votre clé API.

## Exécution du Script

### 1. En Utilisant Python Directement

Une fois la clé API configurée, vous pouvez exécuter le script avec Python :

```bash
python main.py
```

Le script vous demandera d'entrer le nom de la ville pour laquelle vous souhaitez obtenir les données météo. Par exemple, entrez `Paris` pour obtenir les informations météo pour Paris.

### 2. En Utilisant Docker

Si vous préférez utiliser Docker, suivez ces étapes :

#### Construisez l'image Docker :

```bash
docker build -t weather-fetcher .
```

#### Exécutez le conteneur Docker :

Passez votre clé API comme variable d'environnement lors de l'exécution du conteneur :

```bash
docker run -it -e OPENWEATHER_API_KEY="votre_cle_api_ici" weather-fetcher
```

## Documentation de l'API

Pour plus d'informations sur l'API OpenWeatherMap, y compris les paramètres disponibles et les limites d'utilisation, consultez la [documentation officielle](https://openweathermap.org/api).
