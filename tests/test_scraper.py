# Unit tests -v1
from src.scraper import get_python_news
from src.scraper import is_valid_url


def test_get_python_news_is_list():
    """Checks if the function returns a list (even if it's empty)."""
    results = get_python_news("https://www.python.org/blogs", "Python")
    assert isinstance(results, list)

def test_invalid_keyword_returns_empty():
    """Checks if a non-existent term returns an empty list."""
    results = get_python_news("https://www.python.org/blogs", "InexistenTerm123xYz")
    assert len(results) == 0


def test_url_validation_success():
    """Testa se uma URL válida e conhecida retorna True."""
    is_ok, msg = is_valid_url("https://www.google.com")
    assert is_ok is True
    assert "Valid and online" in msg
    
def test_url_validation_invalid_syntax():
    """Testa se URLs sem http/https são barradas."""
    is_ok, msg = is_valid_url("google.com")
    assert is_ok is False
    assert "Invalid URL" in msg

def test_url_validation_offline():
    """Testa o comportamento com um domínio que não existe."""
    is_ok, msg = is_valid_url("https://site.que.nao.existe.xyz")
    assert is_ok is False
    assert "Error to access" in msg