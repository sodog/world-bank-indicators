from pathlib import Path

WORLD_BANK_BASE_URL = "https://api.worldbank.org/v2"
INDICATOR_ENDPOINT = f"{WORLD_BANK_BASE_URL}/indicator"

DEFAULT_TIMEOUT = 30
DEFAULT_PER_PAGE = 20000

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

CSV_PATH = DATA_DIR / "world_bank_indicators.csv"
JSON_PATH = DATA_DIR / "world_bank_indicators.json"
