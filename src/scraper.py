import sys
import errno
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def help():
    print('Please inform URL and, at least, one term to be searched.')
    print(f"Sintax: {sys.argv[0][2:]} <url> <'term/s'>")

def is_valid_url(url):
    """Check if URL has basic structure and is online."""
    try:
        result = urlparse(url)
        # it has http/https protocol and domain (netloc)?
        syntax_ok = all([result.scheme, result.netloc])
        
        if not syntax_ok:
            return False, "Invalid URL structure (example: 'http://' is missed)"

        # does the link respond? (5s timeout to avoid script froze)
        response = requests.head(url, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            return True, "Valid and online URL"
        else:
            return False, f"URL with Status Code {response.status_code}"
            
    except Exception as e:
        return False, f"Error to access URL: {e}"

def get_python_news(url, keyword):
    """Search for text lines on URL link that contain keyword/s."""
    response = requests.get(url) # must display 200 # debug: print(f"Connection Status: {response.status_code}") 
    
    if response.status_code != 200: # request was successful = Status 200
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    # Locates all post titles (in this case, within set HTML tags).
    for title in soup.find_all('p'): # can be set to diverse HTML Tag types, as 'h3', 'p', etc.
        text = title.get_text().strip()
        if keyword.lower() in text.lower():
            results.append(text)            
    return results

if __name__ == "__main__":
    if len(sys.argv) < 3 :
        help()
        sys.exit(errno.EPERM)    # code 1 ; not permitted operation ## sys.exit(1)
        sys.exit(errno.EPERM)    # code 1 ; not permitted operation

    if not is_valid_url(sys.argv[1]):
        help()
        print('Informed URL must be valid')
        sys.exit(errno.EINVAL)   # code 2 ; invalid argument

    url = sys.argv[1]
    terms = sys.argv[2:]
    print (f' \nInto URL: \n {url}')
    print (f'...looking for these terms: {terms} \n')
    for keyword in terms:
        print(f' \nLooking for news about: \'{keyword}\'...')
        news = get_python_news(url, keyword)
        for idx, item in enumerate(news, 1):
            print(f"    -> {idx}. {item}")