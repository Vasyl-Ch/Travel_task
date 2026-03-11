import requests


def get_artwork(art_id):

    url = f"https://api.artic.edu/api/v1/artworks/{art_id}?fields=id,title"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()

    return data.get("data")
