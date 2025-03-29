import requests

def get_wikipedia_dish_info(page_title):
    # URL de base de l'API MediaWiki
    api_url = "https://fr.wikipedia.org/w/api.php"

    # Paramètres de la requête pour obtenir les informations de la page
    params = {
        "action": "query",
        "format": "json",
        "titles": page_title,
        "prop": "extracts|pageimages|pageterms",
        "explaintext": True,
        "piprop": "original",
        "pilicense": "any",
        "wbptterms": "description"
    }

    # Envoyer la requête à l'API
    response = requests.get(api_url, params=params)
    data = response.json()

    # Extraire les informations de la réponse JSON
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))

    title = page["title"]
    extract = page["extract"]
    image_url = page["original"]["source"] if "original" in page else "No image found"
    description = page["terms"]["description"][0] if "description" in page["terms"] else "Description non trouvée"

    # Afficher les informations récupérées
    print(f"Nom du plat: {title}")
    print(f"Image: {image_url}")
    print(f"Description/Origine: {description}")

# Exemple d'utilisation
get_wikipedia_dish_info("Pizza")
