import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


class Unsplashbot(webdriver.Chrome):
    def __init__(self, url: str):
        super().__init__()
        self.maximize_window()
        self.implicitly_wait(10)
        self.get(url)

    def search_images(self, text: str):
        src_input = self.find_element(By.XPATH, '//input[@type="search"]')
        src_input.send_keys(text, Keys.ENTER)

    def get_url_images(self):
        url_list = []
        time.sleep(10)
        images_tag = self.find_elements(By.XPATH, "//div[@class='MorZF']/img")
        for tag in images_tag:
            url_list.append(tag.get_attribute("src"))
        return url_list

    def download_images(self, url_images: list):
        for index, url in enumerate(url_images):
            # Obtenir l'image à partir de l'URL
            response = requests.get(url, stream=True)
            # Enregistrer l'image localement avec un nom unique (img0.jpg, img1.jpg, ...)
            with open(f"img{index}.jpg", "wb") as f:
                for chunk in response.iter_content(chunk_size=128):
                    f.write(chunk)

    def close_driver(self):
        self.close()


# URL de la page web à ouvrir
url = "https://unsplash.com/fr"

# Utilisation de la classe personnalisée pour automatiser le navigateur
with Unsplashbot(url) as bot:
    try:
        # Demande à l'utilisateur d'entrer une chaîne de caractères pour la recherche d'images
        user_input = input("Entrez une chaîne de caractères pour la recherche d'images : ")
        bot.search_images(user_input)

        # Obtient les URL des images et les télécharge
        bot.download_images(bot.get_url_images())

        # Ferme le navigateur
        bot.close_driver()
    except Exception as e:
        print(f'Error : {e}')
