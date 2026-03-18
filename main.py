from src.world_bank import (
    fetch_indicator_catalog,
    build_indicator_dict,
    search_indicators,
    save_json
)
from src.world_bank.config import CSV_PATH, JSON_PATH


def main():
    df = fetch_indicator_catalog()
    indicator_dict = build_indicator_dict(df)

    df.to_csv(CSV_PATH, index=False)
    save_json(indicator_dict, JSON_PATH)

    print("Dataset shape:", df.shape)
    print(search_indicators(df, "gdp"))
    print(indicator_dict.get("NY.GDP.MKTP.KD.ZG"))


if __name__ == "__main__":
    main()
