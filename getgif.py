import random
import requests
import os
from dotenv import load_dotenv

def get_gif(searchTerm, limit=1):
    load_dotenv()
    response = requests.get(
        f"https://tenor.googleapis.com/v2/search?q={searchTerm}&key={os.getenv('TENORKEY')}&client_key={os.getenv('CLIENT_KEY')}&limit={limit}"
        )
    data = response.json()
    gif = random.choice(data["results"])

    return gif['url']