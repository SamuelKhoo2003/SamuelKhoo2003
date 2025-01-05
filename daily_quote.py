from typing import List, Tuple
from dotenv import load_dotenv
import requests
import random
import os

load_dotenv()

def fetch_quote(categories: List[str]) -> Tuple[str, str]:
    category = random.choice(categories)
    api_url = f"https://api.api-ninjas.com/v1/quotes"
    api_key = os.getenv("API_NINJA_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the API_KEY environment variable.")

    headers = {
        'X-Api-Key': api_key
    }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    quote_data = response.json()

    if quote_data:
        return quote_data[0]["quote"], quote_data[0]["author"]
    else:
        raise ValueError("No quotes found for the specified category.")


def update_readme(new_quote: str, new_author: str) -> None:
    with open("README.md", "r", encoding='utf-8') as file:
        readme_content = file.readlines()

    updated_content = []
    for line in readme_content:
        if line.strip().startswith("> "):
            updated_content.append(f'> "{new_quote}" — **{new_author}**\n')
        else:
            updated_content.append(line)

    with open("README.md", "w", encoding='utf-8') as file:
        file.writelines(updated_content)

if __name__ == "__main__":
    categories = ["computers", "education", "architecture", "famous", "inspirational", "intelligence", "success", "life", "learning"]
    quote, author = fetch_quote(categories)
    update_readme(quote, author)
