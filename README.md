# Bot Discord d'Apprentissage Automatique

Ce bot Discord est un projet Python qui permet à un bot Discord de répondre aux messages des utilisateurs en fonction des correspondances stockées dans une base de données SQLite. Les utilisateurs peuvent enseigner au bot de nouvelles réponses en utilisant la commande `&learn` suivie d'une phrase clé et d'une réponse. Le bot peut également sauvegarder la base de données sous un nom spécifié avec la commande `&save`.

## Fonctionnalités principales :
- Enseigner au bot de nouvelles réponses à l'aide de la commande `&learn`.
- Répondre aux messages des utilisateurs en fonction des correspondances stockées dans la base de données.
- Sauvegarder la base de données sous un nom spécifié avec la commande `&save`.

## Prérequis :
- Python 3.x installé.
- Les modules Python `discord.py` et `sqlite3`.

## Installation et configuration :
1. Clonez ce référentiel (repository) sur votre système local.
2. Installez les dépendances requises en exécutant `pip install discord.py` et `pip install sqlite3` dans votre terminal.
3. Créez un bot Discord sur le [portail des développeurs Discord](https://discord.com/developers/applications).
4. Copiez le token du bot et remplacez `"BOT_TOKEN"` dans le code du bot par ce token.
5. Exécutez le bot en utilisant la commande `python bot.py` dans le terminal.

## Utilisation :
- Pour ajouter une nouvelle clé, utilisez la commande `&learn PHRASECLé=PHRASE RéPONSE`.
- Pour demander au bot en utilisant une phrase clé, il vous suffit de saisir la phrase clé dans le chat.

N'hésitez pas à personnaliser ce bot en fonction de vos besoins. Amusez-vous bien !
