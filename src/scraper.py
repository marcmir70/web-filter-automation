import requests
from bs4 import BeautifulSoup

def get_python_news(keyword):
    """Search for titles on Python.org that contain keyword."""
    url = "https://www.python.org/blogs/"
    response = requests.get(url)
    # debug # print(f"Status da conexão: {response.status_code}") # must display 200
    
    # Checking if the request was successful - Status 200
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    # Locates all post titles (in this case, within <h3> tags).
    for title in soup.find_all('h3'):
        text = title.get_text().strip()
        if keyword.lower() in text.lower():
            results.append(text)
            
    return results

if __name__ == "__main__":
    term = "Python"
    # debug # term = ""  # leaving empty to bring all titles + check if connection works
    print(f"Looking for news about: '{term}'...")
    news = get_python_news(term)
    
    for idx, item in enumerate(news, 1):
        print(f"{idx}. {item}")