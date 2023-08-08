# UnsplashBot

UnsplashBot est un script Python qui automatise la recherche et le téléchargement d'images à partir du site web Unsplash en utilisant Selenium et Requests.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir les éléments suivants installés :

- Python 3.x : [Télécharger Python](https://www.python.org/downloads/)
- ChromeDriver : [Télécharger ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Assurez-vous d'ajouter l'emplacement de l'exécutable ChromeDriver à la variable PATH de votre système.

## Comment exécuter

1. Clonez ce dépôt sur votre machine locale.

```sh
git clone https://github.com/rayanhcm2/scrape-unsplash-images-selenium 
cd scrape-unsplash-images-selenium 
pip install -r requirements.txt
python main.py
```
1. Suivez les invitations pour entrer un terme de recherche d'images.

2. Le script ouvrira un navigateur Chrome, effectuera une recherche d'images sur Unsplash, les téléchargera et les sauvegardera dans le répertoire actuel.

3. Une fois le processus terminé, le navigateur se fermera automatiquement.
