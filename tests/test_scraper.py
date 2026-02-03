# Unit tests -v1
from src.scraper import get_python_news

def test_get_python_news_is_list():
    """Checks if the function returns a list (even if it's empty)."""
    results = get_python_news("Python")
    assert isinstance(results, list)

def test_invalid_keyword_returns_empty():
    """Checks if a non-existent term returns an empty list."""
    results = get_python_news("InexistenTerm123xYz")
    assert len(results) == 0