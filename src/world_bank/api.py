import requests
from .config import INDICATOR_ENDPOINT, DEFAULT_TIMEOUT, DEFAULT_PER_PAGE


def get_indicator_page(page=1, per_page=DEFAULT_PER_PAGE, timeout=DEFAULT_TIMEOUT):
    params = {"format": "json", "page": page, "per_page": per_page}

    response = requests.get(INDICATOR_ENDPOINT, params=params, timeout=timeout)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, list) or len(data) < 2:
        raise ValueError("Invalid API response")

    return {"metadata": data[0], "indicators": data[1]}
