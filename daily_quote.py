import requests

def fetch_quote(tags):
    tags_query = ','.join(tags)
    url = f"https://api.quotable.io/quotes/random?tags={tags_query}"
    
    response = requests.get(url)
    response.raise_for_status()
    quote_data = response.json()
    return quote_data["content"], quote_data["author"]

def update_readme(new_quote, new_author):
    with open("README.md", "r") as file:
        readme_content = file.readlines()

    updated_content = []
    quote_replaced = False
    for line in readme_content:
        if line.startswith("## ✨ Quote of the Day ✨"):
            updated_content.append(f'\n## ✨ Quote of the Day ✨\n\n> "{new_quote}" — **{new_author}**\n')
            quote_replaced = True
            continue
        elif quote_replaced and line.startswith("## "):
            quote_replaced = False
            updated_content.append(line)
        else:
            updated_content.append(line)
    
    if not quote_replaced:
        updated_content.append(f'\n## ✨ Quote of the Day ✨\n\n> "{new_quote}" — **{new_author}**\n')

    with open("README.md", "w") as file:
        file.writelines(updated_content)

if __name__ == "__main__":
    tags = ["technology", "famous-quotes"]
    quote, author = fetch_quote(tags)
    update_readme(quote, author)
