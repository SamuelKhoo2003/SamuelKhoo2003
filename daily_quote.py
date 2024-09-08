import requests

response = requests.get("https://api.quotable.io/random")
quote_data = response.json()
quote = quote_data["content"]
author = quote_data["author"]

# Read the current README file
with open("README.md", "r") as file:
    readme_content = file.readlines()

# Update the quote section
updated_content = []
for line in readme_content:
    if line.startswith("## ✨ Quote of the Day ✨"):
        updated_content.append(f'\n## ✨ Quote of the Day ✨\n\n> "{quote}" — **{author}**\n')
    else:
        updated_content.append(line)

# Write the updated README file
with open("README.md", "w") as file:
    file.writelines(updated_content)
