import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_dish(url):
    # Envoyer une requête HTTP pour obtenir le contenu de la page
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code != 200:
        print("Erreur lors de la récupération de la page.")
        return

    # Analyser le contenu HTML de la page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraire le nom du plat
    title = soup.find('h1', {'id': 'firstHeading'}).text

    # Extraire l'image du plat
    image = soup.find('a', {'class': 'image'})
    image_url = image.find('img')['src'] if image else 'No image found'

    # Extraire l'origine du plat
    origin = None
    table = soup.find('table', {'class': 'infobox'})
    if table:
        for row in table.find_all('tr'):
            header = row.find('th')
            if header and 'origine' in header.text.lower():
                origin = row.find('td').text.strip()
                break

    # Afficher les informations récupérées
    print(f"Nom du plat: {title}")
    print(f"Image: {image_url}")
    print(f"Origine: {origin if origin else 'Origine non trouvée'}")

# Exemple d'utilisation
url = 'https://fr.wikipedia.org/wiki/Pizza'
scrape_wikipedia_dish(url)
