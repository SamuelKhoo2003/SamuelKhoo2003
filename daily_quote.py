import requests

def fetch_quote(tags):
    tags_query = '|'.join(tags)
    url = f"https://api.quotable.io/quotes/random?tags={tags_query}"
    
    response = requests.get(url)
    response.raise_for_status()
    quote_data = response.json()
    return quote_data[0]["content"], quote_data[0]["author"]

def update_readme(new_quote, new_author):
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
    tags = ["technology", "famous-quotes"]
    quote, author = fetch_quote(tags)
    update_readme(quote, author)
